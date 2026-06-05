import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Module 4 - Version Control and Project Deployment",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Module 4: Version Control and Project Deployment")
st.markdown("---")

# Sidebar Navigation
st.sidebar.title("📚 Module 4 Contents")

topic = st.sidebar.radio(
    "Select a Topic",
    [
        "Module Overview",
        "1. Introduction to Git and GitHub",
        "2. Installing and Configuring GitHub Desktop",
        "3. Cloning and Managing Repositories",
        "4. Version Control Workflows",
        "5. Branching and Collaboration",
        "6. Project Documentation",
        "7. Streamlit Application Deployment",
        "8. Project Maintenance and Updates",
        "9. Best Practices for Collaborative Development",
        "10. Industry Applications and Case Studies",
        "Module Summary"
    ]
)

# Module Overview
if topic == "Module Overview":

    st.header("Module Overview")

    st.write("""
    Modern software development requires efficient project management,
    version control, collaboration, and deployment practices. Git and
    GitHub are industry-standard tools that help developers track code
    changes, collaborate with teams, and manage projects effectively.
    This module introduces learners to version control concepts,
    GitHub Desktop, repository management, and Streamlit deployment.
    """)

    st.success("Learning Outcomes")

    st.markdown("""
    - Understand version control concepts.
    - Use GitHub Desktop for repository management.
    - Clone, commit, push, and pull projects.
    - Collaborate using branches.
    - Document software projects effectively.
    - Deploy Streamlit applications online.
    """)

# Topic 1
elif topic == "1. Introduction to Git and GitHub":

    st.header("1. Introduction to Git and GitHub")

    st.write("""
    Git is a distributed version control system used to track changes
    in source code. GitHub is a cloud platform that hosts Git repositories
    and enables collaboration among developers.
    """)

    st.subheader("Benefits")

    st.markdown("""
    - Tracks code changes
    - Supports teamwork
    - Maintains project history
    - Enables rollback to previous versions
    - Facilitates open-source collaboration
    """)

# Topic 2
elif topic == "2. Installing and Configuring GitHub Desktop":

    st.header("2. Installing and Configuring GitHub Desktop")

    st.write("""
    GitHub Desktop provides a graphical interface for managing repositories.
    """)

    st.markdown("""
    ### Installation Steps
    1. Download GitHub Desktop
    2. Install the application
    3. Sign in with GitHub account
    4. Configure Git settings
    5. Create or clone repositories
    """)

# Topic 3
elif topic == "3. Cloning and Managing Repositories":

    st.header("3. Cloning and Managing Repositories")

    st.write("""
    Cloning creates a local copy of a remote repository.
    """)

    st.code("""
GitHub Desktop
→ File
→ Clone Repository
→ Select Repository
→ Choose Local Path
→ Clone
""")

    st.subheader("Repository Operations")

    st.markdown("""
    - Create Repository
    - Clone Repository
    - Open Repository
    - Delete Repository
    - Sync Changes
    """)

# Topic 4
elif topic == "4. Version Control Workflows":

    st.header("4. Version Control Workflows")

    st.write("""
    Version control enables developers to track and manage code changes.
    """)

    st.code("""
Modify Files
      ↓
Commit Changes
      ↓
Push to GitHub
      ↓
Collaborators Pull Updates
""")

    st.subheader("Common Operations")

    st.markdown("""
    - Commit
    - Push
    - Pull
    - Fetch
    - Sync
    """)

# Topic 5
elif topic == "5. Branching and Collaboration":

    st.header("5. Branching and Collaboration")

    st.write("""
    Branches allow developers to work on features independently.
    """)

    st.markdown("""
    ### Advantages of Branching

    - Parallel development
    - Safe experimentation
    - Team collaboration
    - Easy feature integration
    """)

    st.code("""
Main Branch
      |
      |---- Feature Branch
      |
      |---- Testing Branch
""")

# Topic 6
elif topic == "6. Project Documentation":

    st.header("6. Project Documentation")

    st.write("""
    Documentation helps users and developers understand the project.
    """)

    st.subheader("README Contents")

    st.markdown("""
    - Project Title
    - Objective
    - Features
    - Installation Steps
    - Usage Instructions
    - Screenshots
    - Contributors
    """)

    st.code("""
# Student Performance Predictor

A Streamlit-based machine learning application
for predicting student performance.
""", language="markdown")

# Topic 7
elif topic == "7. Streamlit Application Deployment":

    st.header("7. Streamlit Application Deployment")

    st.write("""
    Deployment makes Streamlit applications accessible online.
    """)

    st.markdown("""
    ### Deployment Steps

    1. Upload project to GitHub
    2. Connect GitHub repository
    3. Deploy using Streamlit Community Cloud
    4. Share application URL
    """)

    st.code("""
streamlit run app.py
""", language="bash")

# Topic 8
elif topic == "8. Project Maintenance and Updates":

    st.header("8. Project Maintenance and Updates")

    st.write("""
    Software projects require regular maintenance and updates.
    """)

    st.markdown("""
    Activities include:
    - Bug Fixing
    - Feature Enhancements
    - Security Updates
    - Performance Improvements
    - User Feedback Integration
    """)

# Topic 9
elif topic == "9. Best Practices for Collaborative Development":

    st.header("9. Best Practices for Collaborative Development")

    st.markdown("""
    ### Recommended Practices

    - Use meaningful commit messages
    - Create feature branches
    - Review code before merging
    - Maintain project documentation
    - Test before deployment
    - Backup repositories regularly
    """)

# Topic 10
elif topic == "10. Industry Applications and Case Studies":

    st.header("10. Industry Applications and Case Studies")

    st.markdown("""
    ### Software Companies
    GitHub for team collaboration

    ### Startups
    Rapid product development

    ### Research Projects
    Collaborative code management

    ### Educational Projects
    Student project tracking

    ### Open Source Communities
    Global software development
    """)

# Module Summary
elif topic == "Module Summary":

    st.header("Module Summary")

    st.success("""
    Congratulations! You have completed Module 4.
    """)

    st.markdown("""
    ### Key Concepts Covered

    ✅ Git and GitHub Fundamentals

    ✅ GitHub Desktop

    ✅ Repository Management

    ✅ Version Control Workflows

    ✅ Branching and Collaboration

    ✅ Project Documentation

    ✅ Streamlit Deployment

    ✅ Project Maintenance

    ✅ Collaborative Development Practices

    ✅ Industry Applications
    """)

    st.info("""
    Course Outcome Addressed:

    CO5: Employ GitHub-based version control and
    project management practices for collaborative
    software development and deployment.
    """)

    st.markdown("""
    ### Skills Acquired

    - Version Control
    - Repository Management
    - Team Collaboration
    - GitHub Workflows
    - Documentation
    - Application Deployment
    """)

    st.success("""
    🎓 You have completed all modules of
    Advanced Python with Streamlit.
    """)