# Data Governance Schema Tool (Streamlit)

Demo app for the DSA 2026 governance schema: create, upload, validate, and filter governance records.

## Run locally

From the **project root** (`DSA/`):

```bash
pip install -r tool/requirements.txt
streamlit run tool/app.py
```

Then open the URL shown (usually http://localhost:8501).

## Modes

1. **Browse & filter (demo)** — Pre-loaded with the five Africa-related datasets. Filter by:
   - Consent documented
   - Research / commercial / model training allowed
   - Domain (agriculture, health)
   View a summary table and expand each record to see full JSON.

2. **Create governance record** — Form to fill in all schema fields. Validate and download the record as JSON.

3. **Upload JSON** — Upload a JSON file that follows the schema; the app validates it and lets you preview or re-download.

## For the workshop demo

- Start with **Browse & filter**: show the 5 datasets, apply filters (e.g. “Model training allowed” + “Consent documented”) to show how downstream users can select datasets for ethical ML.
- Switch to **Create governance record**: fill a minimal example (e.g. a small survey) and download the JSON to show the artifact.
- Optionally **Upload JSON**: use the downloaded file or `governance_schema/template.json` to show validation.

## Files

- `app.py` — Streamlit app
- `requirements.txt` — streamlit, pyyaml
- Pre-loaded records are read from `../governance_schema/records/*.json` (the five filled records).
