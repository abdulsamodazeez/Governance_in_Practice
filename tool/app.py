"""
Data Governance Schema Tool — DSA 2026 Workshop
Create, upload, validate, and filter governance records for community-level datasets.
"""

import json
from pathlib import Path
from typing import List, Tuple

import streamlit as st

# Path to governance records (relative to project root when run as: streamlit run tool/app.py)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RECORDS_DIR = PROJECT_ROOT / "governance_schema" / "records"
TEMPLATE_PATH = PROJECT_ROOT / "governance_schema" / "template.json"

# Page config
st.set_page_config(
    page_title="Data Governance Schema | DSA 2026",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a cleaner look
st.markdown("""
<style>
    .stAlert { margin-top: 0.5rem; }
    div[data-testid="stExpander"] { border: 1px solid #eee; border-radius: 6px; }
    .gov-badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.85em; }
    .gov-ok { background: #d4edda; color: #155724; }
    .gov-no { background: #f8d7da; color: #721c24; }
</style>
""", unsafe_allow_html=True)


def load_preloaded_records():
    """Load the five pre-filled governance records."""
    records = []
    if not RECORDS_DIR.exists():
        return records
    for path in sorted(RECORDS_DIR.glob("*.json")):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                data["_filename"] = path.name
                records.append(data)
        except Exception as e:
            st.sidebar.warning(f"Could not load {path.name}: {e}")
    return records


def validate_record(data: dict) -> Tuple[bool, List[str]]:
    """Validate governance record against required fields. Returns (ok, list of errors)."""
    errors = []
    required = {
        "identification": ["dataset_id", "title", "domain"],
        "consent": ["consent_type", "consent_scope", "consent_documented"],
        "permitted_use": ["research_allowed", "commercial_use_allowed", "model_training_allowed", "redistribution_allowed"],
        "provenance": ["collector_org"],
    }
    for section, fields in required.items():
        if section not in data:
            errors.append(f"Missing section: {section}")
            continue
        for field in fields:
            if field not in data[section]:
                errors.append(f"{section}.{field} is required")
            elif data[section][field] == "" and field != "geography":
                errors.append(f"{section}.{field} must be filled")
    domain_enum = ["agriculture", "health", "other"]
    if "identification" in data and data["identification"].get("domain") and data["identification"]["domain"] not in domain_enum:
        errors.append("identification.domain must be one of: agriculture, health, other")
    consent_enum = ["individual", "community", "household", "institutional", "not_applicable", "unknown"]
    if "consent" in data and data["consent"].get("consent_type") and data["consent"]["consent_type"] not in consent_enum:
        errors.append("consent.consent_type must be one of: " + ", ".join(consent_enum))
    return len(errors) == 0, errors


def build_record_from_form(state: dict) -> dict:
    """Build governance record dict from session state form values."""
    return {
        "identification": {
            "dataset_id": state.get("dataset_id", ""),
            "title": state.get("title", ""),
            "domain": state.get("domain", "agriculture"),
            "geography": state.get("geography", ""),
        },
        "consent": {
            "consent_type": state.get("consent_type", "household"),
            "consent_scope": state.get("consent_scope", ""),
            "consent_documented": state.get("consent_documented", True),
            "consent_language": state.get("consent_language", ""),
        },
        "permitted_use": {
            "research_allowed": state.get("research_allowed", True),
            "commercial_use_allowed": state.get("commercial_use_allowed", False),
            "model_training_allowed": state.get("model_training_allowed", False),
            "redistribution_allowed": state.get("redistribution_allowed", False),
            "use_restrictions": state.get("use_restrictions", ""),
        },
        "provenance": {
            "collector_org": state.get("collector_org", ""),
            "collection_date_start": state.get("collection_date_start", ""),
            "collection_date_end": state.get("collection_date_end", ""),
            "version": state.get("version", ""),
            "last_updated": state.get("last_updated", ""),
        },
        "audit": {
            "contact_email": state.get("contact_email", ""),
            "governance_review_date": state.get("governance_review_date", ""),
            "notes": state.get("notes", ""),
        },
    }


def render_browse_filter(records: list):
    """Browse pre-loaded records and filter by permitted use."""
    st.subheader("Browse & filter governance records")
    st.caption("Pre-loaded: five Africa-related datasets (agriculture & health). Filter to find datasets suitable for research, model training, etc.")

    if not records:
        st.info("No pre-loaded records found. Add JSON files in `governance_schema/records/` or use **Create / Upload** to add your own.")
        return

    # Filters in sidebar
    with st.sidebar:
        st.markdown("### Filters")
        filter_consent_doc = st.checkbox("Consent documented", value=True, help="Only show records with consent documented")
        filter_research = st.checkbox("Research allowed", value=False)
        filter_commercial = st.checkbox("Commercial use allowed", value=False)
        filter_model_training = st.checkbox("Model training allowed", value=True)
        filter_domain = st.selectbox("Domain", ["All", "agriculture", "health", "other"])

    filtered = []
    for r in records:
        ident = r.get("identification", {})
        consent = r.get("consent", {})
        use = r.get("permitted_use", {})
        if filter_consent_doc and not consent.get("consent_documented", False):
            continue
        if filter_research and not use.get("research_allowed", False):
            continue
        if filter_commercial and not use.get("commercial_use_allowed", False):
            continue
        if filter_model_training and not use.get("model_training_allowed", False):
            continue
        if filter_domain != "All" and ident.get("domain") != filter_domain:
            continue
        filtered.append(r)

    st.markdown(f"**{len(filtered)}** of **{len(records)}** records match filters.")

    # Summary table
    rows = []
    for r in filtered:
        ident = r.get("identification", {})
        consent = r.get("consent", {})
        use = r.get("permitted_use", {})
        rows.append({
            "Dataset": ident.get("title", "—")[:50] + ("…" if len(ident.get("title", "")) > 50 else ""),
            "Domain": ident.get("domain", "—"),
            "Geography": ident.get("geography", "—")[:30],
            "Consent type": consent.get("consent_type", "—"),
            "Consent doc.": "✓" if consent.get("consent_documented") else "✗",
            "Research": "✓" if use.get("research_allowed") else "✗",
            "Commercial": "✓" if use.get("commercial_use_allowed") else "✗",
            "Model training": "✓" if use.get("model_training_allowed") else "✗",
        })
    if rows:
        st.dataframe(rows, width="stretch", hide_index=True)

    # Expandable details per record
    st.markdown("---")
    st.markdown("#### Record details")
    for r in filtered:
        title = r.get("identification", {}).get("title", "Untitled")
        with st.expander(f"📄 {title}"):
            st.json(r)


def render_create_form():
    """Form to create a new governance record."""
    st.subheader("Create a governance record")
    st.caption("Fill in the schema fields. Required fields are marked. You can then validate and download the record as JSON.")

    with st.form("governance_form"):
        st.markdown("##### Identification")
        c1, c2 = st.columns(2)
        with c1:
            dataset_id = st.text_input("Dataset ID *", placeholder="e.g. DOI or internal ID")
            title = st.text_input("Title *", placeholder="Short dataset title")
        with c2:
            domain = st.selectbox("Domain *", ["agriculture", "health", "other"])
            geography = st.text_input("Geography", placeholder="e.g. Uganda, East Africa")

        st.markdown("##### Consent")
        c1, c2 = st.columns(2)
        with c1:
            consent_type = st.selectbox(
                "Consent type *",
                ["individual", "community", "household", "institutional", "not_applicable", "unknown"],
            )
            consent_documented = st.checkbox("Consent documented *", value=True)
        with c2:
            consent_scope = st.text_area("Consent scope *", placeholder="What was consented to (e.g. research only, reuse)")
            consent_language = st.text_input("Consent language(s)", placeholder="e.g. English, Luganda")

        st.markdown("##### Permitted use")
        c1, c2 = st.columns(2)
        with c1:
            research_allowed = st.checkbox("Research allowed", value=True)
            commercial_use_allowed = st.checkbox("Commercial use allowed", value=False)
        with c2:
            model_training_allowed = st.checkbox("Model training allowed (incl. Gen AI)", value=False)
            redistribution_allowed = st.checkbox("Redistribution allowed", value=False)
        use_restrictions = st.text_area("Use restrictions (optional)", placeholder="Free-text conditions")

        st.markdown("##### Provenance")
        c1, c2 = st.columns(2)
        with c1:
            collector_org = st.text_input("Collecting organisation *", placeholder="Institution or project name")
            collection_date_start = st.text_input("Collection start (YYYY-MM-DD)", placeholder="")
            collection_date_end = st.text_input("Collection end (YYYY-MM-DD)", placeholder="")
        with c2:
            version = st.text_input("Version", placeholder="e.g. 1.0")
            last_updated = st.text_input("Last updated (YYYY-MM-DD)", placeholder="")

        st.markdown("##### Audit")
        contact_email = st.text_input("Contact email", placeholder="For governance enquiries")
        governance_review_date = st.text_input("Governance review date (YYYY-MM-DD)", placeholder="")
        notes = st.text_area("Notes", placeholder="Optional notes or references")

        submitted = st.form_submit_button("Validate & build record")

    if submitted:
        state = {
            "dataset_id": dataset_id, "title": title, "domain": domain, "geography": geography,
            "consent_type": consent_type, "consent_scope": consent_scope, "consent_documented": consent_documented,
            "consent_language": consent_language,
            "research_allowed": research_allowed, "commercial_use_allowed": commercial_use_allowed,
            "model_training_allowed": model_training_allowed, "redistribution_allowed": redistribution_allowed,
            "use_restrictions": use_restrictions,
            "collector_org": collector_org,
            "collection_date_start": collection_date_start, "collection_date_end": collection_date_end,
            "version": version, "last_updated": last_updated,
            "contact_email": contact_email, "governance_review_date": governance_review_date, "notes": notes,
        }
        record = build_record_from_form(state)
        ok, errs = validate_record(record)
        if ok:
            st.success("Record is valid. You can download it below.")
            st.download_button(
                "Download as JSON",
                data=json.dumps(record, indent=2),
                file_name="governance_record.json",
                mime="application/json",
            )
            with st.expander("Preview record"):
                st.json(record)
        else:
            st.error("Validation failed:")
            for e in errs:
                st.markdown(f"- {e}")


def render_upload_json():
    """Upload a JSON file and validate / preview."""
    st.subheader("Upload governance record (JSON)")
    st.caption("Upload a JSON file that follows the governance schema. We will validate and let you preview or re-download.")

    uploaded = st.file_uploader("Choose a JSON file", type=["json"])
    if uploaded is None:
        return
    try:
        data = json.load(uploaded)
    except json.JSONDecodeError as e:
        st.error(f"Invalid JSON: {e}")
        return

    ok, errs = validate_record(data)
    if ok:
        st.success("File is valid and matches the governance schema.")
        st.download_button(
            "Download validated JSON",
            data=json.dumps(data, indent=2),
            file_name="governance_record_validated.json",
            mime="application/json",
        )
        with st.expander("Preview"):
            st.json(data)
    else:
        st.error("Validation failed:")
        for e in errs:
            st.markdown(f"- {e}")
    st.markdown("---")
    st.caption("Tip: Use the template from `governance_schema/template.json` or create a record with the form, then upload to validate.")


def main():
    st.title("📋 Data Governance Schema Tool")
    st.markdown("**DSA 2026 Workshop** — *Foundational & Practical Data Science in the Age of Generative AI*")
    st.markdown("Document consent, permitted use, and provenance for community-level datasets (agriculture & health).")

    mode = st.sidebar.radio(
        "Mode",
        ["Browse & filter (demo)", "Create governance record", "Upload JSON"],
        index=0,
        help="Browse pre-loaded records, create a new record with the form, or upload and validate a JSON file.",
    )

    if mode == "Browse & filter (demo)":
        records = load_preloaded_records()
        render_browse_filter(records)
    elif mode == "Create governance record":
        render_create_form()
    else:
        render_upload_json()

    st.sidebar.markdown("---")
    st.sidebar.caption("Schema: identification, consent, permitted use, provenance, audit. See `governance_schema/` in the project.")


if __name__ == "__main__":
    main()
