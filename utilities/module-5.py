import streamlit as st

st.set_page_config(
    page_title="Module 5 - Capstone Project",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Module 5: Capstone Project and Industry Applications")
st.markdown("---")

st.sidebar.title("📚 Module 5 Contents")

topic = st.sidebar.radio(
    "Select Topic",
    [
        "Module Overview",
        "1. Capstone Project Introduction",
        "2. Project Planning",
        "3. Requirement Analysis",
        "4. Designing Streamlit Solutions",
        "5. Integrating Data Handling",
        "6. Integrating Machine Learning",
        "7. Testing and Validation",
        "8. GitHub Repository Management",
        "9. Project Presentation",
        "10. Industry Applications",
        "Project Guidelines",
        "Module Summary"
    ]
)

if topic == "Module Overview":

    st.header("Module Overview")

    st.write("""
    The Capstone Project serves as the culmination of the course,
    allowing learners to apply Streamlit, Python, Data Handling,
    Machine Learning, GitHub, and Deployment concepts to solve
    real-world problems.
    """)

    st.success("""
    Learning Outcomes:
    • Plan a software project
    • Design Streamlit applications
    • Integrate data processing
    • Integrate machine learning models
    • Deploy applications
    • Present project outcomes
    """)

elif topic == "1. Capstone Project Introduction":

    st.header("1. Capstone Project Introduction")

    st.write("""
    A capstone project is a comprehensive project that demonstrates
    the knowledge and skills acquired throughout the course.
    """)

    st.markdown("""
    Components:
    - Problem Statement
    - Solution Design
    - Implementation
    - Testing
    - Deployment
    - Documentation
    """)

elif topic == "2. Project Planning":

    st.header("2. Project Planning")

    st.markdown("""
    Project planning involves:
    
    - Defining objectives
    - Identifying users
    - Selecting technologies
    - Creating timelines
    - Allocating responsibilities
    """)

elif topic == "3. Requirement Analysis":

    st.header("3. Requirement Analysis")

    st.markdown("""
    Requirement Analysis identifies:

    - Functional Requirements
    - Non-functional Requirements
    - User Needs
    - System Constraints
    """)

elif topic == "4. Designing Streamlit Solutions":

    st.header("4. Designing Streamlit Solutions")

    st.markdown("""
    Design Considerations:

    - User-friendly Interface
    - Navigation
    - Forms
    - Charts
    - Responsiveness
    """)

elif topic == "5. Integrating Data Handling":

    st.header("5. Integrating Data Handling")

    st.markdown("""
    Data Handling Features:

    - CSV Upload
    - JSON Processing
    - Data Cleaning
    - Visualization
    - Reporting
    """)

elif topic == "6. Integrating Machine Learning":

    st.header("6. Integrating Machine Learning")

    st.markdown("""
    Machine Learning Integration:

    - Load Model
    - Accept User Inputs
    - Prediction
    - Classification
    - Result Interpretation
    """)

elif topic == "7. Testing and Validation":

    st.header("7. Testing and Validation")

    st.markdown("""
    Testing Activities:

    - Functional Testing
    - Input Validation
    - User Acceptance Testing
    - Error Handling
    """)

elif topic == "8. GitHub Repository Management":

    st.header("8. GitHub Repository Management")

    st.markdown("""
    Repository Deliverables:

    - Source Code
    - README.md
    - Screenshots
    - Commit History
    - Project Documentation
    """)

elif topic == "9. Project Presentation":

    st.header("9. Project Presentation")

    st.markdown("""
    Presentation Structure:

    - Introduction
    - Problem Statement
    - Methodology
    - Demo
    - Results
    - Future Scope
    """)

elif topic == "10. Industry Applications":

    st.header("10. Industry Applications")

    st.markdown("""
    Domains:

    - Healthcare
    - Education
    - Agriculture
    - Retail
    - Finance
    - Environment
    """)

elif topic == "Project Guidelines":

    st.header("Capstone Project Guidelines")

    st.success("""
    Project Requirements
    """)

    st.markdown("""
    ✔ Streamlit Interface

    ✔ Minimum 5 User Inputs

    ✔ Data Handling (CSV/JSON)

    ✔ At Least 2 Visualizations

    ✔ Machine Learning Component (Optional for Basic Level)

    ✔ GitHub Repository

    ✔ Deployment

    ✔ Documentation

    ✔ Project Presentation
    """)

elif topic == "Module Summary":

    st.header("Module Summary")

    st.success("""
    Congratulations!
    You have completed the course.
    """)

    st.markdown("""
    Skills Acquired:

    ✅ Streamlit Development

    ✅ Data Handling

    ✅ Data Visualization

    ✅ Machine Learning Integration

    ✅ GitHub Version Control

    ✅ Deployment

    ✅ Project Management
    """)