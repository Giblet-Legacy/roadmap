# Absorbing the-full-stack

ABSORB.md — the plan for taking the best of the-full-stack into the Legacy and archiving the rest.

Function:
    Records James's decision of 2026-11-17, what the-full-stack holds,
    where each part goes, and the steps in order. Each step is done only
    on James's word, spec first and tests red first, and anything signed
    is signed by James. Nothing is deleted: "remove" means archive
    (governance-v8, consolidation). This file is updated as steps finish.

## The decision

James, 2026-11-17: "the-full-stack was only ever given as context to
legacy's origins; we need to absorb the best bits and remove the rest".

He chose:

- **Signing key: his Forge key.** Absorbed documents are re-signed with
  the Forge key the Legacy layers and his claims already use. Each one
  records its origin (the-full-stack path, sha256 and foundation
  signature), so the chain back to the foundation key stays provable.
  The Legacy then has one signing identity.
- **Home: a new repository** in the Giblet-Legacy organisation for the
  constitution, the glossary and the spine documents (working name
  `forge-constitution`). This roadmap stays planning only.
- **Consumers: one by one** (table below, confirmed by James).

## What the-full-stack holds

the-full-stack (JamesTheGiblet/the-full-stack, 47 commits since
2026-08-08) is the foundation the Legacy layers were built from.

### Already absorbed: archive

| the-full-stack | Now in |
|---|---|
| `sign.py` | P2 Sign (sign-layer) |
| `freeze.py` | P3 Freeze (freeze-layer) |
| `ledger.py` | P4 Ledger (ledger-layer) |
| `genesis.py` | P5 Genesis (genesis-layer) |
| `datacube.py` | P13 DataCube (datacube-layer) |
| `leighton_weight.py` | P14 Leighton Engine (leighton-engine-layer) |
| `hal.py` | P15 HAL (hal-layer) |
| `forge_core/canon.py` | P1 Envelope (canonical JSON) |
| `master_mediator/` | P17 Mediator (mediator-layer) |
| `consumer/keystone_gate` | Giblet-Legacy/keystone_gate (transferred 2026-11-17) |

### Not yet in any Legacy layer: absorb

1. **The constitution.** Governance up to v9: immutability, ledger
   scopes, number encoding, HAL score freshness, consolidation, the
   six-stage spine.
2. **The terminology and the spine documents.** glossary-v2, the SCP
   specification, DataCube, Leighton Weight (and its engine,
   implementation definition and loop observation), ChronoSCRIBE, HAL
   (and its implementation definition), the gate pattern, AXIOM's
   retirement record.
3. **The hardening the Saboteur forced**, found missing from the
   P-layers on 2026-11-17 (each to be checked again before it is built):
   ledger replay detection (P4), refusal of a stale authoriser score
   (P15), refusal of fractional numbers at signing and a signature on
   every referenced document (P2), and every live pinned hash checked
   against its document (P3).
4. **The audit** (`audit/architectural-gaps-v1`) and its order of work.
5. **The record of where it came from.** the-full-stack's root ledger
   (141 signed entries) and CHANGELOG stay in the archive, readable and
   verifiable; the constitution records the commit and hashes it was
   absorbed from.

### The consumers (confirmed by James, 2026-11-17)

| Consumer | Decision |
|---|---|
| keystone_gate | Done: Giblet-Legacy/keystone_gate |
| ccemk2 | Transfer to the organisation, kept private |
| Nova-bot | Its own repository in the organisation, history kept |
| giblets-forge (style capsules) | Into the constitution repository |
| Long Con Generator | Archive |
| cobblewright, minecraft-main | Archive (the personal minecraft-main repository is untouched) |
| Replicant | Archive the pointer (the personal repository is untouched) |
| lifeforge | Archive |
| echo-chip | Archive |
| fiction (The Dust Margin, The Last Full Stop) | Archive |

Archived means readable, signed and verifiable in the archived
the-full-stack, never deleted. Any of it can come back later as its own
repository.

## The steps

Each step starts only on James's word and ends green.

1. **The constitution repository.** Create it; bring in the
   governance (as the constitution's own v1, recording governance-v9 as
   its origin), glossary-v2, the spine documents, the audit and the
   giblets-forge style capsules, each with its origin record; its own
   ledger; a check that verifies every signature, pinned hash and
   ledger row with the Forge key. James signs. Done when a fresh clone
   verifies green.
2. **The hardening, as new layers.** For each of the four checks in
   "absorb" item 3: confirm it is still missing, then a new layer over
   the P-layer (never an edit), spec and tests red first. Frozen on
   James's word.
3. **The Saboteur turns to the Legacy.** A new Saboteur version attacks
   the constitution and the P-layers instead of the-full-stack; threats
   that only make sense against the-full-stack's tools are retired, as
   threats 03, 05, 09, 11 and 12 were.
4. **The consumers.** ccemk2 transferred (the VPS's read-only deploy key
   moves with it); Nova-bot split out with its history; giblets-forge
   moved in step 1.
5. **The VPS follows.** The verification node checks the Legacy
   repositories, the constitution, keystone_gate and the Saboteur, not
   the-full-stack. VPS.md is updated.
6. **The references.** The repositories that still point at
   the-full-stack (forge-time's foundation test, mediator-layer's
   `--foundation` default, this roadmap's README and STATUS) point at
   the constitution instead, as new layers or document updates.
7. **Archive the-full-stack.** A last CHANGELOG entry and signed record
   say where everything went; then the GitHub repository is archived
   (read-only, kept). The laptop copy is removed only when James says.

## Rules for the whole move

- Nothing frozen is edited; nothing is deleted.
- Every signature is James's, made on the laptop. No key goes on the VPS.
- A step is not done until a fresh clone of what it touched is green.
- This repository is public: no addresses, tailnet names or key ids.
