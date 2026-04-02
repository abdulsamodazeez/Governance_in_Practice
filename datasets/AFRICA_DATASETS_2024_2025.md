# Five recent Africa-related datasets (2024–2025)

**Purpose:** Candidate datasets for Step 3 (Application section). All are public, recent, and relevant to African agriculture or health for applying the governance schema.

---

## 1. HarvestStat Africa — Harmonized subnational crop statistics (SSA)

| Field | Detail |
|-------|--------|
| **Domain** | Agriculture |
| **Geography** | Sub-Saharan Africa (33 countries) |
| **Content** | 574,204 records: quantity produced, harvested area, yields; 94 crop types; 1980–2022 (updated through 2025) |
| **Published** | Sept 2024 (data); Nature Scientific Data 2025 (descriptor) |
| **Access** | Dryad (CC0); GitHub (HarvestStat/HarvestStat-Africa) |
| **DOI** | 10.5061/dryad.vq83bk42w |
| **URL** | https://datadryad.org/stash/dataset/doi:10.5061/dryad.vq83bk42w |
| **Citation** | Desbureaux, S. et al. HarvestStat Africa – Harmonized subnational crop statistics for Sub-Saharan Africa. *Nature Scientific Data* (2025). https://doi.org/10.1038/s41597-025-05001-z |

**Governance note:** Aggregate/subnational statistics; consent typically at country/source level. Schema application: document domain (agriculture), geography (SSA/country), provenance (source: FEWS-NET–derived), permitted use (check Dryad/paper).

---

## 2. LSMS-ISA harmonized dataset — Agricultural productivity and welfare (SSA)

| Field | Detail |
|-------|--------|
| **Domain** | Agriculture, welfare (household/individual) |
| **Geography** | Ethiopia, Malawi, Mali, Niger, Nigeria, Tanzania, Uganda |
| **Content** | 200,000+ plot observations; 59,000+ households; 400,000+ individuals; longitudinal 2008–2024 |
| **Published** | 2025 (Nature Scientific Data); Zenodo v1.1 Oct 2024 |
| **Access** | World Bank Microdata Library; Zenodo; GitHub (lsms-worldbank/LSMS-ISA-harmonised-dataset-on-agricultural-productivity-and-welfare) |
| **Zenodo** | https://zenodo.org/records/14016696 |
| **Citation** | Gourlay, S. et al. A longitudinal cross-country dataset on agricultural productivity and welfare in Sub-Saharan Africa. *Nature Scientific Data* (2025). https://doi.org/10.1038/s41597-025-05639-9 |

**Governance note:** Household/plot-level; collected under country-level survey ethics and consent. Schema application: consent_type (household/institutional), consent_scope and permitted_use from World Bank/DHS-style terms; provenance (World Bank, country NSOs).

---

## 3. GROW-Africa — Africa-wide agricultural production database

| Field | Detail |
|-------|--------|
| **Domain** | Agriculture |
| **Geography** | Africa-wide |
| **Content** | 535,844 georeferenced crop yield observations; 25 key crops; mix of government stats, household surveys, plot-level measurements |
| **Published** | July 2025 (Nature Scientific Data) |
| **Access** | See paper for data availability (Nature Scientific Data) |
| **URL** | https://www.nature.com/articles/s41597-025-05257-5 |
| **Citation** | Jain, M. et al. An Africa-wide agricultural production database to support policy and satellite-based measurement systems. *Nature Scientific Data* (2025). https://doi.org/10.1038/s41597-025-05257-5 |

**Governance note:** Multi-scale (regional to plot); assimilated from multiple sources. Schema application: document provenance (multiple sources), domain (agriculture), permitted use (as per paper/repository).

---

## 4. Demographic and Health Surveys (DHS) — e.g. Nigeria 2024, Malawi 2024

| Field | Detail |
|-------|--------|
| **Domain** | Health (fertility, maternal/child health, nutrition, malaria, HIV, etc.) |
| **Geography** | 46+ African countries; recent: Nigeria DHS 2024, Malawi DHS 2024, Zambia 2024, Mali 2023–24 |
| **Content** | Household and individual-level surveys; biomarkers (e.g. Malawi: anthropometrics, anemia, malaria, water quality) |
| **Published** | Ongoing; Nigeria 2024 (Dec 2023–May 2024), Malawi 2024 (May–Aug 2024) |
| **Access** | Registration required; DHS Program (dhsprogram.com); DataFirst (UCT) catalog |
| **URL** | https://dhsprogram.com/data/available-datasets.cfm |
| **Terms** | https://dhsprogram.com/data/Terms-of-Use.cfm |

**Governance note:** Strong consent and use governance: registration, project-specific use, no commercial use, no redistribution of microdata, no identification of individuals/communities; host country owns data. **Ideal for schema application:** consent_documented (yes), consent_scope (research, no commercial), permitted_use (research_allowed yes, commercial_use_allowed no, model_training_allowed per DHS terms), provenance (DHS/country NSO).

---

## 5. HarvestNet — Smallholder farming activity (Ethiopia)

| Field | Detail |
|-------|--------|
| **Domain** | Agriculture (remote sensing + ground labels) |
| **Geography** | Ethiopia (Tigray, Amhara) |
| **Content** | 7,000 hand-labeled images; 2,000 ground labels (harvest piles); 2020–2023 |
| **Published** | AAAI 2024 (dataset paper) |
| **Access** | See paper / repository (HarvestNet) |
| **URL** | https://ojs.aaai.org/index.php/AAAI/article/view/30251 |

**Governance note:** Community/smallholder context; imagery + ground data. Schema application: geography (Ethiopia), domain (agriculture), consent_type (community/household if applicable), provenance (collecting institution from paper).

---

## Summary — all five used for the paper

| Dataset | Domain | Governance record |
|---------|--------|--------------------|
| **HarvestStat Africa** | Ag | `governance_schema/records/harveststat_africa_governance.json` |
| **LSMS-ISA** | Ag + welfare | `governance_schema/records/lsms_isa_governance.json` |
| **GROW-Africa** | Ag | `governance_schema/records/grow_africa_governance.json` |
| **DHS Malawi 2024** | Health | `governance_schema/records/dhs_malawi_2024_governance.json` |
| **HarvestNet (Ethiopia)** | Ag | `governance_schema/records/harvestnet_ethiopia_governance.json` |

**Status:** All five have filled governance records for Section 4 (Application). See `governance_schema/records/README.md`.
