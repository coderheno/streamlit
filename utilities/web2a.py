# app.py
"""
Streamlit app to display the BCA 301-4 .NET Course Plan
Lightweight version — no python-docx, no markdownify.
You can paste or upload plain text.
Run with:
    streamlit run app.py
"""

import streamlit as st
import re

# ----------------------------
# App configuration
# ----------------------------
st.set_page_config(page_title="BCA301-4 .NET Course Plan", layout="wide")

st.title("BCA 301-4 — .NET Course Plan")
st.caption("Minimal Streamlit app (no external parsing libraries)")

# ----------------------------
# Helper: split text into SECTION blocks
# ----------------------------
SECTION_PATTERN = re.compile(r"(SECTION\s+[IVXLC]+)", flags=re.IGNORECASE)

def split_sections(text: str):
    parts = SECTION_PATTERN.split(text)
    sections = {}
    if len(parts) == 1:
        sections["Full Document"] = text
        return sections
    i = 1
    while i < len(parts):
        header = parts[i].strip()
        content = parts[i + 1].strip() if (i + 1) < len(parts) else ""
        sections[header] = content
        i += 2
    return sections


# ----------------------------
# Sidebar: input options
# ----------------------------
st.sidebar.header("Input Options")
source_option = st.sidebar.radio(
    "Choose how to load the course plan:",
    ["Paste text manually", "Upload text file"],
)

text_content = ""

if source_option == "Paste text manually":
    text_content = st.text_area(
        "Paste course content here:",
        height=300,
        placeholder="Paste the full course content (including SECTION I, II, etc.)...",
    )
elif source_option == "Upload text file":
    uploaded = st.sidebar.file_uploader("Upload .txt or .md file", type=["txt", "md"])
    if uploaded is not None:
        text_content = uploaded.read().decode("utf-8")
        st.success("File uploaded successfully.")

# ----------------------------
# Fallback summary
# ----------------------------
FALLBACK_SUMMARY = """
**Course**: BCA 301-4 — Dot Net  
**Semester**: IV  
**Hours**: 75 (3+2 per week)  
**Faculty**: Dr Smitha Vinod, Dr Vijay Arputharaj J, Dr Gayathry S Warrier, Dr Deepa BG  
**Contact**: see uploaded or pasted content for details.  
"""

col1, col2 = st.columns([3, 1])

# ----------------------------
# Display logic
# ----------------------------
if not text_content.strip():
    col1.markdown(FALLBACK_SUMMARY)
else:
    sections = split_sections(text_content)

    # Sidebar navigation
    st.sidebar.header("Navigate")
    section_keys = list(sections.keys())
    choice = st.sidebar.radio("Select section", section_keys, index=0)

    # Search box
    query = st.sidebar.text_input("Search inside document")

    # Display chosen section
    with col1:
        st.subheader(choice)
        content = sections.get(choice, "")
        if query:
            lines = content.splitlines()
            matched = [ln for ln in lines if query.lower() in ln.lower()]
            if matched:
                st.markdown(f"**Search results for '{query}':**")
                for ln in matched:
                    st.markdown(f"- {ln}")
            else:
                st.info(f"No matches for '{query}' in this section.")
        else:
            subblocks = [b for b in re.split(r"\n{2,}", content) if b.strip()]
            for i, block in enumerate(subblocks):
                if len(block) > 300:
                    with st.expander(f"Part {i+1}"):
                        st.markdown(block)
                else:
                    st.markdown(block)

    # Right-side summary
    with col2:
        st.markdown("### All Sections")
        for sec, cnt in sections.items():
            with st.expander(sec, expanded=False):
                preview = cnt[:800] + ("..." if len(cnt) > 800 else "")
                st.markdown(preview)

# ----------------------------
# Footer
# ----------------------------

