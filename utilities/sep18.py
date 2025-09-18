
import streamlit as st

st.set_page_config(page_title="Draft Paper (IEEE Format)", layout="wide")

st.title("📑 Draft Paper Writing – IEEE Style")
st.markdown("This interactive app guides you through drafting a **Survey/Working Paper** following the **IEEE template** – like a PowerPoint but interactive.")

# Slide 1 – Types of Templates
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    ["Types of Templates", "Core Sections", "References & Citations",
     "Draft Your Paper", "Tips & Do's/Don'ts", "Preview Draft", "Export"]
)

with tab1:
    st.header("📝 Types of Scientific Templates")
    st.subheader("Conference Paper")
    st.write("""
    • 4–6 pages, concise, focused on new results  
    • Uses IEEE two-column format  
    """)
    st.subheader("Research Article / Journal Paper")
    st.write("""
    • 6–10+ pages, detailed methodology, experiments, discussion  
    • Follows IEEE Access or journal-specific style  
    """)
    st.subheader("Book Chapter")
    st.write("""
    • 15–25 pages, narrative style with more background & references  
    • Template often provided by publisher (Springer, Elsevier)  
    """)
    st.info("💡 Tip: Download official IEEE templates at https://www.ieee.org/conferences/publishing/templates.html")

with tab2:
    st.header("📚 Core Sections in IEEE Template")

    st.markdown("""
    | Section | Should Contain | Avoid |
    |---------|----------------|-------|
    | **Title** | Short, descriptive, no abbreviations | Jargon, unnecessary words |
    | **Abstract** | 150–250 words (problem, method, results, conclusion) | Figures, citations |
    | **Keywords** | 4–6 relevant terms | Sentences, long phrases |
    | **Introduction** | Context, problem, contributions | Full results, unrelated history |
    | **Literature Review** | Related works, critical analysis | Copy-pasted abstracts |
    | **Methodology** | Data, tools, algorithms, diagrams | Results discussion |
    | **Results / Case Analysis** | Tables, figures, comparisons | Excessive theory |
    | **Discussion** | Interpret results, implications | Repeating methodology |
    | **Conclusion** | Key findings, future work, limitations | New data or figures |
    | **Acknowledgment** | Funding, support, collaborations | Personal dedications |
    | **References** | IEEE style, numbered | Other citation styles |
    """)

with tab3:
    st.header("📑 References & Citation Format")

    st.subheader("In-text citation")
    st.code('Several works have studied hyperspectral imaging [3].')

    st.subheader("Reference List (IEEE Style Examples)")
    st.code("""
[1] J. Smith and A. Doe, "Title of paper," IEEE Transactions on XYZ, vol. 12, no. 3, pp. 45-50, Mar. 2024.
[2] A. Author, Book Title, 3rd ed. New York, NY, USA: Publisher, 2022.
""")

    st.info("💡 Always number references in the order they appear and enclose numbers in square brackets [ ].")

with tab4:
    st.header("🖊️ Draft Your Paper")
    st.write("Fill in each section of your draft paper below:")

    title = st.text_input("Paper Title")

    abstract = st.text_area("Abstract (150–250 words)")

    keywords = st.text_input("Keywords (4–6 terms separated by commas)")

    intro = st.text_area("Introduction")

    literature = st.text_area("Literature Review / Related Works")

    methodology = st.text_area("Methodology")

    results = st.text_area("Results / Case Analysis")

    discussion = st.text_area("Discussion (optional)")

    conclusion = st.text_area("Conclusion")

    references = st.text_area("References (IEEE Style)")

    st.session_state['draft'] = {
        "Title": title,
        "Abstract": abstract,
        "Keywords": keywords,
        "Introduction": intro,
        "Literature": literature,
        "Methodology": methodology,
        "Results": results,
        "Discussion": discussion,
        "Conclusion": conclusion,
        "References": references
    }

with tab5:
    st.header("💡 Tips & Do's / Don'ts")
    with st.expander("Writing Style"):
        st.write("Use formal, objective tone. Avoid 'I / we / our' unless journal allows.")
    with st.expander("Figures & Tables"):
        st.write("High resolution, numbered sequentially, proper captions.")
    with st.expander("Units & Formatting"):
        st.write("Use SI units, check font sizes, align columns.")
    with st.expander("Plagiarism Check"):
        st.write("Ensure similarity <15% using Turnitin or equivalent.")

with tab6:
    st.header("📄 Preview Your Draft Paper")
    if 'draft' in st.session_state:
        draft = st.session_state['draft']
        st.subheader(draft.get("Title",""))
        st.markdown(f"**Abstract:** {draft.get('Abstract','')}")
        st.markdown(f"**Keywords:** {draft.get('Keywords','')}")
        st.markdown("### Introduction")
        st.write(draft.get("Introduction",""))
        st.markdown("### Literature Review")
        st.write(draft.get("Literature",""))
        st.markdown("### Methodology")
        st.write(draft.get("Methodology",""))
        st.markdown("### Results / Case Analysis")
        st.write(draft.get("Results",""))
        if draft.get("Discussion",""):
            st.markdown("### Discussion")
            st.write(draft.get("Discussion",""))
        st.markdown("### Conclusion")
        st.write(draft.get("Conclusion",""))
        st.markdown("### References")
        st.write(draft.get("References",""))

with tab7:
    st.header("⬇️ Export / Download Draft")
    st.write("You can copy your draft above into Word or LaTeX template for final formatting.")
    st.info("Future feature: Direct download as Word/PDF.")

