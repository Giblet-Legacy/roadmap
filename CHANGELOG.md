# CHANGELOG — roadmap

## [Unreleased]

### Good

- `VPS.md` (2026-11-15): the VPS verification node. A locked `forge` user
  runs the foundation's tests, `sign_v3`, `freeze_v3`, `ledger_v2` and the
  Saboteur every 6 hours, GREEN or RED; no signing keys on the machine,
  ccemk2 read through a read-only deploy key. First run GREEN. Includes
  the rebuild steps, the setup script, and what went wrong on the day.
  No addresses or ids: the repository is public.
- Cockpit entry point now forge_cli_v1_6 (frozen 1.6.0, 2026-11-14): `forge answer`
  (v1.5) and `forge imagine` / `forge dreams` (v1.6, local Ollama for dreams only).
- `STATUS.md`: dated status report (2026-11-14), corrected from a phone draft: test
  counts per surface, only v1 of every primitive frozen, P16/P17 the only sealed
  capsules, the foundation listed, P17 grouped with HAL.
- Frozen 2026-11-13 (James: "freeze commmit and push"; laptop run, S24 to confirm): P9 substrate_v4
  4.0.0 (entities, subjects), P13 datacube_v3 3.0.0 (polarity-aware gate),
  Cockpit forge_cli_v1_3 1.3.0, Weaver weaver_v1_3 1.3.0, LLLM Voice
  0.1.2, SCP Substrate serve_v4 4.0.0, The Legacy legacy_v7 1.3.0.
  Consumers updated to those entry points. The LLLM engine is reached
  through LLLM_CLI (its README's shell function is invisible to Python).
- Consumers updated to the current entry points: SCP Substrate
  `serve_v3` (ISO times; v2 broke the field on attested claims), The Legacy
  `legacy_v5`, and a line for the Voice (`Giblet-Legacy/lllm`).
- The Legacy's entry point is now `legacy_v6` (frozen 1.2.0); SCP Substrate
  v3 frozen 3.0.0. S24 runs confirmed on the S24 by James, 2026-11-13.

### Bad

- (none)

### Ugly

- (none)

## [v1.1.0] — 2026-11-13

### Good

- Every layer in the current-layers table is frozen (James: "freeze all", 2026-11-13).
- README: current-layers table, the dependency graph the README promised, shared FORGE_HOME files, and verified test totals (957). Added as new sections (SPEC.md §3); the original sections are unchanged.
- TIERS: the Weaver, the Echo and forge-queue added to Tier 1.

### Bad

- "Tier 3 — COMPLETE" and "731+ tests" are left as written; the new section explains that COMPLETE means every v1 is frozen.

### Ugly

- (none)

## [v1.0.0] — 2026-11-13

### Good
- Initial roadmap and TIERS documentation.
