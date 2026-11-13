# CHANGELOG — roadmap

## [Unreleased]

### Good

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
