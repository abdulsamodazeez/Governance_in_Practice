# Rationale for governance schema sections

**Purpose:** Short justification for each section of the schema, for use in the paper (Schema design section). Citations refer to the digested literature in `../literature/DIGESTED_LITERATURE.md`.

---

## 1. Identification

**Rationale:** Enables unique reference to the dataset and basic filtering by domain and geography. Minimal identification (id, title, domain) is required for any governance record; geography is optional where datasets span multiple regions or are anonymised at location level. Aligns with dataset documentation practice (Gebru et al. — motivation, composition) while keeping the schema lightweight for community-level use.

**For the paper (1–2 sentences):** The identification section provides a unique identifier, title, domain (agriculture, health, other), and optional geography so that datasets can be referenced and filtered. This mirrors standard dataset documentation (Gebru et al.) while remaining minimal for community collectors.

---

## 2. Consent

**Rationale:** Documents *what* was consented to and *whether* it is recorded, addressing the gap that Datasheets do not model consent (Gebru et al.). Consent type (individual, community, household, institutional, etc.) reflects African contexts where community or household consent is common (Munung et al.; Omutoko et al.). Consent scope and consent_documented support transparency and accountability demanded by SSA health researchers (Brown et al.; Chabilall et al.). Optional consent_language supports multilingual consent processes (Omutoko et al.).

**For the paper (1–2 sentences):** The consent section captures consent type, scope, whether consent is documented, and optionally the language(s) used. This addresses the absence of explicit consent in standard dataset documentation (Gebru et al.) and supports the emphasis on transparent, documented consent in African health and community data (Munung et al.; Brown et al.; Omutoko et al.).

---

## 3. Permitted use

**Rationale:** Makes reuse conditions machine-readable so that downstream users and systems can filter by permitted use (e.g. “use only where model_training_allowed and research_allowed”). Research, commercial, model training, and redistribution are the main reuse dimensions identified in governance and benefit-sharing literature (Munung et al.; Chabilall et al.). Explicit model_training_allowed supports consent-aware ML in the age of generative AI (workshop theme). Free-text use_restrictions allow additional conditions (e.g. “non-commercial research only”).

**For the paper (1–2 sentences):** The permitted use section provides boolean flags for research, commercial use, model training, and redistribution, plus optional free-text restrictions. This enables filtering for ethical downstream ML (e.g. use only datasets where model training is permitted) and operationalises benefit-sharing and licensing concerns raised in African data governance (Munung et al.; Chabilall et al.).

---

## 4. Provenance

**Rationale:** Records who collected the data and when, supporting accountability and audit trails (Munung et al.; Barrett et al.; Abebe et al.). Collector_org is required; dates and version are optional but recommended for compliance and re-use decisions. Aligns with Datasheets’ “collection process” and “maintenance” (Gebru et al.) and with the need for transparent, accountable reuse in African contexts (Abebe et al.).

**For the paper (1–2 sentences):** The provenance section records the collecting organisation (required) and optionally collection dates, version, and last update. This supports accountability and audit trails for compliance and aligns with calls for transparent, accountable data reuse (Gebru et al.; Munung et al.; Abebe et al.).

---

## 5. Audit

**Rationale:** Optional contact and governance review date support ongoing stewardship and compliance checks. Notes allow for exceptions, clarifications, or references to institutional policies. Keeps the schema minimal while enabling “who to ask” and “when last reviewed” for data governance (Effoduh et al.; Brown et al.).

**For the paper (1–2 sentences):** The audit section provides optional contact, governance review date, and notes to support stewardship and compliance. It keeps the schema lightweight while enabling accountability and “who to ask” for governance questions (Brown et al.; Effoduh et al.).
