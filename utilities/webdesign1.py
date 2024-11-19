import streamlit as st
from datetime import datetime, timedelta

def web_designing_course_plan():
    # Set base dates
    start_date = datetime.today() + timedelta(days=1)
    mse_start = datetime(2025, 2, 3)
    mse_end = datetime(2025, 2, 8)
    semester_end = datetime(2024, 4, 30)

    # Title and Overview
    st.title("CHRIST (Deemed to be University) - Department of Commerce")
    st.header("4 B.Com (Hons) - WEB DESIGNING COURSE PLAN")
    st.write("**Faculty Members:** Vijay Arputharaj J, Sangeetha G, Poornima NV, Loveline Zeema J")
    st.write("Contact: vijay.arputharaj@christuniversity.in | sangeetha.g@christuniversity.in")

    # Course Details
    st.subheader("Course Details")
    st.write("**Course Code:** COH461B")
    st.write("**Hours:** 60 (2+2 per week, Theory + Lab)")
    st.write("**Objective:** To provide fundamental knowledge in Web Designing and practical skills to develop websites.")
    st.write("**Outcomes:**")
    st.markdown("""
    - LO1: Principles of creating effective web pages (CO1)
    - LO2: HTML & CSS basics, responsive design (CO2)
    - LO3: Digital imaging & programming skills (CO3)
    - LO4: Embedding social media content (CO4)
    """)

    # Schedule
    st.subheader("Schedule and Weekly Plan")
    weeks = [
        {"unit": "UNIT-I: WORLD WIDE WEB", "topics": ["Introduction to Internet", "TCP/IP Protocols"], "start_date": start_date, "hours": 4},
        {"unit": "UNIT-I: WORLD WIDE WEB", "topics": ["Web Browsers, Applications"], "start_date": start_date + timedelta(days=7), "hours": 4},
        {"unit": "UNIT-II: HTML", "topics": ["HTML Basics, Web Page Development"], "start_date": start_date + timedelta(days=21), "hours": 4},
        {"unit": "UNIT-II: HTML", "topics": ["Multimedia on Web Pages"], "start_date": start_date + timedelta(days=35), "hours": 4},
        {"unit": "UNIT-III: CSS", "topics": ["CSS Basics, Benefits"], "start_date": start_date + timedelta(days=49), "hours": 4},
        {"unit": "MID SEMESTER EXAM", "topics": ["MSE Week"], "start_date": mse_start, "end_date": mse_end},
        {"unit": "UNIT-III: CSS", "topics": ["CSS Page Layout"], "start_date": mse_end + timedelta(days=2), "hours": 4},
        {"unit": "UNIT-IV: JAVASCRIPT", "topics": ["Basics of JavaScript"], "start_date": mse_end + timedelta(days=7), "hours": 4},
        {"unit": "UNIT-V: TOOLS", "topics": ["Adobe Photoshop, HTML Editors"], "start_date": mse_end + timedelta(days=21), "hours": 4},
        {"unit": "UNIT-V: TOOLS", "topics": ["Review and Comprehensive Test"], "start_date": semester_end - timedelta(days=7), "hours": 4},
    ]

    for week in weeks:
        st.markdown(f"### {week['unit']}")
        st.write(f"**Topics:** {', '.join(week['topics'])}")
        if "end_date" in week:
            st.write(f"**Dates:** {week['start_date'].strftime('%d %b %Y')} - {week['end_date'].strftime('%d %b %Y')}")
        else:
            st.write(f"**Start Date:** {week['start_date'].strftime('%d %b %Y')} ({week['hours']} hours/week)")

    # Evaluation Pattern
    st.subheader("Evaluation Pattern")
    st.markdown("""
    - **CIA I:** Lab Exercises (20 Marks)
    - **CIA II:** Assignment/Practical Test (20 Marks)
    - **CIA III:** Individual Project (20 Marks)
    - **CIA V:** Comprehensive Exam (50 Marks)
    """)

    # Learning Outcomes and Rubrics
    st.subheader("Learning Outcomes and Evaluation Rubrics")
    st.markdown("""
    **LO1:** Understand web page principles (R1, R5)
    **LO2:** HTML & CSS techniques (R2, R3, R4)
    **LO3:** Digital imaging & programming (R1, R5)
    **LO4:** Embed social media (R2, R3)
    """)

    rubrics = {
        "Content": {"Excellent": 4, "Good": 3, "Satisfactory": 2},
        "Completion": {"Excellent": 4, "Good": 3, "Satisfactory": 2},
        "Creativity": {"Excellent": 4, "Good": 3, "Satisfactory": 2},
    }
    st.write("### Rubrics:")
    st.table(rubrics)

    st.success("Plan successfully displayed!")

# To execute the function
web_designing_course_plan()
