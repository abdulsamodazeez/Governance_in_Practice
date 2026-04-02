# Literature for Problem 2 — Data governance & consent for community datasets

**Purpose:** Step 1 of the paper roadmap — related work and “how we differ.”  
**Use:** Cite in the paper; note what each source contributes and where your schema adds value.

---

## 1. Foundational (dataset documentation — not Africa-specific)

### Gebru et al., Datasheets for Datasets
- **Citation:** T. Gebru, J. Morgenstern, B. Vecchione, J. Wortman Vaughan, H. Wallach, H. Daumé III, and K. Crawford. Datasheets for datasets. *Communications of the ACM*, 64(12):86–92, 2021.  
- **DOI:** https://doi.org/10.1145/3458723  
- **arXiv:** https://arxiv.org/abs/1803.09010  
- **What it does:** Proposes standardized documentation for ML datasets (motivation, composition, collection, recommended uses).  
- **What to note for your paper:** They do **not** explicitly model consent type/scope or machine-readable “permitted use” (e.g. research vs commercial vs model training). Your schema adds **consent + permitted_use + audit** in a minimal, ML-oriented form.  
- **Quote for Related work:** “Dataset creators should document motivation, composition, collection process, and recommended uses” — your contribution: *plus consent, permitted reuse, and audit fields for community datasets.*

---

## 2. African scholars / Africa-focused (data governance, consent, sharing)

### 2.1 Effoduh, Akpudo & Kong — Data governance policy for AI in Africa
- **Citation:** J. O. Effoduh, U. E. Akpudo, and J. D. Kong. Toward a trustworthy and inclusive data governance policy for the use of artificial intelligence in Africa. *Data & Policy*, 2024.  
- **URL:** https://www.cambridge.org/core/journals/data-and-policy/article/toward-a-trustworthy-and-inclusive-data-governance-policy-for-the-use-of-artificial-intelligence-in-africa/6C22513DE8598A0A8B1EDBD9A2D6A102  
- **What it does:** Proposes five design principles for African AI data governance: domestic priorities, human-centric protection, alignment with AU/Charter, critical evaluation of AI reliability, representative and interoperable data with transparent procurement.  
- **What to note for your paper:** Policy-level; your schema is **operational** (machine-readable metadata for consent and reuse). Cite to show African policy context; your work implements a concrete, dataset-level layer.  
- **African authorship:** Yes (Effoduh, Akpudo, Kong — African institutions/contexts).

---

### 2.2 Munung, Ewuoso, Chimusa & Ogundiran — Equity-oriented data sharing culture (African health)
- **Citation:** N. S. Munung, C. Ewuoso, E. R. Chimusa, and T. Ogundiran. Cultivating an equity-oriented data sharing culture for African health research initiatives. *Nature Communications*, 2025.  
- **DOI:** https://doi.org/10.1038/s41467-025-63289-2  
- **URL:** https://www.nature.com/articles/s41467-025-63289-2  
- **What it does:** Proposes a framework anchored in **data justice and solidarity**: dynamic consent, equitable benefit-sharing, reciprocity, data custodianship, controlled access (e.g. CADEs), data sovereignty. Four pillars: fairness/equity, inclusivity/visibility, harm prevention, reciprocity.  
- **What to note for your paper:** Values and principles; your schema is a **minimal technical implementation** (fields for consent, permitted_use, provenance) that can support such frameworks. Cite for African health data context and consent/benefit-sharing; your contribution = machine-readable schema for documenting consent and reuse per dataset.  
- **African authorship:** Yes (Munung — UCT; Ewuoso — Wits; Ogundiran — Nigeria; Chimusa — African genomics context).

---

### 2.3 Brown, Chabilall, Cengiz & Moodley — Trust and equitable data sharing (SSA health researchers)
- **Citation:** Q. Brown, J. Chabilall, N. Cengiz, and K. Moodley. Trust as moral currency: Perspectives of health researchers in sub-Saharan Africa on strategies to promote equitable data sharing. *PLOS Digital Health*, 3(9):e0000551, 2024.  
- **DOI:** https://doi.org/10.1371/journal.pdig.0000551  
- **What it does:** Qualitative study (16 SSA countries): strategies for data sharing — (1) policy-level guidelines, (2) strengthening data governance to improve quality, (3) reciprocity. Trust central; need for national/institutional guidelines and governance.  
- **What to note for your paper:** Empirical evidence that **governance and guidelines** are what researchers ask for; your schema is a concrete **governance artifact** (documentation + filtering) that supports such guidelines.  
- **African authorship:** Yes (Stellenbosch; Moodley — well-known African bioethics scholar; multi-country SSA focus).

---

### 2.4 Chabilall, Brown, Cengiz & Moodley — Challenges sharing health data in SSA
- **Citation:** J. Chabilall, Q. Brown, N. Cengiz, and K. Moodley. Data as scientific currency: Challenges experienced by researchers with sharing health data in sub-Saharan Africa. *PLOS Digital Health*, 3(10):e0000635, 2024.  
- **DOI:** https://doi.org/10.1371/journal.pdig.0000635  
- **What it does:** Same 16-country qualitative study: five barriers — individual fears, structural issues, recognition/scooping, ethical (confidentiality, consent, benefit-sharing), legal gaps. Need for robust guidelines and data sharing agreements.  
- **What to note for your paper:** Directly supports the **problem** — unclear consent, reuse, and governance reduce willingness to share; your schema addresses “document consent and permitted use” so reuse is transparent.  
- **African authorship:** Yes (same Stellenbosch team; SSA-wide perspective).

---

### 2.5 Omutoko et al. — Informed consent, multilingualism, data-intensive research in SSA
- **Citation:** L. Omutoko, G. R. Chingarande, M. Botes, F. Moyana, S. Singh, W. Jaoko, E. Sevene, T. K. Mtande, A. K. Edwin, L. Matandika, T. Burgess, and K. Moodley. Understanding and processing informed consent during data-intensive health research in sub-Saharan Africa: challenges and opportunities from a multilingual perspective. *Research Ethics*, 21(3):503–518, 2024.  
- **DOI:** https://doi.org/10.1177/17470161241274809  
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12346138  
- **What it does:** Considers consent in data-intensive research in SSA: multilingualism, terminology, literacy; suggests iconography, graphic elicitation, multimedia to improve comprehension and documentation.  
- **What to note for your paper:** Consent **process** and documentation in African contexts; your schema captures **what** was consented to (type, scope, documented) and permitted use — complementary to “how” consent is obtained.  
- **African authorship:** Yes (Kenya, South Africa, Zimbabwe, Mozambique, Malawi, Ghana — multi-country SSA team).

---

### 2.6 Barrett, Okolo, Biira et al. — African Data Ethics (decolonial data science)
- **Citation:** T. Barrett, C. T. Okolo, B. Biira, E. Sherif, A. X. Zhang, and L. Battle. African Data Ethics: A Discursive Framework for Black Decolonial Data Science. *arXiv:2502.16043*, 2025.  
- **URL:** https://arxiv.org/abs/2502.16043  
- **What it does:** Six principles: challenge power asymmetries, assert data self-determination, invest in local data institutions, utilize communalist practices, center marginalized communities, uphold common good. Counters data colonialism and Western-centric data science.  
- **What to note for your paper:** Normative framework; your schema supports **operationalizing** consent and permitted use in a way that can respect community authority and reuse conditions (e.g. no commercial use without agreement).  
- **African authorship:** Yes (Okolo, Biira — African scholars; framework centers African voices).

---

### 2.7 Abebe, Aruleba, Birhane et al. — Narratives and counternarratives on data sharing in Africa
- **Citation:** R. Abebe, K. Aruleba, A. Birhane, et al. Narratives and counternarratives on data sharing in Africa. In *Proc. ACM Conference on Fairness, Accountability, and Transparency (FAccT)*, pp. 329–341, 2021.  
- **What it does:** Critiques power imbalances and extractive data practices; discusses barriers to equitable data sharing and colonial legacies.  
- **What to note for your paper:** Motivates why **transparent, documented** consent and reuse (your schema) matter for equitable sharing and accountability.  
- **African authorship:** Yes (Abebe — Ethiopia; Birhane — Ethiopia; Aruleba — African context).

---

## Summary for your Related Work (≈0.5 page)

| Source | Role in your paper |
|--------|---------------------|
| Gebru et al. | Foundational dataset documentation; your schema adds consent + permitted_use + audit. |
| Effoduh et al. | African AI data governance policy; you provide a dataset-level, implementable schema. |
| Munung et al. | Data justice/solidarity in African health; your schema as technical implementation. |
| Brown et al. / Chabilall et al. | Empirical evidence of need for governance and clear consent/reuse; your schema as response. |
| Omutoko et al. | Consent process in SSA; your schema documents *scope* and *permitted use* of consent. |
| Barrett et al. | African data ethics; your schema supports community-oriented, documented reuse. |
| Abebe et al. | Motivation for transparent, accountable consent and reuse. |

**One-sentence “how we differ”:** We propose a **minimal, machine-readable governance schema** that captures consent type/scope, permitted use (research, commercial, model training), and provenance/audit, filling a gap between high-level frameworks (e.g. data justice, Datasheets) and operational documentation for community-level datasets in African agriculture and health.

---

## Where to get full text

- **Gebru et al.:** ACM DL, arXiv (free).  
- **Effoduh et al.:** Cambridge Core (Data & Policy).  
- **Munung et al.:** Nature Communications (open access).  
- **Brown / Chabilall et al.:** PLOS Digital Health (open access).  
- **Omutoko et al.:** SAGE Research Ethics; PMC (free).  
- **Barrett et al.:** arXiv (free).  
- **Abebe et al.:** ACM FAccT (check institutional access or author pages).

---

## Next step

Read at least the abstracts and “Discussion”/“Conclusion” of (1) Gebru et al., (2) Munung et al., (3) one of Brown/Chabilall, (4) Omutoko et al., (5) Effoduh et al. or Barrett et al. Take 1–2 sentences per paper on “what they do” and “what our schema adds.” Use this to draft the Related work section and the “gap” in the Intro.
