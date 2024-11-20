import streamlit as st
from datetime import datetime

def dot_net_course_plan():
    # Course Information
    st.title("BCA 301-4: Dot Net Tentative Plan")
    st.subheader("Course Details")
    st.markdown("""
    **Semester**: IV  
    **Class**: 4 BCA A & B  
    **Hours**: 75 (3 + 2 hours per week)  
    **Faculty**: Dr. Vijay Arputharaj J, Dr. Smitha Vinod 
    **Contact**:  
    - Dr. Vijay: 9677188654, vijay.arputharaj@christuniversity.in
    - Dr. Smitha Vinod: 9886495919, smitha.vinod@christuniversity.in  

    **Note:** This is a tentative plan and may be subject to changes.
    """)

    # Tabs for interaction
    tabs = st.tabs(["Lectures", "Practicals", "Tools & Resources", "Assessments", "Activities"])

    # Lectures Tab
    with tabs[0]:
        st.header("Lecture Plan")
        lecture_schedule = [
            {"unit": "UNIT-I: Windows Forms", "topics": ["Overview of System.Windows.Forms", "Anatomy of a Form", "Common Control I"], "dates": "20th - 30th Nov 2024"},
            {"unit": "UNIT-II: Anatomy of Basic C#", "topics": ["Variable Scope", "Basic Input and Output"], "dates": "9th - 14th Dec 2024"},
            {"unit": "UNIT-III: Exceptions", "topics": ["Throwing & Catching Exceptions", "Finally Block"], "dates": "13th - 25th Jan 2025"},
            {"unit": "UNIT-IV: Menu Creation and Dialog Controls", "topics": ["Toolbar Controls", "Dialog Properties"], "dates": "27th Jan - 22nd Feb 2025"},
            {"unit": "UNIT-V: Database Connectivity", "topics": ["SQL Server Queries", "Report Generation"], "dates": "3rd - 22nd Mar 2025"},
        ]
        for lecture in lecture_schedule:
            st.markdown(f"### {lecture['unit']}")
            st.write(f"**Topics:** {', '.join(lecture['topics'])}")
            st.write(f"**Dates:** {lecture['dates']}")

    # Practicals Tab
    with tabs[1]:
        st.header("Practical Plan")
        practical_schedule = [
            {"week": 1, "exercise": "Login application with multiple authentication strategies", "dates": "20th - 30th Nov 2024"},
            {"week": 2, "exercise": "Simple calculator or to-do list application", "dates": "2nd - 7th Dec 2024"},
            {"week": 3, "exercise": "Registration form with input validation", "dates": "9th - 14th Dec 2024"},
            {"week": 4, "exercise": "Survey application using additional controls", "dates": "6th - 11th Jan 2025"},
            {"week": 5, "exercise": "Event planner using date and time", "dates": "13th - 17th Jan 2025"},
            {"week": 6, "exercise": "Quiz application with menus and toolbars", "dates": "27th - 1st Feb 2025"},
            {"week": 7, "exercise": "Notepad application using dialog controls", "dates": "10th - 14th Feb 2025"},
            {"week": 8, "exercise": "Database connectivity for project management application", "dates": "3rd - 8th Mar 2025"},
            {"week": 9, "exercise": "Report generation and .exe file creation", "dates": "17th - 22nd Mar 2025"},
        ]
        for practical in practical_schedule:
            st.write(f"**Week {practical['week']}:** {practical['exercise']} ({practical['dates']})")

    # Tools & Resources Tab
    with tabs[2]:
        st.header("Tools and Resources")
        st.markdown("""
        - **IDE**: Visual Studio, Visual Studio Code  
        - **Version Control**: GitHub, Git  
        - **Databases**: SQL Server, SQLite  
        - **Online Resources**:  
          - [Microsoft Learn](https://learn.microsoft.com/en-us/)  
          - [W3Schools C#](https://www.w3schools.com/cs/)  
          - [TutorialsPoint](https://www.tutorialspoint.com/csharp/)  
        - **Books**:  
          - Andrew Troelsen, "Pro C# 7 with .NET and .NET Core", 8th Edition  
          - Mark Michaelis, "Essential C#", Addison-Wesley  

        **Installation Guidelines**:  
        - Download Visual Studio from [Visual Studio Free Developer Offers](https://visualstudio.microsoft.com/free-developer-offers/)
        """)

    # Assessments Tab
    with tabs[3]:
        st.header("Assessment Plan")
        st.markdown("""
        **CIA-I**: Lab Test & Problem Solving (40 Marks)  
        **CIA-II**: Weekly Lab Evaluations (50 Marks)  
        **ESE-I**: Mid-Semester MCQ Quiz (20 Marks)  
        **ESE-II**: Coding Challenge / Debugging (50 Marks)  
        **ESE-III**: Project Presentation / Lab Test (30 Marks)  

        **Rubrics**:  
        - Problem-Solving Skills: 20%  
        - Complexity Handling: 20%  
        - Concept Clarity: 20%  
        - Documentation: 20%  
        - Validation and Correctness: 20%  
        """)

    # Activities Tab
    with tabs[4]:
        st.header("Activities and Engagement")
        st.markdown("""
        ### Project Domain Activity
        **Objective**: Encourage students to develop practical applications while addressing real-world problems.  
        
        **Suggested Domains**:
        - **Community Services**:
            - NGO Management System: Application to manage volunteer activities, events, and fundraisers.
            - Blood Donation System: Real-time database for blood bank availability and donor registration.
        - **Education**:
            - Online Quiz System: Create a database-backed system for quizzes with different subjects.
            - Student Progress Tracker: Application to monitor and report academic performance.
        - **Healthcare**:
            - Appointment Scheduling System: Simplify booking appointments with real-time slots.
            - Prescription Tracker: Help patients keep track of prescribed medications.
        - **Environment & SDGs**:
            - Carbon Footprint Calculator: Allow users to assess their environmental impact.
            - Waste Management System: Facilitate better waste segregation and recycling efforts.
        - **Small Businesses**:
            - Inventory Management System: Track stock, suppliers, and orders for small shops.
            - Food Ordering System: Design a simple system for online orders with admin control.
        
        **Submission Guidelines**:
        - Deliverable: Functional application with detailed documentation.
        - Timeline: Projects must be finalized and submitted by **Week 16**.
        
        ### Fun Group Activity: "Code Quest: Calculator Showdown!"
        - **Objective**: Extend calculator functionality while competing in fun challenges.  
        - **Setup**:
            1. Form 4–5 teams of 3–5 students each.
            2. Provide a basic calculator starter code.
        - **Tasks**:
            - Add Features: Expand functionality with at least 2 new operations.
            - Improve UI: Make the calculator visually appealing and interactive.
            - Handle Errors: Implement error handling for invalid inputs.
        - **Challenges**:
            - **Button Bonanza**: Add a special button like "Clear All" or "Calculate Squares".
            - **Math Madness**: Use improved calculators to answer random math questions.
            - **Creative Spark**: Rename the calculator app and pitch its features.
        - **Scoring**:
            - Basic Functionality: 10 points
            - New Features Added: 10 points
            - UI Improvements: 5 points
            - Error Handling: 5 points
            - Creative App Name: 5 points
            - Team Pitch Presentation: 5 points
        
        **Submission**: Upload projects and assignments to Google Classroom.
        """)
        st.write("**Google Classroom Invite Link:** [Join Class](https://classroom.google.com/c/NzM0NjExNzUyMTQ1?cjc=j6y7j6v)")
        st.write("**Class Code:** j6y7j6v")

    st.success("Course Plan for Dot Net - Semester IV, Dr. Vijay & Dr. Smitha")

# Execute the function
dot_net_course_plan()
