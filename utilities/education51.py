import streamlit as st
from PIL import Image
import io
import base64
from collections import Counter
import pandas as pd
import textwrap

st.set_page_config(page_title="Microlearning Session 2 Demo", layout="wide")

st.title("Microlearning for the Masses — Session 2 Demo")
st.subheader("Low-code, No-code and Quick ICT Tool Builder")

st.markdown("""
This demo app helps you run a simple in-app poll (simulating the Slido question), explains coding vs no-code vs low-code, lists platforms, and lets participants **generate a small ICT tool** (a feedback app) they can download and run.

Flow:
1. Quick Poll (in-app simulation of Slido)
2. Short explainer and platforms list with screenshots/placeholders
3. Build a Quick ICT Tool (auto-generate Streamlit code)
4. Download the generated app or copy the code
""")

# ----------------------
# 1) Quick Poll (simulate Slido)
# ----------------------
st.header("1 — Quick Poll: Essential skill for the future")
st.write("""Question: Which of the following is an essential skill for the future?
Hint: the right answer is often a combination of these.
""")

poll_choice = st.radio("Choose one:", ("Coding", "No-code", "Low-code"), key="poll")
if st.button("Submit Poll Response"):
    if 'poll_results' not in st.session_state:
        st.session_state.poll_results = {'Coding': 0, 'No-code': 0, 'Low-code': 0}
    st.session_state.poll_results[poll_choice] += 1
    st.success(f"Recorded: {poll_choice}")

if 'poll_results' in st.session_state:
    st.write("**Live poll results (in this session)**")
    results = st.session_state.poll_results
    df = pd.DataFrame({'choice': list(results.keys()), 'count': list(results.values())}).set_index('choice')
    st.bar_chart(df)
    st.write(results)
else:
    st.info("No responses yet. Ask participants to submit their choice.")

st.markdown("---")

# ----------------------
# Local Word Collector (fallback demo)
# ----------------------
st.header("Local word cloud demo (fallback and activity)")
st.write("Participants may also enter a single word here; this builds an in-app tag cloud you can discuss while Slido aggregates live responses.")

if 'local_words' not in st.session_state:
    st.session_state.local_words = []

col1, col2 = st.columns([3, 1])
with col1:
    local_word = st.text_input("Enter one word that describes 'Microlearning'", key="local_word")
with col2:
    if st.button("Submit word", key='submit_local'):
        if local_word:
            st.session_state.local_words.append(local_word.strip().lower())
            st.success("Word submitted")

if st.session_state.local_words:
    counts = Counter(st.session_state.local_words)
    st.write("**Local responses so far**")
    st.write(dict(counts))

    def render_tag_cloud(counter):
        max_count = max(counter.values())
        min_count = min(counter.values())
        html_tags = []
        for w, c in counter.most_common():
            if max_count == min_count:
                size = 24
            else:
                size = 14 + int(34 * (c - min_count) / (max_count - min_count))
            html_tags.append(f"<span style='font-size:{size}px; margin:6px; padding:4px; display:inline-block; background:#f0f0f0; border-radius:6px;'>{w}</span>")
        return "".join(html_tags)

    tag_html = render_tag_cloud(counts)
    st.markdown(tag_html, unsafe_allow_html=True)
else:
    st.info("No local words yet. Ask participants to submit one word and press Submit.")

st.markdown("---")

# ----------------------
# 2) Explain and list platforms
# ----------------------
st.header("2 — Quick Explainer: Coding vs No-code vs Low-code")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Coding**")
    st.write("Full programming: highest flexibility, custom analytics, full control (e.g., Python, JS). Example uses: custom learning analytics, complex simulations.")
    st.markdown("**When to use:** complex bespoke tools, heavy data processing, custom integrations.")

    st.markdown("**No-code**")
    st.write("Build applications visually with drag and drop; no programming knowledge required. Great for rapid prototyping and teacher-led creations.")
    st.markdown("**When to use:** quick class apps, forms, simple interactive lessons, teacher-owned tools.")

with col2:
    st.markdown("**Low-code**")
    st.write("Visual building with optional code snippets for customization (best of both worlds). Useful for power-users and teams.")
    st.markdown("**When to use:** internal tools needing some logic, extendable teacher apps, integrations with school systems.")

st.markdown("---")

st.subheader("Popular Platforms — pick based on skill and scale")
platforms = {
    'No-code': ['Glide', 'Bubble', 'Canva Apps', 'Google Sites'],
    'Low-code': ['Power Apps', 'Zoho Creator', 'AppSheet', 'Streamlit (minimal code)'],
    'Coding': ['Custom Python + Streamlit', 'React + Node', 'Django/Flask backends']
}

for k, v in platforms.items():
    st.markdown(f"**{k} examples:** {', '.join(v)}")

st.write("You can upload screenshots for any platform to show in the session (optional). Use the uploader below:")
up1 = st.file_uploader("Upload a Before screenshot (optional)", type=['png', 'jpg', 'jpeg'], key='up_before')
up2 = st.file_uploader("Upload an After screenshot (optional)", type=['png', 'jpg', 'jpeg'], key='up_after')
if up1:
    st.image(Image.open(up1), caption='Before screenshot', use_column_width=True)
if up2:
    st.image(Image.open(up2), caption='After screenshot', use_column_width=True)

st.markdown("---")

# ----------------------
# 3) Build a Quick ICT Tool (auto-generate Streamlit code)
# ----------------------
st.header("3 — Build a Quick ICT Tool: Feedback App Generator")
st.write("This simple generator creates a tiny Streamlit feedback app. Teachers can download the file, run `streamlit run feedback_app.py`, and collect responses locally.")

app_title = st.text_input("App title", value="Quick Student Feedback")
teacher_name = st.text_input("Teacher name (optional)", value="Your Name")
collect_email = st.checkbox("Collect email from students?", value=True)
questions = st.text_area("Enter up to 5 short questions (one per line)", value="How would you rate today's lesson?\nWhat went well?\nWhat could improve?")


def generate_streamlit_code(title, teacher, email_flag, q_text):
    qs = [q.strip() for q in q_text.splitlines() if q.strip()][:5]
    lines = []
    lines.append("import streamlit as st")
    lines.append("import csv")
    lines.append("from datetime import datetime")
    lines.append("")
    lines.append(f"st.title({title!r})")
    lines.append(f"st.write('Teacher: ' + {teacher!r})")
    lines.append("")
    if email_flag:
        lines.append("email = st.text_input('Your Email (optional)')")
    lines.append("responses = {}")
    lines.append("")
    for i, q in enumerate(qs, start=1):
        var = f"q{i}"
        lines.append(f"{var} = st.text_input({q!r})")
        lines.append(f"responses[{q!r}] = {var}")
    lines.append("")
    lines.append("if st.button('Submit'):")
    lines.append("    responses['timestamp'] = datetime.now().isoformat()")
    lines.append("    try:")
    lines.append("        with open('feedback_responses.csv', 'a', newline='', encoding='utf-8') as f:")
    lines.append("            writer = csv.DictWriter(f, fieldnames=responses.keys())")
    lines.append("            # write header if file is empty")
    lines.append("            f.seek(0, 2)")
    lines.append("            if f.tell() == 0:")
    lines.append("                writer.writeheader()")
    lines.append("            writer.writerow(responses)")
    lines.append("        st.success('Thanks for your feedback!')")
    lines.append("    except Exception as e:")
    lines.append("        st.error('Could not save response: ' + str(e))")

    return "\n".join(lines)

if st.button("Generate App Code"):
    code_text = generate_streamlit_code(app_title, teacher_name, collect_email, questions)
    st.code(code_text, language='python')

    # provide download
    b = code_text.encode('utf-8')
    b64 = base64.b64encode(b).decode()
    href = f"data:file/text;base64,{b64}"
    st.markdown(f"[Download generated app as feedback_app.py]({href})", unsafe_allow_html=True)

st.markdown("---")

# ----------------------
# 4) Quick usage guide and tie to microcredential
# ----------------------
st.header("4 — Education 5.0: Self-Paced Learning & Microcredential Pathways")
st.write("**The Power of Microlearning and Microcredentials**:")

st.markdown("""
- I have developed a **microcredential course** made up of small, focused learning units.
- Each micro-module includes a **1-minute explainer video** and a **3-question quiz**.
- Learners complete the module, then share feedback using a quick **Streamlit feedback app**.
- Simple analytics (even from a CSV) track participation and performance, which contribute to awarding **digital badges**.
- In the future, **AI-driven analytics** can personalize the next module based on each learner’s progress and needs.
""")


st.markdown("---")
st.markdown("""
**Quick Links:**  
[Microcredential Course](https://mooc.christuniversity.in/course/view.php?id=157) | [Session-1](https://13july.streamlit.app)
""")