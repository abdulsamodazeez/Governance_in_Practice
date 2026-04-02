# Governance in Practice

**A Minimal Schema for Consent and Reuse of Community Data in African Agriculture and Health**

This repository contains the governance schema, filled records, Streamlit tool, and paper source for the DSA 2026 Workshop submission.

## Overview

Community-level datasets in African agriculture and health remain underused because consent, permitted reuse, and machine-readable metadata are rarely clear. This project introduces a minimal governance schema that records:

1. **Consent** type and scope
2. **Permitted use** (research, commercial, model training, redistribution)
3. **Provenance** and audit information

The schema is applied to five recent Africa-related datasets: HarvestStat Africa, LSMS-ISA harmonised, GROW-Africa, Malawi DHS 2024, and HarvestNet (Ethiopia).

## Repository Structure

```
├── governance_schema/       # Schema definition, template, rationale, and filled records
│   ├── schema.yaml          # YAML schema specification
│   ├── template.json        # Blank JSON template
│   ├── RATIONALE.md         # Design rationale for each field
│   └── records/             # Five filled governance records
├── datasets/                # Notes on Africa-related datasets (2024-2025)
├── literature/              # Digested literature review
├── tool/                    # Streamlit app for creating and browsing records
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
├── DSA2026_paper/           # LaTeX source for the DSA 2026 workshop paper
│   ├── main.tex
│   ├── references.bib
│   └── dsa2026.sty
└── DLI2026_paper/           # LaTeX source for the DLI 2026 submission (IJCAI format)
    ├── main.tex
    ├── references.bib
    ├── ijcai26.sty
    └── named.bst
```

## Streamlit Tool

To run the governance-record tool locally:

```bash
cd tool
pip install -r requirements.txt
streamlit run app.py
```

The tool allows browsing and filtering the five governance records by domain, consent type, and permitted-use flags, and creating new records through a guided form.

## Schema

The schema has five sections:

| Section        | Required fields                              | Optional fields                  |
|----------------|----------------------------------------------|----------------------------------|
| Identification | dataset_id, title, domain                    | geography                        |
| Consent        | consent_type, scope, documented              | consent_language                 |
| Permitted use  | research, commercial, model_training, redist | use_restrictions                 |
| Provenance     | collector_org                                | dates, version, last_updated     |
| Audit          | —                                            | contact, review_date, notes      |

## Licence

This project is released for academic and research purposes.
