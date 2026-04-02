# Governance schema — table for the paper

**Use:** Copy this table into the paper (Schema design section) or convert to a figure. Format as needed for LaTeX/Word.

---

## Table: Governance schema sections and fields

| Section | Field | Type | Required | Description |
|--------|--------|------|----------|-------------|
| **Identification** | dataset_id | string | Yes | Unique identifier (e.g. DOI, internal ID). |
| | title | string | Yes | Dataset title. |
| | domain | string | Yes | Primary domain: agriculture, health, or other. |
| | geography | string | No | Country/region (e.g. Uganda, East Africa). |
| **Consent** | consent_type | string | Yes | individual, community, household, institutional, not_applicable, or unknown. |
| | consent_scope | string | Yes | What was consented to (e.g. research only, publication, reuse). |
| | consent_documented | boolean | Yes | Whether consent is recorded (form, register, etc.). |
| | consent_language | string | No | Language(s) used for consent. |
| **Permitted use** | research_allowed | boolean | Yes | Use for research permitted. |
| | commercial_use_allowed | boolean | Yes | Commercial use permitted. |
| | model_training_allowed | boolean | Yes | Use in ML/AI training (including generative AI) permitted. |
| | redistribution_allowed | boolean | Yes | Redistribution permitted. |
| | use_restrictions | string | No | Free-text restrictions or conditions. |
| **Provenance** | collector_org | string | Yes | Collecting organisation. |
| | collection_date_start | date | No | Start of collection period (YYYY-MM-DD). |
| | collection_date_end | date | No | End of collection period (YYYY-MM-DD). |
| | version | string | No | Dataset version. |
| | last_updated | date | No | Last update (YYYY-MM-DD). |
| **Audit** | contact_email | string | No | Contact for governance enquiries. |
| | governance_review_date | date | No | Date of last governance review (YYYY-MM-DD). |
| | notes | string | No | Additional notes, exceptions, or references. |

---

## Compact version (for figure or slide)

| Section | Required fields | Optional fields |
|--------|------------------|------------------|
| Identification | dataset_id, title, domain | geography |
| Consent | consent_type, consent_scope, consent_documented | consent_language |
| Permitted use | research_allowed, commercial_use_allowed, model_training_allowed, redistribution_allowed | use_restrictions |
| Provenance | collector_org | collection_date_start, collection_date_end, version, last_updated |
| Audit | — | contact_email, governance_review_date, notes |
