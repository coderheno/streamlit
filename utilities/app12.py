import pandas as pd
import streamlit as st
import os
import random
import io
import base64

def display_groups():
    # Input for names and number of groups
    names_input = st.text_input("Enter names separated by commas")
    num_groups = st.number_input("Enter number of groups", min_value=1, step=1)
    
    # Split the names and shuffle them randomly
    names = [name.strip() for name in names_input.split(",") if name.strip()]
    random.shuffle(names)
    
    # Initialize the groups dictionary
    groups = {f"Group {i+1}": [] for i in range(num_groups)}
    
    # Assign names to groups randomly
    for i, name in enumerate(names):
        group_key = f"Group {(i % num_groups) + 1}"
        groups[group_key].append(name)
    
    # Create a DataFrame for displaying in Streamlit
    df = pd.DataFrame(groups.values(), index=groups.keys()).transpose()
    
    # Display the table using Streamlit
    st.write("Groups and Members:")
    st.table(df)
    
    # Save the groups to a CSV file
    save_option = st.checkbox("Save groups to CSV file")
    if save_option:
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="groups.csv">Download CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)

def submission():
    st.title("Learner Submission Portal")

    # Input fields for student details
    name = st.text_input("Enter your name:")
    reg_no = st.text_input("Enter your group id and your roll number:")

    # File upload
    st.write("Upload your submission file:")
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt'])

    if st.button("Submit"):
        if name and reg_no and uploaded_file:
            # Save the uploaded file
            file_path = os.path.join("submissions", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Save student details to a CSV file
            with open("student_submissions.csv", "a") as csv_file:
                csv_file.write(f"{name},{reg_no},{file_path}\n")

            st.success("Submission added successfully!")
        else:
            st.error("Please fill in all the fields and upload a file.")

def lca_contents():
    st.title("Learner Centered Approach Contents")

    # Unit 1: INTRODUCING PYTHON
    st.header("Unit-1: INTRODUCING PYTHON")
    
    # Formative Activity: Group Discussion
    st.subheader("Formative Activity: Group Discussion")
    st.write("Description: Group Discussion on “How python differs from other programming languages?”")
    st.write("Objective: Students will form teams of five to discuss the features and advantages of Python compared to other programming languages.")

    # Experiential Learning
    st.subheader("Experiential Learning")
    st.write("Objective: To reinforce basic Python syntax and concepts.")
    st.write("Activity: Use online platforms like Codecademy, LeetCode, or HackerRank to complete interactive coding exercises.")

    # Problem-solving Sessions
    st.subheader("Problem-solving Sessions")
    st.write("Description: The problem solving sessions and questions are designed to assess comprehension, application, and problem-solving skills, ensuring a comprehensive review of the material.")

    # Unit 2: PYTHON DATA TYPES: LISTS AND TUPLES
    st.header("Unit-2: PYTHON DATA TYPES: LISTS AND TUPLES")
    
    # Participatory Learning: Poster Presentation
    st.subheader("Participatory Learning: Poster Presentation")
    st.write("Description: Divide the students into small groups of 3-4. Assign each group a specific data type or data structure to focus on. Each group will create a poster with definition, syntax, operations, practical use cases etc.")
    st.write("Objective: Each group will present their poster to the class, explaining the key points and demonstrating examples.")

    # Instructional activity: Brainstorming
    st.subheader("Instructional activity: Brainstorming")
    st.write("Description: Divide students into small groups of 3-4. Provide each group with sticky notes or plain sheets. Ask each group to brainstorm and write down ideas for features and functionalities of the movie recommendation system.")
    st.write("Objective: Based on the brainstormed ideas, collaboratively outline the design of the system.")

    # Formative Assessment: Quiz using Kahoot
    st.subheader("Formative Assessment: Quiz using Kahoot")
    st.write("Description: The formative assessment using Kahoot provides an engaging and interactive way to evaluate students' understanding of Python concepts covered in the course.")
    st.write("Objective: Students participate in a quiz session where they answer multiple-choice questions related to Python fundamentals, data structures, functions, and other key topics.")

    # Unit 3: PYTHON DATA TYPES: SETS AND DICTIONARIES
    st.header("Unit-3: PYTHON DATA TYPES: SETS AND DICTIONARIES")
    
    # Experiential Learning : Code Review Session (Review by peer)
    st.subheader("Experiential Learning : Code Review Session (Review by peer)")
    st.write("Description: Code Review Session on writing a function employees_in_all_projects.")
    st.write("Question: How does the employees_in_all_projects function handle the case where a specified project does not exist in the assignments dictionary?")

    # Participatory Learning: Think-Pair- Share Activities
    st.subheader("Participatory Learning: Think-Pair- Share Activities")
    st.write("Description: The Think-Pair-Share activity on sets in Python aimed to deepen students' understanding through active participation and peer collaboration.")
    st.write("Scenario: Write a Python function to find transactions that are both high priority and occurred in the last month.")

    # Summative Assessment: Concept Map (or) Mind map
    st.subheader("Summative Assessment: Concept Map (or) Mind map")
    st.write("Description: The summative assessment activity involved students creating a comprehensive concept map or mind map on Python data structures, with a particular emphasis on dictionaries.")
    st.write("Objective: This visual representation required students to organize and interconnect various data structures such as lists, tuples, sets, and dictionaries, highlighting their characteristics, use cases, and methods.")

    # Unit 4: Comprehensions and Functions
    st.header("Unit-4: Comprehensions and Functions")
    
    # Diagnostic Assessment: Debugging Challenges
    st.subheader("Diagnostic Assessment: Debugging Challenges")
    st.write("Description: The diagnostic assessment activity involved a debugging challenge focused on revising Python data structures and comprehensions.")
    st.write("Objective: Students were tasked with identifying and fixing errors in provided code snippets, each designed to test their understanding of these concepts.")

    # Instructional activity - Code Enrichment
    st.subheader("Instructional activity - Code Enrichment")
    st.write("Description: The instructional activity on Code Enrichment centered around the topic of functions in Python.")
    st.write("Objective: Students were guided through the process of writing and enhancing Python functions, experimenting with positional, keyword, default, and variable-length arguments.")

    # Participatory Learning - Role play
    st.subheader("Participatory Learning - Role play")
    st.write("Description: In the participatory learning activity, students engaged in a role-play exercise focusing on unpacking arguments and recursive functions in Python.")
    st.write("Objective: By assuming different roles, such as function callers and function implementers, students demonstrated the process of unpacking arguments in various scenarios.")

    # Unit 5: Functional Programming
    st.header("Unit-5: Functional Programming")
    
    # Experiential Learning: Workshops
    st.subheader("Experiential Learning: Workshops")
    st.write("Description: In the experiential learning activity, students participated in a workshop led by a top industry professional, providing them with invaluable insights into the practical applications of Python programming.")

    # Experiential Learning: PBL (Project Deployment)
    st.subheader("Experiential Learning: PBL (Project Deployment)")
    st.write("Description: In this experiential learning activity, students engaged in project-based learning with a focus on project deployment, culminating in an industry-focused presentation.")

    # Research Based Learning and Case Study
    st.subheader("Research Based Learning and Case Study")
    st.write("Description: In this research-based learning activity, students conducted in-depth investigations on specific Python programming topics, culminating in a detailed case study.")


  
def course_contents():
    st.title("BCA541B: Graphics and Animation")
    st.write("""
    **Course Description:**
    This course aims to provide students with comprehensive knowledge in three-dimensional modeling and animation using 3DS Max/Blender software. Students will learn how to effectively render animated scenes, with a focus on lighting and material design. The course offers hands-on experience in graphic and animation application development, and covers fundamental concepts of both 3D and 2D design.

    **Course Objective:**
    This course is designed to equip students with a comprehensive understanding of three-dimensional modeling and animation using 3DS Max/Blender software. Students will develop proficiency in creating detailed 3D models and animating them with realistic movements. Emphasis will be placed on mastering lighting and material design to enhance the visual quality of rendered scenes. Through hands-on experience, students will learn to develop graphic and animation applications, gaining a solid foundation in both 2D and 3D concepts. The course encourages creative problem-solving and teamwork, preparing students for professional opportunities in the graphics and animation industry.

    **Learning Outcomes:**
    - By the end of this unit, students will be able to navigate Autodesk 3ds Max, understand its interface, and work with basic objects. They will demonstrate their knowledge by presenting real-time project models that identify the application areas of 3ds Max and by completing an individual MCQ test on these topics. 
    - Students will be able to create and modify shapes using splines, edit meshes, and create complex objects. Additionally, they will demonstrate proficiency in lighting models and enhancing them with materials. This will be reflected in their ability to name, organize, and render objects with appropriate light and material effects.
    - Students will gain skills in using the 3ds Max camera, setting up environments, and managing scenes. They will also understand the principles of animation, including keyframes and controlling elements over time. These skills will be assessed through a project involving graphic modeling with AR/VR animation and an e-learning module on graphics or graphics tools, along with a self-assessment report.
    - Students will demonstrate advanced competency in using the 3ds Max camera for creating interior views and immersive environments for animation. They will also efficiently organize objects and manage scenes, showing their ability to replace objects and use the rendered framework window effectively.
   
    **Learner-Centric Approach (LCA):**
    This course employs a learner-centric approach to enhance student engagement and learning outcomes. Key features include:
    - Hands-on practical exercises and projects.
    - Interactive sessions and discussions.
    - Personalized feedback and guidance.
    - Integration of real-world applications and case studies.

    **Career Opportunities:**
    Completion of this course opens doors to various career opportunities, including:
    - 3D Modeler
    - Animation Artist
    - Visual Effects (VFX) Artist
    - Graphic Designer
    - Game Designer/Developer
    - Architectural Visualization Artist
    - Product Designer
    - Multimedia Specialist
    - Film and Video Editor
    - Augmented Reality (AR) / Virtual Reality (VR) Developer
    """)

def display_groups():
    # Define the groups and mentors
    groups = {
        "Group 1": ["YUVRAJ RAISINGHANI ", "JOSHUA RAJESH THACHIL ", "AAKASH ALLORIA", "PRANAV SRINIVASAN ", "AADHARSH KRISHNAA G", "AYAN ARORA"],
        "Group 2": ["PALA ADITHYAN ", "AGAMJOT KAUR DUA", "SORAVICH PINRAT", "Nayana k Benny", "SADINENI BHARGAV", "NAVNEET JOSHI"],
        "Group 3": ["AMRITHA S NAIR", "JESSICA P", "MRIDUL MAHAJAN", "NAVANEETH KISHOR C H", "SARIT NONTARAJ", "HARDIK ABHINEET SHAH"],
        "Group 4": ["GREESHMA GIRISH C", "ADRIJ MONDAL", "BRITO JAISON ", "AMULYA SRIVASTAVA", "PRIYAK SARKAR", "MANUSHREE R"]
    }
    
    # Create a DataFrame for displaying in Streamlit
    df = pd.DataFrame(groups.values(), index=groups.keys()).transpose()
    
    # Display the table using Streamlit
    st.write("Groups and Mentors:")
    st.table(df)


def practical_programs():
    st.title("Practical Programs in Graphics and Animation")

    st.subheader("Program 1: Simple Car/Jeep Modeling")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Modeling basic objects using standard primitives.")

    st.subheader("Program 2: Modeling Dining Table and Objects")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Editing shapes with meshes, focusing on mesh editing techniques.")

    st.subheader("Program 3: Biomedical Visualization")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Applying transformations and filling of images for biomedical visualization.")

    st.subheader("Program 4: Simple 3D Character Modeling")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Working with color palette and layers for basic 3D character modeling.")

    st.subheader("Program 5: Cartoon Model Design (e.g., Minions)")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Enhancing objects with lights and shadows to create cartoon-style models.")

    st.subheader("Program 6: Enhancing Cartoon Model and Objects")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Enhancing models with materials, focusing on applying textures and materials.")

    st.subheader("Program 7: Simple Game Assets with Special Effects")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Creation of images with special effects for game asset design.")

    st.subheader("Program 8: Application-based Rendering the Animation (Game Design)")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Rendering a scene with layers in the timeline for game design.")

    st.subheader("Program 9: Advanced Animation Elements and Keyframe Animation")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objective:** Implementing keyframe animation techniques for advanced animation elements.")

    st.subheader("Program 10: Application-based Rendering the Animation")
    st.write("- **Software:** 3ds Max / Blender")
    st.write("- **Objectives:** Rendering animations in various domains such as interior design, biomedical visualization, character modeling, and cartoon modeling.")


def unit_content_activity():
    st.title("Graphics and Animation Course: Unit-wise Contents, LO Mapping, and Assessments")

    st.subheader("Unit 1: Getting to Know Autodesk 3ds Max")
    st.write("**Topics Covered:**")
    st.write("- Introduction to 3ds Max")
    st.write("- Touring the Interface")
    st.write("- Working with Objects")
    st.write("- Viewing Objects")
    st.write("- Understanding Standard Primitives")
    st.write("- Modelling with Modifiers")
    st.write("- Making Clones")
    st.write("- Working with Groups")
    st.write("**Learning Outcome 1 (LO1):**")
    st.write("- Students will navigate Autodesk 3ds Max, understand its interface, and work with basic objects.")
    st.write("**Assessment 1:**")
    st.write("- Group Presentation on application areas of 3ds Max and real-time project models (10 marks)")
    st.write("- Class Test (Individual MCQ) on Unit 1 topics (10 marks)")

    st.subheader("Unit 2: Creating Shapes with Splines")
    st.write("**Topics Covered:**")
    st.write("- Drawing with Splines")
    st.write("- Modifying Shapes")
    st.write("- Outlining and Extruding Splines")
    st.write("- Combining and Extruding Primitive Splines")
    st.write("- Creating Solid Forms with Splines")
    st.write("**Learning Outcome 2 (LO2):**")
    st.write("- Students will create and modify shapes using splines, edit meshes, and create complex objects.")

    st.subheader("Unit 3: Lighting and Materials")
    st.write("**Topics Covered:**")
    st.write("- Lighting Models")
    st.write("- Rendering Views")
    st.write("- Ambient Light and Shadow Effects")
    st.write("- Using Scene States")
    st.write("- Understanding Texture Maps")
    st.write("- Adding and Editing Materials")
    st.write("**LO2 Continued:**")
    st.write("- Students will demonstrate proficiency in lighting models and enhancing them with materials.")

    st.subheader("Unit 4: Using the Camera")
    st.write("**Topics Covered:**")
    st.write("- Understanding the 3ds Max Camera")
    st.write("- Setting Up an Interior View")
    st.write("- Creating an Environment")
    st.write("- Using Immersive Environments for Animation")
    st.write("- Using Render Type and Elements")
    st.write("- Matching Scenes to Background Images")
    st.write("**Learning Outcome 3 (LO3):**")
    st.write("- Students will gain skills in using the 3ds Max camera, setting up environments, and managing scenes.")

    st.subheader("Unit 5: Animation Principles")
    st.write("**Topics Covered:**")
    st.write("- Understanding Video Time and Keyframes")
    st.write("- Creating and Editing Animations")
    st.write("- Controlling Camera and Lights Over Time")
    st.write("**LO3 Continued:**")
    st.write("- Students will understand animation principles, including keyframes and controlling elements over time.")
    st.write("**Assessment 3:**")
    st.write("- Project on graphic modeling with AR/VR animation (10 marks)")
    st.write("- E-learning module on graphics/graphics tools with self-assessment report (10 marks)")

    st.subheader("Unit 6: Advanced Camera and Scene Management")
    st.write("**Topics Covered:**")
    st.write("- Advanced Use of the 3ds Max Camera")
    st.write("- Organizing Objects")
    st.write("- Scene Management Techniques")
    st.write("- Using the Rendered Framework Window")
    st.write("**Learning Outcome 4 (LO4):**")
    st.write("- Students will demonstrate advanced competency in using the 3ds Max camera and efficiently managing scenes.")
def assessments():
    st.title("Assessments in Graphics and Animation Course")

    st.subheader("ASSESSMENT: CIA IA")
    st.write("- **Assessment component:** Class Test (Individual)")
    st.write("- **Portion:** Unit 1 and Unit 2")
    st.write("- **Mode of conduct:** Test portal (Online) / Class test (Offline)")
    st.write("- **Date of exam:** Week 3 (1-6 July)")
    st.write("- **Type of questions:** Subjective + Objective")
    st.write("- **Maximum marks:** 10 (To be converted CIA-I marks)")
    st.write("- **General Instructions:** No late submission, strict templates should be followed")

    st.subheader("ASSESSMENT: CIA IB")
    st.write("- **Assessment component:** Project")
    st.write("- **Portion:** Unit 1 and Unit 2")
    st.write("- **Mode of conduct:** Practical & Presentation")
    st.write("- **Technology tool used:** 3ds Max / Blender")
    st.write("- **Date of assessment:** Week 4 (8-13 July)")
    st.write("- **Type of questions:** Identify the application area of 3ds max and presentation with real-time project models")
    st.write("- **Maximum marks:** 20 (To be converted CIA-I marks)")
    st.write("- **General Instructions:** No late submission, strict templates should be followed")

    st.subheader("CIA II (Mid-semester exam)")
    st.subheader("ASSESSMENT III")
    st.write("- **Assignment Type:** e-learning module on graphics/graphics tools")
    st.write("- **Nature of the assignment:** Individual Assignment/Project/P")
    st.write("- **Assignment Description:**")
    st.write("  - The module should complete any one topic of e-learning for students")
    st.write("  - User interactions should be included")
    st.write("  - Completion certificate should be added")
    st.write("- **Submission mode:** Google Classroom – Autodesk 3ds max file submission with completion certificate")
    st.write("- **Deadline:** Week 12 (2-7 Sep)")
    st.write("- **Maximum marks:** 20 Marks")
    st.write("- **General Instructions:** Late submission will not be entertained.")
def display_instructions():
  """Displays instructions for all three activities"""
  st.header("Instructions")

  # Activity 1
  st.subheader("Activity 1: Gauge Your Interest (Individual)")
  st.write("Visit Mentimeter to assess your interest and expectations in 2D/3D animation tools.")
  st.write("You can access Mentimeter through the following link:")
  st.write("[Mentimeter](https://www.menti.com/al3dwebt2az8)")
  st.write("Alternatively, use the access code provided: 8205 9248")

  # Activity 2
  st.subheader("Activity 2: 3ds Max vs. Other Software (Group Discussion)")
  st.write("Form groups of five and discuss the features and advantages of 3ds Max compared to other 3D tools and software.")
  st.write("Consider these aspects during your discussion:")
  st.write("* Modeling capabilities")
  st.write("* Animation tools")
  st.write("* Rendering engines")
  st.write("* Industry usage")
  st.write("* User interface and workflow")

  # Activity 3
  st.subheader("Activity 3: Project Brainstorming (Group of 2-3)")
  st.write("Form groups of 2-3 members and choose an area or domain in graphics and animation that interests you, such as:")
  st.write("* Interior design")
  st.write("* Game design")
  st.write("* Character modeling")
  st.write("* Biomedical visualization")
  st.write("(This list is not exhaustive, feel free to explore other areas!)")
  st.write("Brainstorm and develop a project idea within your chosen domain. Define the following for your project:")
  st.write("* Domain: The specific area your project focuses on (e.g., interior design)")
  st.write("* Title: A catchy and descriptive name for your project")
  st.write("* Scope: A clear outline of what your project will encompass (consider its size and complexity)")
  st.write("* Objectives: The specific goals you aim to achieve with your project")
  st.write("* AR/VR Integration: How your project could potentially incorporate Augmented Reality (AR) or Virtual Reality (VR) elements")
  st.write("**Remember:**")
  st.write("* Ensure your project has a clear connection to AR/VR modeling.")
  st.write("* Be creative and explore the possibilities of using AR/VR technology within your chosen domain.")
  st.write("* Prepare to present your project idea to the class.")
  st.write("**Submission:**")
  st.write("Upload your project details (Domain, Title, Scope, Objectives, AR/VR Integration) through the designated channel:")
  st.write("[Google Classroom](https://classroom.google.com/c/Njk2MTg4ODk1NzQx?cjc=lj2dywt)") 
  st.write("**GCR code:** lj2dywt")
def quiz():
    st.title("Blender Basics Quiz: Primitives and Viewports")

    # Questions and choices
    questions = [
        ("In Blender, which shortcut is used to add a new primitive object?", 
         ["Shift+A", "Ctrl+A", "Alt+A", "A"], "Shift+A"),
        ("Which of the following is NOT a basic primitive object in Blender?", 
         ["Cube", "Sphere", "Monkey", "Cone"], "Monkey"),
        ("What is the default primitive object when you first open Blender?", 
         ["Cube", "Plane", "Sphere", "Suzanne"], "Cube"),
        ("Which viewport shading mode allows you to see the object with materials and textures applied?", 
         ["Wireframe", "Solid", "Material Preview", "Rendered"], "Material Preview"),
        ("What is the shortcut to switch to the top orthographic view in Blender?", 
         ["Numpad 7", "Numpad 1", "Numpad 3", "Numpad 5"], "Numpad 7"),
        ("How can you switch to the wireframe view in the 3D viewport?", 
         ["Z", "Alt+Z", "Ctrl+Z", "Shift+Z"], "Z"),
        ("Which panel in the Properties editor is used to add modifiers to an object?", 
         ["Modifiers", "Object Properties", "Material Properties", "Scene Properties"], "Modifiers"),
        ("What does pressing the period (.) key on the Numpad do in Blender?", 
         ["Focuses on the selected object", "Adds a new object", "Renders the scene", "Opens preferences"], "Focuses on the selected object"),
        ("How do you delete a selected object in Blender?", 
         ["X", "Shift+X", "Alt+X", "Ctrl+X"], "X"),
        ("Which tool allows you to move objects in Blender?", 
         ["Grab Tool (G)", "Rotate Tool (R)", "Scale Tool (S)", "Extrude Tool (E)"], "Grab Tool (G)"),
    ]

    # Initialize score
    score = 0

    # Display questions and collect answers
    for i, (question, options, correct_answer) in enumerate(questions):
        st.write(f"Q{i+1}: {question}")
        if options:
            answer = st.radio("", options, key=f"q{i}")
        else:
            answer = st.text_input("", key=f"q{i}")

        if answer.strip().lower() == correct_answer.strip().lower():
            score += 1

    # Display score and corresponding icon/smiley
    st.write(f"Your score: {score}/{len(questions)}")

    if score == len(questions):
        st.success("Excellent! 🎉😃")
    elif score >= len(questions) * 0.7:
        st.success("Good job! 😊")
    elif score >= len(questions) * 0.4:
        st.warning("Fair effort! 🙂")
    else:
        st.error("Needs Improvement! 😕")

def main():
 
     
    # Sidebar tabs and hyperlinks
    st.sidebar.title('BCA541B: Quick Navigation')
    tab = st.sidebar.radio('Go to', ['Home', 'Groups', 'Theory Contents', 'Practical Programs', 'Assessments', 'Activities and Instructions'])
    if tab == 'Home':
        course_contents()
           
    elif tab == 'Activities and Instructions':
        display_instructions()

    elif tab == 'Theory Contents':
        unit_content_activity()

    elif tab == 'Practical Programs':
        practical_programs()
        
    elif tab == 'Groups':
        display_groups()
    elif tab == 'Submissions':
        submission()
    elif tab == 'Assessments':
        assessments()
if __name__ == "__main__":
    main()
