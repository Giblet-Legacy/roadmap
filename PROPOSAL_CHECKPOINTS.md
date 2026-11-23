# PROPOSAL — checkpoints: the trusted, current heads the gap fixes need

PROPOSAL_CHECKPOINTS.md — where trusted checkpoints live, who signs them, how freshness is proven, and the order to switch the gap fixes on. Design only.

Function:
    The Saboteur's 154 red threats have draft fixes, each a new version
    beside the frozen one, uncommitted on 2026-11-22: ledger_v3,
    canon_verify_v3, store_v3, record_v3 and substrate_v5. Every one of
    them needs a **trusted, current checkpoint** from its caller:

    | Draft | Checkpoint it needs |
    |---|---|
    | ledger_v3, canon_verify_v3 | the ledger's head |
    | store_v3 | the store's head |
    | record_v3 | the record's SHA-256 |
    | substrate_v5 | an approved snapshot digest |

    Each spec warns of the same two traps:
    - a checkpoint read from the data it vouches for cannot detect
      rollback;
    - an old checkpoint accepted as current cannot either.

    Where checkpoints live, who signs them, and how "current" is proven
    is undesigned. This is that design. The decisions are James's (§8).

Status:   agreed 2026-11-23, then amended after the red team (§9: several witnesses); run 0003 parked; not built
Licence:  MSL-1.0
Author:   James Gilbert (Giblets Forge)

---

## 1. What a checkpoint is

A checkpoint is a **signed capsule** (P2 sign_v2, under the owner's key):

    {"type": "checkpoint", "subject": "store",          # a logical name, never a path
     "kind": "store-head",                               # ledger-head | store-head | record-sha256 | substrate-snapshot
     "value": "<64 lowercase hex>",
     "seq": 42,                                          # +1 per subject, never reused
     "prev": "<sha256 of the previous checkpoint for this subject>",
     "at": "2026-11-22T12:00:00Z"}                       # P16 forge-time

- **Hashes only:** no content. A checkpoint can be shown or copied
  anywhere without exposing anything (R9 safe).
- **`seq` and `prev`** chain each subject's checkpoints, so a gap or a
  replaced checkpoint is visible.

## 2. Where checkpoints live

`~/.forge/checkpoints.jsonl`, an **append-only P4 ledger of checkpoints**.
It is the stack's own primitive, with chained and signed entries. Nothing
new to trust.

Being a ledger, the checkpoint log could itself be rolled back. So it needs
a **witness** outside it (§3).

## 3. Freshness: the VPS as witness

**After every checkpoint,** the laptop pushes the latest checkpoint for
that subject to the VPS: `/srv/forge/witness/<subject>.json`.

- That's public data: a signed capsule of hashes.
- **The VPS holds no key.** It only keeps the highest `seq` it has seen,
  and refuses a lower one.

**A verifier compares the local checkpoint with the witness:**

| Local `seq` vs witness | Means | Result |
|---|---|---|
| equal | current | **verified** |
| lower | rolled back, locally | **FAIL** |
| higher | the witness lags (offline, a push failed) | **verified, unwitnessed**, and the push is retried |
| no witness reachable | can't prove freshness | **verified, unwitnessed**, reported plainly, never hidden |

"Unwitnessed" is to freshness what λ = 1.0 is to trust: **unknown, not
failed**. It shows in the daily report, so a long-unwitnessed subject gets
noticed.

## 4. Who writes checkpoints, and when

- **Ledgers and stores:** the writer that appends (the Legacy) appends the
  checkpoint **in the same operation**:
  1. the data first;
  2. then the checkpoint, signed by the same owner key that already signs
     every entry;
  3. then the witness push.
- **A crash between data and checkpoint** leaves the data *ahead* of its
  checkpoint. The verifier accepts **checkpointed prefix + a valid signed
  extension**, and rejects only data that is **shorter** (rollback) or
  **diverges** (a fork). The drafts compare for equality, so this needs one
  added mode (§8.2).
- **Records:** each record's SHA-256 is checkpointed when it is written
  (subject `record:<name>`).
- **The substrate:** substrate_v5's `checkpoint_candidate` cannot discover
  rows deleted earlier, so a candidate is **approved by James**, with a HAL
  seal (P15). It is never approved automatically. This is the one place a
  human must sign each checkpoint.

## 5. The first checkpoints: trust on first use, recorded

Today's heads can only be trusted as far as the frozen verifiers can
vouch for them. For each subject:

1. verify with the frozen layer (v2 / v2.1 / v4);
2. James signs the first checkpoint;
3. the CHANGELOG records **"trusted on first use, 2026-MM-DD"**.

Anything rolled back **before** that date cannot be detected. That is
stated, not hidden.

## 6. Switching on, in order

1. **The checkpoint log and the witness** (§2, §3). Nothing changes for
   readers yet.
2. **Migrate the store** (`store-layer/migrate_v3.py`, rehearsed on a copy
   2026-11-22):
   - 401 of 630 records are rewritten into canonical form;
   - no hash or signature changes;
   - v2.1 still verifies, so the Legacy is unaffected.
3. **The first checkpoints** (§5), signed by James.
4. **The Saboteur:** a new rotation version runs the threats against the
   v3/v5 layers, with fixture checkpoints.
   - Gaps that now pass show as **healed**. That's RED in 1.1.0, by
     design, so James sees each one.
   - They come off `known_gaps` only on his word, recorded in the
     CHANGELOG.
5. **The Legacy adopts the v3/v5 readers** and the coordinated append (§4).
6. **Each draft is frozen,** after its checklist run (P19: advise first, a
   run per new major version).

## 7. Cautions

- **A stolen owner key forges checkpoints too.** Checkpoints defend
  against rollback and substitution, not key theft. That is the key's own
  problem (sign-layer).
- **The witness proves freshness only as far as it has heard.** A
  long-offline laptop is unwitnessed. It's shown, not failed.
- **"Trusted on first use"** leaves history before day one unprotected
  (§5).

## 8. Decisions for James

1. **The checkpoint log:** a P4 ledger at `~/.forge/checkpoints.jsonl`,
   signed by the owner key in the same write as the data. Recommended.
2. **Prefix and extension:** for ledgers and stores, a verifier accepts a
   checkpointed prefix plus a valid signed extension, so a crash between
   writes isn't mistaken for an attack. That needs one added mode in
   ledger_v3 and store_v3. Records and substrate snapshots stay
   exact-match. Recommended.
3. **The VPS as witness:** it holds the latest signed checkpoint per
   subject and no key. "Unwitnessed" is reported, never failed.
   Recommended.
4. **The substrate:** each checkpoint approved by James with a HAL seal.
   Recommended.
5. **Where the code lives:** a new primitive, **P20 Checkpoint**
   (`checkpoint-layer`), used by P4, P6, P7, P8 and P9. Recommended over
   spreading it across them. It gets a P19 checklist run before it's
   built.
6. **The order of §6:** recommended as written. The store migration
   (step 2) can run whenever James chooses: it is reversible from its
   backup, and v2.1 still verifies afterwards, so the Legacy is
   unaffected. James runs it.

---

## 9. After the red team: several witnesses (2026-11-23)

Run 0003 (validation-layer) was red-teamed by a fresh AI agent. Its main
finding, checked against VPS.md, holds: **the VPS witness is not
independent of the laptop.**

- The laptop already syncs whole databases there, and holds the SSH and
  sudo path into it, so whoever can roll back the laptop can usually
  rewrite the witness too.
- An "unwitnessed" result also passed, so rolling back and then blocking
  the push went unnoticed.

As written, §3 catches **accidental** rollback, not a deliberate attacker
on the laptop.

**James's decision: B, several witnesses.** It replaces §3 and §8.3:

1. **Three witnesses:**
   - **the VPS;**
   - **the S24**, the second device in James's dual-device workflow;
   - **GitHub**, a checkpoint-witness repository whose commit history the
     laptop can add to.

   An attacker must control all three to hide a rollback.
2. **Every witness checks** each checkpoint's signature against the
   owner's public key before keeping it, and keeps only a higher `seq`.
   A forged high `seq` is refused, not stored.
3. **The rule:** a local `seq` below **any** witness is a rollback and
   **FAILS**. An equal `seq` with a different value is a **fork** and
   **FAILS**.
4. **Unwitnessed for more than 24 hours is not verified.** It shows as
   **STALE**, fails the daily check, and is asked about. Under 24 hours,
   it's still "verified, unwitnessed".
5. **Still to design before building** (the review's other findings):
   - crash handling for records and the substrate, which stay
     exact-match (§4);
   - truncation after the last checkpoint;
   - a torn half-line;
   - the credentials each witness push needs;
   - first checkpoints cross-checked against the VPS's older synced
     copies.

Run 0003 is **PARKED** until this section is designed in full and
red-teamed again.

## Document control

- 2026-11-22: drafted by the VS Code AI from the five draft SPECs (ledger_v3,
  canon_verify_v3, store_v3, record_v3, substrate_v5) and the store
  migration rehearsal.
- 2026-11-23: **agreed.** James: "yes to all checkpoint decisions" (§8.1–6,
  as recommended).
  - **Next, by decision 5:** a P19 checklist run on P20 Checkpoint before
    any of it is built (validation-layer `runs/0003`).
  - **The store migration** (§6.2) is James's to run, when he chooses.
- 2026-11-23: red-teamed (run 0003). James: "b park 0003": §9 replaces the single VPS witness with three (VPS, S24, GitHub), and unwitnessed for more than 24 hours is not verified.
