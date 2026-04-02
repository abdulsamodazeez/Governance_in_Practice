# DSA 2026 Workshop — Problem Ideas for Quick Formulation & Submission

**Workshop theme:** Foundational & Practical Data Science in the Age of Generative AI  
**Deadline:** 31 March 2026 | **Venue:** Makerere University, Kampala (23–24 July 2026)  
**Format:** Max 5 pages, OpenReview | Types: Research / Industry / Work-in-progress

---

## Recommended: Fastest to formulate and start

### **1. Low-resource African language evaluation for generative AI (Axis: Generative AI & African Language Models)**

**Problem:**  
Standard LLMs are weak or untested on many African languages. There is no lightweight, reproducible benchmark to measure *practical* utility (e.g. question-answering, summarisation, instruction-following) for a small set of African languages with limited labelled data.

**What you do:**
- Pick 2–3 African languages (e.g. Luganda, Swahili, Amharic — at least one with less resource).
- Define 3–5 tasks: short QA, summarisation, or simple instruction following.
- Curate or generate a small evaluation set (100–500 examples per task) — can mix human-written + synthetic with clear provenance.
- Evaluate 1–2 open models (e.g. LLaMA-3, Mistral, or a smaller African-focused model if available) with a clear protocol (prompts, metrics, seeds).
- Report: performance by language and task, failure modes, and recommendations for “practical data science” in low-resource settings.

**Why it fits:** Directly addresses African Language Models; combines foundational ML evaluation with generative AI; scoped to be doable before March; high relevance for Kampala/DSA audience.

**First steps:** Choose languages → define tasks → collect or create 50–100 seed examples per task → run baseline evaluations.

---

### **2. Data governance and consent for community health / agriculture datasets (Axis: Data Governance + applications)**

**Problem:**  
Community-level datasets (e.g. smallholder agriculture, local health surveys) in African contexts are underused for ML/DS because of unclear consent, reuse conditions, and metadata. A practical framework is missing for “governance-aware” dataset documentation that supports both ethical reuse and model training.

**What you do:**
- Design a minimal **governance schema** (metadata + consent/reuse fields) suitable for one domain (e.g. agriculture or health).
- Apply it to 1–2 real or synthetic datasets (or existing public African datasets).
- Show how this schema supports: (a) documenting consent and permitted use, (b) filtering for downstream ML (e.g. “use only consent-for-research”), (c) audit trail for compliance.
- Optionally: simple tooling (e.g. a checklist, script, or template) that data collectors can use.

**Why it fits:** Data Governance is an explicit axis; links to Healthcare/Agriculture; manageable as a 5-page paper with a clear proposal + one worked example.

**First steps:** Review existing schemas (e.g. Datasheets, consent frameworks) → define your minimal schema → apply to one dataset and write the narrative.

---

### **3. Robust forecasting with limited data: climate or crop yield (Axis: AI/DS for Climate, Agriculture, Environmental Risks)**

**Problem:**  
In many African regions, time series for climate or crop yield are short, sparse, or missing. Standard deep learning needs large data; simple stats are interpretable but limited. The gap: **practical methods that combine small data, uncertainty quantification, and (optionally) external cues** (e.g. satellite, weather) without requiring big compute.

**What you do:**
- Pick one target: e.g. local crop yield, seasonal rainfall, or a simple environmental indicator.
- Use one real or public dataset (e.g. UEA/UCR, or an African climate/ag dataset from FAO, ICPAC, or similar).
- Compare: (a) classical (e.g. ARIMA, simple regression), (b) one lightweight ML method (e.g. small NN, gradient boosting), (c) optionally a tiny use of “foundation” signals (e.g. precomputed embeddings or indices) — with clear train/validation split and uncertainty (e.g. prediction intervals).
- Focus on: sample size vs performance, robustness to missing data, and practical takeaways for data-scarce settings.

**Why it fits:** Directly under “Climate, Healthcare, Agriculture, Environmental Risks”; combines foundational DS and modern ML; one dataset + one geography is enough for a solid 5-page contribution.

**First steps:** Choose target variable and geography → locate one dataset → implement baseline + one ML method and report metrics and uncertainty.

---

## How to choose and start today

| If you have… | Prefer |
|--------------|--------|
| NLP/LLM experience, interest in languages | **Problem 1** (African language evaluation) |
| Policy/ethics/data management interest | **Problem 2** (Data governance schema) |
| Stats/ML + climate or agriculture interest | **Problem 3** (Robust forecasting) |

**Next step:** Pick one problem → turn it into a one-paragraph **title + abstract** → list 3–5 concrete milestones (e.g. “Week 1: dataset; Week 2: baselines; …”) → start with the “First steps” above.

---

## ✅ Chosen: Problem 2 — Data governance and consent for community datasets

### Working title (draft)
**A minimal governance schema for community-level datasets: consent, reuse, and downstream ML in African agriculture and health.**

### One-paragraph abstract (draft)
Community-level datasets in African contexts (e.g. smallholder agriculture, local health surveys) are underused for data science and ML because consent, permitted reuse, and machine-readable metadata are often unclear. We propose a minimal, domain-agnostic **governance schema** that captures (1) consent type and scope, (2) permitted use (e.g. research, commercial, model training), (3) provenance and audit fields. We apply the schema to [one agriculture and/or one health dataset], show how it supports filtering for ethical downstream ML (e.g. “use only consent-for-research”) and an audit trail for compliance, and provide a reusable template and checklist for data collectors. The work targets practical data governance in the age of generative AI, where reuse and training on community data must be traceable and consent-aware.

### Paper outline (5 pages)
1. **Intro (0.75 pp):** Motivation — community data in Africa, gap in governance-aware documentation, aim of the paper.
2. **Related work (0.5 pp):** Datasheets for datasets, consent frameworks, existing data governance efforts; how our schema differs (minimal, ML-oriented, consent+reuse).
3. **Schema design (1–1.25 pp):** Fields (consent type, scope, permitted use, provenance, retention), rationale, optional vs required; one figure (schema diagram or table).
4. **Application (1.25–1.5 pp):** Apply to 1–2 datasets (name them, describe context); show filled-in governance records; how filtering/audit would work.
5. **Discussion + limitations (0.5 pp):** Practical takeaways, limitations, future work (e.g. tooling, adoption).
6. **Conclusion + references (0.5 pp).**

### Milestones (to submission 31 March 2026)
| Week | Milestone |
|------|-----------|
| 1 | Finalise schema (fields, optional/required); document in `governance_schema/` and README. |
| 2 | Choose 1–2 datasets (e.g. one public African ag or health dataset); fill in governance records. |
| 3 | Draft Sections 1–3; create schema figure/table. |
| 4 | Draft Sections 4–5; write abstract; internal pass. |
| 5 | Apply LaTeX template; polish; submit via OpenReview. |
