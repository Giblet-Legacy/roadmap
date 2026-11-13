# ⚒️ The Forge Stack

The Forge Stack is a sovereign, local-first AI architecture. It is not a SaaS product. It is a set of frozen, signed primitive layers that compose into a working system you can verify yourself, in any language, on any machine.

## Documentation

- [`README.md`](README.md) — this file (overview, primitive layers, dependency graph)
- [`TIERS.md`](TIERS.md) — the four architectural tiers (Consumers, Spine, Primitives, Hardware)

## The 15 Primitive Layers (Tier 3 — COMPLETE)

| Layer | Repository | Purpose |
| :--- | :--- | :--- |
| **P1** | [`envelope-layer`](https://github.com/Giblet-Legacy/envelope-layer) | Canonicalisation, SHA-256, Ed25519, did:key |
| **P2** | [`sign-layer`](https://github.com/Giblet-Legacy/sign-layer) | Capsule signing and detached `.sig` sidecars |
| **P3** | [`freeze-layer`](https://github.com/Giblet-Legacy/freeze-layer) | Inject `document_sha256` before signing |
| **P4** | [`ledger-layer`](https://github.com/Giblet-Legacy/ledger-layer) | ChronoSCRIBE: hash-chained append-only log |
| **P5** | [`genesis-layer`](https://github.com/Giblet-Legacy/genesis-layer) | Mint the root ledger's first batch |
| **P6** | [`canon-verify-layer`](https://github.com/Giblet-Legacy/canon-verify-layer) | Zero-trust independent verifier |
| **P7** | [`record-layer`](https://github.com/Giblet-Legacy/record-layer) | Passphrase-protected keys and disk I/O |
| **P8** | [`store-layer`](https://github.com/Giblet-Legacy/store-layer) | SQLite ledger per node |
| **P9** | [`substrate-layer`](https://github.com/Giblet-Legacy/substrate-layer) | Semantic memory graph (Claims, Evidence) |
| **P10** | [`weight-layer`](https://github.com/Giblet-Legacy/weight-layer) | Leighton neutral-attractor decay formula |
| **P11** | [`trust-layer`](https://github.com/Giblet-Legacy/trust-layer) | Trust fusion engine |
| **P12** | [`rules-layer`](https://github.com/Giblet-Legacy/rules-layer) | Rule engine firing from capsules |
| **P13** | [`datacube-layer`](https://github.com/Giblet-Legacy/datacube-layer) | Six-face classifier and Keystone Gate |
| **P14** | [`leighton-engine-layer`](https://github.com/Giblet-Legacy/leighton-engine-layer) | Canonical λ computation |
| **P15** | [`hal-layer`](https://github.com/Giblet-Legacy/hal-layer) | Human Accountability Layer |

## Verifying the Stack

Each layer has its own test suite. Run them in dependency order. Total: 731+ passing tests across the stack.

## Current layers (2026-11-13 review)

"COMPLETE" above means every primitive's **v1 is frozen**. Each layer
has since grown stricter layers above v1 (Immutable Rule: add a layer,
never rewrite). New code imports the module in the middle column.

| Layer | Import | State |
| :--- | :--- | :--- |
| P1 | `envelope_v2` | frozen 2.0.0 |
| P2 | `sign_v2` | frozen 2.0.0 |
| P3 | `freeze_v2` | frozen 2.0.0 |
| P4 | `ledger_v2` | frozen 2.0.0 (2026-11-13) |
| P5 | `genesis_v3` | frozen 3.0.0 |
| P6 | `canon_verify_v2` | frozen 2.0.0 |
| P7 | `record_v2` | frozen 2.0.0 |
| P8 | `store_v2_1` | frozen 2.1.0 |
| P9 | `substrate_v3` | frozen 3.0.0 |
| P10 | `weight_v2` | 1.1.0 |
| P11 | `trust_v2` | 1.1.0 |
| P12 | `rules_v3` | frozen 3.0.0 |
| P13 | `datacube_v2` | frozen 2.0.0 |
| P14 | `leighton_engine_v3` | frozen 1.2.0 |
| P15 | `hal_v2` | 1.1.0 |

All frozen on James's sign-off ("freeze all", 2026-11-13). Confirmed on
the S24 by James the same day.

## Dependency graph

Arrows read "is used by". Every layer also uses P1.

```
P1 Envelope ─► P2 Sign ─► P3 Freeze
P1 ─► P4 Ledger ─► P5 Genesis
P4 ─► P8 Store
P6 Canon Verify            (standalone: imports no layer; checks P4's files)
P2 ─► P7 Record
P2 ─► P9 Substrate
P10 Weight ─► P11 Trust ─► P14 Leighton Engine
P2 ─► P12 Rules ─► P13 DataCube ◄─ P14
P14, P2, P4 ─► P15 HAL

Consumers
  Cockpit (forge_cli_v1_3)  writes: P13 v3 gate → P2 → P9 → P5/P4 → P8; HAL via P15 → P4 + P9
  SCP Substrate (serve_v4)  reads P9 (verified), keyword clusters     :8085
  Weaver (weaver_v1_3)      reads P9, P14 V3 (days); briefing from claims, LLLM line
  Echo (echo_v1_1)          reads P9, P12 v3, P13, P14 V3
  SC-OS (peer_v2, nerves)   P1, P2, P7; pins at $FORGE_HOME/sc-os/
  The Legacy (legacy_v7)    one page: health, Weaver, Field, Cockpit,  :8080
                            Echo preview -> inbox draft, Nerves, LLLM
  LLLM (JamesTheGiblet/lllm) n-gram model; builds anchored in the ledger by the Cockpit
  The Voice (Giblet-Legacy/lllm, lllm_v0_1_2) speaks claims' signed text, via the Legacy
```

Shared files under `$FORGE_HOME` (default `~/.forge`): `forge.db` (P9),
`ledger.jsonl` (P4, LF only), `store.db` (P8 mirror), `key.pem` (P7),
`sc-os/pins.sc.json` (SC-OS).

## Test totals (2026-11-13, laptop)

957 passing: 778 across the 15 primitive repos, 179 across the six
consumers. Run `python -m pytest -q` in each repo.

## The Legacy

"I wanted it. So I forged it. Now forge yours."
— James Gilbert (Giblets Forge)
