# The Forge VPS

VPS.md — what the Forge Stack's VPS does, how it is built, and how to run it.

Function:
    Records the VPS's two jobs: the verification node (2026-11-15) and
    the read-only Legacy (2026-11-16). For each: its purpose, the rules
    it keeps, its layout, how to read and update it, how to rebuild it
    from nothing, and what went wrong on the way. The scripts are in
    the appendices; on the laptop they are kept in
    `Documents\forge-vps\`. This repository is public, so addresses,
    the tailnet name, instance ids and key ids are not written here;
    they live in the Contabo panel, the Tailscale admin page and the
    laptop's `~/.ssh/config` (host `forge`).

## What it is for

The VPS watches the stack. Every 6 hours it pulls the latest commits and
proves, on a machine that is neither the laptop nor the S24, that the
foundation still verifies:

- the foundation's test suite;
- `sign_v3.py --verify`: every capsule and referenced artefact signature,
  and governance-v7's number rule;
- `freeze_v3.py --check`: every live capsule's pinned document hash;
- `ledger_v2.py verify`: the root ledger's chain and signatures;
- the Saboteur (`saboteur_v2.py`): every known attack is caught and named.

Each run ends GREEN or RED. A RED is news: something pushed has broken a
signature, a pin, the ledger or a guard.

## The rules it keeps

1. **No signing keys, ever.** Not James's identity key, not his Forge key.
   The VPS verifies; James signs, on the laptop. A machine that is always
   on and always reachable is the wrong home for an identity.
2. **Read-only access to code.** Public repositories are cloned over
   HTTPS. The one private repository (`ccemk2`) is read with a GitHub
   *deploy key* that is read-only and scoped to that repository alone.
3. **Nothing is served to the internet.** The firewall admits SSH only.
   Anything the VPS shows later is reached over Tailscale.
4. **The checks run as a locked user.** `forge` is a system user with no
   login shell, no sudo and no password.

## The machine

| | |
| :--- | :--- |
| Provider | Contabo Cloud VPS, EU (instance in the Contabo panel) |
| System | Ubuntu 24.04 LTS, Python 3.12, 11 GB RAM, ~190 GB disk |
| Admin | user `james` (sudo), SSH key only; root and password login off |
| Network | `ufw`: deny incoming except SSH; Tailscale for private access |
| Guard | `fail2ban` (repeated failed SSH logins are banned for a while) |
| Laptop access | `ssh forge` (alias in the laptop's `~/.ssh/config`, key `forge_vps`) |

## Layout

```
/srv/forge/                  home of the locked `forge` user
  the-full-stack/            with submodules consumer/ccemk2, consumer/keystone_gate
  the-saboteur/
  venv/                      Python: cryptography, pytest
  check.sh                   one verification run
  logs/<UTC stamp>.log       one log per run, kept 30 days
  logs/latest                the newest log
  logs/history               one line per run: time, GREEN or RED, log
  .ssh/ccemk2_deploy         the read-only deploy key (forge only)

/etc/systemd/system/forge-check.service   runs check.sh as forge, sandboxed
/etc/systemd/system/forge-check.timer     00:00, 06:00, 12:00, 18:00 (server time), and 10 min after boot
```

## Day to day

```bash
ssh forge
tail -5 /srv/forge/logs/history           # the last five verdicts
sudo cat /srv/forge/logs/latest           # what the last run said
sudo systemctl start forge-check.service  # run it now (exit status = verdict)
systemctl list-timers forge-check.timer   # when it runs next
```

`/srv/forge` belongs to `forge`, so reading it as `james` needs `sudo`.

A RED log names the step that failed and shows the last 25 lines of its
output. Fix the cause in the repository (on the laptop, signed as
usual) and push; the next run picks it up. Never fix it on the VPS.

## Rebuilding it

On a fresh Ubuntu 24.04 VPS:

1. **Get in.** Make a key on the laptop (`ssh-keygen -t ed25519 -f
   ~/.ssh/forge_vps`), log in as root once (password from the Contabo
   panel's *Reset password*), and append `forge_vps.pub` to
   `/root/.ssh/authorized_keys`. Confirm `ssh -i ~/.ssh/forge_vps
   root@<ip>` logs in without a password.
2. **Update.** `apt update && apt -y full-upgrade && reboot`.
3. **Admin user.** `adduser james`, add to `sudo`, copy root's
   `authorized_keys` to `/home/james/.ssh/`. Test the login and `sudo`
   from a second window *before* the next step.
4. **Close the doors.** As james:
   ```bash
   printf 'PermitRootLogin no\nPasswordAuthentication no\nKbdInteractiveAuthentication no\n' | sudo tee /etc/ssh/sshd_config.d/99-forge.conf
   sudo sshd -t && sudo systemctl reload ssh
   sudo ufw default deny incoming && sudo ufw default allow outgoing && sudo ufw allow OpenSSH && sudo ufw --force enable
   sudo apt -y install fail2ban && sudo systemctl enable --now fail2ban
   curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up
   ```
5. **The verification node.** Copy the script in the appendix to the VPS
   and run `bash setup_forge_check.sh`. It pauses once: add the public
   key it prints to `JamesTheGiblet/ccemk2` → Settings → Deploy keys,
   with *Allow write access* **off** (or, from the laptop:
   `gh repo deploy-key add key.pub -R JamesTheGiblet/ccemk2 --title "forge-vps (read-only)"`).
   It ends with a first run; it must be GREEN.

## The read-only Legacy (2026-11-16)

The Legacy and its Field, with James's data, on one private link:

```
https://<vps tailnet name>/          The Legacy
https://<vps tailnet name>/field/    The Field (also embedded in the Legacy page)
```

Reachable from any device on the tailnet (Tailscale on), never from the
public internet. `tailscale serve status` on the VPS prints the name.

### Its rules

1. **No key goes up.** The laptop sends `forge.db`, `store.db`,
   `ledger.jsonl` and `lllm.db`, and nothing else; `key.pem` never
   leaves the laptop. The VPS refuses any other uploaded file.
2. **Read-only.** The Legacy refuses every write (POST) whose Host is
   not `localhost`, so through Tailscale nothing can be saved, answered
   or signed. Change things on the laptop, then sync.
3. **The laptop is the source of truth.** Each sync replaces the VPS
   copy whole; anything that differs there is overwritten.
4. **Both servers listen on 127.0.0.1 only.** Tailscale Serve is the
   only way in, over HTTPS, with `/field` passed to the Field with the
   prefix removed.

### Layout

```
/srv/legacy/                 home of the locked `legacy` user
  src/<24 repositories>      the Forge Stack side by side, as on the laptop
  venv/                      Python: cryptography
  forge-home/                FORGE_HOME: forge.db, store.db, ledger.jsonl, lllm.db
  forge-home/.incoming/      where an upload lands before it is installed

/usr/local/sbin/legacy-refresh            install an upload, pull every repo, restart
/etc/systemd/system/legacy-field.service  boot_v6.py as legacy, FORGE_FIELD_PUBLIC_URL=/field/
```

`legacy_v11` / `boot_v6` (the-legacy SPEC_V13.md) exist for this: the
page is told `/field/` for the Field instead of the address the server
probes (`127.0.0.1:8085`), which no other device can reach.

### Updating it

On the laptop, after any change worth seeing on the VPS:

```powershell
python $HOME\Documents\forge-vps\sync_legacy_to_vps.py
```

It snapshots the four files (SQLite's own backup, safe while the
laptop's Legacy runs), uploads them, and runs `sudo legacy-refresh` on
the VPS, which also pulls the latest code. It asks for the `forge_vps`
key's passphrase twice and james's sudo password once. `--dry-run`
shows what would be sent and sends nothing.

What does not work there, by design: the Voice and dreams (no LLLM
engine or Ollama on the VPS) and every write.

### Rebuilding it

After the verification node's steps 1–4: copy `setup_legacy_vps.sh`
(appendix B) to the VPS and run it; log out and back in (the `legacy`
group); then run the sync from the laptop.

## What went wrong on 2026-11-15, and what it taught

- **A key pair that did not match.** The server recognised the laptop's
  old `contabo_vps` public key but the login still failed: the private
  file did not match it. A fresh pair (`forge_vps`) fixed it. Lesson:
  `ssh -v` shows "Server accepts key" followed by a fall-back to
  password when the two halves disagree.
- **Locked out by our own guesses.** Three wrong root passwords made the
  server stop answering for a while. Lesson: never guess; reset.
- **Two servers.** The account had an older VPS as well; the work moved
  to the new one. The old one is to be cancelled or put to use.
- **Commands run on the wrong machine.** `scp` and `grep` typed into the
  server instead of the laptop, and vice versa. Lesson: read the prompt
  first: `PS C:\…>` is the laptop, `james@vmi…:~$` is the VPS.
- **The deploy key was never added,** so ccemk2 did not clone; the run
  was RED for exactly that reason. Lesson: a RED that names its cause
  is the system working.
- **A half-filled submodule.** The interrupted first clone left
  `keystone_gate` at the right commit with files missing; git did not
  flag it, and two tests went RED. `check.sh` now runs `git submodule
  update --init --force`, which restores missing files every run.

## What went wrong on 2026-11-16, and what it taught

- **A list split over lines broke a loop.** The repository list in the
  setup script spanned three lines and was expanded inside a `bash -c`
  string, so the newlines ended the `for` statement early. Fixed by
  folding it onto one line first. The script is safe to rerun.
- **The Field's own port did not reach the phone,** and the Legacy page
  pointed its Field at `127.0.0.1:8085`, the server's own address. The
  fix was one link: the Field under `/field/` on the Legacy's address,
  and the page told that address (legacy_v11).
- **A new group needs a new login.** Adding james to `legacy` only took
  effect after logging out and back in.

## Not done yet

- **Alerts.** A RED is only seen when someone looks. Next: a message to
  the phone on RED (Telegram or ntfy).
- **More on the box:** ccemk2 under PM2.
- **Freeze** legacy_v11 / boot_v6 once used on the phone.

## Appendix A: setup_forge_check.sh

This is the script as run on 2026-11-15, with the `--force` fix in
`check.sh`. Copy it to the VPS as `setup_forge_check.sh`.

```bash
#!/usr/bin/env bash
# setup_forge_check.sh — make this VPS a Forge Stack verification node.
#
# Function:
#     Run once, as james (sudo), on the VPS. It:
#       1. creates a locked system user `forge` (no login, no sudo, no keys
#          of James's) with its home at /srv/forge;
#       2. makes a read-only GitHub deploy key for the private ccemk2 repo
#          and stops until you have added it on GitHub;
#       3. clones the-full-stack (with ccemk2 and keystone_gate) and
#          the-saboteur, and builds a Python venv (cryptography, pytest);
#       4. installs /srv/forge/check.sh and a systemd timer that, every
#          6 hours, pulls and runs: the foundation's tests, sign_v3
#          --verify, freeze_v3 --check, ledger_v2 verify and the Saboteur.
#          Each run's log is kept (30 days); logs/history has one
#          GREEN/RED line per run.
#     No signing key is ever put on this machine. It verifies; James signs.
#
#     Usage: bash setup_forge_check.sh
set -euo pipefail

HOME_DIR=/srv/forge
say() { printf '\n== %s\n' "$*"; }

say "1. user forge"
if ! id forge >/dev/null 2>&1; then
  sudo useradd --system --create-home --home-dir "$HOME_DIR" --shell /usr/sbin/nologin forge
fi
sudo apt-get -qq update && sudo apt-get -y -qq install python3-venv git >/dev/null
as_forge() { sudo -u forge -H bash -c "$1"; }

say "2. read-only deploy key for ccemk2"
as_forge '
mkdir -p ~/.ssh && chmod 700 ~/.ssh
[ -f ~/.ssh/ccemk2_deploy ] || ssh-keygen -q -t ed25519 -N "" -C "forge-vps-ccemk2-readonly" -f ~/.ssh/ccemk2_deploy
cat > ~/.ssh/config <<EOF
Host github-ccemk2
  HostName github.com
  User git
  IdentityFile ~/.ssh/ccemk2_deploy
  IdentitiesOnly yes
EOF
chmod 600 ~/.ssh/config
ssh-keyscan -t ed25519 github.com >> ~/.ssh/known_hosts 2>/dev/null
'
echo "Add this PUBLIC key on GitHub as a READ-ONLY deploy key on JamesTheGiblet/ccemk2"
echo "(repo -> Settings -> Deploy keys -> Add deploy key; leave 'Allow write access' OFF):"
echo
sudo cat "$HOME_DIR/.ssh/ccemk2_deploy.pub"
echo
read -r -p "Press Enter once it is added... " _

say "3. clone and venv"
as_forge '
cd ~
[ -d the-full-stack ] || git clone -q https://github.com/JamesTheGiblet/the-full-stack.git
cd the-full-stack
git config submodule.consumer/ccemk2.url git@github-ccemk2:JamesTheGiblet/ccemk2.git
git submodule update -q --init --force consumer/ccemk2 consumer/keystone_gate
cd ~
[ -d the-saboteur ] || git clone -q https://github.com/Giblet-Legacy/the-saboteur.git
[ -d venv ] || python3 -m venv venv
venv/bin/pip install -q --upgrade pip cryptography pytest
mkdir -p logs
'

say "4. check script and 6-hourly timer"
sudo tee "$HOME_DIR/check.sh" >/dev/null <<'EOF'
#!/usr/bin/env bash
# check.sh — pull and verify the Forge Stack; GREEN or RED. Runs as forge.
set -u
cd /srv/forge
export PATH=/srv/forge/venv/bin:$PATH
stamp=$(date -u +%Y%m%dT%H%M%SZ)
log=logs/$stamp.log
fail=0
run() {  # run NAME DIR CMD...
  local name=$1 dir=$2; shift 2
  local out; out=$(mktemp)
  if (cd "$dir" && "$@") >"$out" 2>&1; then echo "PASS  $name"
  else echo "FAIL  $name"; tail -25 "$out" | sed 's/^/      /'; fail=1; fi
  rm -f "$out"
}
{
  echo "Forge check $stamp"
  run "pull the-full-stack" the-full-stack git pull -q --ff-only
  run "submodules" the-full-stack git submodule update -q --init --force consumer/ccemk2 consumer/keystone_gate
  run "pull the-saboteur" the-saboteur git pull -q --ff-only
  echo "the-full-stack $(git -C the-full-stack rev-parse --short HEAD), the-saboteur $(git -C the-saboteur rev-parse --short HEAD)"
  run "tests" the-full-stack python -m pytest tests -q
  run "sign_v3 --verify" the-full-stack python sign_v3.py --verify
  run "freeze_v3 --check" the-full-stack python freeze_v3.py --check
  run "ledger_v2 verify" the-full-stack python ledger_v2.py verify
  run "saboteur" the-saboteur python saboteur_v2.py --target ../the-full-stack
} >"$log" 2>&1
status=GREEN; [ "$fail" = 1 ] && status=RED
echo "$(date -u +%FT%TZ) $status $log" >> logs/history
ln -sfn "$stamp.log" logs/latest
find logs -name '*.log' -mtime +30 -delete
exit "$fail"
EOF
sudo chown forge:forge "$HOME_DIR/check.sh" && sudo chmod 755 "$HOME_DIR/check.sh"

sudo tee /etc/systemd/system/forge-check.service >/dev/null <<'EOF'
[Unit]
Description=Forge Stack verification (tests, signatures, hashes, ledger, Saboteur)
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
User=forge
Group=forge
WorkingDirectory=/srv/forge
ExecStart=/srv/forge/check.sh
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ReadWritePaths=/srv/forge
ProtectHome=yes
EOF
sudo tee /etc/systemd/system/forge-check.timer >/dev/null <<'EOF'
[Unit]
Description=Run the Forge Stack verification every 6 hours

[Timer]
OnBootSec=10min
OnCalendar=*-*-* 00/6:00:00
Persistent=true

[Install]
WantedBy=timers.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now forge-check.timer

say "first run (a few minutes)"
sudo systemctl start forge-check.service && echo "GREEN" || echo "RED (see the log)"
sudo cat "$HOME_DIR/logs/latest"
echo
systemctl list-timers forge-check.timer --no-pager
```

## Appendix B: setup_legacy_vps.sh

Run once on the VPS, as james, after the verification node's steps 1–4.

```bash
#!/usr/bin/env bash
# setup_legacy_vps.sh — a read-only Legacy and Field on the VPS, over Tailscale.
#
# Function:
#     Run once, as james (sudo), on the VPS. It:
#       1. creates a locked system user `legacy` (no login, no sudo), home
#          /srv/legacy, and adds james to its group so he can upload data;
#       2. clones the Forge Stack repositories side by side under
#          /srv/legacy/src (as on the laptop) and builds a venv
#          (cryptography);
#       3. makes /srv/legacy/forge-home, the FORGE_HOME the Legacy reads.
#          Data arrives from the laptop (sync_legacy_to_vps.py): forge.db,
#          store.db, ledger.jsonl, lllm.db. Never key.pem: there is no
#          signing key on this machine;
#       4. installs /usr/local/sbin/legacy-refresh: moves an uploaded data
#          set into place, pulls every repository, restarts the service;
#       5. runs boot_v6.py (the Field v8 and The Legacy v11) as `legacy`
#          under systemd, both listening on 127.0.0.1 only;
#       6. publishes them to the tailnet only, with Tailscale Serve:
#          https://<this machine's tailnet name>/         The Legacy
#          https://<this machine's tailnet name>/field/   The Field (one link)
#     The Legacy refuses every write (POST) whose Host is not localhost,
#     so through Tailscale it is read-only; edits and signing stay on the
#     laptop.
#
#     Usage: bash setup_legacy_vps.sh
set -euo pipefail

BASE=/srv/legacy
REPOS="canon-verify-layer datacube-layer envelope-layer explorer-d334-forge forge-time
freeze-layer genesis-layer hal-layer ledger-layer leighton-engine-layer lllm mediator-layer
record-layer rules-layer sc-os scp-substrate sign-layer store-layer substrate-layer the-echo
the-legacy the-weaver trust-layer weight-layer"
REPOS=$(echo $REPOS)  # one line: it is expanded inside a bash -c string below
say() { printf '\n== %s\n' "$*"; }

say "1. user legacy"
if ! id legacy >/dev/null 2>&1; then
  sudo useradd --system --create-home --home-dir "$BASE" --shell /usr/sbin/nologin legacy
fi
sudo usermod -aG legacy james
sudo chmod 750 "$BASE"
sudo apt-get -qq update && sudo apt-get -y -qq install python3-venv git sqlite3 >/dev/null

say "2. repositories and venv"
sudo -u legacy -H bash -c "
set -e
mkdir -p $BASE/src && cd $BASE/src
for r in $REPOS; do
  [ -d \"\$r\" ] || git clone -q https://github.com/Giblet-Legacy/\$r.git
done
cd $BASE
[ -d venv ] || python3 -m venv venv
venv/bin/pip install -q --upgrade pip cryptography
"

say "3. data folder (FORGE_HOME)"
sudo install -d -o legacy -g legacy -m 2770 "$BASE/forge-home" "$BASE/forge-home/.incoming"

say "4. legacy-refresh"
sudo tee /usr/local/sbin/legacy-refresh >/dev/null <<EOF
#!/usr/bin/env bash
# legacy-refresh — install an uploaded data set, pull the code, restart.
set -euo pipefail
HOME_DIR=$BASE/forge-home
IN=\$HOME_DIR/.incoming
ALLOWED="forge.db store.db ledger.jsonl lllm.db"
for f in \$(ls -A "\$IN"); do
  case " \$ALLOWED " in *" \$f "*) ;; *) echo "refusing unexpected file: \$f"; rm -f "\$IN/\$f";; esac
done
for f in \$ALLOWED; do
  if [ -f "\$IN/\$f" ]; then
    chown legacy:legacy "\$IN/\$f"; chmod 660 "\$IN/\$f"
    rm -f "\$HOME_DIR/\$f-wal" "\$HOME_DIR/\$f-shm" "\$HOME_DIR/\$f-journal"
    mv -f "\$IN/\$f" "\$HOME_DIR/\$f"
    echo "installed \$f"
  fi
done
sudo -u legacy -H bash -c 'cd $BASE/src && for r in */; do git -C "\$r" pull -q --ff-only || echo "pull failed: \$r"; done'
systemctl restart legacy-field
sleep 3
systemctl is-active legacy-field
EOF
sudo chmod 750 /usr/local/sbin/legacy-refresh

say "5. service"
sudo tee /etc/systemd/system/legacy-field.service >/dev/null <<EOF
[Unit]
Description=The Legacy and the Field (read-only copy, served over Tailscale)
Wants=network-online.target
After=network-online.target

[Service]
User=legacy
Group=legacy
WorkingDirectory=$BASE/src/the-legacy
Environment=FORGE_HOME=$BASE/forge-home
Environment=PYTHONUNBUFFERED=1
Environment=FORGE_FIELD_PUBLIC_URL=/field/
ExecStart=$BASE/venv/bin/python $BASE/src/the-legacy/boot_v6.py --host 127.0.0.1 --port 8080 --field-port 8085
Restart=always
RestartSec=10
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ReadWritePaths=$BASE
ProtectHome=yes

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now legacy-field
sleep 5
systemctl is-active legacy-field || sudo journalctl -u legacy-field -n 30 --no-pager

say "6. Tailscale Serve (tailnet only)"
sudo tailscale serve --bg --https=443 http://127.0.0.1:8080
sudo tailscale serve --bg --set-path /field http://127.0.0.1:8085
tailscale serve status

say "done"
echo "No data yet: run sync_legacy_to_vps.py on the laptop next."
```

## Appendix C: sync_legacy_to_vps.py

Run on the laptop (`Documents\forge-vps\`) whenever the VPS copy should
catch up.

```python
#!/usr/bin/env python3
"""sync_legacy_to_vps.py — send a snapshot of ~/.forge to the VPS's read-only Legacy.

Function:
    Run on the laptop whenever the VPS copy should catch up. It:
      1. takes a consistent snapshot of ~/.forge (or FORGE_HOME): the
         SQLite files through SQLite's own backup (safe while the
         Legacy is running), ledger.jsonl copied as is;
      2. sends ONLY forge.db, store.db, ledger.jsonl and lllm.db.
         key.pem, and anything not on that list, never leaves the
         laptop; the script refuses to run if the list ever names a key;
      3. uploads them over SSH (host `forge`) into the VPS's incoming
         folder, then runs `sudo legacy-refresh` there, which moves them
         into place, pulls the code and restarts the service. sudo asks
         for james's password on the VPS.
    The VPS copy is read-only: anything changed there is replaced at the
    next sync. The laptop stays the source of truth.

    Usage: python sync_legacy_to_vps.py [--host forge] [--dry-run]

Depends:  Python 3 standard library; OpenSSH (scp, ssh) on PATH
Licence:  MSL-1.0
"""

import argparse
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys
import tempfile

SEND = ("forge.db", "store.db", "ledger.jsonl", "lllm.db")
REMOTE_IN = "/srv/legacy/forge-home/.incoming/"


def forge_home():
    return pathlib.Path(os.environ.get("FORGE_HOME") or pathlib.Path.home() / ".forge")


def snapshot(src, dst):
    """A consistent copy: SQLite backup for databases, plain copy otherwise."""
    if src.suffix == ".db":
        s = sqlite3.connect(f"file:{src}?mode=ro", uri=True)
        d = sqlite3.connect(dst)
        try:
            s.backup(d)
        finally:  # close both: on Windows an open handle locks the temp copy
            d.close()
            s.close()
    else:
        shutil.copy2(src, dst)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Send a snapshot of ~/.forge to the VPS Legacy.")
    ap.add_argument("--host", default="forge", help="SSH host (default: forge, from ~/.ssh/config)")
    ap.add_argument("--dry-run", action="store_true", help="snapshot and list, upload nothing")
    args = ap.parse_args(argv)

    if any("key" in name or name.endswith(".pem") for name in SEND):
        sys.exit("refusing: the send list names a key")
    home = forge_home()
    files = [home / n for n in SEND if (home / n).is_file()]
    missing = [n for n in SEND if not (home / n).is_file()]
    if not files:
        sys.exit(f"nothing to send in {home}")

    with tempfile.TemporaryDirectory(prefix="forge-sync-") as tmp:
        out = []
        for f in files:
            dst = pathlib.Path(tmp) / f.name
            snapshot(f, dst)
            out.append(dst)
            print(f"snapshot  {f.name:13} {dst.stat().st_size:>10,} bytes")
        for n in missing:
            print(f"skipped   {n:13} (not present)")
        print(f"never sent: {', '.join(sorted(p.name for p in home.iterdir() if p.name not in SEND))}")
        if args.dry_run:
            print("dry run: nothing uploaded.")
            return 0
        subprocess.run(["scp", "-q", *map(str, out), f"{args.host}:{REMOTE_IN}"], check=True)
        print("uploaded. Installing on the VPS (sudo asks for james's password):")
        return subprocess.run(["ssh", "-t", args.host, "sudo /usr/local/sbin/legacy-refresh"]).returncode


if __name__ == "__main__":
    sys.exit(main())
```
