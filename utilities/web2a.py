# app.py
"""
BCA 301-4 DOT NET COURSE PLAN Viewer
------------------------------------
- Shows the exact contents of the course plan (no upload or parsing needed)
- Fully self-contained
Run:
    pip install streamlit
    streamlit run app.py
"""

import streamlit as st
import re

st.set_page_config(page_title="BCA301-4 DOT NET COURSE PLAN", layout="wide")

st.title("BCA 301-4 DOT NET COURSE PLAN")
st.caption("Exact text version — no modifications or omissions")

# -------------------------------------------------------------------------------------
# The complete document content EXACTLY as provided (do not change or reformat)
# -------------------------------------------------------------------------------------
COURSE_PLAN = """BCA 301-4 DOT NET COURSE PLAN
SECTION I
Semester	IV	Class	 4 BCA A & B
Course Code	 BCA 301-4	Course title	Dot Net
Hours	 75	Hours per week	3+2
Faculty name	Dr Smitha Vinod
Dr Vijay Arputharaj J
Dr Gayathry S Warrier
Dr Deepa BG
	Contact 
details	Mobile:  9886495919, 9677188654, 9497640670, 8105095047
Mail:  smitha.vinod@christuniversity.in
vijay.arputharaj@christuniversity.in
gayathry.warrier@christuniversity.in
deepa.bg@christuniversity.in
Class policies and guidelines	1.	All communication will be done through CHRIST University Official Mail/Google Class/Moodle.
2.	Read the course content / resources shared in Google Drive before coming to the class.
3.	Usage of the Laptop is only with the prior permission (as per the requirements of the Class work/Lab/Demo)
4.	Mentoring sessions, discussions, and assistance will be available only on prior appointment. Please schedule your sessions in advance to ensure availability and effective preparation.
Course Description	This course provides an in-depth understanding of .NET technologies, focusing on C# and VB.NET for Windows Forms applications. Students will explore .NET Framework, CLR, OOPS concepts, Windows-based application development, database integration using ADO.NET, file handling, security, and deployment. The course emphasizes hands-on learning through practical lab exercises and culminates in a real-world mini-project aligned with SDG’s and social initiatives.
Course Objectives	This course equips students with .NET development skills, focusing on C# and VB.NET for Windows Forms applications. It covers .NET Framework, OOP concepts, event-driven programming, ADO.NET database integration, file handling, security, and deployment.
Students will explore advanced applications like face recognition, voice-based systems, and biometrics. The course culminates in a real-world mini-project supporting NGOs, SDGs, or
social initiatives, preparing students for industry-ready software development.
Learning Outcomes for the Course	CO1: Explain the core concepts of .NET Framework and compare the features of C# and VB.NET for Windows application development.
CO2: Develop Windows Forms applications using event-driven programming, implementing custom controls, menus, toolbars, and dialog boxes for interactive user interfaces.
CO3: Integrate databases with ADO.NET, demonstrating proficiency in connected and disconnected architectures, and performing CRUD operations using SQL Server.
CO4: Implement file handling techniques using System.IO, including text, binary, and secure data storage, ensuring efficiency and security in .NET applications.
CO5: Design and deploy advanced applications using face recognition, voice-based systems, and biometric authentication, applying real-world secure coding practices.

 

SECTION II
Module/ Unit	Topic details	Week
(starting and
end dates)	Hours
per
Chapter	Teaching learning methods used/ activities and dates for assessment 	Resource/ Reference details
Unit-1

.NET AND OBJECT-ORIENTED PROGRAMMING
(Teaching Hours: 15)	.NET Framework and .NET 6/7 Overview, CLR, MSIL, Assemblies, Metadata, Garbage
Collection, C# vs. VB.NET – Key Differences	Week 1

30th - 31st  Oct 2025 and 3rd - 5th Nov 2025	5	


Experiential Learning

Problem Solving Sessions

Diagnostic Assessments
 
ICT tools used: Visual Studio 
JetBrains Rider
.NET CLI
You Tube
GitHub	Text Books
Ref. Books

Online Tutorials

	Advanced OOPS in C# and VB.NET
(Encapsulation, Inheritance, Polymorphism)	Week 2


	5		Text Books
Ref. Books

Online Tutorials
	Delegates, Events, Lambda Expressions,
Working with Threads and Asynchronous Programming

	5		Text Books
Ref. Books

Online Tutorials
Unit-2

WINDOWS APPLICATIONS & EVENT-DRIVEN PROGRAMMING  (Teaching Hours:15)	Windows Forms Development in C# and VB.NET, Event Handling, Common controls,	Week 4

	5	Activity: Collaborative Learning	Text Books
Ref. Books

Online Tutorials
	ListView, TreeView, ProgressBar, Components: Errorlogs, Timer Creating Custom Controls
in Windows Forms,
	Week 5


	5 + 2	CIA -I (KP 4th Jan)
Formative Assessment: Problem Solving Lab test-1 (40 Marks)	Text Books
Ref. Books

Online Tutorials
	Menus, Toolbars and Dialog Boxes, Interoperability between VB.NET
and C#
	Week 6

6th - 11th Jan 	5	Experiential 
Learning : Code Review Session (Review by peer)	Text Books
Ref. Books

Online Tutorials
Unit-3

DATABASE INTEGRATION WITH ADO.NET (Teaching Hours:15)	Introduction to ADO.NET, Connection, Command, DataReader, and DataAdapter, DataSet,	Week 7

	5	ESE -I (KP 25th Jan)
Formative Assessment: Problem Solving MCQ Quiz (20 Marks)	Text Books
Ref. Books

Online Tutorials
	DataTable, and DataGridView Controls, Connected vs. Disconnected Architecture,	Week 8


20th - 25th Jan	5	Participatory 
Learning: Think-Pair-Share Activities
	Text Books
Ref. Books

Online Tutorials
	Mid Semester Week ( Week-9: 3rd - 8th Feb )
...
SECTION IV
Assessment Description: CIA – I
Assessment Name	CIA I
Schedule 	Every week (As per lab schedule)
Weightage	50%
Individual Assignment Details   	Individual 
Assessment description:	Regular Lab exercises evaluations
Mode of the Test	Practical & GCR Submission/ Moodle.
Marks	50 Marks
Duration	Based on lab schedule
Topics Covered	List of Programs 1 to 8 and project from Unit-5 (regular Lab evaluation)
Remarks	●	No Late evaluation
●	GCR submissions are mandatory. 

Evaluation Rubrics:
S. No.	Evaluation Rubrics	Marks 
1	On-time completion & Domain based knowledge 	2
2	Execution With Complexity	2
3	Formatting & Validation	2
4	Concept Clarity/Completion of task assigned on the spot	2
5	Viva	2
...
* * * * * * * * * 
"""

# -------------------------------------------------------------------------------------
# Helper: split text into sections
# -------------------------------------------------------------------------------------
SECTION_PATTERN = re.compile(r"(SECTION\s+[IVXLC]+)", flags=re.IGNORECASE)

def split_sections(text: str):
    parts = SECTION_PATTERN.split(text)
    if len(parts) == 1:
        return {"Full Document": text}
    sections = {}
    i = 1
    while i < len(parts):
        header = parts[i].strip()
        content = parts[i + 1].strip() if (i + 1) < len(parts) else ""
        sections[header] = content
        i += 2
    return sections


# -------------------------------------------------------------------------------------
# Display logic
# -------------------------------------------------------------------------------------
sections = split_sections(COURSE_PLAN)

st.sidebar.header("Navigate")
selected = st.sidebar.radio("Select Section", list(sections.keys()), index=0)
search = st.sidebar.text_input("Search text")

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(selected)
    text = sections[selected]
    if search:
        lines = text.splitlines()
        hits = [ln for ln in lines if search.lower() in ln.lower()]
        if hits:
            st.markdown(f"**Search results for '{search}':**")
            for h in hits:
                st.markdown(f"- {h}")
        else:
            st.info("No matches found.")
    else:
        blocks = [b for b in re.split(r"\n{2,}", text) if b.strip()]
        for i, b in enumerate(blocks):
            if len(b) > 600:
                with st.expander(f"Part {i+1}"):
                    st.markdown(b)
            else:
                st.markdown(b)

with col2:
    st.markdown("### Quick View")
    for name, content in sections.items():
        with st.expander(name, expanded=False):
            preview = content[:800] + ("..." if len(content) > 800 else "")
            st.text(preview)

st.markdown("---")
st.download_button("Download Full Course Plan (TXT)", COURSE_PLAN, file_name="BCA301-4_DOTNET_COURSE_PLAN.txt")
st.caption("Exact course plan text displayed — no deviations or edits.")
