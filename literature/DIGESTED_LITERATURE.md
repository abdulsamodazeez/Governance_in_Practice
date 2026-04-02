# Digested Literature — Data Governance, Consent & Community Datasets

**Purpose:** Synthesized takeaways from all listed sources for your DSA 2026 paper (Problem 2). Use this to draft Related work and to sharpen “how we differ.”

---

## 1. Gebru et al. — Datasheets for Datasets (CACM 2021 / arXiv 2018)

**Core idea:** ML datasets should come with standardized documentation (like electronics datasheets): motivation, composition, collection process, recommended uses, maintenance/distribution. No such standard exists today, which harms transparency and accountability in high-stakes domains.

**Key sections they propose:** Motivation → Composition → Collection process → Preprocessing/cleaning → Uses (recommended and not) → Distribution → Maintenance.

**What they do *not* do:** They do **not** model (a) **consent** (type, scope, documented or not), (b) **permitted use** as machine-readable flags (e.g. research / commercial / model training), or (c) **audit** fields (who, when, version) for compliance. Recommended uses are narrative, not structured for filtering.

**Takeaway for your paper:** Datasheets are the canonical “document your dataset” move. Your schema **extends** this by adding **consent + permitted_use + provenance/audit** in a minimal, machine-readable form for community-level datasets (ag/health) and downstream ML.

---

## 2. Munung, Ewuoso, Chimusa & Ogundiran — Equity-oriented data sharing (Nature Commun. 2025)

**Core idea:** African health data sharing should be governed by **data justice** and **data solidarity**, not extractive or charity-driven models. Propose a **four-pillar framework**: (1) fairness and equity, (2) inclusivity and visibility, (3) harm prevention and oversight, (4) reciprocity. Operational roadmap: data sovereignty, controlled access (e.g. CADEs), **dynamic consent**, benefit-sharing, licensing, custodianship.

**Key claims:** Trust-based sharing is insufficient; need accountability, transparency, scientific freedom, equity. Dynamic consent (e.g. SMS/app + offline channels) lets data subjects update preferences. Benefit-sharing and licensing must be formalized. African researchers willing to share when safeguards exist.

**Takeaway for your paper:** They give the **normative and operational** layer (values + roadmap). Your schema is the **technical implementation** layer: machine-readable fields for consent type/scope, permitted use (research/commercial/model training), and provenance so that “consent-for-research only” or “no commercial use” can be **filtered and enforced** at the dataset level.

---

## 3. Brown, Chabilall, Cengiz & Moodley — Trust as moral currency (PLOS Digital Health 2024)

**Core idea:** Qualitative study (16 SSA countries): health researchers see **trust** as central to equitable data sharing. Three strategy themes: (1) **Policy-level** — guidelines at international, national, institutional levels; context matters (“consent cannot be overruled,” country-specific rules); diverse stakeholders (researchers, RECs, lawyers, communities). (2) **Strengthening data governance** — sound governance, data quality, mechanisms to protect researchers and participants. (3) **Reciprocity** — equitable sharing, equity between countries, data sharing with communities.

**Key quotes:** “Guidelines should prioritize non-maleficence, justice… enabling environment for researchers and benefits.” “Protection of research participants… valid informed consent… confidentiality… at the top of every guideline.”

**Takeaway for your paper:** Empirical evidence that researchers **want** guidelines and governance; your schema is a concrete **governance artifact** — a minimal documentation standard that supports “guideline development” and “strengthening data governance” by making consent and permitted use explicit and machine-readable.

---

## 4. Chabilall, Brown, Cengiz & Moodley — Data as scientific currency (PLOS Digital Health 2024)

**Core idea:** Same 16-country sample; focus on **barriers** to sharing. Five themes: (1) **Individual** — fear of sharing, publication pressure, hoarding. (2) **Structural** — data quality, storage, institutional support. (3) **Recognition** — scooping, inadequate acknowledgement. (4) **Ethical** — confidentiality, **informed consent**, commercialisation, **benefit-sharing**. (5) **Legal** — gaps in laws and regulations. Discomfort and reluctance persist despite recognition of scientific benefits; need robust guidelines, governance, data sharing agreements.

**Takeaway for your paper:** Directly supports your **problem statement**: unclear consent, reuse, and governance **reduce** willingness to share. Your schema addresses this by **documenting** consent and permitted use so that “what was agreed” is clear and filterable (e.g. “use only where model_training_allowed and consent_documented”).

---

## 5. Omutoko et al. — Informed consent, multilingualism (Research Ethics 2024)

**Core idea:** In SSA, **language diversity** (2000+ languages) and **multilingualism** make informed consent in data-intensive research hard: terminology, translation, literacy. Propose **alternative mechanisms**: iconography, graphic elicitation, multimedia (e.g. Speaking Books®, Biobanking and Me) to improve comprehension and documentation. GDPR-style “transparency by design” (icons, clear language) noted; many African data laws silent on iconography. RECs should assess consent process and forms; visuals should **complement** text, not replace it.

**Takeaway for your paper:** They focus on **how** consent is obtained and understood (process + format). Your schema focuses on **what** is consented to and **what use is permitted** (structured fields: consent_type, consent_scope, consent_documented, permitted_use). Complementary: they improve comprehension; you make scope and reuse **machine-readable** for governance and filtering.

---

## 6. Barrett, Okolo, Biira et al. — African Data Ethics (arXiv 2025)

**Core idea:** Thematic analysis of 50 documents → **six principles** for African data ethics / decolonial data science: (1) Challenge power asymmetries, (2) Assert data self-determination (“For Africans, by Africans”), (3) Invest in local data institutions & infrastructures, (4) Utilize communalist practices (community-engaged consensus, reciprocal relationships), (5) Center communities on the margins, (6) Uphold common good. Practices include: localized/decentralized practices, data agency (e.g. data trusts, community data management), algorithmic impact assessments, design in solidarity, preserve dignity of data contributors, open data ecosystems that compensate data subjects.

**Takeaway for your paper:** High-level **ethical framework**; your schema **operationalizes** parts of it: documenting consent and permitted use supports “data self-determination” and “protect data agency”; provenance/audit supports “accountability” and “dignity of data contributors.” You can cite them for African data ethics context and state that your schema is one technical instantiation for **community-level datasets**.

---

## 7. Abebe, Aruleba, Birhane et al. — Narratives and counternarratives (ACM FAccT 2021)

**Core idea:** Data-sharing conversations about Africa are often driven by **non-African** stakeholders and **deficit narratives** (lack of education, training, resources). That obscures the real issues: **power imbalances**, colonial legacies, **extractive practices**, disinvestment in **trust**, Western-centric policies ill-suited to African context. Use personas from African data experts to surface **barriers** and **inequities in benefits**. Call for addressing these when sharing data generated on the continent.

**Takeaway for your paper:** Motivates **why** transparent, documented consent and reuse matter — to counter extractive practices and inequitable benefit distribution. Your schema supports **transparency** (what was consented to, what use is allowed) and **audit** (who, when), so reuse can be accountable and aligned with community agreements.

---

## 8. Effoduh, Akpudo & Kong — Data governance policy for AI in Africa (Data & Policy)

**Core idea (from search):** Five design principles for **trustworthy and inclusive** data governance for AI in Africa: (1) African states assess domestic priorities and strengths/weaknesses, (2) human-centric approach (data security, privacy, fair processing), (3) alignment with supranational standards (African Charter, AU Convention on Cybersecurity), (4) critical evaluation of AI reliability in public sector, (5) representative, interoperable data and transparent procurement. Africa as “under-sampled majority”; need localized, inclusive policy rather than imported frameworks.

**Takeaway for your paper:** **Policy-level** principles; your schema is **dataset-level** implementation. Cite for African AI/data governance context; your contribution = a minimal, machine-readable schema that can sit under such policies for **community datasets** (consent, permitted use, provenance).

---

## Cross-cutting themes (for your Related work)

| Theme | Who says it | Your schema’s role |
|-------|-------------|----------------------|
| **Documentation** | Gebru: motivation, composition, uses | You add: consent, permitted_use, audit |
| **Consent** | Munung: dynamic consent; Omutoko: process/multilingual; Brown/Chabilall: consent as barrier | You: **structured fields** for type, scope, documented |
| **Permitted use / reuse** | Munung: benefit-sharing, licensing; Chabilall: commercialisation, benefit-sharing | You: **machine-readable** research/commercial/model_training flags |
| **Governance & trust** | Brown: governance and guidelines build trust; Chabilall: need robust governance | You: **governance artifact** — minimal schema for documentation + filtering |
| **African context** | Munung, Barrett, Abebe, Effoduh: justice, self-determination, anti-extraction | You: schema **for** community-level African ag/health datasets; supports accountability |
| **Audit / accountability** | Munung: oversight; Barrett: accountability; Abebe: transparent reuse | You: **provenance + audit** fields (collector, dates, version, review) |

---

## One-paragraph Related work (draft)

Dataset documentation has been advanced by Datasheets for Datasets (Gebru et al.), which standardize motivation, composition, collection, and recommended uses but do not model consent or machine-readable permitted use. In African contexts, data governance and consent are central: frameworks emphasize data justice and solidarity (Munung et al.), dynamic consent and benefit-sharing (Munung et al.), and culturally grounded consent processes including multilingual and visual approaches (Omutoko et al.). Empirical work with health researchers across sub-Saharan Africa shows that trust and willingness to share depend on clear guidelines and governance, while barriers include unclear consent, commercialisation, and legal gaps (Brown et al.; Chabilall et al.). African data ethics frameworks stress self-determination, communalist practice, and accountability (Barrett et al.; Abebe et al.), and policy work calls for trustworthy, inclusive data governance for AI in Africa (Effoduh et al.). These efforts are largely normative or process-oriented; a gap remains for **minimal, machine-readable documentation** of consent, permitted use, and provenance at the dataset level. We propose a governance schema that fills this gap for community-level datasets in African agriculture and health, enabling filtering for ethical downstream ML and audit trails for compliance.

---

## How to use this digest

1. **Intro:** Use “Cross-cutting themes” and the problem (unclear consent/reuse → underuse of community data; gap = no minimal schema).
2. **Related work:** Use the one-paragraph draft above; expand 1–2 sentences per source from the “Takeaway” bullets.
3. **Schema section:** When justifying each field group (consent, permitted_use, provenance), cite the relevant source (e.g. Munung for dynamic consent and benefit-sharing; Chabilall for consent and commercialisation; Omutoko for consent scope).
4. **Discussion:** Cite Brown/Chabilall for limitations (e.g. adoption depends on institutional/national guidelines) and Barrett/Abebe for future work (alignment with African data ethics and community agency).
