import streamlit as st

st.set_page_config(page_title="Python Quiz – CO1 & CO2", layout="centered")
st.title("🐍 Python Quiz: Control Structures & Data Structures")
st.markdown("Test your knowledge with slightly complex, output-based and concept MCQs!")

# Instructions and Learning Outcomes
with st.expander("📘 Instructions & Learning Outcomes"):
    st.markdown("""
### 🌟 Course Outcomes
- **CO1**: Apply programming logics using control statements and functions
- **CO2**: Understand Python environment and data structures like lists, tuples, sets, and dictionaries

### 📚 RBT Levels
- **L2 – Understanding**
- **L3 – Applying**
- **L4 – Analyzing**

### 📜 Guidelines
- Multiple correct options may be present.
- Use checkboxes to select all that apply.
- Click "Start Quiz" to begin.
""")

start = st.button("🚀 Start Quiz")

# Define questions with checkbox-style options
questions = [
    {
        "question": "Q1. What will be printed?",
        "code": "def check():\n    x = 5\n    if x and not 0:\n        print('Pass')\n    else:\n        print('Fail')\ncheck()",
        "options": ["Pass", "Fail", "Error", "None"],
        "answer": ["Pass"],
        "co": "CO1",
        "rbt": "L3",
        "explanation": "x is 5 (truthy), not 0 is True, so prints 'Pass'."
    },
    {
        "question": "Q2. Which of the following are valid Python identifiers?",
        "options": ["student_1", "def", "_private", "1number"],
        "answer": ["student_1", "_private"],
        "co": "CO2",
        "rbt": "L2",
        "explanation": "Identifiers can't start with numbers or use keywords."
    },
    {
        "question": "Q3. Output of this code?",
        "code": "x = 4 ** 2 + 3 * 2\nprint(x)",
        "options": ["22", "16", "10", "None"],
        "answer": ["22"],
        "co": "CO1",
        "rbt": "L4",
        "explanation": "4 ** 2 = 16, 3 * 2 = 6, total = 22."
    },
    {
        "question": "Q4. Which are immutable types?",
        "options": ["List", "Tuple", "Dictionary", "String"],
        "answer": ["Tuple", "String"],
        "co": "CO2",
        "rbt": "L2",
        "explanation": "Tuples and strings cannot be modified."
    },
    {
        "question": "Q5. Output of the following?",
        "code": "for i in range(5, 0, -2):\n    print(i, end=' ')",
        "options": ["5 3 1", "5 4 3", "3 1", "Error"],
        "answer": ["5 3 1"],
        "co": "CO1",
        "rbt": "L4",
        "explanation": "range(5,0,-2) gives 5,3,1."
    }
]

# Quiz logic
if start:
    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"### {q['question']}")
        if "code" in q:
            st.code(q['code'], language='python')
        selections = []
        for option in q["options"]:
            selected = st.checkbox(option, key=f"q{i}_{option}")
            if selected:
                selections.append(option)

        # Evaluate answer
        if set(selections) == set(q["answer"]):
            st.success("✅ Correct!")
            score += 1
        elif selections:
            st.error(f"❌ Incorrect. Correct: {', '.join(q['answer'])}")

        if selections:
            st.info(f"💡 {q['explanation']} ({q['co']}, {q['rbt']})")
        st.markdown("---")

    st.markdown(f"### 🧾 Final Score: **{score} / {len(questions)}**")
else:
    st.warning("Click **Start Quiz** to begin.")
