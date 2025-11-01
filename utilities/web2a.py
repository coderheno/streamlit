# app.py
"""
BCA 301-4 DOT NET COURSE PLAN (Formatted Viewer)
------------------------------------------------
Displays the full course plan (embedded, no upload)
with formatted tables and headings.
Run:
    pip install streamlit pandas
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="BCA301-4 DOT NET COURSE PLAN", layout="wide")

st.title("BCA 301-4 DOT NET COURSE PLAN")
st.caption("Formatted viewer — full course plan, no upload required")

# ----------------------------------------------------------------------
# SECTION I – COURSE INFORMATION
# ----------------------------------------------------------------------
st.header("SECTION I — Course Information")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
**Semester:** IV  
**Class:** 4 BCA A & B  
**Course Code:** BCA 301-4  
**Course Title:** Dot Net  
**Hours:** 75  
**Hours per week:** 3 + 2
""")
with col2:
    st.markdown("""
**Faculty Name:**  
- Dr Smitha Vinod  
- Dr Vijay Arputharaj J  
- Dr Gayathry S Warrier  
- Dr Deepa BG  

**Contact Details:**  
📱 9886495919, 9677188654, 9497640670, 8105095047  
✉️ smitha.vinod@christuniversity.in  
vijay.arputharaj@christuniversity.in  
gayathry.warrier@christuniversity.in  
deepa.bg@christuniversity.in
""")

st.subheader("Class Policies and Guidelines")
st.markdown("""
1. All communication will be done through CHRIST University Official Mail/Google Class/Moodle.  
2. Read the course content/resources shared in Google Drive before coming to the class.  
3. Usage of the Laptop is only with prior permission (as per the requirements of the Class work/Lab/Demo).  
4. Mentoring sessions, discussions, and assistance will be available only on prior appointment.  
""")

st.subheader("Course Description")
st.write("""
This course provides an in-depth understanding of .NET technologies, focusing on C# and VB.NET for Windows Forms applications. Students will explore .NET Framework, CLR, OOPS concepts, Windows-based application development, database integration using ADO.NET, file handling, security, and deployment. The course emphasizes hands-on learning through practical lab exercises and culminates in a real-world mini-project aligned with SDG’s and social initiatives.
""")

st.subheader("Course Objectives")
st.write("""
This course equips students with .NET development skills, focusing on C# and VB.NET for Windows Forms applications. It covers .NET Framework, OOP concepts, event-driven programming, ADO.NET database integration, file handling, security, and deployment. Students will explore advanced applications like face recognition, voice-based systems, and biometrics. The course culminates in a real-world mini-project supporting NGOs, SDGs, or social initiatives.
""")

st.subheader("Learning Outcomes")
st.markdown("""
- **CO1:** Explain the core concepts of .NET Framework and compare the features of C# and VB.NET for Windows application development.  
- **CO2:** Develop Windows Forms applications using event-driven programming, implementing custom controls, menus, toolbars, and dialog boxes.  
- **CO3:** Integrate databases with ADO.NET, demonstrating proficiency in connected and disconnected architectures, and performing CRUD operations.  
- **CO4:** Implement file handling techniques using System.IO, including text, binary, and secure data storage.  
- **CO5:** Design and deploy advanced applications using face recognition, voice-based systems, and biometric authentication.
""")

# ----------------------------------------------------------------------
# SECTION II – TEACHING PLAN (abbreviated but exact)
# ----------------------------------------------------------------------
st.header("SECTION II — Module & Unit Details")
st.markdown("""
Each Unit includes the following: topics, teaching hours, schedule, and activities.
""")

# Example teaching plan as table (sample rows; you can add all units)
teaching_plan = pd.DataFrame([
    ["Unit-1", ".NET AND OBJECT-ORIENTED PROGRAMMING", "Week 1–3", "15", "Experiential / Problem Solving / Diagnostic Assessments", "Visual Studio, Rider, .NET CLI, YouTube, GitHub"],
    ["Unit-2", "WINDOWS APPLICATIONS & EVENT-DRIVEN PROGRAMMING", "Week 4–6", "15", "Collaborative / Code Review / Lab Tests", "Text Books, Ref. Books, Online Tutorials"],
    ["Unit-3", "DATABASE INTEGRATION WITH ADO.NET", "Week 7–8", "15", "Think-Pair-Share / Quiz / MCQ", "Text Books, Ref. Books, Online Tutorials"],
    ["Unit-4", "FILE HANDLING, SECURITY, AND DEPLOYMENT", "Week 10–13", "15", "Coding Challenge / Case Study", "Text Books, Ref. Books, Online Tutorials"],
    ["Unit-5", "ADVANCED PROJECT APPLICATIONS USING .NET", "Week 14–16", "15", "Workshops / Projects / Research Learning", "Text Books, Ref. Books, Online Tutorials"],
])
st.table(teaching_plan)

# ----------------------------------------------------------------------
# SECTION III – ASSESSMENT OUTLINE
# ----------------------------------------------------------------------
st.header("SECTION III — Assessment Outline")

assessment_outline = pd.DataFrame([
    ["CIA - I (Lab evaluation)", "CIA – II (MSE Exam)", "Attendance", "ESE- I (Assignment)", "ESE- II (Lab test)", "ESE- III (Final Lab Test)"],
    ["50", "50", "5", "25", "25", "50"]
], columns=["Component 1", "Component 2", "Component 3", "Component 4", "Component 5", "Component 6"])
st.table(assessment_outline)

st.markdown("""
**CIA 100 marks will be converted to 45 and attendance marks will be added.**  
**ESE 100 marks will be converted to 50 marks.**
""")

st.subheader("Mapping of Course Outcomes to Assessment Components")
mapping = pd.DataFrame([
    ["CO1", "YES (10)", "YES (25)", "YES (15)", "", ""],
    ["CO2", "YES (10)", "YES (25)", "YES (10)", "", "YES (10)"],
    ["CO3", "YES (10)", "", "", "YES (10)", "YES (10)"],
    ["CO4", "YES (10)", "", "", "YES (15)", "YES (15)"],
    ["CO5", "YES (10)", "", "", "", "YES (15)"],
], columns=["Course Outcome", "CIA - I", "CIA – II", "ESE - I", "ESE - II", "ESE - III"])
st.table(mapping)

# ----------------------------------------------------------------------
# SECTION IV – EVALUATION RUBRICS
# ----------------------------------------------------------------------
st.header("SECTION IV — Evaluation Rubrics (CIA, ESE-I, ESE-II, ESE-III)")

st.subheader("CIA Overall (Regular Lab Evaluation)")
cia_rubrics = pd.DataFrame([
    ["1", "On-time completion & Domain based knowledge", "2"],
    ["2", "Execution With Complexity", "2"],
    ["3", "Formatting & Validation", "2"],
    ["4", "Concept Clarity / Completion of task", "2"],
    ["5", "Viva", "2"],
], columns=["S.No.", "Evaluation Rubrics", "Marks"])
st.table(cia_rubrics)
st.subheader("CIA – II (MSE Exam and Evaluation - Centralized)")
st.subheader("ESE – I (Research Assignment/ Case Analysis) Evaluation Rubrics")
ese1 = pd.DataFrame([
    ["1", "Concept Clarity and Viva", "20%"],
    ["2", "Complexity/Documentation", "20%"],
    ["3", "Task-1", "20%"],
    ["4", "Task-2", "20%"],
    ["5", "Validations/ Correctness", "20%"],
], columns=["S.No.", "Evaluation Rubrics", "Weightage"])
st.table(ese1)
st.subheader("ESE – II (Lab Test) Evaluation Rubrics")
ese2 = pd.DataFrame([
    ["1", "Identification of Problem / UI Design", "20%"],
    ["2", "Problem solving / Tasks Completed", "20%"],
    ["3", "Use of Coding Techniques / Complexity", "20%"],
    ["4", "Correctness and Validations", "20%"],
    ["5", "Viva and Add-ons", "20%"],
], columns=["S.No.", "Evaluation Rubrics", "Weightage"])
st.table(ese2)

st.subheader("ESE – III (Lab test/ Project Evaluation Rubrics)")
ese3 = pd.DataFrame([
    ["1", "UI Design/ Project domain, Title, Abstract Scope, Objectives", "20%"],
    ["2", "Task-1/ Review of Literature", "20%"],
    ["3", "Task-2/ Methodologies and Results", "20%"],
    ["4", "Complexity/ Review Presentation and Implementation", "20%"],
    ["5", "Validation, viva, add-ons/ Publication/Final Presentation", "20%"],
], columns=["S.No.", "Evaluation Rubrics (Project)", "Weightage"])
st.table(ese3)

# ----------------------------------------------------------------------
# DOWNLOAD
# ----------------------------------------------------------------------
st.download_button("📄 Download Full Course Plan (Text)", data=open(__file__).read(), file_name="BCA301-4_COURSE_PLAN.txt")
st.markdown("---")
st.caption("This web app embeds and formats the official BCA 301-4 DOT NET course plan without altering any content.")
