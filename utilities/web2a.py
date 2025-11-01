# app.py
"""
Streamlit app to display the BCA 301-4 .NET course plan.
Place 'BCA301-4 Updated.docx' in the same directory to parse the uploaded file automatically.
Requires: streamlit, python-docx, markdownify
Install:
    pip install streamlit python-docx markdownify
Run:
    streamlit run app.py
"""

import streamlit as st
from pathlib import Path
from docx import Document
import re
from markdownify import markdownify as md

st.set_page_config(page_title="BCA301-4 .NET Course Plan", layout="wide")

DOCX_FILENAME = "BCA301-4 Updated.docx"

st.title("BCA 301-4 — .NET Course Plan")
st.caption("Source: uploaded document. :contentReference[oaicite:1]{index=1}")

col1, col2 = st.columns([3,1])

# Utility: read docx as plain text (preserves paragraphs)
def read_docx_text(path: Path) -> str:
    doc = Document(path)
    paras = []
    for p in doc.paragraphs:
        text = p.text.strip()
        if text:
            paras.append(text)
    return "\n\n".join(paras)

# Utility: split into SECTION blocks (SECTION I, SECTION II, SECTION III, SECTION IV)
SECTION_PATTERN = re.compile(r"(SECTION\s+[IVXLC]+)", flags=re.IGNORECASE)

def split_sections(text: str):
    # Find positions of "SECTION ..." headings (case-insensitive)
    parts = SECTION_PATTERN.split(text)
    # parts likely like ['', 'SECTION I', 'content1', 'SECTION II', 'content2', ...]
    sections = {}
    if len(parts) == 1:
        sections["Full Document"] = text
        return sections
    i = 1
    while i < len(parts):
        header = parts[i].strip()
        content = parts[i+1].strip() if (i+1) < len(parts) else ""
        sections[header] = content
        i += 2
    return sections

# If doc exists, parse it; else, provide file upload
doc_path = Path(DOCX_FILENAME)
text_content = None
if doc_path.exists():
    try:
        text_content = read_docx_text(doc_path)
    except Exception as e:
        st.error(f"Error reading {DOCX_FILENAME}: {e}")
else:
    uploaded = st.sidebar.file_uploader("Upload course DOCX (optional)", type=["docx"])
    if uploaded is not None:
        with open("uploaded_course.docx", "wb") as f:
            f.write(uploaded.getbuffer())
        try:
            text_content = read_docx_text(Path("uploaded_course.docx"))
            st.success("Uploaded document parsed.")
        except Exception as e:
            st.error(f"Could not parse uploaded file: {e}")

# If we have no parsed content, show a helpful fallback (small hand-coded summary)
FALLBACK_SUMMARY = """
**Course**: BCA 301-4 — Dot Net  
**Semester**: IV  
**Hours**: 75 (3+2 per week)  
**Faculty**: Dr Smitha Vinod, Dr Vijay Arputharaj J, Dr Gayathry S Warrier, Dr Deepa BG  
**Contact**: see uploaded file for emails and phone numbers.  
(Upload the DOCX if you'd like the full content parsed.)
"""

if not text_content:
    col1.markdown(FALLBACK_SUMMARY)
else:
    sections = split_sections(text_content)

    # Sidebar navigation
    st.sidebar.header("Navigate")
    section_keys = list(sections.keys())
    default_idx = 0
    choice = st.sidebar.radio("Select section", section_keys, index=default_idx)

    # Search box (simple)
    query = st.sidebar.text_input("Search inside document (simple substring search)")

    # Download parsed markdown button
    md_text = md(text_content) if text_content else ""
    st.sidebar.download_button("Download as Markdown", md_text, file_name="BCA301-4_course_plan.md", mime="text/markdown")

    # Show chosen section in main area
    with col1:
        st.subheader(choice)
        content = sections.get(choice, "")
        # If user asked search, highlight lines containing query
        if query:
            lines = content.splitlines()
            matched = [ln for ln in lines if query.lower() in ln.lower()]
            if matched:
                st.markdown(f"**Search results for '{query}':**")
                for ln in matched:
                    st.markdown(f"- {ln}")
            else:
                st.info(f"No matches for '{query}' in this section.")
        # break the content into subblocks by double newlines for nicer display
        subblocks = [b for b in re.split(r"\n{2,}", content) if b.strip()]
        for i, block in enumerate(subblocks):
            # Present longer blocks in expanders
            if len(block) > 300:
                with st.expander(f"Part {i+1}"):
                    st.markdown(block)
            else:
                st.markdown(block)

    # Show all sections as expanders in the right column for quick scanning
    with col2:
        st.markdown("### All Sections")
        for sec, cnt in sections.items():
            with st.expander(sec, expanded=False):
                preview = cnt[:800] + ("..." if len(cnt) > 800 else "")
                st.markdown(preview)
                if st.button(f"Open {sec}", key=f"open_{sec}"):
                    # update selection in sidebar (hacky - streamlit rerun with query param could be used, but we set st.session_state)
                    st.session_state["selected_section"] = sec
                    st.experimental_rerun()

# Extra: if session state contains 'selected_section', set radio to that (so 'Open' buttons work)
if "selected_section" in st.session_state:
    # rerun will already have happened; we can't mutate the radio selection after render easily
    pass

# Bottom: small utilities
st.markdown("---")
st.markdown("**Utilities**")
st.info("To update the source: replace `BCA301-4 Updated.docx` file (or upload a new DOCX) and rerun the app.")

# show contact details quickly (attempt extract)
if text_content:
    # try to extract lines containing 'Mobile' or '@' for emails
    lines = text_content.splitlines()
    contact_lines = [ln for ln in lines if "mobile" in ln.lower() or "@" in ln or "contact" in ln.lower()]
    if contact_lines:
        st.sidebar.markdown("### Contacts (extracted)")
        for ln in contact_lines:
            st.sidebar.write(ln)

# Footer with citation
st.markdown("---")
st.caption("Course plan source: uploaded document. :contentReference[oaicite:2]{index=2}")
