# The Forge Stack — Status Report

STATUS.md — where the whole stack stands on one date.

Function:
    A one-page status of the Forge Stack: what is built, what is frozen,
    what is signed and what the tests say. Each claim is one checked on
    that date; anything not checked is marked as such. A new date gets a
    new section at the top, never an edit to an old one.

## 2026-11-24

- **P19 Validation 0.2.0-dev, first slice pushed** (validation-layer
  `407494d`, `c86665e`, `4e19c75`). `relevance_v0_2.py` is a dry run. It
  builds the import graph from five real entry points and computes λ per
  claim through Leighton V3. Eleven layers have confirmed claims.
  - Holds: PURPOSE for sign, store, canon-verify and the Saboteur.
  - Doubted: CONFORMS for sign, store and canon-verify, from the
    Saboteur's known gaps.
  - Unknown, and asked: the rest. Tests 54/54.
- **James's first answers** (recorded, unsigned; not evidence):
  - **retire:** forge-gate and seed;
  - **keep:** keystone_gate, forge-time and mediator-layer;
  - **wait:** self-layer and consumer.
- **Retired:**
  - **forge-gate:** moved off the laptop workspace to
    `Documents/Giblets_Legacy_retired/forge-gate`, with its git history
    and an uncommitted README edit that is not this session's, kept as
    it was. The GitHub repo is **not archived yet**: James runs
    `gh repo archive Giblet-Legacy/forge-gate`. The S24 still has a
    clone.
  - **seed:** moved to `Documents/Giblets_Legacy_retired/seed`, whole,
    including its identity material. It was never a git repository and
    was never pushed.
- **Not checked on this date:** the S24 and the VPS.

## 2026-11-22 (later)

- **The Legacy 2.1.0 frozen and published:** first-time guidance and
  Advanced navigation; tag `v2.1.0`, commit `f3e005d`. The frozen 2.0.0
  routes and files remain available. 63/63 tests passed on the laptop;
  desktop and mobile-width browser navigation was checked.
- **Not checked:** 2.1.0 on the S24 or VPS; a real Gemini request.

## 2026-11-23

- **The James Checklist 2.3.0 frozen** (private), and **P19 Validation
  0.1.1 frozen and pushed** (tag `v0.1.1`). A red team's findings must now
  be decided before they lift the score.
  - In 2.2.0, logging any review took a run from 65 to 100, though the
    reviewer would build none of them as planned.
  - Under 2.3.0, runs 0001 and 0002 show 65 (findings undecided), and run
    0003 shows 100 (decided and parked).
  - Tests: 43/43 on the laptop.
- **Checkpoints** (PROPOSAL_CHECKPOINTS.md): agreed, then red-teamed as
  run 0003.
  - **The finding:** the VPS witness is not independent of the laptop,
    which already syncs whole databases to it and holds the SSH path into
    it.
  - **James's decision (§9):** three witnesses (VPS, S24, GitHub); each
    checks signatures; behind any witness, or a fork, fails; unwitnessed
    for more than 24 hours is STALE.
  - **Run 0003 is parked** until §9 is designed in full and red-teamed
    again. P20 is not built.
- **Gap-fix drafts** (another session; uncommitted): ledger_v3,
  canon_verify_v3, store_v3, record_v3 and substrate_v5. They wait on
  checkpoints.
  - `store-layer/migrate_v3.py` rewrites 401 of 630 live store records
    into canonical form. Hashes are unchanged. It was rehearsed on a copy;
    the live store is untouched. James runs it.
- **Not checked on this date:** the S24; the VPS (James's
  forge_check_v2/v3 rerun is still due).

## 2026-11-22

- **P19 Validation 0.1.0 frozen and published**
  ([Giblet-Legacy/validation-layer](https://github.com/Giblet-Legacy/validation-layer),
  tag `v0.1.0`). The James Checklist's method joins the stack.
  - **The checklist:** frozen at 2.2.0 first, in James's private folder.
  - **The engine:** scores a run exactly as the checklist page does,
    proven by running the page's own script under Node on 12 synthetic
    runs. 21/21 on the laptop; 8 run anywhere.
  - **Private by design:** James's rules, R9 guard words and runs stay in
    `~/.forge/validation/`. Before the first push, the history was checked
    against his real guard words.
  - **Runs 0001 and 0002**, on the layer and on its next version: 65/100
    each, capped. Nobody outside James has checked them yet (F9).
- **P19 0.2.0 agreed, not built:** validation over a lifetime.
  - Each layer's and entity's reasons become claims, with λ through P14
    and a decay per kind.
  - A claim that goes unknown or doubted is asked about in the daily
    report and the Field.
  - James answers with a signed seal.
  - **Waiting on James:** the first 5 layers to claim, and run 0002's
    verdict.
- **Not checked on this date:** the S24; the VPS (validation-layer is not
  yet in its repo list).

## 2026-11-21

- **the-saboteur 1.1.0 frozen** (rotation; SPEC_V1_1.md), 76/76, tagged
  `v1.1.0`, merged into main in one commit.
  - Each 6-hour UTC slot runs 250 of the 1000 attacks, interleaved, so all
    1000 run each day.
  - A slot is RED only for a new problem, any UGLY or SKIP, or one of the
    154 known gaps starting to pass.
  - A daily report covers the slots, coverage, new and healed, and
    changes since the day before.
  - First real slot (slot 3, 2026-11-20 23:44 UTC): 250 attacks in 4
    minutes, PASS 212 / FAIL 38 (all known), GREEN.
- **VPS:** not yet rotating. James runs `forge_check_v3.sh` (VPS.md
  Appendix F), which adds one slot to every 6-hourly check and yesterday's
  report after midnight.
- **Not checked on this date:** the S24; the VPS run of check_v3.

## 2026-11-20

- **the-legacy 1.12.0 frozen** (the AI on the page through ai-gate; Claims
  merged into Ask), 88/88, tagged `v1.12.0`.
- **the-legacy 2.0.0 frozen**: the consolidation of 1.12.0
  (CONSOLIDATION_V2.md, SPEC_V2.md). One module, one boot and one page
  replace a fourteen-layer chain. 1.12.0 is byte-identical in
  `archive/1.12.0/`. 59/59. Run side by side with 1.12.0 against a copy of
  the real ~/.forge: 51 checks, 0 differences. Tagged `v2.0.0`. Merged into
  main as one merge commit, so reverting it returns 1.12.0.
- **VPS:** run-latest v2 picks `boot_v2.py` against the real files (checked
  on the laptop). It is not yet refreshed on the VPS: James runs
  `legacy-refresh`.
- **Not checked on this date:** the S24 (James: no S24 run for 2.0.0).
- **the-saboteur 0.5.0 to 0.9.0 frozen:**
  - 1000 attacks on the Legacy's own layers, against a fixture signed
    with throwaway keys;
  - a run lock (0.5.1);
  - substitution attacks (0.8.0);
  - every known gap class mapped (0.9.0).

  154 are red, in 7 gap classes: rollback, duplicate keys,
  self-certifying rows, deleted rows, unsigned columns, non-canonical
  bytes and substitution. Each fix is a new layer, when James decides.
  No layer raised on any attack. Tagged `v0.9.0`.
- **the-saboteur 1.0.0 frozen:** the consolidation of 0.9.0
  (CONSOLIDATION_V1.md, SPEC_V1.md).
  - One runner, one mutation module and one guard replace a six-layer
    chain.
  - 0.9.0 is byte-identical in `archive/0.9.0/`.
  - 65/65.
  - Gate: 0.9.0 and 1.0.0 each ran all 1000 attacks, PASS 846 / FAIL
    154. All 1000 verdicts are identical.
  - Tagged `v1.0.0`, and merged into main in one commit.
  - The VPS check runs its 65 tests. Rotation (250 attacks every 6 hours,
    a daily report) is planned as 1.1.0.

## 2026-11-19

- **VPS:** run-latest v2 is in place, and the read-only Legacy serves
  1.11.0 (`boot_v1_11.py`). Check v2 is GREEN on all 26 Legacy suites,
  confirmed by James.
- **Agents:** every repository has `agent_<repo>.py` (agent-layer
  0.1.0-dev, 13/13). `python agent-layer/agents.py --no-tests` reports
  31 agents: 26 ok and 4 warn (the four new repositories have no GitHub
  remote yet: ai-gate, consumer, self-layer, agent-layer), with none
  failing. keystone's old digest is a valid old-format signature, not a
  forgery.
- **lllm 0.1.2:** its VERSION now records the 2026-11-13 freezes.
- **Designed, not built:** ai-gate (spec draft 4), consumer (spec draft
  2; story, trading and game designs), P18 Self.

## 2026-11-18 (later): frozen, and files named for their version

James: "freeze", and "if you look at all the _v versions we have there
all over the place we need consistency" (he chose name = version;
`NAMING.md`). Frozen today, each renamed to its version first:

- keystone_gate 1.1.0 (`mediator/digest_v1_1.py`), 65/65.
- forge-time 1.0.1 (`SPEC_V1_0_1.md`), 9/9; capsule `sc/p16-time-v2.sc.json` unsigned, for James.
- mediator-layer 1.1.0 (`mediator_v1_1.py`, `SPEC_V1_1.md`), 19/19; capsule `sc/p17-mediator-v2.sc.json` unsigned, for James.
- the-saboteur 0.4.0 (`saboteur_v0_4.py`), 18/18.
- explorer-d334-forge 1.8.0 (`forge_cli_v1_8.py`: drafts in the order written, a bug the VPS check found), 83/83.
- the-legacy 1.11.0 (`legacy_v1_11.py`, `boot_v1_11.py`: drafts through Cockpit 1.8.0), 78/79 (Q18's race, passes alone).

VPS: check v2 verifies the 26 Legacy repositories (first two runs RED on
fresh-clone setup gaps and the Cockpit order bug, all fixed). run-latest
v2 picks the Legacy boot by header version, so `boot_v1_11.py` is found;
it is written, not yet run on the VPS. Not checked on this date: the S24.

## 2026-11-18

### the-full-stack is reference only

James: "the forge stack was for reference only and not meant to be a
layer involved in the legacy program." The "foundation" sections below
(2026-11-14, 2026-11-15) record what was believed then. They are not
how the Legacy stands. Ties removed today (none frozen yet; tests run on
the laptop):

- keystone_gate 1.1.0: no `forge_core` (65/65).
- forge-time 1.0.1: no foundation agreement test (8/8).
- mediator-layer 1.1.0: `mediator_v2.py`, no `--foundation` (18/18).
- the-saboteur 0.4.0-dev: `saboteur_v3.py`, no default target (18/18).
  Nothing attacks the Legacy layers yet.

Not checked on this date: the S24, the VPS. Plan: `ABSORB_V2.md`.

## 2026-11-15

Only the foundation and the Saboteur were checked on this date; every
other line of 2026-11-14 below is unchanged and not re-checked.

### The foundation

`forge-stack-governance-v7` is the governance root: it adds
`number_encoding` (no fractional JSON numbers) and `hal_score_freshness`
(authoriser scores at most 30 days old). The live spine capsules are
pinned by `forge-stack/manifest-v11`. Hardening 6.2 to 6.4 added six
layers, frozen today at 1.0.0: `sign_v2`, `sign_v3`, `sign_capsule`,
`ledger_v2`, `hal_v3`, `freeze_v3`. 70/70 tests; `sign_v3 --verify`,
`freeze_v3 --check` and `ledger_v2 verify` all green, the first time
the root checks have been clean since August.

### The Saboteur

[JamesTheGiblet/the-saboteur](https://github.com/JamesTheGiblet/the-saboteur)
v2, frozen at 0.3.3: 15 live threats, PASS 15 / FAIL 0 / UGLY 0 against
the foundation. Five threats against the original tools (whose gaps
stay, by the Immutable Rule) are retired to `threats_v2/retired/`.

Not yet checked: the S24 run of either.

## 2026-11-14

### The foundation

[JamesTheGiblet/the-full-stack](https://github.com/JamesTheGiblet/the-full-stack)
is the constitution every layer descends from: the five-stage spine
(Declare → Classify → Trust-score → Audit → Act), forge-c14n-1
canonical JSON, Ed25519 under one did:key, and the governance root
`forge-stack-governance-v6`. Hardening 6.1 (key handling, Master
Mediator fixes) landed today; its CHANGELOG is re-signed and verifies.

### Tier 3: the primitives (P1–P17)

Seventeen layers, one repository each. Every primitive's v1 is frozen.
Newer layers sit on top of v1 (the Immutable Rule: add a layer, never
rewrite one); most of those are frozen too. P10 Weight, P11 Trust and
P15 HAL are at 1.1.0, not yet frozen (README, "Current layers").

| Group | Layers |
| :--- | :--- |
| Crypto and format | P1 Envelope, P2 Sign, P3 Freeze, P16 Time |
| Storage and chain | P4 Ledger, P5 Genesis, P6 Canon Verify, P7 Record, P8 Store, P9 Substrate |
| Trust and logic | P10 Weight, P11 Trust, P12 Rules, P13 DataCube, P14 Leighton Engine |
| Accountability and growth | P15 HAL, P17 Mediator |

P16 Time and P17 Mediator were added today from the foundation,
frozen at 1.0.0, and their primitive capsules sealed by James (P3
Freeze v2). They are the only primitives with a sealed capsule so far.

### Tier 1: the consumers

| Repository | Role |
| :--- | :--- |
| `explorer-d334-forge` | The Cockpit: CLI and web UI |
| `scp-substrate` | The Field: 3D viewer of the memory graph |
| `the-weaver` | The Morning Briefing |
| `sc-os` | The Nerves: multi-node network |
| `the-echo` | The Mirror: "what if" simulation |
| `the-legacy` | The Legacy: one page over all of it |
| `lllm` | The Voice: speaks claims' signed text |

### Infrastructure and outside the stack

- `roadmap`: navigation and the dependency graph (this repository).
- `forge-gate`: sync relay. On GitHub; not cloned on the laptop.
- `forge-queue`: a timed challenge build. Not part of the stack.

### Verification

| Surface | Repositories with tests | Tests | Failing |
| :--- | ---: | ---: | ---: |
| Laptop (`Giblets_Legacy`, run 2026-11-14) | 25 | 1,152 | 0 |
| S24 (fresh clone to `~/Giblets_Legacy`, reported by James) | — | 1,113 | 0 |

The two surfaces hold slightly different sets of repositories (the
phone has `forge-gate` and `forge-queue`; the laptop has
`the-full-stack` and `seed`), which accounts for at least part of the
difference. A per-repository run on both would close it.

Code: about 41,000 lines across the Giblets_Legacy repositories and
about 21,000 in the foundation with its submodules (Python, JavaScript,
HTML, CSS; documentation not counted).

### Philosophy

This is not a SaaS product. It is The Legacy. The system is built to
compensate for human fragmentation: every layer frozen (the Immutable
Rule), documented (Good / Bad / Ugly), and verifiable by anyone, in any
language, on any machine.

"I wanted it. So I forged it. Now forge yours."
— James Gilbert (Giblets Forge)
