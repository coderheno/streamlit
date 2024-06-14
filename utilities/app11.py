import pandas as pd
import streamlit as st
import os

def case_study_recipe_management():
    st.title("Case Study: Streamlining Recipe Management")

    st.subheader("Background")
    st.write("""
    **Bake My Day**, a popular bakery known for its delicious and creative pastries, is struggling with recipe management. Their recipes are currently stored on handwritten cards and scattered notebooks, making it difficult for bakers to find specific recipes quickly and consistently. This chaos often leads to errors in ingredient measurements and baking times, impacting the quality and consistency of their baked goods.
    """)
    
    st.write("""
    **Challenges:**
    - Handwritten recipes are time-consuming to locate and prone to damage or misplacement.
    - Variations in handwriting and lack of standardized units can lead to inaccurate measurements and inconsistencies in baking results.
    - New recipes developed by one baker are not readily accessible to others, hindering knowledge sharing and innovation.
    - Estimating ingredient needs based on handwritten recipes is difficult, leading to potential overstocking or understocking of ingredients.
    """)

    st.write("""
    **Proposed Solution:**
    - Using dictionaries and lists to provide a structured and searchable way to store and access recipes, eliminating reliance on handwritten cards.
    - Calculations can ensure consistent ingredient amounts, leading to more reliable baking results.
    - All bakers can access and share recipes within the program, fostering knowledge exchange and recipe innovation.
    - The system can calculate the total ingredient needs for a recipe batch, aiding in inventory planning and preventing stock shortages.
    """)

    st.subheader("Discussion Questions")
    st.write("""
    1. **What are some limitations of using simple data types for recipe management?**
        - Simple data types such as strings and basic lists can lack the necessary structure and flexibility needed for comprehensive recipe management.
        - They may not easily support complex queries or updates, and large amounts of data can become cumbersome to manage and prone to errors.
    
    2. **How could these limitations be addressed by incorporating libraries or more complex data structures?**
        - Incorporating libraries such as pandas can allow for more sophisticated data manipulation and querying capabilities.
        - Using more complex data structures like nested dictionaries or dataframes can provide better organization and accessibility for recipes, allowing for more efficient searches, updates, and calculations.
    
    3. **How can Bake My Day further leverage the system to automate other aspects of their operations?**
        - Bake My Day can integrate inventory management by linking ingredient usage with stock levels to automate reordering processes.
        - They can implement scheduling and task management for bakers, automating workflow and ensuring timely preparation of baked goods.
        - Additionally, they can use the system to analyze sales data and customer preferences, optimizing recipe offerings and improving customer satisfaction.
    """)

def display_groups():
    # Define the groups and mentors
    groups = {
        "Group 1": ["Dr RESMI K R", "Dr SARAVANAKUMAR K", "Dr Manasa", "Dr FABIOLA HAZEL POHRMEN", "Dr SAGAYA AURELIA P", "Dr SANDEEP J"],
        "Group 2": ["Dr MOHANA PRIYA T", "Dr ROHINI V", "Dr Chanti", "Dr SREEJA C S", "Dr Amrutha K", "Dr KIRUBANAND V B", "Dr BEAULAH SOUNDARABAI P"],
        "Group 3": ["Dr HUBERT", "Dr SARAVANAN K N", "Dr New begin", "Dr ASHOK IMMANUEL V", "Dr Sangeetha GOVINDA", "Dr NISMON RIO R"],
        "Group 4": ["Dr Vijay", "Dr AROKIA PAUL RAJAN R", "Dr RAMAMURTHY B", "Dr VINEETHA KR", "Dr SMITHA VINOD", "Dr MANJUNATHA HIREMATH", "Dr SMERA C"]
    }
    
    # Create a DataFrame for displaying in Streamlit
    df = pd.DataFrame(groups.values(), index=groups.keys()).transpose()
    
    # Display the table using Streamlit
    st.write("Groups and Mentors:")
    st.table(df)



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

#def course_plan():
#    st.header("Course Schedule: Introduction to Python")

    # Unit 1: INTRODUCING PYTHON
 #   st.subheader("Unit-1: INTRODUCING PYTHON")
 #   st.subheader("Unit details:")
  #  st.write("Introduction, Python Fundamentals, Features of Python, Components of a Python Program")

   # st.subheader("Week 1 (19-22 June)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Activity: Group Discussion")
    #st.markdown("- [Python Features](https://www.geeksforgeeks.org/python-features/)")

    #st.subheader("Week 2 (24-29 June)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Experiential Learning: (colab, VS code, Jupyter Notebook, Python IDE, Pycharm etc.)")
    #st.markdown("- [Python Keywords and Identifiers](https://www.geeksforgeeks.org/python-keywords-and-identifiers/)")

    #st.subheader("Week 3 (1-6 July)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Problem-solving Sessions.")
    #st.markdown("- Assessment-1 (20 Marks)")
    #st.markdown("- [Precedence and Associativity of Operators in Python](https://www.javatpoint.com/precedence-and-associativity-of-operators-in-python)")

    # Unit 2: PYTHON DATA TYPES: LISTS AND TUPLES
    #st.subheader("Unit-2: PYTHON DATA TYPES: LISTS AND TUPLES")
    #st.subheader("Unit details:")
    #st.write("Introduction to Python Data types and Data structures")

    #st.subheader("Week 4 (8-13 July)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Activity: Participatory Learning: Poster Presentation")
    #st.markdown("- [Lists: Accessing elements, Basic List operations, Built-in methods](https://corporatefinanceinstitute.com/resources/data-science/python-data-structures/)")

    #st.subheader("Week 5 (15-19 July)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Instructional activity: Brainstorming")
    #st.markdown("- [Tuples: working with elements, Basic Tuple operation, Tuple methods and Type of Tuples](https://www.geeksforgeeks.org/list-methods-python/)")

    #st.subheader("Week 6 (22-27 July)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Formative Assessment: Quiz using Kahoot")
    #st.markdown("- Assessment-2 (20 Marks)")
    #st.markdown("- [Python Tuple Methods](https://www.geeksforgeeks.org/python-tuple-methods/)")

    # Unit 3: PYTHON DATA TYPES: SETS AND DICTIONARIES
    #st.subheader("Unit-3: PYTHON DATA TYPES: SETS AND DICTIONARIES")
    #st.subheader("Unit details:")
    #st.write("Introduction to Sets and Dictionaries")

    #st.subheader("Week 7 (29 July - 3 Aug)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Experiential Learning: Code Review Session (Review by peer)")
    #st.markdown("- [Sets: Definition, Set Elements, Built-in methods, basic set operations](https://www.geeksforgeeks.org/python-operators-for-sets-and-dictionaries/)")

    #st.subheader("Week 8 (5-10 Aug)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Participatory Learning: Think-Pair-Share Activities")
    #st.markdown("- [Dictionaries: Defining a dictionary, accessing elements, basic operations, methods](https://www.geeksforgeeks.org/sets-in-python/)")

    #st.subheader("Week 9 (12-16 Aug)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Summative Assessment: Concept Map (or) Mind map (Assessment-3: 10 Marks)")
    #st.markdown("- [Dictionary Methods in Python](https://www.w3schools.com/python/python_ref_dictionary.asp)")

    # Unit 4: Comprehensions and Functions
    #st.subheader("Unit-4: Comprehensions and Functions")
    #st.subheader("Unit details:")
    #st.write("Comprehensions: List Comprehensions, Set Comprehension, Dictionary Comprehension")

    #st.subheader("Week 10 (19-24 Aug)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Diagnostic Assessment: Debugging Challenges (Assessment-4: 30 Marks)")
    #st.markdown("- [Python List Comprehension and Dictionary](https://www.netguru.com/blog/python-list-comprehension-dictionary)")

    #st.subheader("Week 12 (2-7 Sep)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Instructional Activity: Code Enrichment")
    #st.markdown("- [Functions: Defining a function, Types of arguments](https://www.geeksforgeeks.org/python-functions/)")
    #st.markdown("- Unpacking arguments, Recursive functions")

    # Unit 5: Functional Programming
    #st.subheader("Unit-5: Functional Programming")
    #st.subheader("Unit details:")
    #st.write("Lambda functions, Higher order functions, Map, Filter, Reduce")

    #st.subheader("Week 14 (16-20 Sep)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Experiential Learning: Workshops and MooC courses")
    #st.markdown("- [Using Lambda with map(), filter(), reduce()](https://www.javatpoint.com/map-filter-and-reduce-in-python-with-examples)")

    #st.subheader("Week 15 (23-28 Sep)")
    #st.write("Hours per Chapter: 4")
    #st.subheader("Learner Centered Approach:")
    #st.markdown("- Project Deployment Project Based learning")
    #st.markdown("- [Modules, Packages and Namespaces: Main module, built-in, creation of user defined modules](https://realpython.com/python-modules-packages/)")

def course_contents():
    st.title("BCA263: Introduction to Python")
    st.write("""
    **Course Description:**
    This course covers the introductory concepts associated with Python such as the Python Fundamentals, Data structures, and Functions of Python with the help of built-in modules. This course aims to provide comprehensive knowledge of Python programming paradigms.

    **Course Objective:**
    This course aims to provide comprehensive knowledge of Python programming paradigms.

    **Learning Outcomes:**
    - Understand the Python Environment, fundamental concepts, and Control Structures.
    - Demonstrate the Python Data Structures such as lists, Tuples, sets, and Dictionaries.
    - Apply Python programming concepts and principles in real-world scenarios such as data analysis, web development, etc.
    - Develop Python-based projects and applications from concepts of functional programming, modules, packages, namespaces, etc.

    **Learner-Centric Approach (LCA):**
    This course employs a learner-centric approach to enhance student engagement and learning outcomes. Key features include:
    - Hands-on practical exercises and projects.
    - Interactive sessions and discussions.
    - Personalized feedback and guidance.
    - Integration of real-world applications and case studies.

    **Career Opportunities:**
    Completion of this course opens doors to various career opportunities, including:
    - Python Developer
    - Data Analyst
    - Web Developer
    - Software Engineer
    - Systems Analyst
    """)
def activity2():
    st.title("Case Study: Faculty Enhancement System in a University ERP")
    st.write("A professor at our university envisioned creating a comprehensive Faculty Enhancement System (FES) within the university's Knowledge Pro (KP) system. With a solid understanding of Python programming, the professor embarked on a journey to develop this system to help both faculty and students efficiently manage academic information.")
    
    st.header("Project Overview")
    st.write("The project began by defining the core data structures and functions for the system. A FacultyMember class was created to represent each faculty member, with attributes such as name, faculty ID, courses, and performance metrics. Utilizing methods and constructors, the professor ensured that each faculty member object could be instantiated with the necessary details.")
    
    st.write("As the system grew, the professor recognized the importance of organizing faculty by courses for better navigation and management. Data structures like lists, sets, and dictionaries were employed to implement different types of course-related information and performance metrics. To maintain security and encapsulation, the professor used access specifiers to control the visibility and interaction of class members.")
    
    st.write("As the system expanded further, the professor faced the challenge of calculating performance metrics and ratings efficiently. Functions were used to perform these calculations. For optimization and stability, sets were used to ensure the uniqueness of course assignments and tuples to store immutable data like faculty IDs.")
    
    st.write("The professor also envisioned a way to handle diverse faculty types and academic structures. With determination and mastery of Python programming, the vision was successfully brought to life. The Faculty Enhancement System became a beacon of organization and efficiency for faculty and students at the university, showcasing the power and elegance of Python programming.")
    
    st.header("Discussion Questions:")
    st.write("1. How were sets used to find common courses between faculty members?")
    st.write("2. How was encapsulation ensured and the integrity of the platform's internal structure maintained?")
    st.write("3. What were the specific advantages of each data structure in this context?")
    
    st.header("Evaluation Rubrics (Case Study)")
    st.write("S. No. | Evaluation Rubrics (Case study)          | Marks")
    st.write("1     | Understanding and Analysis               | 10%")
    st.write("2     | Research and Use of Evidence             | 10%")
    st.write("3     | Organization and Structure               | 10%")
    st.write("4     | Clarity and Precision                    | 10%")
    st.write("5     | Creativity and Originality               | 10%")
    
    st.subheader("Marking scheme:")
    st.write("- Excellent: 90-100% marks")
    st.write("- Good: 70-89% marks")
    st.write("- Satisfactory: 50-69% marks")
    st.write("- Needs Improvement: 30-49% marks")
    st.write("- Unsatisfactory: 0-29% marks")


def display_groups():
    # Define the groups and mentors
    groups = {
        "Group 1": ["Dr RESMI K R", "Dr SARAVANAKUMAR K", "Dr Manasa", "Dr FABIOLA HAZEL POHRMEN", "Dr SAGAYA AURELIA P", "Dr SANDEEP J", "Member-6"],
        "Group 2": ["Dr MOHANA PRIYA T", "Dr ROHINI V", "Dr Chanti", "Dr SREEJA C S", "Dr Amrutha K", "Dr KIRUBANAND V B", "Dr BEAULAH SOUNDARABAI P"],
        "Group 3": ["Dr HUBERT", "Dr SARAVANAN K N", "Dr New begin", "Dr ASHOK IMMANUEL V", "Dr Sangeetha GOVINDA", "Dr NISMON RIO R", "Member-6"],
        "Group 4": ["Dr Vijay", "Dr AROKIA PAUL RAJAN R", "Dr RAMAMURTHY B", "Dr VINEETHA KR", "Dr SMITHA VINOD", "Dr MANJUNATHA HIREMATH", "Dr SMERA C"]
    }
    
    # Create a DataFrame for displaying in Streamlit
    df = pd.DataFrame(groups.values(), index=groups.keys()).transpose()
    
    # Display the table using Streamlit
    st.write("Groups and Mentors:")
    st.table(df)



def activity1():
    st.title("Learner-Centric Approach Activity: Creating a Mind Map on Python Data Structures")
    st.subheader("Objective:")
    st.write("Learners will create a mind map focusing on a specific Python data structure within a chosen domain, fostering a deeper understanding of how data structures are applied in real-world scenarios.")

    st.subheader("Materials Needed:")
    st.write("- Paper and colored pens/pencils (for offline activity)")
    st.write("- Mind mapping software or online tools (such as MindMeister, Coggle, or Lucidchart) (for online activity)")
    st.write("- Access to Python documentation and resources")

    st.subheader("Steps:")
    
    st.write("**Introduction (5 minutes)**")
    st.write("- Briefly introduce the concept of data structures in Python (lists, tuples, dictionaries, sets, etc.).")
    st.write("- Explain the importance of understanding data structures in the context of problem-solving and application development.")
    st.write("- Introduce the mind mapping technique and how it can help organize and visualize information.")

    st.write("**Topic Selection (5 minutes)**")
    st.write("- Each group of students chooses a specific data structure (e.g., lists, dictionaries, sets) and a domain (e.g., web development, data analysis, machine learning, game development).")
    st.write("Examples:")
    st.write("  - Lists in data analysis")
    st.write("  - Dictionaries in web development")
    st.write("  - Sets in machine learning")

    st.write("**Research and Information Gathering (Optional)**")
    st.write("- Learners research their chosen data structure and domain, focusing on:")
    st.write("  - Definition and characteristics of the data structure")
    st.write("  - Common operations and methods associated with the data structure")
    st.write("  - Real-world applications and examples within the chosen domain")
    st.write("- Encourage learners to use Python documentation, online tutorials, and relevant articles.")

    st.write("**Mind Map Creation (10 minutes)**")
    st.write("- Learners create a mind map that includes:")
    st.write("  - The central theme (chosen data structure and domain)")
    st.write("  - Branches for definition, characteristics, operations/methods, and applications/examples")
    st.write("  - Sub-branches for more detailed information, such as code snippets, use cases, and advantages/disadvantages")
    st.write("- Encourage creativity in the presentation, using colors, icons, and images to enhance understanding.")

    st.write("**Presentation and Discussion (5 minutes)**")
    st.write("- Learners present their mind maps to the class, explaining their findings and the connections they made.")
    st.write("- Facilitate a discussion on the different data structures and their applications in various domains.")
    st.write("- Encourage students to ask questions and provide feedback on each other’s mind maps.")

    st.write("**Reflection (5 minutes)**")
    st.write("- Learners write a brief reflection on what they learned about their chosen data structure and how the mind mapping activity helped them understand its applications.")
    st.write("- Mandatorily, students have to share their reflections on other group presentations in the GCR.")

    st.subheader("Evaluation:")
    st.write("- Evaluation of the mind maps based on completeness(5 Marks), accuracy(5 Marks), creativity(5 Marks), and presentation(5 Marks).")
    st.write("- Learners will be assessed based on the understanding of the data structure and its applications through their presentations and reflections.")

    st.write("Outcome of this activity: It engages learners in active learning, encourages collaboration, and helps them see the practical applications of Python data structures in various fields.")

def main():
    
     
    # Sidebar tabs and hyperlinks
    st.sidebar.title('BCA263: Quick Navigation')
    tab = st.sidebar.radio('Go to', ['Home', 'Groups', 'Activity-1', 'Case Study-1', 'Case Study-2', 'Submissions', 'LCA-Activities'])
    if tab == 'Home':
        course_contents()
           
    elif tab == 'LCA-Activities':
        lca_contents()

    elif tab == 'Activity-1':
        activity1()

    elif tab == 'Case Study-1':
        activity2()
    elif tab == 'Case Study-2':
        case_study_recipe_management()
    elif tab == 'Groups':
        display_groups()
    elif tab == 'Submissions':
        submission()

if __name__ == "__main__":
    main()
