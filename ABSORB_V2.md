# the-full-stack: reference only

ABSORB_V2.md — replaces ABSORB.md. the-full-stack is not absorbed. It is cut loose and archived as the Legacy's ancestor.

Function:
    Records James's correction of 2026-11-18, what was done about it,
    and what is left. ABSORB.md (2026-11-17) is kept as written; this
    file supersedes it. Each step happens only on James's word, and
    nothing is deleted.

## The correction

James, 2026-11-18: "the forge stack was for reference only and not meant
to be a layer involved in the legacy program", and "the whole repo
should be archived and a doc created or the readme used and stored in
docs as an ancestor to the legacy program".

ABSORB.md still treated the-full-stack as a source: its constitution
re-signed as a new repository, its hardening ported as P-layers, its
Saboteur threats carried over. That was the same mistake made smaller.
The Legacy does not take its authority from the-full-stack. It shows
where the ideas came from, and nothing more.

So, from ABSORB.md:

- **No constitution repository.** The governance (v1–v9), glossary-v2
  and spine documents stay in the archive as history.
- **No hardening "absorbed".** If the Legacy wants any of those checks
  (ledger replay, stale authoriser score, fractional numbers, referenced
  signatures, live pins), each one is ordinary new Legacy work in its
  own right, on James's word, specified from the Legacy layers.
- **The consumer table is on hold.** Everything stays readable in the
  archive. Any consumer can come back as its own repository later.
  keystone_gate already has.
- **Rules James stated himself still stand** (never overwrite, the
  consolidation rule) because he said them, not because the-full-stack
  ratified them.

## The steps (in the order James approved)

| # | Step | State |
|---|---|---|
| 1 | keystone_gate: drop `forge_core` | Done: 1.1.0, `mediator/digest_v2.py`, 1.0.0 files in `archive/1.0.0/` |
| 2 | forge-time: drop the foundation agreement test | Done: 1.0.1, `SPEC_V1_0_1.md` |
| 3 | mediator-layer: drop `--foundation` and its governance | Done: 1.1.0, `SPEC_V2.md`, `mediator_v2.py` |
| 4 | the-saboteur: no default target, the-full-stack refused | Done: 0.4.0-dev, `SPEC_V3.md`, `saboteur_v3.py`; `threats_v3/` empty |
| 5 | This roadmap: ABSORB.md replaced by this file | Done |
| 6 | VPS: stop verifying the-full-stack | See VPS.md |
| 7 | Archive the-full-stack on GitHub (read-only, kept); its README kept as the ancestor document, `the-legacy/docs/ancestor-the-full-stack.md` | See below |

None of 1–4 is frozen. Each waits for James to freeze it.

## Left open

- **Saboteur threats against the Legacy's own layers** (`threats_v3/`).
  Until they exist, nothing attacks the Legacy.
- **Signed capsules that name forge-stack governance** in `inherits`
  (about 35 across the layers) stay as signed. They are history, and
  new capsules use `null`.
- **The laptop clone** `Giblets_Legacy/the-full-stack` is removed only
  when James says.

## Rules

- Nothing frozen is edited; nothing is deleted.
- Every signature is James's, made on the laptop.
- This repository is public: no addresses, tailnet names or key ids.
