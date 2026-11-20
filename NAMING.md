# Naming: a file says its version

NAMING.md — the one rule for versioned file names in every Legacy repository, and a map for the frozen files that predate it.

Function:
    Records James's rule of 2026-11-18 ("if you look at all the _v
    versions we have there all over the place we need consistency"; he
    chose "name = version"), how it applies to modules, specs, tests and
    pages, and which frozen files still use the old counter names, with
    the version each one shipped. Navigation only.

## The rule

A versioned file is named after the version it ships.

| Version | Suffix | Examples |
|---|---|---|
| X.0.0 | `_vX` | `sign_v2.py`, `SPEC_V2.md`, `test_sign_v2.py` |
| X.Y.0 | `_vX_Y` | `forge_cli_v1_8.py`, `SPEC_V1_8.md`, `legacy_v1_11.py`, `boot_v1_11.py`, `static/projection_v1_11.html` |
| X.Y.Z | `_vX_Y_Z` | `SPEC_V1_0_1.md` |

- **Modules, specs and pages** follow the table.
- **A module's tests** are `test_<module>.py` (`mediator_v1_1.py` is tested
  by `test_mediator_v1_1.py`).
- **A frozen suite carried into a later version with a change** is
  `<suite>_at_v<version>.py` (`test_forge_v1_2_at_v1_8.py`,
  `test_mediator_at_v1_1.py`, `test_forge_time_at_v1_0_1.py`). The
  original stays byte-identical in `archive/<old version>/`, which
  `pytest.ini` keeps out of collection.
- **Folders that belong to a version** follow it too (`threats_v0_4/`).
- **Not covered:** an SCP capsule id's `-vN` (`p16-time-v2`) is SCP's own
  identity counter. A revised capsule is a new identity, whatever the
  layer's version.
- **Never rename a frozen file.** Signed capsules and the VPS pin paths.
  A repository comes into line at its next consolidation (one clean
  major version, old layers archived byte-identical; governance-v8
  `consolidation`, which James stated himself).
- **Unfrozen work is marked `-dev`** in its header `Version:` until it is
  frozen. The VPS runs a boot only if its version is not above VERSION
  (run-latest v2, VPS.md).

## Frozen files with the old counter names

Until each repository is consolidated, these names do not say their
version. The version each one shipped:

### the-legacy (in line from 2.0.0)

The Legacy came into line at its 2.0.0 consolidation (2026-11-20; the-legacy
CONSOLIDATION_V2.md): `legacy_v2.py`, `boot_v2.py`, `SPEC_V2.md` and
`static/projection_v2.html` are 2.0.0. Every file below is now in
`archive/1.12.0/`, byte-identical, and at the tag `v1.12.0`. Four of the
old counter names (`legacy_v2.py`, `boot_v2.py`, `SPEC_V2.md`,
`test_legacy_v2.py`) are reused at the root by 2.0.0; their 0.1.2 and 1.5.0
bytes are the archived ones.

| File | Version | | File | Version |
|---|---|---|---|---|
| `legacy_v2.py`, `SPEC_V2.md` | 0.1.2 | | `boot.py`, `legacy_v8.py`, `SPEC_V8.md` | 1.4.0 |
| `legacy_v3.py`, `SPEC_V3.md` | 0.1.3 | | `boot_v2.py`, `SPEC_V9.md` | 1.5.0 |
| `legacy_v4.py`, `SPEC_V4.md` | 1.0.0 | | `legacy_v9.py`, `boot_v3.py`, `SPEC_V10.md` | 1.6.0 |
| `legacy_v5.py`, `SPEC_V5.md` | 1.1.0 | | `legacy_v10.py`, `boot_v4.py`, `SPEC_V11.md` | 1.7.0 |
| `legacy_v6.py`, `SPEC_V6.md` | 1.2.0 | | `boot_v5.py`, `SPEC_V12.md` | 1.8.0 |
| `legacy_v7.py`, `SPEC_V7.md` | 1.3.0 | | `legacy_v11.py`, `boot_v6.py`, `SPEC_V13.md` | 1.9.0 |
| | | | `legacy_v12.py`, `boot_v7.py`, `SPEC_V14.md`, `projection_v10.html` | 1.10.0 |

From 1.11.0 the names follow the rule (`legacy_v1_11.py`, `boot_v1_11.py`,
`SPEC_V1_11.md`, `projection_v1_11.html`; 1.12.0 is `legacy_v1_12.py`,
`boot_v1_12.py`, `SPEC_V1_12.md`, `projection_v1_12.html`), also archived.
Old suites carried into 2.0.0 are `<suite>_at_v2.py` (`test_legacy_v4_at_v2.py`).

### Primitives and other consumers

| Repository | File | Version |
|---|---|---|
| hal-layer (P15) | `hal_v2.py`, `SPEC_V2.md` | 1.1.0 |
| leighton-engine-layer (P14) | `leighton_engine_v2.py`, `SPEC_V2.md` | 1.1.0 |
| | `leighton_engine_v3.py`, `SPEC_V3.md` | 1.2.0 |
| trust-layer (P11) | `trust_v2.py`, `SPEC_V2.md` | 1.1.0 |
| weight-layer (P10) | `weight_v2.py`, `SPEC_V2.md` | 1.1.0 |
| sc-os | `peer_v2.py`, `SPEC_V2.md` | 0.2.0 |
| | `SPEC_V3.md` (nerves.py) | 0.3.0 |
| the-saboteur | `saboteur_v2.py`, `harness_guard_v2.py`, `mutations_v2.py`, `SPEC_V2.md`, `threats_v2/` | 0.3.0–0.3.3 |

Every other repository already follows the rule: canon-verify, datacube,
envelope, freeze, genesis, ledger, record, rules, sign, store, substrate,
scp-substrate and the-legacy from 2.0.0 (`_vX` for X.0.0), and the Cockpit,
the Weaver, the Echo, lllm and forge-time (`_vX_Y`).

## Renamed before their freeze (2026-11-18)

| Built as | Frozen as | Repository, version |
|---|---|---|
| `mediator/digest_v2.py` | `mediator/digest_v1_1.py` | keystone_gate 1.1.0 |
| `test_forge_time_v1_0_1.py` | `test_forge_time_at_v1_0_1.py` | forge-time 1.0.1 |
| `mediator_v2.py`, `SPEC_V2.md`, `test_mediator_v2.py`, `test_mediator_v1_1.py` | `mediator_v1_1.py`, `SPEC_V1_1.md`, `test_mediator_v1_1.py`, `test_mediator_at_v1_1.py` | mediator-layer 1.1.0 |
| `saboteur_v3.py`, `SPEC_V3.md`, `threats_v3/` | `saboteur_v0_4.py`, `SPEC_V0_4.md`, `threats_v0_4/` | the-saboteur 0.4.0 |
| `test_forge_v1_2_v2.py` | `test_forge_v1_2_at_v1_8.py` | explorer-d334-forge 1.8.0 |
| `legacy_v13.py`, `boot_v8.py`, `SPEC_V15.md`, `projection_v11.html` | `legacy_v1_11.py`, `boot_v1_11.py`, `SPEC_V1_11.md`, `projection_v1_11.html` | the-legacy 1.11.0 |
