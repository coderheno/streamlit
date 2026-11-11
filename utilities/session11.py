import streamlit as st

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="React Learning Portal",
    page_icon="⚛️",
    layout="wide",
)

# -----------------------------------------------------
# Custom CSS
# -----------------------------------------------------
st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:bold;
    color:#1E88E5;
}

.subtitle{
    font-size:22px;
    color:gray;
}

.card{
    padding:20px;
    border-radius:12px;
    background-color:#F8F9FA;
    border:1px solid #E0E0E0;
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

st.sidebar.title("⚛️ React Learning Portal")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📘 Module 1",
        "📗 Module 2",
        "📙 Module 3",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
"""
**Course**

MCA413-1

Full Stack Development

Duration : 45 Hours
"""
)

# -----------------------------------------------------
# HOME
# -----------------------------------------------------

if page=="🏠 Home":

    st.markdown('<p class="main-title">⚛️ Full Stack Development using React</p>',unsafe_allow_html=True)

    st.markdown('<p class="subtitle">Interactive Learning Portal</p>',unsafe_allow_html=True)

    st.divider()

    st.write(
"""
Welcome to the **React Learning Portal**.

This portal provides concise theory, important concepts, examples, and hands-on exercises for learning React from basics to CRUD applications.
"""
)

    st.subheader("📚 Course Modules")

    col1,col2,col3=st.columns(3)

    with col1:

        st.markdown("""
<div class="card">

<h3>📘 Module 1</h3>

<h4>React Fundamentals</h4>

✔ React Introduction

✔ JSX

✔ Components

✔ Props

✔ ES6

✔ NPM

</div>
""",unsafe_allow_html=True)

    with col2:

        st.markdown("""
<div class="card">

<h3>📗 Module 2</h3>

<h4>React Interactivity</h4>

✔ Hooks

✔ useState

✔ useEffect

✔ Forms

✔ Events

✔ Images

✔ Conditional Rendering

</div>
""",unsafe_allow_html=True)

    with col3:

        st.markdown("""
<div class="card">

<h3>📙 Module 3</h3>

<h4>CRUD & Routing</h4>

✔ Routing

✔ Axios

✔ JSON Server

✔ SQLite

✔ CRUD Operations

</div>
""",unsafe_allow_html=True)

    st.divider()

    st.subheader("🎯 Running Example")

    st.success("""
Student Attendance Management System
""")

    st.write("""
Throughout this course, we will build **one complete React application**.

### Module 1
Develop the User Interface

### Module 2
Add Interactivity using Hooks

### Module 3
Store Attendance using CRUD Operations
""")

    st.divider()

    st.subheader("📈 Learning Progress")

    st.progress(0)

    st.info("Complete each module sequentially.")

# -----------------------------------------------------
# MODULE 1
# -----------------------------------------------------

elif page=="📘 Module 1":

    st.title("📘 Module 1")
    st.subheader("React Fundamentals")

    st.divider()

    st.success(
"""
Learning Outcome

After completing this module students will be able to

✔ Explain React fundamentals

✔ Create React applications

✔ Understand JSX

✔ Build reusable components

✔ Pass data using Props

✔ Apply ES6 concepts

✔ Manage packages using NPM
"""
    )

    st.divider()

    tab1,tab2,tab3=st.tabs(
        [
            "📖 Overview",
            "📚 Topics",
            "💻 Exercise"
        ]
    )

    # -----------------------------------

    with tab1:

        st.header("Module Overview")

        st.write("""
React is a JavaScript library used for developing interactive and reusable user interfaces.

Instead of building an entire webpage repeatedly, React divides the UI into reusable components, making development faster and easier.
""")

        st.info("""
Key Features

• Component-Based Development

• Virtual DOM

• Reusable Components

• Faster Rendering

• Single Page Applications
""")

        st.subheader("Why Learn React?")

        col1,col2=st.columns(2)

        with col1:

            st.metric("Industry Demand","⭐⭐⭐⭐⭐")

            st.metric("Difficulty","Intermediate")

        with col2:

            st.metric("Performance","High")

            st.metric("Popularity","Very High")

    # -----------------------------------

    with tab2:

        st.header("Topics Covered")

        topics=[
            "React Introduction",
            "JSX",
            "Components",
            "Props",
            "ES6 Features",
            "NPM"
        ]

        for i,t in enumerate(topics,start=1):
            st.write(f"**{i}. {t}**")

        st.divider()

        st.subheader("Application Developed")

        st.success("Student Attendance Dashboard")

        st.write("""
Students will develop a static attendance dashboard using:

• JSX

• Components

• Props

• ES6

This application will be enhanced in the next modules.
""")

    # -----------------------------------

    with tab3:

        st.header("Hands-on Exercise")

        st.write("""
Develop a **Student Attendance Dashboard**.
""")

        st.subheader("Requirements")

        st.checkbox("Create Header Component")

        st.checkbox("Create Student Card Component")

        st.checkbox("Create Attendance Form")

        st.checkbox("Display Course Information")

        st.checkbox("Create Footer Component")

        st.divider()

        st.success("""
Concepts Covered

✔ React

✔ JSX

✔ Components

✔ Props

✔ ES6

✔ NPM
""")

# -----------------------------------------------------
# MODULE 2
# -----------------------------------------------------

elif page==" Module 1":

    st.title("📘 Module 1 : React Fundamentals")
    st.divider()

    st.success("""
    🎯 Learning Outcome

    • Understand React fundamentals
    • Create React projects using Vite
    • Develop reusable components
    • Pass data using Props
    • Apply ES6 concepts
    """)

    tab1, tab2 = st.tabs(["📖 Theory", "💻 Running Example"])

    # ===========================================================
    # THEORY
    # ===========================================================

    with tab1:

        # React Introduction
        with st.expander("1️⃣ React Introduction", expanded=True):

            st.write("""
React is an open-source JavaScript library used to build fast,
interactive and reusable user interfaces.

React divides a webpage into reusable Components.
            """)

            st.info("""
Important Points

✔ Developed by Meta

✔ Component-Based Architecture

✔ Virtual DOM

✔ Single Page Application (SPA)

✔ Reusable Components
""")

        # JSX

        with st.expander("2️⃣ JSX"):

            st.write("""
JSX (JavaScript XML) allows writing HTML inside JavaScript.

It makes UI development easier and more readable.
""")

            st.code("""

function App(){

   return(
      <h1>Hello React</h1>
   );

}

""", language="jsx")

            st.success("Output : Hello React")

            st.warning("""
Remember

• One parent element

• className instead of class

• JavaScript inside { }
""")

        # Components

        with st.expander("3️⃣ Components"):

            st.write("""
A Component is a reusable piece of UI.

Example

Header

Attendance Form

Footer
""")

            st.code("""

function Header(){

   return <h2>Attendance System</h2>

}

""", language="jsx")

            st.info("""
Advantages

✔ Reusable

✔ Easy Maintenance

✔ Modular Design
""")

        # Props

        with st.expander("4️⃣ Props"):

            st.write("""
Props are used to pass data from Parent Component to Child Component.
""")

            st.code("""

<Student
   name="Rahul"
   course="MCA"
/>

""", language="jsx")

            st.code("""

function Student({name,course}){

   return(
      <>
      <h3>{name}</h3>
      <p>{course}</p>
      </>
   );

}

""", language="jsx")

            st.success("Props are Read Only")

        # ES6

        with st.expander("5️⃣ ES6 Features"):

            st.write("""
React uses modern JavaScript (ES6).
""")

            col1,col2=st.columns(2)

            with col1:

                st.markdown("""
**Important Features**

- let

- const

- Arrow Functions

- Destructuring
""")

            with col2:

                st.markdown("""

- Template Literals

- Spread Operator

- Import

- Export

""")

            st.code("""

const student={
name:"John",
course:"MCA"
}

const {name,course}=student;

""", language="javascript")

        # NPM

        with st.expander("6️⃣ NPM"):

            st.write("""
NPM (Node Package Manager) installs and manages React packages.
""")

            st.code("""

npm install

npm run dev

npm install axios

""", language="bash")

            st.info("""
Uses

✔ Install Libraries

✔ Run React

✔ Manage Dependencies
""")

    # ===========================================================
    # RUNNING EXAMPLE
    # ===========================================================

    with tab2:

        st.header("🎯 Running Example")

        st.success("Student Attendance Dashboard")

        st.markdown("""
Application Structure


App
│
├── Header
├── StudentCard
├── AttendanceForm
└── Footer

""")

        col1,col2=st.columns(2)

        with col1:

            st.subheader("Student Card")

            st.code("""

<Student

name="Rahul"

course="MCA"

section="A"

/>

""", language="jsx")

        with col2:

            st.subheader("Output")

            st.success("""
Name : Rahul

Course : MCA

Section : A
""")

        st.divider()

        st.subheader("Components Used")

        c1,c2,c3,c4=st.columns(4)

        c1.metric("JSX","✔")

        c2.metric("Components","✔")

        c3.metric("Props","✔")

        c4.metric("ES6","✔")

        st.divider()

        st.subheader("Exercise")

        st.info("""
Develop a Student Attendance Dashboard.

Requirements

✔ Header

✔ Student Card

✔ Attendance Form

✔ Footer

Use

• JSX

• Components

• Props

• ES6
""")
elif page=="📗 Module 2":

    st.title("📗 Module 2 : React Interactivity")
    st.divider()

    st.success("""
🎯 Learning Outcome

• Understand React Hooks
• Manage data using useState()
• Perform actions using useEffect()
• Handle Forms and Events
• Display Images
• Apply Conditional Rendering
""")

    tab1, tab2 = st.tabs(["📖 Theory", "💻 Running Example"])

    # =====================================================
    # THEORY
    # =====================================================

    with tab1:

        # Hooks
        with st.expander("1️⃣ Hooks", expanded=True):

            st.write("""
Hooks allow Functional Components to use React features such as
State and Lifecycle methods.
""")

            st.info("""
Important Points

✔ Introduced in React 16.8

✔ Used only inside Functional Components

✔ Common Hooks:
   • useState()
   • useEffect()
""")

        # useState
        with st.expander("2️⃣ useState()"):

            st.write("""
useState() stores and updates dynamic data inside a component.
""")

            st.code("""
const [name, setName] = useState("");
""", language="javascript")

            st.success("""
Uses

✔ Store Input

✔ Update UI

✔ Manage State
""")

        # useEffect
        with st.expander("3️⃣ useEffect()"):

            st.write("""
useEffect() executes code after the component is rendered.

Mostly used for:
• API Calls
• Loading Data
• Timers
""")

            st.code("""
useEffect(() => {

   loadStudents();

}, []);
""", language="javascript")

            st.warning("""
[] → Runs only once after loading.
""")

        # Forms
        with st.expander("4️⃣ Forms"):

            st.write("""
Forms collect user input using controlled components.
""")

            st.markdown("""
**Common Form Elements**

- Textbox
- Select
- Radio Button
- Checkbox
- Button
""")

        # Images
        with st.expander("5️⃣ Images"):

            st.write("""
Images can be displayed using local files or URLs.
""")

            st.code("""
import student from "./student.png";

<img src={student}/>
""", language="jsx")

        # Conditional Rendering
        with st.expander("6️⃣ Conditional Rendering"):

            st.write("""
Display UI based on a condition.
""")

            st.code("""
{present ? "Present" : "Absent"}
""", language="jsx")

            st.success("Used for Login, Status, Validation etc.")

        # Events
        with st.expander("7️⃣ Events"):

            st.write("""
Events respond to user actions.
""")

            st.markdown("""
**Common Events**

- onClick
- onChange
- onSubmit
- onMouseOver
""")

            st.code("""
<button onClick={saveAttendance}>
Save
</button>
""", language="jsx")

    # =====================================================
    # RUNNING EXAMPLE
    # =====================================================

    with tab2:

        st.header("🎯 Student Attendance App")

        st.write("""
The dashboard created in Module 1 is now converted into an interactive application.
""")

        st.markdown("""
### Workflow


Enter Name
│
▼
Select Course
│
▼
Choose Attendance
│
▼
Click Submit
│
▼
Attendance Recorded

""")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Features")

            st.checkbox("Student Name")

            st.checkbox("Course")

            st.checkbox("Present / Absent")

            st.checkbox("Student Image")

            st.checkbox("Submit Button")

            st.checkbox("Reset Button")

        with col2:

            st.subheader("React Concepts Used")

            st.metric("Hooks", "✔")

            st.metric("useState()", "✔")

            st.metric("useEffect()", "✔")

            st.metric("Forms", "✔")

            st.metric("Events", "✔")

            st.metric("Conditional Rendering", "✔")

        st.divider()

        st.subheader("Application Preview")

        st.info("""
----------------------------------

📸 Student Image

Name : ____________

Course : ▼ MCA

Attendance

( ) Present

( ) Absent

[ Submit ]

[ Reset ]

----------------------------------
""")

        st.success("""
Exercise

Develop an Interactive Student Attendance App.

Requirements

✔ Student Name

✔ Course

✔ Attendance Status

✔ Student Image

✔ Submit Button

✔ Reset Button

Use

• Hooks

• useState()

• useEffect()

• Forms

• Events

• Conditional Rendering
""")
elif page=="📙 Module 3":

    st.title("📙 Module 3 : Routing & CRUD")
    st.divider()

    st.success("""
🎯 Learning Outcome

• Navigate between React pages using Routing
• Connect React with APIs using Axios
• Store data using JSON Server
• Connect React with SQLite
• Perform CRUD operations
""")

    tab1, tab2 = st.tabs(["📖 Theory", "💻 Running Example"])

    # ===================================================
    # THEORY
    # ===================================================

    with tab1:

        # Routing
        with st.expander("1️⃣ Routing", expanded=True):

            st.write("""
React Router enables navigation between pages without
reloading the application.
""")

            st.info("""
Important Points

✔ Single Page Navigation

✔ BrowserRouter

✔ Routes

✔ Route

✔ Link
""")

            st.code("""

<BrowserRouter>

<Routes>

<Route path="/" element={<Home/>}/>

<Route path="/attendance" element={<Attendance/>}/>

</Routes>

</BrowserRouter>

""", language="jsx")

        # Axios

        with st.expander("2️⃣ Axios"):

            st.write("""
Axios is a JavaScript library used to communicate with
backend APIs.
""")

            st.info("""
Supports

✔ GET

✔ POST

✔ PUT

✔ DELETE
""")

            st.code("""

axios.get("http://localhost:3001/students")

""", language="javascript")

        # JSON Server

        with st.expander("3️⃣ JSON Server"):

            st.write("""
JSON Server provides a fake REST API for frontend development.
""")

            st.code("""

npm install -g json-server

npx json-server --watch db.json --port 3001

""", language="bash")

            st.code("""

{
 "students":[]
}

""", language="json")

            st.success("""
Advantages

✔ No Backend Coding

✔ Easy CRUD

✔ REST API
""")

        # SQLite

        with st.expander("4️⃣ SQLite"):

            st.write("""
SQLite is a lightweight file-based relational database.
""")

            st.info("""
Important Points

✔ No Server Required

✔ SQL Queries

✔ Fast

✔ Portable
""")

            st.code("""

CREATE TABLE students(

id INTEGER PRIMARY KEY,

name TEXT,

course TEXT,

status TEXT

);

""", language="sql")

        # CRUD

        with st.expander("5️⃣ CRUD Operations"):

            st.write("""
CRUD represents the four basic database operations.
""")

            col1, col2 = st.columns(2)

            with col1:

                st.success("""
Create

Add Attendance
""")

                st.info("""
Read

View Attendance
""")

            with col2:

                st.warning("""
Update

Edit Attendance
""")

                st.error("""
Delete

Remove Attendance
""")

    # ===================================================
    # EXAMPLE
    # ===================================================

    with tab2:

        st.header("🎯 Student Attendance Management System")

        st.write("""
The Attendance App developed in Module 2 is now connected
to a database.
""")

        st.subheader("Application Flow")

        st.code("""

Login
   │
   ▼
Dashboard
   │
   ▼
Attendance List
   │
   ▼
Add Attendance
   │
   ▼
Edit Attendance
   │
   ▼
Delete Attendance

""")

        st.divider()

        st.subheader("Application Modules")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.success("""
🏠 Dashboard

• Welcome

• Navigation

• Summary
""")

        with col2:

            st.info("""
📄 Attendance

• Add

• View

• Search
""")

        with col3:

            st.warning("""
⚙ CRUD

• Update

• Delete
""")

        st.divider()

        st.subheader("Technology Stack")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("React Router", "✔")

        c2.metric("Axios", "✔")

        c3.metric("JSON Server", "✔")

        c4.metric("SQLite", "✔")

        st.divider()

        st.subheader("Attendance CRUD Flow")

        st.code("""

Student Form
      │
      ▼
Axios POST
      │
      ▼
JSON Server / SQLite
      │
      ▼
Save Record
      │
      ▼
Axios GET
      │
      ▼
Display Records
      │
      ▼
Update/Delete

""")

        st.success("""
Exercise

Develop a Student Attendance Management System.

Requirements

✔ Dashboard

✔ Add Attendance

✔ View Attendance

✔ Edit Attendance

✔ Delete Attendance

Use

• Routing

• Axios

• JSON Server / SQLite

• CRUD
""")
