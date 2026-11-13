# SPEC — roadmap

SPEC.md — specification for the roadmap repository.

Function:
    Defines what the roadmap repo contains and what it does not.

## 1. Contents
- `README.md` — the 15-layer overview, dependency graph, and
  verification commands.
- `TIERS.md` — the four architectural tiers (Consumers, Spine,
  Primitives, Hardware).
- `CLAUDE.md`, `VERSION`, `CHANGELOG.md`, `.gitignore`,
  `.gitattributes` — standard meta-files.

## 2. Non-contents
- Not a layer. Primitives live in their own `*-layer` repos.
- Not a consumer. Applications live in their own repos.
- No runtime code. Documentation only.

## 3. Update discipline
- The README and TIERS update as layers freeze and consumers ship.
- A new tier or layer is a new section, not a rewrite of prior
  sections. The history of the roadmap itself lives in CHANGELOG.md.
