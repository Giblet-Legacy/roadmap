# The Forge Stack — Status Report

STATUS.md — where the whole stack stands on one date.

Function:
    A one-page status of the Forge Stack: what is built, what is frozen,
    what is signed and what the tests say. Each claim is one checked on
    that date; anything not checked is marked as such. A new date gets a
    new section at the top, never an edit to an old one.

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
