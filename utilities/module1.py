import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Advanced Python with Streamlit - Module 1",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 Module 1: Introduction to Streamlit and Interactive Web Applications")
st.markdown("---")

# Sidebar Navigation
st.sidebar.title("📚 Module 1 Contents")
topic = st.sidebar.radio(
    "Select a Topic",
    [
        "Course Overview",
        "1. Introduction to Streamlit",
        "2. Setting up the Development Environment",
        "3. Streamlit Application Structure",
        "4. Text Elements and Display Functions",
        "5. User Input Widgets",
        "6. Buttons, Checkboxes, Radio Buttons and Select Boxes",
        "7. Forms and Interactive Components",
        "8. Layouts and Containers",
        "9. Session State Management",
        "10. Error Handling and Debugging",
        "Module Summary"
    ]
)

# Course Overview
if topic == "Course Overview":
    st.header("Course Overview")

    st.write("""
    Streamlit is an open-source Python framework that enables developers,
    educators, data scientists, and students to create interactive web
    applications with minimal effort. Unlike traditional web development,
    Streamlit does not require HTML, CSS, or JavaScript knowledge.

    In this module, you will learn the fundamentals of Streamlit, build
    interactive interfaces, manage application states, and create
    user-friendly web applications.
    """)

    st.success("Learning Outcomes")
    st.markdown("""
    - Understand Streamlit architecture and workflow.
    - Create simple Streamlit applications.
    - Use widgets for user interaction.
    - Design application layouts.
    - Manage application state.
    - Debug and handle application errors.
    """)

# Topic 1
elif topic == "1. Introduction to Streamlit":
    st.header("1. Introduction to Streamlit")

    st.write("""
    Streamlit is a Python library that allows developers to build
    data-driven web applications quickly and efficiently.
    """)

    st.subheader("Why Streamlit?")
    st.markdown("""
    - Easy to learn and use
    - Pure Python coding
    - Interactive widgets
    - Real-time updates
    - Rapid prototyping
    - Suitable for AI and Data Science applications
    """)

    st.subheader("Installation")
    st.code("pip install streamlit", language="bash")

    st.subheader("First Streamlit Program")
    st.code("""
import streamlit as st

st.title("Hello World")
st.write("Welcome to Streamlit!")
""", language="python")

# Topic 2
elif topic == "2. Setting up the Development Environment":
    st.header("2. Setting up the Development Environment")

    st.markdown("""
    ### Software Requirements
    - Python 3.10+
    - VS Code / PyCharm
    - Streamlit
    - GitHub Desktop (Optional)

    ### Installation Steps
    1. Install Python.
    2. Install Streamlit using pip.
    3. Create a project folder.
    4. Create app.py.
    5. Run the application.
    """)

    st.code("streamlit run app.py", language="bash")

# Topic 3
elif topic == "3. Streamlit Application Structure":
    st.header("3. Streamlit Application Structure")

    st.write("""
    A Streamlit application is a Python script executed from top to bottom
    whenever a user interacts with the interface.
    """)

    st.code("""
import streamlit as st

st.title("My App")

name = st.text_input("Enter Name")

if name:
    st.write("Hello", name)
""", language="python")

    st.info("Every widget interaction causes the script to rerun.")

# Topic 4
elif topic == "4. Text Elements and Display Functions":
    st.header("4. Text Elements and Display Functions")

    st.markdown("""
    Streamlit provides various text display functions.
    """)

    st.code("""
st.title("Main Title")
st.header("Header")
st.subheader("Sub Header")
st.text("Simple Text")
st.write("Flexible Output")
st.markdown("**Bold Text**")
""", language="python")

# Topic 5
elif topic == "5. User Input Widgets":
    st.header("5. User Input Widgets")

    st.markdown("""
    Widgets collect information from users.
    """)

    st.code("""
name = st.text_input("Name")
age = st.number_input("Age")
dob = st.date_input("Date of Birth")
""", language="python")

    st.subheader("Common Widgets")
    st.markdown("""
    - text_input()
    - number_input()
    - slider()
    - date_input()
    - selectbox()
    - multiselect()
    """)

# Topic 6
elif topic == "6. Buttons, Checkboxes, Radio Buttons and Select Boxes":
    st.header("6. Buttons, Checkboxes, Radio Buttons and Select Boxes")

    st.code("""
if st.button("Click Me"):
    st.success("Button Clicked")

agree = st.checkbox("I Agree")

gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)

course = st.selectbox(
    "Select Course",
    ["BCA", "MCA", "BSc"]
)
""", language="python")

# Topic 7
elif topic == "7. Forms and Interactive Components":
    st.header("7. Forms and Interactive Components")

    st.write("""
    Forms allow multiple inputs to be submitted together.
    """)

    st.code("""
with st.form("student_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")

    submit = st.form_submit_button("Submit")

    if submit:
        st.success("Form Submitted")
""", language="python")

# Topic 8
elif topic == "8. Layouts and Containers":
    st.header("8. Layouts and Containers")

    st.markdown("""
    Streamlit supports modern layouts.
    """)

    st.code("""
col1, col2 = st.columns(2)

with col1:
    st.write("Column 1")

with col2:
    st.write("Column 2")
""", language="python")

    st.subheader("Layout Components")
    st.markdown("""
    - columns()
    - container()
    - expander()
    - sidebar()
    - tabs()
    """)

# Topic 9
elif topic == "9. Session State Management":
    st.header("9. Session State Management")

    st.write("""
    Session State stores variables across reruns.
    """)

    st.code("""
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase"):
    st.session_state.counter += 1

st.write(
    "Counter:",
    st.session_state.counter
)
""", language="python")

# Topic 10
elif topic == "10. Error Handling and Debugging":
    st.header("10. Error Handling and Debugging")

    st.markdown("""
    Error handling improves application reliability.
    """)

    st.code("""
try:
    num = int(
        st.text_input("Number")
    )
    st.write(num)

except:
    st.error(
        "Please enter a valid number"
    )
""", language="python")

    st.subheader("Debugging Tips")
    st.markdown("""
    - Read error messages carefully.
    - Use st.write() for testing.
    - Check variable names.
    - Validate user inputs.
    - Test incrementally.
    """)

# Summary
elif topic == "Module Summary":
    st.header("Module Summary")

    st.success("""
    Congratulations! You have completed Module 1.
    """)

    st.markdown("""
    ### Key Concepts Learned
    - Streamlit Fundamentals
    - Application Structure
    - Text Display Functions
    - Interactive Widgets
    - Forms
    - Layout Design
    - Session State
    - Error Handling

    ### Next Module
    Data Handling and Visualization
    """)