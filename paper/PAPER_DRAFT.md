# A Minimal Governance Schema for Community-Level Datasets: Consent, Reuse, and Downstream ML in African Agriculture and Health

**DSA 2026 Workshop — Foundational & Practical Data Science in the Age of Generative AI**  
*Draft for LaTeX transfer. Max 5 pages (including references).*

---

## Abstract

Community-level datasets in African contexts (e.g. smallholder agriculture, local health surveys) are underused for data science and ML because consent, permitted reuse, and machine-readable metadata are often unclear. We propose a minimal, domain-agnostic governance schema that captures (1) consent type and scope, (2) permitted use (research, commercial, model training), and (3) provenance and audit fields. We apply the schema to five recent Africa-related datasets—HarvestStat Africa, LSMS-ISA harmonised, GROW-Africa, Malawi DHS 2024, and HarvestNet (Ethiopia)—and show how it supports filtering for ethical downstream ML (e.g. “use only where consent is documented and model training permitted”) and an audit trail for compliance. We provide a reusable template and rationale for data collectors. The work targets practical data governance in the age of generative AI, where reuse and training on community data must be traceable and consent-aware.

**Keywords:** data governance, consent, permitted use, community datasets, Africa, agriculture, health, ML, generative AI.

---

## 1. Introduction

Community-level data from African agriculture and health—smallholder surveys, local health records, household panels—are critical for research, policy, and machine learning. Yet such datasets are often underused because *who* consented to *what*, and *whether* reuse (including model training) is permitted, is rarely documented in a way that downstream users or systems can use [Brown et al.; Chabilall et al.]. Researchers in sub-Saharan Africa report that unclear consent, commercialisation concerns, and weak governance reduce willingness to share data despite recognition of scientific benefits [Chabilall et al.]. At the same time, frameworks for data justice, dynamic consent, and benefit-sharing in African health and agriculture are gaining traction [Munung et al.; Barrett et al.], but they are largely normative or process-oriented. A gap remains: **minimal, machine-readable documentation** of consent, permitted use, and provenance at the *dataset* level, so that (a) data collectors can record governance in a standard way, (b) users can filter datasets by permitted use (e.g. model training allowed, research only), and (c) auditors can trace who collected what and when.

We propose a **governance schema**—a small set of required and optional fields—that fills this gap for community-level datasets in African agriculture and health. The schema extends ideas from Datasheets for Datasets [Gebru et al.] by adding explicit consent and permitted-use fields that Datasheets do not model, and it operationalises concerns from African data governance and ethics literature [Munung et al.; Omutoko et al.; Brown et al.] in a form that supports filtering and audit. We describe the schema (Section 3), apply it to five recent Africa-related datasets (Section 4), and discuss limitations and future work (Section 5). Our contribution is a concrete, reusable artifact: the schema definition, a template, rationales for each section, and five filled governance records that demonstrate application and filtering use cases.

---

## 2. Related Work

Dataset documentation has been advanced by Datasheets for Datasets [Gebru et al.], which standardise motivation, composition, collection process, and recommended uses but do not model consent or machine-readable permitted use. In African contexts, data governance and consent are central: frameworks emphasise data justice and solidarity, dynamic consent, benefit-sharing, and data sovereignty [Munung et al.], and culturally grounded consent processes including multilingual and visual approaches [Omutoko et al.]. Empirical work with health researchers across sub-Saharan Africa shows that trust and willingness to share depend on clear guidelines and governance, while barriers include unclear consent, commercialisation, and legal gaps [Brown et al.; Chabilall et al.]. African data ethics frameworks stress self-determination, communalist practice, and accountability [Barrett et al.; Abebe et al.], and policy work calls for trustworthy, inclusive data governance for AI in Africa [Effoduh et al.]. These efforts are largely normative or process-oriented; a gap remains for minimal, machine-readable documentation of consent, permitted use, and provenance at the dataset level. Our schema fills this gap for community-level datasets in African agriculture and health, enabling filtering for ethical downstream ML and audit trails for compliance.

---

## 3. Schema Design

The schema has five sections: **identification**, **consent**, **permitted use**, **provenance**, and **audit**. Table 1 summarises the fields; a full field list is in the supplementary material.

**Identification.** The schema requires a unique dataset identifier, title, and domain (agriculture, health, or other); geography is optional. This mirrors standard dataset documentation [Gebru et al.] while staying minimal for community collectors.

**Consent.** We capture consent *type* (individual, community, household, institutional, not_applicable, unknown), *scope* (free text: what was consented to), and whether consent is *documented* (boolean); consent_language is optional. This addresses the absence of explicit consent in Datasheets and supports the emphasis on transparent, documented consent in African health and community data [Munung et al.; Brown et al.; Omutoko et al.].

**Permitted use.** Four boolean flags—research_allowed, commercial_use_allowed, model_training_allowed, redistribution_allowed—plus optional free-text use_restrictions make reuse conditions machine-readable. Downstream users can filter (e.g. “use only where model_training_allowed and consent_documented”). This operationalises benefit-sharing and licensing concerns in African data governance [Munung et al.; Chabilall et al.] and supports consent-aware ML in the age of generative AI.

**Provenance.** The collecting organisation is required; collection dates, version, and last_updated are optional. This supports accountability and audit trails [Gebru et al.; Munung et al.; Abebe et al.].

**Audit.** Optional contact_email, governance_review_date, and notes support stewardship and “who to ask” for governance questions [Brown et al.; Effoduh et al.].

**Table 1.** Governance schema sections (compact). Full field-level table in supplementary material.

| Section         | Required fields                                                                 | Optional fields                                   |
|-----------------|----------------------------------------------------------------------------------|---------------------------------------------------|
| Identification  | dataset_id, title, domain                                                        | geography                                         |
| Consent         | consent_type, consent_scope, consent_documented                                 | consent_language                                  |
| Permitted use   | research_allowed, commercial_use_allowed, model_training_allowed, redistribution_allowed | use_restrictions                          |
| Provenance      | collector_org                                                                   | collection_date_start/end, version, last_updated   |
| Audit           | —                                                                               | contact_email, governance_review_date, notes       |

The schema is available as YAML (canonical), JSON template, and filled examples in a public repository (anonymised for review; to be linked in camera-ready).

---

## 4. Application to Five Africa-Related Datasets

We applied the schema to five recent, public, Africa-related datasets: three agriculture (HarvestStat Africa, LSMS-ISA harmonised, GROW-Africa), one health (Malawi DHS 2024), and one agriculture/remote-sensing (HarvestNet, Ethiopia). Table 2 summarises the filled governance records; full JSON records are in the supplementary material.

**Table 2.** Application summary: five datasets and selected governance fields.

| Dataset            | Domain     | Geography        | Consent type   | Research | Commercial | Model training | Redist. | Consent doc. |
|--------------------|------------|------------------|----------------|----------|------------|----------------|---------|--------------|
| HarvestStat Africa | Agriculture | SSA (33 countries) | Institutional  | ✓        | ✓          | ✓              | ✓       | ✓            |
| LSMS-ISA harmonised| Agriculture | 7 SSA countries  | Household      | ✓        | ✗          | ✓              | ✗       | ✓            |
| GROW-Africa        | Agriculture | Africa-wide      | Institutional  | ✓        | ✗          | ✓              | ✗       | ✓            |
| Malawi DHS 2024    | Health     | Malawi           | Individual     | ✓        | ✗          | ✓              | ✗       | ✓            |
| HarvestNet (Ethiopia) | Agriculture | Ethiopia (Tigray, Amhara) | Household | ✓   | ✗          | ✓              | ✗       | ✓            |

**HarvestStat Africa** [Desbureaux et al.] is an aggregate subnational crop-statistics dataset (574k records, 33 SSA countries) under CC0. Consent is institutional (country/source agreements); all uses permitted. The governance record documents provenance (CIRAD/FEWS-NET–derived) and makes explicit that the data is aggregate-only—no individual/household re-identification.

**LSMS-ISA harmonised** [Gourlay et al.] is a longitudinal household and plot-level dataset (7 countries, 2008–2024). Consent type is household; terms (World Bank Microdata Library) allow research and model training but prohibit commercial use and redistribution of microdata. The filled record captures these conditions and provenance (World Bank and national statistical offices).

**GROW-Africa** [Jain et al.] is an Africa-wide assimilated crop-yield database (535k observations) from multiple sources. We document institutional consent, research and model training allowed, no commercial or redistribution, and multi-source provenance.

**Malawi DHS 2024** is a demographic and health survey (22k+ households; biomarkers). DHS has strong governance: individual consent, documented; research and model training allowed for registered projects; commercial use and microdata redistribution prohibited; no identification of individuals or communities. The governance record encodes these conditions and serves as a health-sector example where consent and permitted use are explicit.

**HarvestNet** (Ethiopia) is a smallholder remote-sensing and ground-label dataset (Tigray, Amhara). We record household-level consent, research and model training allowed, no commercial or redistribution, and provenance from the project.

**Filtering and audit.** With the schema, a user can (1) **filter for ethical ML:** e.g. “use only datasets where consent_documented = true and model_training_allowed = true” (all five qualify; for DHS, additional registration applies). (2) **Filter by domain or geography:** e.g. health only (Malawi DHS) or Ethiopia (HarvestNet). (3) **Audit:** provenance and audit fields support “who collected, when, who to contact” for compliance or re-use decisions. This demonstrates that the schema is applicable across aggregate and microdata, agriculture and health, and supports both consent-aware reuse and accountability.

---

## 5. Discussion and Limitations

**Takeaways.** The schema is minimal (few required fields), domain-agnostic within ag/health, and machine-readable, so it can sit alongside existing policies [Effoduh et al.] and support guidelines that researchers in SSA have called for [Brown et al.; Chabilall et al.]. Applying it to five diverse datasets shows that consent type and permitted use vary (institutional vs household vs individual; CC0 vs restricted), and that encoding them in a standard way enables filtering and audit without replacing existing terms of use.

**Limitations.** Filled records were produced by the authors from public documentation and terms; they are not formally endorsed by data custodians. Adoption depends on institutional or national guidelines and incentives for data collectors to complete the template. The schema does not enforce compliance—it documents conditions; enforcement remains with custodians and legal frameworks. We did not validate the schema with data collectors or RECs in Africa; such validation is important future work.

**Future work.** (1) Tooling: a simple form or checklist for collectors; (2) alignment with African data ethics frameworks [Barrett et al.] and with data justice principles [Munung et al.]; (3) adoption pilots with one or two African institutions or consortia; (4) extension to retention or data minimisation if needed by local regulation.

---

## 6. Conclusion

We proposed a minimal governance schema for community-level datasets that captures consent type and scope, permitted use (research, commercial, model training, redistribution), and provenance and audit fields. We applied it to five recent Africa-related datasets in agriculture and health and showed how it supports filtering for ethical downstream ML and audit trails. The schema, template, rationales, and filled records are provided as a reusable artifact for practical data governance in the age of generative AI, where reuse and training on community data must be traceable and consent-aware.

---

## References (to be formatted in LaTeX; key sources)

1. Barrett et al., African Data Ethics: A Discursive Framework for Black Decolonial Data Science, arXiv:2502.16043, 2025.
2. Brown et al., Trust as moral currency: Perspectives of health researchers in sub-Saharan Africa on strategies to promote equitable data sharing, PLOS Digital Health, 2024.
3. Chabilall et al., Data as scientific currency: Challenges experienced by researchers with sharing health data in sub-Saharan Africa, PLOS Digital Health, 2024.
4. Desbureaux et al., HarvestStat Africa – Harmonized subnational crop statistics for Sub-Saharan Africa, Nature Scientific Data, 2025.
5. Effoduh et al., Toward a trustworthy and inclusive data governance policy for the use of artificial intelligence in Africa, Data & Policy, 2024.
6. Gebru et al., Datasheets for Datasets, Communications of the ACM, 2021.
7. Gourlay et al., A longitudinal cross-country dataset on agricultural productivity and welfare in Sub-Saharan Africa, Nature Scientific Data, 2025.
8. Jain et al., An Africa-wide agricultural production database to support policy and satellite-based measurement systems, Nature Scientific Data, 2025.
9. Munung et al., Cultivating an equity-oriented data sharing culture for African health research initiatives, Nature Communications, 2025.
10. Omutoko et al., Understanding and processing informed consent during data-intensive health research in sub-Saharan Africa, Research Ethics, 2024.
11. Abebe et al., Narratives and counternarratives on data sharing in Africa, ACM FAccT, 2021.

*[DHS Program Terms of Use: dhsprogram.com/data/Terms-of-Use.cfm. HarvestNet: AAAI 2024.]*

---

**Supplementary material (to be linked):** Full schema (YAML), JSON template, five filled governance records (JSON), and field-level schema table.
