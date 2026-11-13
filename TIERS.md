# The Four Tiers of the Forge Stack

TIERS.md — the architectural map of The Legacy.

## Tier 1: Consumers
These are the applications that use the primitive layers to do work.

*   **`explorer-d334-forge` (The Cockpit):** The CLI (`./forge`), web UI, spatial pods, and Active Knowledge Building.
*   **`SC-OS` (The Nervous System):** Multi-node agent network, TCP, key pinning, edge microcontrollers (M5StickC).
*   **`scp-substrate` (The Memory):** The 4D semantic graph (Entities, Subjects, Claims, Evidence).
*   **`The Legacy` (The Final GUI):** The ultimate projection of the self. The connector that unifies all the work.

### Tier 1 additions (2026-11-13)
*   **`the-weaver` (The Compensator):** Morning Briefing from fading UNKNOWN claims (P9, P14, LLLM).
*   **`the-echo` (The Mirror):** Read-only "what if I committed this claim?" simulator (P9, P12, P13, P14).
*   **`forge-queue`:** A standalone stdlib job queue (a timed challenge build). Not part of the stack and depends on no layer.

## Tier 2: The Spine Stages
Every artefact in the Forge Stack is produced by exactly one of five stages. The symmetry is enforced, not decorative.

1.  **Declare (P1):** The Semantic Capsule Protocol (SCP) declares intent.
2.  **Classify (P13):** DataCube assigns knowledge to the six faces.
3.  **Trust-score (P10/P11/P14):** The Leighton Engine calculates the neutral-attractor λ.
4.  **Audit (P4/P6):** ChronoSCRIBE signs and anchors the artefact in the hash chain.
5.  **Act (P15):** HAL gates consequential actions behind human validation.

## Tier 3: Primitive Layers (P1–P15) — COMPLETE
The immutable physics of the stack. 15 layers, over 700 passing tests.
*See the main `README.md` for the full list and dependency graph.*

## Tier 4: Physical Environment
The hardware the stack runs on.
*   **The Gate:** Pi 3B (internet-facing).
*   **The Vault:** Ryzen 3300U (air-gapped).
*   **The Edge:** M5StickC microcontrollers.
