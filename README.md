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

## The Legacy

"I wanted it. So I forged it. Now forge yours."
— James Gilbert (Giblets Forge)
