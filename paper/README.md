# DSA 2026 paper draft

**Title:** A Minimal Governance Schema for Community-Level Datasets: Consent, Reuse, and Downstream ML in African Agriculture and Health

**File:** `PAPER_DRAFT.md` — full draft in Markdown (Sections 1–6, abstract, references).

**Next steps:**
1. Copy content into the DSA 2026 LaTeX template ([workshop page](https://www.datascienceafrica.org/dsa-workshops/dsa-2026-workshop)).
2. Convert tables to LaTeX (e.g. `tabular` or `booktabs`).
3. Format references with BibTeX (use `literature/LITERATURE_REVIEW.md` and `literature/DIGESTED_LITERATURE.md` for full citations).
4. Add schema figure if desired (use `governance_schema/SCHEMA_TABLE.md` compact table or a simple diagram).
5. Supplementary: link or append schema YAML, template JSON, and the five records from `governance_schema/records/`.
6. Proofread; check 5-page limit; submit via OpenReview by 31 March 2026.

**Word count (approx):** ~1,400 (body); with refs and spacing, should fit within 5 pages in LaTeX.

**Demo:** A Streamlit app in `../tool/` lets attendees browse and filter the five governance records, create a new record via form, or upload and validate JSON. Run from project root: `pip install -r tool/requirements.txt && streamlit run tool/app.py`.
