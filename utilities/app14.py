import streamlit as st

# Set up the sidebar navigation
st.sidebar.title("BCA581 - Project I")
options = ["Home", "Project Instructions", "Project Guidelines","Synopsis Guidelines", "Evaluation and Schedule"]
choice = st.sidebar.radio("Go to", options)

# Home Page
if choice == "Home":
    st.title("BCA581 – PROJECT")
    
    st.header("Course Description")
    st.write("""
    Project-I is designed to provide students with a hands-on learning experience in the field of Computer Applications. 
    In this course, students will collaborate in small groups (typically 2 to 3 students per group) to undertake mini projects 
    aligned with Sustainable Development Goals (SDG) and industrial needs. The emphasis is on practical application, 
    problem-solving, and staying attuned to the latest industry trends.
    """)
    
    st.header("Course Objectives")
    st.write("""
    - **Comprehensive Understanding (Linked to CO1)**: Demonstrate a deep understanding of fundamental principles and concepts within the realm of Computer Applications, effectively applying this knowledge to the mini project.
    - **Technological Adaptability (Linked to CO2)**: Apply emerging tools and technologies, ensuring the mini project aligns with the latest advancements in the dynamic field of Computer Applications.
    - **Problem Analysis and Solution Development (Linked to CO3)**: Analyze real-time problems associated with the mini project, utilizing a variety of tools and techniques. Develop and implement effective solutions, showcasing proficiency in problem-solving.
    - **Entrepreneurial and Innovative Thinking (Linked to CO4)**: Cultivate entrepreneurial skills and innovative thinking by creating sustainable and creative mini projects. Provide solutions that transcend conventional approaches, demonstrating an ability to address real-time problems with ingenuity.
    """)

    st.header("Course Outcomes")
    st.write("""
    After completion of this course the students will be able to:
    - **CO1**: Demonstrate the ability to comprehend and apply the fundamental principles and concepts relevant to their mini project in Computer Applications.
    - **CO2**: Apply emerging tools and technologies in their mini project, ensuring it aligns with the latest advancements in the field of Computer Applications.
    - **CO3**: Analyze real-time problems related to their mini project, utilizing various tools and techniques, and subsequently design and develop effective solutions to address those problems.
    - **CO4**: Develop entrepreneurial and innovative solutions by providing sustainable and creative projects to solve real-time problems through their major project, showcasing an ability to think beyond conventional approaches.
    """)

    st.header("Text Books and Reference Books")
    st.write("""
    1. "Software Engineering: A Practitioner's Approach" by Roger S. Pressman, 7th Edition, McGraw Hill Education, 2009
    2. "INTRODUCTION TO ALGORITHMS, FOURTH EDITION" by Charles E. Leiserson, Thomas H. Cormen, MIT Press, 2022
    3. "Head First Design Patterns: Building Extensible and Maintainable Object-Oriented Software", O'Reilly Media, 2021
    """)

    st.header("Essential Reading / Recommended Reading")
    st.write("""
    1. "Clean Code: A Handbook of Agile Software Craftsmanship" by Robert C. Martin, Pearson Education, 2018
    2. "Introduction to the Theory of Computation" by Michael Sipser, Cengage India Private Limited, 2014
    3. "The Pragmatic Programmer" by David Thomas and Andrew Hunt, Pearson India Education Services Pvt Ltd, 20th Edition, 2019
    """)

    st.header("Web Resources")
    st.write("""
    1. [Mozilla Developer Network (MDN) Web Docs](https://developer.mozilla.org/)
    2. [GitHub](https://github.com/)
    3. [Stack Overflow](https://stackoverflow.com/)
    4. [Google Developers](https://developers.google.com/)
    5. [The Pragmatic Bookshelf](https://pragprog.com/)
    """)
elif choice == "Project Instructions":
    st.title("Project Instructions")
    
    st.header("1. Attendance and Laptop Requirement:")
    st.write("""
    - Attendance is mandatory for project lab and activities.
    - Laptop is essential for participating in project lab activities. Students without a laptop will not be accommodated, and attendance will not be granted if assigned tasks are incomplete.
    """)
    
    st.header("2. Work Dairy Notebook:")
    st.write("""
    - Students must bring a work dairy notebook along with their laptops.
    """)
    
    st.header("3. Weekly Tasks Submissions:")
    st.write("""
    - Weekly tasks must be submitted weekly or in the stipulated time. Portals will automatically disable after 7 days of submission deadlines.
    - Automatic reduction of marks will be applied for late submission. Without proper justification, resubmissions will not be accepted.
    - Adhere to timelines as failure to submit files on time will result in reduced marks.
    """)
    
    st.header("4. Compliance with Guidelines:")
    st.write("""
    - Diligently follow project lab guidelines, particularly with respect to timelines due to time constraints.
    """)
    
    st.header("5. Dedicated Engagement:")
    st.write("""
    - Engage fully in project-related practical implementations and documentations with utmost dedication.
    - Strictly adhere to assigned practical tasks; no deviations are allowed.
    """)
    
    st.header("6. Restricted Use of Mobile Phones and Headphones:")
    st.write("""
    - Mobile phones and headphones are prohibited during project lab sessions and evaluations.
    - If their use is necessary for specific tasks, inform the project lab teacher in advance.
    """)
    
    st.header("7. Respectful Conduct:")
    st.write("""
    - Show utmost respect to project lab teachers, in-charges, and guides.
    - Avoid engaging in arguments, speaking rudely, or being loud.
    - Complaints or warnings about disrespectful behavior will not be tolerated.
    """)
    
    st.header("8. Leaving the Class and Food Items:")
    st.write("""
    - If you need to leave the class during a session, inform the subject teacher without fail.
    - Failure to do so will result in recorded absence.
    - Food items are not allowed in the classrooms during class sessions.
    """)
    
    st.header("9. Project Guide Advisory Meeting:")
    st.write("""
    - It is expected to meet the guide weekly and show the progress, for the same report will be collected from guides every week.
    """)

# Evaluation and Tentative Schedule Page
elif choice == "Evaluation and Schedule":
    st.title("Evaluation and Schedule (Tentative)")

    st.header("Document Submission – CIA (60 Marks)")
    st.write("""
    1. Project Title, Abstract and Title defense: Week 1
    2. Synopsis: Week 2  (Week 1 and Week 2 Submission) - 5 Marks
    3. Software requirement specification: Week 3 - 10 Marks
    4. Database design: Week 6 - 10 Marks
    5. User Interface design: Week 7 - 10 Marks
    6. Initial draft: Week 8 & Week 13 - 10 Marks
    7. Final copy: Week 14 - 10 marks
    8. Attendance: 5 marks
    """)

    st.write("Total: 60 Marks")

    st.header("Project Diary – CIA (40 Marks)")
    st.write("""
    Project Progress Tracking (PPT) Week 6 to Week 13 (8*5=40): Alternate week from Week 6 - 40 Marks
    """)

    st.write("Total (CIA): 100 Marks")

    st.header("Project Presentation & Demonstration – ESE (100 Marks)")
    st.write("""
    1. Presentation: Analysis and Design (Guide, Internal Faculty, Peer Faculty Evaluation): Schedule: Immediate week after Theory CIA1 - 20 Marks
    2. Presentation and Demo 1 (50% of the project to be completed): Guide and Alumni Evaluation: Schedule: Immediate week after Theory CIA2 - 40 Marks
    3. Presentation and Demo 2: Guide and Internal Faculty from other cluster (PG/BSc) Evaluation: Week 15/Last week of the semester - 40 Marks
    """)

    st.write("Total (ESE): 100 Marks")

elif choice == "Synopsis Guidelines":
    st.title("GUIDELINES FOR SUBMITTING A SYNOPSIS")
    
    st.header("General Instructions:")
    st.subheader("1. Title Page:")
    st.markdown("""
    - **Project Title:** Clearly mention the title of the project.
    - **Team Members:** List all team members with their names and register numbers.
      - **Example:**
        - Joanna Varkey - 2141150
        - Akash K Raj - 2141105
        - Nevin Sebastian - 2141122
    """)
    
    st.subheader("2. Abstract:")
    st.markdown("""
    - Provide a concise summary of the project, including its purpose, scope, and main objectives. The abstract should not exceed 250 words.
    """)
    
    st.subheader("3. Objectives:")
    st.markdown("""
    - Clearly state the primary goals and objectives of the project. Each objective should be specific, measurable, achievable, relevant, and time-bound (SMART).
    """)
    
    st.subheader("4. Existing Systems:")
    st.markdown("""
    - Describe the current systems or solutions related to the project topic. Include a brief overview of their functionalities and limitations.
    """)
    
    st.subheader("5. Limitations of Existing Systems:")
    st.markdown("""
    - Identify and explain the drawbacks or challenges associated with the existing systems. Highlight the areas that need improvement.
    """)
    
    st.subheader("6. Proposed Solution/Functionalities:")
    st.markdown("""
    - Outline the proposed solution and its functionalities. Provide a detailed description of how the project aims to address the limitations of the existing systems and meet the objectives.
    """)
    
    st.subheader("7. Tools and Technologies:")
    st.markdown("""
    - List the tools, technologies, and programming languages proposed to be used in the project.
      - **Example:**
        - HTML, CSS, PHP
        - JavaScript
        - APIs
        - MySQL
        - Python
    """)
    
    st.header("Formatting Guidelines:")
    st.markdown("""
    - **Font:** Times New Roman, 12-point size.
    - **Spacing:** Double-spaced.
    - **Margins:** 1-inch margins on all sides.
    - **Page Numbering:** Bottom center of each page.
    - **Headings:** Bold and appropriately sized for each section.
    - **File Format:** Submit the synopsis in both .DOC and PDF format.
    """)
    
    st.header("Submission Details:")
    st.markdown("""
    - **Deadline:** 1st July 2024
    - **Submission Method:** GCR Submission
    """)
    
    st.header("Evaluation Criteria:")
    st.markdown("""
    - **Clarity and Coherence:** The synopsis should be well-structured and clearly convey the project's goals and objectives.
    - **Relevance:** The proposed solution should be relevant to the identified problem.
    - **Feasibility:** The project plan should be realistic and achievable within the given timeframe and resources.
    - **Innovation:** The project should offer innovative approaches or improvements over existing systems.
    - **Technical Detailing:** The choice of tools and technologies should be justified and align with the project requirements.
    """)
    
    st.header("Note:")
    st.markdown("""
    - **Plagiarism and usage of AI Tools:** Strictly prohibited. Ensure that all content is original or properly cited.
    - **Guidance:** Seek guidance from your guides if you have any questions or need further clarification on the guidelines.
    """)
    
# Project Guidelines Page
else:
    st.title("Project Guidelines - Week 1")

    st.header("Guidelines for Abstract Submission for Minor Project (PROJECT-I: BCA581)")
    st.write("""
    The project group has already been finalized, consisting of 3 members each, and has been approved by the department. 
    Project guides will be assigned to the respective groups and informed accordingly.
    """)

    st.header("Abstract Submission Requirements")
    st.write("""
    Students are expected to submit an abstract following the format outlined below. The abstract should be between 150 to 200 words and include the following sections:
    - Project Title Justification: Explain the relevance and importance of the chosen project title.
    - Rationale of Front-end and Back-end Tools: Provide a rationale for selecting the front-end and back-end tools you plan to use.
    - Purpose of the Project: Clearly state the purpose of the project.
    - Need for the Project: Explain why this project is needed.
    - Achieving Objectives: Describe how the project objectives can be achieved.
    """)

    st.header("Additional Information to Include in the Document")
    st.write("""
    - Roles and Responsibilities of Team Members: Outline the roles and responsibilities of each team member. (Note: A detailed agreement will be prepared later.)
    - Student Profiles: Include short profiles of each team member with their LinkedIn and GitHub IDs.
    """)

    st.info("In the next project hour, it is expected that you will submit a synopsis. The format and other details for the synopsis submission will be shared shortly.")

    st.header("Sample Abstract and Keywords")
    st.write("""
    **Project Title:** A Dashboard for Real-time Insights and Decision-making in Food Industrial Processing
    **Abstract:** This project developed a comprehensive business dashboard for selected Food Industry in Nigeria, aimed at monitoring key business metrics and providing real-time insights into food processing's environmental variables. Despite the advantages of dashboards for informed decision-making and performance improvement, their adoption in Nigeria, particularly among small and medium-sized businesses, remains low.
    The objectives were twofold: creating an intuitive dashboard leveraging IoT technology to capture and transmit real-time sensor readings (e.g., light sensitivity, temperature, moisture, humidity), and designing an interactive user interface for compatibility using HTML, CSS, and JavaScript. Methods included analyzing operational requirements and data sources, integrating IoT devices and protocols, implementing data processing algorithms, and conducting rigorous testing for accuracy and reliability.
    The findings demonstrated successful real-time sensor data visualization, allowing user access through login/logout, and enabling seamless production oversight with CCTV footage. The project achieved its goals, enhancing data-driven decisions and optimizing food processing at selected Nigerian Food Industries.
    **Keywords:** Internet of Things, Data visualization, Dashboards, Decision-making.
    """)