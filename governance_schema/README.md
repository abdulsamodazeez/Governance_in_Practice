# Governance schema for community-level datasets

Minimal schema for documenting **consent**, **permitted reuse**, and **provenance** so that community datasets (e.g. agriculture, health) can be used for ML/DS in a traceable, consent-aware way.

## Goals

1. **Document consent** — How was consent obtained? What scope (e.g. research only, model training)?
2. **Permitted use** — What uses are allowed (research, commercial, training)?
3. **Audit trail** — Who collected, when, and what version; supports compliance.

## Schema files

- `schema.yaml` — Canonical field definitions (human- and tool-friendly); includes required vs optional summary.
- `template.json` — Empty template to fill per dataset.
- `example_agriculture.json` — Example filled for one agriculture-style dataset.
- `records/` — Filled governance records for five Africa-related datasets (paper Application section).
- `RATIONALE.md` — Justification for each section (for the paper Schema design section).
- `SCHEMA_TABLE.md` — Table of sections/fields for the paper (copy into LaTeX/Word or use as figure).

## How to use

1. Copy `template.json` for a new dataset.
2. Fill every required field; add optional fields as needed.
3. Store alongside the dataset or in a registry; use `permitted_use` for filtering (e.g. only use records where `model_training_allowed === true` and consent is documented).

## References (for the paper)

- Gebru et al., Datasheets for Datasets.
- Consent frameworks (e.g. GDPR, local norms); cite as appropriate for your context.
