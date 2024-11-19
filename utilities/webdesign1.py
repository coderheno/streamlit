import streamlit as st
from datetime import datetime, timedelta

def web_designing_course_plan():
    # Base Dates
    mse_start = datetime(2025, 2, 3)
    mse_end = datetime(2025, 2, 8)

    # Tabs for better interaction
    tabs = st.tabs(["Lectures", "Practicals", "Tools & Resources", "Activities & Submissions"])

    # Lectures Tab
    with tabs[0]:
        st.header("Lecture Plan")
        st.write("Detailed plan for all lectures in the semester.")
        lecture_schedule = [
            {"unit": "UNIT-I: WORLD WIDE WEB", "topics": ["Introduction to Internet", "TCP/IP Protocols"], "dates": "20th - 23rd Nov 2024"},
            {"unit": "UNIT-II: HTML", "topics": ["HTML Basics, Web Page Development"], "dates": "9th - 14th Dec 2024"},
            {"unit": "UNIT-III: CSS", "topics": ["CSS Basics, Benefits"], "dates": "20th - 25th Jan 2025"},
            {"unit": "MID SEMESTER EXAM", "topics": ["MSE Week"], "dates": "3rd - 8th Feb 2025"},
            {"unit": "UNIT-IV: JAVASCRIPT", "topics": ["Basics of JavaScript"], "dates": "10th - 14th Feb 2025"},
            {"unit": "UNIT-V: TOOLS", "topics": ["Adobe Photoshop, HTML Editors"], "dates": "17th - 22nd Mar 2025"},
        ]
        for lecture in lecture_schedule:
            st.markdown(f"### {lecture['unit']}")
            st.write(f"**Topics:** {', '.join(lecture['topics'])}")
            st.write(f"**Dates:** {lecture['dates']}")

    # Practicals Tab
    with tabs[1]:
        st.header("Practical Plan")
        st.write("Plan for lab exercises and hands-on activities.")
        practical_schedule = [
            {"week": 1, "exercise": "Creating a simple web page for the department", "dates": "20th - 23rd Nov 2024"},
            {"week": 2, "exercise": "Creating a personalized web page for a company", "dates": "25th - 30th Nov 2024"},
            {"week": 3, "exercise": "Creating an NGO website to embed multimedia", "dates": "2nd - 7th Dec 2024"},
            {"week": 4, "exercise": "Creating a travel/hotel reservation page/site", "dates": "9th - 14th Dec 2024"},
            {"week": 5, "exercise": "Create a passport portal page/site", "dates": "16th - 20th Dec 2024 and 2nd - 4th Jan 2025"},
            {"week": 6, "exercise": "Lab Test 1: Personalized website with themes", "dates": "6th - 11th Jan 2025"},
            {"week": 7, "exercise": "Online marketing website with form validation", "dates": "13th - 17th Jan 2025"},
            {"week": 8, "exercise": "Food ordering website design", "dates": "20th - 25th Jan 2025"},
            {"week": 9, "exercise": "Mid Semester Week", "dates": "3rd - 8th Feb 2025"},
            {"week": 10, "exercise": "Login Page Validation", "dates": "27th - 1st Feb 2025"},
            {"week": 11, "exercise": "Calculator design using HTML and JS", "dates": "10th - 14th Feb 2025"},
            {"week": 12, "exercise": "Student project domain selection and finalization", "dates": "17th - 22nd Feb 2025"},
            {"week": 13, "exercise": "Student project design and documentation", "dates": "24th - 1st Mar 2025"},
            {"week": 14, "exercise": "Continued project design and documentation", "dates": "3rd - 8th Mar 2025"},
            {"week": 15, "exercise": "Project presentation", "dates": "10th - 14th Mar 2025"},
            {"week": 16, "exercise": "Comprehensive final test", "dates": "17th - 22nd Mar 2025"},
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

    # Activities & Submissions Tab
    with tabs[3]:
        st.header("Activities, Fun Submission & Interaction")
        
        # Choice-Based Activity
        st.subheader("Choice-Based Activity: Fun or Practical!")
        st.write("**Students can choose one of the following activities for submission:**")

        st.markdown("""
        ### Option 1: Creative Fun Activity
        - **Activity:** Create a fun meme or a short video based on Unit 1 topics!
        - **Topics:** 
          - Introduction to Internet
          - Internet Service Providers
          - TCP/IP Protocol Suite
          - Bandwidth
          - World Wide Web (WWW)
          - Web Browsers
          - Search Engines and SEO
        - **Guidelines:**
          - Use tools like Canva or Meme Generators for memes.
          - Videos should be 1 minute max, using animations or enactments.
          - **Submission:** Upload to Google Classroom.
          - **Deadline:** End of Week 1.

        ### Option 2: Group Project Pitch
        - **Activity:** Submit a group project pitch for a web-based idea.
        - **Guidelines:**
          - Form groups of 3-4 members.
          - Create an abstract that includes:
            - Project title.
            - Problem it solves.
            - Brief implementation plan.
          - **Submission:** Upload abstract to Google Classroom.
          - **Deadline:** End of Week 1.

        **Objective:** Engage with course concepts in an interactive and collaborative way!
        """)

        # Class invite link and code
        st.subheader("Classroom Invite Link & Code")
        st.write("**Invite Link:** [Google Classroom](https://classroom.google.com/c/NzMyNDY5NDQ3MTMx?cjc=z2d5nfm)")
        st.write("**Class Code:** z2d5nfm")

    st.success("COM661B - Web Designing , Dr VIJAY ARPUTHARAJ J and Dr MOHANA PRIYA T")

# To execute the function
web_designing_course_plan()
