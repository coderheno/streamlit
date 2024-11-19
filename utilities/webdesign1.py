import streamlit as st
from datetime import datetime, timedelta

def web_designing_course_plan():
    # Base Dates
    start_date = datetime.today() + timedelta(days=1)
    mse_start = datetime(2025, 2, 3)
    mse_end = datetime(2025, 2, 8)
    semester_end = datetime(2024, 4, 30)

    # Tabs for better interaction
    tabs = st.tabs(["Lectures", "Practicals", "Tools & Resources", "Activities & Submission"])

    # Lectures Tab
    with tabs[0]:
        st.header("Lecture Plan")
        st.write("Detailed plan for all lectures in the semester.")
        lecture_schedule = [
            {"unit": "UNIT-I: WORLD WIDE WEB", "topics": ["Introduction to Internet", "TCP/IP Protocols"], "start_date": start_date, "hours": 4},
            {"unit": "UNIT-II: HTML", "topics": ["HTML Basics, Web Page Development"], "start_date": start_date + timedelta(days=21), "hours": 4},
            {"unit": "UNIT-III: CSS", "topics": ["CSS Basics, Benefits"], "start_date": start_date + timedelta(days=49), "hours": 4},
            {"unit": "MID SEMESTER EXAM", "topics": ["MSE Week"], "start_date": mse_start, "end_date": mse_end},
            {"unit": "UNIT-IV: JAVASCRIPT", "topics": ["Basics of JavaScript"], "start_date": mse_end + timedelta(days=7), "hours": 4},
            {"unit": "UNIT-V: TOOLS", "topics": ["Adobe Photoshop, HTML Editors"], "start_date": mse_end + timedelta(days=21), "hours": 4},
        ]
        for lecture in lecture_schedule:
            st.markdown(f"### {lecture['unit']}")
            st.write(f"**Topics:** {', '.join(lecture['topics'])}")
            if "end_date" in lecture:
                st.write(f"**Dates:** {lecture['start_date'].strftime('%d %b %Y')} - {lecture['end_date'].strftime('%d %b %Y')}")
            else:
                st.write(f"**Start Date:** {lecture['start_date'].strftime('%d %b %Y')} ({lecture['hours']} hours/week)")

    # Practicals Tab
    with tabs[1]:
        st.header("Practical Plan")
        st.write("Plan for lab exercises and hands-on activities.")
        practical_schedule = [
            {"week": 1, "exercise": "Creating a simple web page for the department", "dates": "06/12/2023 - 09/12/2023"},
            {"week": 2, "exercise": "Creating a personalized web page for a company", "dates": "11/12/2023 - 16/12/2023"},
            {"week": 3, "exercise": "Creating an NGO website to embed multimedia", "dates": "18/12/2023 - 23/12/2023"},
            {"week": 4, "exercise": "Creating a travel/hotel reservation page/site", "dates": "02/01/2024 - 06/01/2024"},
            {"week": 6, "exercise": "Lab Test 1: Personalized website with themes", "dates": "15/01/2024 - 20/01/2024"},
            {"week": 9, "exercise": "Login Page Validation", "dates": "05/02/2024 - 10/02/2024"},
            {"week": 12, "exercise": "Student project domain selection and finalization", "dates": "26/02/2024 - 02/03/2024"},
        ]
        for practical in practical_schedule:
            st.write(f"**Week {practical['week']}:** {practical['exercise']} ({practical['dates']})")

    # Tools & Resources Tab
    with tabs[2]:
        st.header("Tools and Resources")
        st.write("Recommended tools and resources for the course.")
        st.markdown("""
        - **HTML Editors:** Notepad++, Sublime Text, Visual Studio Code
        - **CSS Tools:** Adobe Dreamweaver, Visual Studio Code
        - **Version Control & Deployment Tools:** 
          - GitHub
          - GitHub Desktop
          - Firebase
          - Netlify
        - **Online Resources:** 
          - [W3Schools](https://www.w3schools.com)
          - [DigitalOcean Tutorials](https://www.digitalocean.com/community/tutorials)
        - **Books:** 
          - Steven M. Schafer, HTML, XHTML and CSS Bible, 5th Edition, Wiley-Eastern Publishing Inc., 2011
        """)

    # Activities & Submission Tab
    with tabs[3]:
        st.header("Activities, Submission & Interaction")
        st.subheader("Ice-Breaking Interactive Activity")
        st.write("**Activity:** Submit a brief HTML page introducing yourself.")
        st.markdown("""
        - Content should include:
          - Your Name
          - A short bio
          - Your interest in Web Designing
        - **Submission Mode:** Upload your HTML file to Google Classroom.
        - **Deadline:** First class
        """)
        st.subheader("Classroom Invite Link & Code")
        st.write("**Invite Link:** [Google Classroom](https://classroom.google.com/c/NzMyNDY5NDQ3MTMx?cjc=z2d5nfm)")
        st.write("**Class Code:** z2d5nfm")

    st.success("Course plan updated with new features!")

# To execute the function
web_designing_course_plan()
