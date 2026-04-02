# Full paper roadmap — where to start & what to look for

**Goal:** A complete, well-acceptable DSA 2026 workshop paper (Problem 2: Data governance & consent for community datasets).  
**Deadline:** 31 March 2026 | **Length:** Max 5 pages (including references).

---

## Where to start (order of work)

| Order | Step | What you do |
|-------|------|-------------|
| **1** | **Literature (Related work)** | Read 4–6 key papers; note what exists and how your schema differs. |
| **2** | **Lock your schema** | Finalise `governance_schema/schema.yaml` and template; decide required vs optional. ✅ *Done: RATIONALE.md, SCHEMA_TABLE.md, schema summary.* |
| **3** | **Pick 1–2 datasets** | Choose real public datasets (ag or health, ideally African); fill governance records. ✅ *Done: all 5 (HarvestStat, LSMS-ISA, GROW-Africa, DHS Malawi 2024, HarvestNet) in governance_schema/records/.* |
| **4** | **Draft paper** | Write Intro → Related work → Schema → Application → Discussion → Conclusion. ✅ *Done: paper/PAPER_DRAFT.md.* |
| **5** | **Figure/table** | One clear schema figure or table. ✅ *Table 1 (schema) and Table 2 (application) in draft.* |
| **6** | **Abstract + polish** | Final abstract; LaTeX; proofread; submit via OpenReview. |

**Start from Step 1 (literature).** It gives you the “what to cite” and “how we differ” for Related work and strengthens the whole paper.

---

## Step 1 — Literature: what to look for

Read and take short notes on:

1. **Datasheets for Datasets**  
   - Gebru et al., “Datasheets for Datasets,” *Communications of the ACM* (2021) / arXiv:1803.09010.  
   - **Look for:** What they document (provenance, use, limitations); what they *don’t* (explicit consent, model-training flags). Say how your schema adds consent + ML reuse.

2. **Dataset documentation / ML documentation**  
   - “Model Cards for Model Reporting” (Mitchell et al.); “Data Statements” (Bender & Friedman).  
   - **Look for:** Documentation practices in ML; gap for *community* and *consent*.

3. **Consent & data governance**  
   - GDPR (consent, lawful basis); “Consent and data governance in the data economy” type papers; any African/local framework (e.g. AU Data Policy, national laws).  
   - **Look for:** Consent types, scope, reuse conditions; how your schema makes them machine-readable.

4. **Domain (agriculture / health data)**  
   - Papers on smallholder data, health data sharing, or FAIR/governance in ag/health in Africa.  
   - **Look for:** Reported pain points (consent unclear, reuse unclear); your schema as a practical response.

**Where to search:** Google Scholar, ACM DL, arXiv (cs.CY, cs.DB), and “data governance Africa” / “consent community data.”

**Output:** 1–2 pages of notes + 8–12 references for the paper. Use this to write **Related work (≈0.5 pp)** and to sharpen the **Intro** (“gap” and “contribution”).

---

## Step 2 — Schema: what to lock in

- **Files:** `governance_schema/schema.yaml`, `template.json`, `example_agriculture.json`.
- **Decide:** Which fields are **required** vs **optional**; any extra field (e.g. retention, data minimisation) you want.
- **Output:** Final schema + one **figure or table** for the paper (schema overview).  
- **Rationale:** In the paper, briefly justify each group of fields (identification, consent, permitted_use, provenance, audit).

---

## Step 3 — Datasets: what to look for

Pick **1–2 real, public datasets** (ideally African agriculture or health) so the “Application” section is concrete.

**What to look for:**

- **Relevance:** Community-level or smallholder/health data; or widely used African dataset with unclear governance.
- **Availability:** Public or documented access; you can fill a governance form *as if* you were the steward.
- **Use case:** You can show how filtering by `permitted_use` / consent would work for downstream ML.

**Where to look:**

- **Agriculture:** FAO microdata, CGIAR/ILRI datasets, national ag surveys (e.g. Uganda), crop/weather datasets used in African ML papers.
- **Health:** DHS (Demographic and Health Surveys), IHME, WHO; African health surveys or trial datasets with documented consent.
- **General:** Kaggle datasets from African contexts; papers that release “community” or “smallholder” data — check their supplements/data statements.

**Output:** 1–2 chosen datasets + one filled `template.json` (or equivalent) per dataset. These become **Section 4 (Application)** and your abstract’s “[one agriculture and/or one health dataset]”.

---

## Step 4 — Drafting the paper

Use your existing **paper outline** in `DSA2026_PROBLEM_IDEAS.md`:

1. **Intro (≈0.75 pp):** Problem (community data in Africa underused; consent/reuse unclear) → gap (no minimal, ML-oriented governance schema) → contribution (schema + application + template).
2. **Related work (≈0.5 pp):** Datasheets, consent/governance, ML documentation; one short paragraph on how your schema differs (minimal, consent + permitted_use + audit).
3. **Schema design (≈1–1.25 pp):** Fields, rationale, required/optional; **one figure or table**.
4. **Application (≈1.25–1.5 pp):** Describe the 1–2 datasets; show filled governance records; how filtering/audit would work for ML reuse.
5. **Discussion + limitations (≈0.5 pp):** Practical takeaways; limitations (e.g. adoption, enforcement); future work (tooling, more domains).
6. **Conclusion + references (≈0.5 pp).**

**What to look for while drafting:** Clear motivation, one main idea (the schema), concrete application, honest limitations.

---

## Step 5 & 6 — Figure, abstract, polish

- **Figure/table:** One schema overview (e.g. box diagram or table of sections/fields). Keep it simple.
- **Abstract:** Use the draft in `DSA2026_PROBLEM_IDEAS.md`; replace “[one agriculture and/or one health dataset]” with your real dataset names.
- **LaTeX:** Use DSA 2026 LaTeX template from [workshop page](https://www.datascienceafrica.org/dsa-workshops/dsa-2026-workshop).
- **Check:** 5-page limit, all refs cited, no placeholder text; ACM guidelines on AI tool use if applicable.

---

## What makes the paper “well acceptable”

| Criterion | What to do |
|-----------|------------|
| **Relevance** | Tie to DSA 2026 theme (Data Governance + practical DS in the age of Gen AI) and African/community context. |
| **Clarity** | One clear contribution (minimal schema); problem → gap → method → application. |
| **Grounding** | Cite related work (Datasheets, consent/governance); state how you differ. |
| **Concrete application** | Real datasets + filled governance records; show filtering/audit, not just theory. |
| **Honest limitations** | Short discussion of adoption, enforcement, scope. |
| **Format** | 5 pages, template, references; submit on OpenReview before 31 March 2026. |

---

## Quick reference — what to look for by step

| Step | Look for |
|------|----------|
| **Literature** | Datasheets, consent/governance, ML documentation, African ag/health data governance; “how we differ.” |
| **Schema** | Required vs optional fields; one figure/table for the paper. |
| **Datasets** | 1–2 public, community/ag/health (ideally African); can fill governance form and show filtering. |
| **Draft** | Clear problem, one contribution, concrete application, limitations. |
| **Acceptability** | Relevance to DSA, clarity, citations, real application, format. |

Start with **Step 1 (literature)**; use this file as a checklist and tick off each step as you go.
