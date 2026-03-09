import streamlit as st

st.set_page_config(page_title="Advanced Project Applications using .NET", layout="wide")

st.title("Advanced Project Applications using .NET")
st.subheader("Study Material & Project Guide")

menu = st.sidebar.selectbox(
    "Select Topic",
    [
        "Unit Overview",
        "Windows Forms Project Development",
        "Face Recognition & Biometrics",
        "Voice-Based Applications",
        "IoT Integration with Windows Forms",
        "CPCG Attendance Mini Project",
        "Project-Based Lab Work",
        "Service Learning Mini Project",
        "Assessment Rubrics"
    ]
)

# --------------------------------------------------
# COURSE OVERVIEW
# --------------------------------------------------

if menu == "Unit Overview":

    st.header("Unit Overview")

    st.write("""
    This unir focuses on developing **real-world applications using C# and .NET technologies**.
    Students will learn how to design intelligent and interactive systems by integrating:

    - Windows Forms Application Development
    - Face Recognition and Biometric Authentication
    - Speech Recognition Systems
    - IoT Device Integration
    - Real-world problem solving through project-based learning
    """)

    st.subheader("Learning Outcomes")

    st.markdown("""
    - Develop desktop applications using **Windows Forms in C#**
    - Implement **face recognition and biometric systems**
    - Build **voice-based applications using speech recognition**
    - Integrate **IoT devices with desktop applications**
    - Design solutions for **NGOs, SDGs, and social impact initiatives**
    """)

# --------------------------------------------------
# WINDOWS FORMS
# --------------------------------------------------

elif menu == "Windows Forms Project Development":

    st.header("Real-World Project Development using Windows Forms")

    st.write("""
    **Windows Forms** is a GUI framework used to build desktop applications
    using the **.NET platform and C# programming language**.
    """)

    st.subheader("Key Features")

    st.markdown("""
    - Event-driven programming
    - Drag and drop interface design
    - Integration with databases
    - Rapid application development
    """)

    st.subheader("Example Application")

    st.write("Student Attendance Management System")

    st.code("""
using System;
using System.Windows.Forms;

namespace AttendanceApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnSubmit_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Attendance Recorded Successfully");
        }
    }
}
""", language="csharp")

    st.info("Exercise: Create a simple Windows Forms application for NGO volunteer registration.")

# --------------------------------------------------
# FACE RECOGNITION
# --------------------------------------------------

elif menu == "Face Recognition & Biometrics":

    st.header("Face Recognition and Biometrics in C#")

    st.write("""
    Face recognition systems identify or verify individuals using facial features.
    These systems are widely used in:
    
    - Security systems
    - Attendance monitoring
    - Smart authentication
    - Biometric access control
    """)

    st.subheader("How Face Recognition Works")

    st.markdown("""
    1. Image Capture
    2. Face Detection
    3. Feature Extraction
    4. Face Matching
    """)

    st.subheader("Example Library")

    st.write("Developers often use **EmguCV (OpenCV wrapper for .NET)**.")

    st.code("""
using Emgu.CV;
using Emgu.CV.Structure;

Capture capture = new Capture();
Image<Bgr, byte> image = capture.QueryFrame();
""", language="csharp")

    st.success("Mini Task: Design a facial recognition attendance system for a small NGO school.")

# --------------------------------------------------
# VOICE APPLICATIONS
# --------------------------------------------------

elif menu == "Voice-Based Applications":

    st.header("Voice-Based Applications using Speech Recognition")

    st.write("""
    Speech recognition enables computers to understand and process spoken language.
    In .NET applications, developers can use the **System.Speech library**.
    """)

    st.subheader("Applications")

    st.markdown("""
    - Voice-controlled software
    - Accessibility tools
    - Smart assistants
    - Voice-operated data entry
    """)

    st.subheader("C# Example")

    st.code("""
using System.Speech.Recognition;

SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine();

Choices commands = new Choices();
commands.Add(new string[] { "start", "stop" });

GrammarBuilder gb = new GrammarBuilder();
gb.Append(commands);

Grammar grammar = new Grammar(gb);
recognizer.LoadGrammar(grammar);

recognizer.SpeechRecognized += (s, e) =>
{
    Console.WriteLine("Command recognized: " + e.Result.Text);
};

recognizer.SetInputToDefaultAudioDevice();
recognizer.RecognizeAsync(RecognizeMode.Multiple);
""", language="csharp")

    st.info("Exercise: Create a voice-based application to control smart classroom devices.")

# --------------------------------------------------
# IOT
# --------------------------------------------------

elif menu == "IoT Integration with Windows Forms":

    st.header("IoT-Based Integration using Windows Forms")

    st.write("""
    IoT allows desktop applications to interact with physical devices such as sensors,
    cameras, and microcontrollers.
    """)

    st.subheader("Typical Architecture")

    st.markdown("""
    IoT Device → Cloud / API → Windows Forms Application
    """)

    st.subheader("Example Scenario")

    st.write("""
    Smart water monitoring system for villages.
    
    Sensors collect data → sent to cloud → Windows Forms dashboard displays data.
    """)

    st.code("""
HttpClient client = new HttpClient();
var response = await client.GetAsync("http://iotdevice/api/data");
""", language="csharp")

    st.success("Task: Build a dashboard to monitor environmental data from IoT sensors.")

# --------------------------------------------------
# LAB WORK
# --------------------------------------------------

elif menu == "Project-Based Lab Work":

    st.header("Project-Based Lab Work")

    st.write("""
    Students will develop a **mini project** that integrates multiple technologies learned
    in the course.
    """)

    st.subheader("Possible Mini Projects")

    st.markdown("""
    1. Face Recognition Attendance System
    2. Voice-Based Smart Assistant for Office
    3. IoT Environmental Monitoring Dashboard
    4. Biometric Authentication System
    5. Smart Donation Management System for NGOs
    """)

# --------------------------------------------------
# SERVICE LEARNING
# --------------------------------------------------

elif menu == "Service Learning Mini Project":

    st.header("Service Learning Mini Project")

    st.write("""
    The mini project must align with **Service Learning principles** by supporting:

    - NGOs
    - Sustainable Development Goals (SDG)
    - Social Action Initiatives
    """)

    st.subheader("Example Ideas")

    st.markdown("""
    **SDG 3 – Good Health**
    - Voice-based patient registration system

    **SDG 4 – Quality Education**
    - Face recognition attendance system for rural schools

    **SDG 11 – Smart Cities**
    - IoT-based environmental monitoring system

    **NGO Support**
    - Volunteer management application
    """)

# --------------------------------------------------
# RUBRICS
# --------------------------------------------------

elif menu == "Assessment Rubrics":

    st.header("Project Evaluation Rubrics")

    st.table({
        "Criteria": [
            "Problem Identification",
            "Application Design",
            "Technology Integration",
            "Innovation",
            "Presentation"
        ],
        "Marks": [10, 15, 15, 5, 5]
    })

    
elif menu == "CPCG Attendance Mini Project":

    st.header("CPCG Class Attendance Management Mini Project")
    st.subheader("Real-World Application for CHRIST University")

    st.write("""
    CHRIST University aims to develop a **Windows-based Attendance Management Application**
    to replace the **manual attendance system used in CPCG skill enhancement classes**.

    Students will design and implement this application using **.NET Windows Forms
    (VB.NET or C#.NET)**.
    """)

    st.markdown("---")

    st.subheader("Project Scenario")

    st.write("""
    CPCG conducts skill development and training programs for students.
    Currently attendance is recorded manually, which makes it difficult to:

    - Maintain accurate records
    - Track attendance history
    - Generate reports quickly
    - Monitor student participation

    The proposed system should automate attendance management using a
    **Windows Forms Desktop Application connected to a SQL database**.
    """)

    st.markdown("---")

    st.subheader("Functional Requirements")

    st.markdown("""
    The system should allow faculty members to:

    - Login securely into the application
    - Add and manage student details
    - Mark attendance for classes
    - View attendance reports
    - Store and retrieve data from a database
    """)

    st.markdown("---")

    st.subheader("Expected Forms in the Application")

    st.markdown("""
    Students must design **4 to 5 Windows Forms** such as:

    1. **Login Form**
       - Username
       - Password
       - Authentication validation

    2. **Student Management Form**
       - Add Student
       - Update Student
       - Delete Student
       - Search Student

    3. **Attendance Form**
       - Select Student
       - Mark Present / Absent
       - Save Attendance

    4. **Attendance Report Form**
       - View attendance records
       - Filter by date or student

    5. **Dashboard Form (Optional)**
       - Overview of total students
       - Attendance summary
    """)

    st.markdown("---")

    st.subheader("Suggested Database Structure")

    st.code("""
Table: Students
-----------------------
StudentID (Primary Key)
StudentName
Course
Email
Phone

Table: Attendance
-----------------------
AttendanceID
StudentID
Date
Status (Present / Absent)

Table: Users
-----------------------
UserID
Username
Password
Role
""", language="sql")

    st.markdown("---")

    st.subheader("Evaluation Rubrics")

    rubric = {
        "Criteria": [
            "UI Design",
            "Usage of Controls and Database",
            "Database Connectivity and Security",
            "Complexity / Advanced Concepts"
        ],
        "Marks": [
            "25%",
            "25%",
            "25%",
            "25%"
        ]
    }

    st.table(rubric)

    st.markdown("---")

    st.subheader("1. UI Design – 25% Marks")

    st.markdown("""
    Students must design a **clear, simple, and user-friendly interface**.

    The application should contain **4–5 forms**, such as:

    - Login Form
    - Student Management Form
    - Attendance Form
    - Attendance Report Form
    - Dashboard (optional)

    The interface should be **easy to navigate and visually organized**.
    """)

    st.markdown("---")

    st.subheader("2. Usage of Controls and Database – 25% Marks")

    st.markdown("""
    Students must use **appropriate Windows Forms controls**, such as:

    - Buttons
    - Textboxes
    - Labels
    - ComboBoxes
    - DataGridView
    - Menus
    - Dialog boxes

    The system should allow users to:

    - Login and authenticate
    - Enter or select student details
    - Select course or class
    - Display student records
    - Display attendance records
    """)

    st.markdown("---")

    st.subheader("3. Database Connectivity and Security – 25% Marks")

    st.markdown("""
    Students must connect their application to a **SQL database**.

    The system should:

    - Create required database tables
    - Insert student records
    - Store attendance data
    - Retrieve attendance reports
    """)

    st.markdown("---")

    st.subheader("4. Complexity / Advanced Concepts – 25% Marks")

    st.markdown("""
    Students must implement **at least one advanced feature** such as:

    **Security**
    - Password encryption
    - Password hashing
    - Advanced authentication strategies

    **Search and Filtering**
    - Filter attendance by student name
    - Filter attendance by date

    **Additional Features**
    - Export attendance reports
    - Dashboard analytics
    - Attendance percentage calculation
    """)

    st.markdown("---")

    st.success("Total Marks: 40")

    st.info("Tip: Students are encouraged to design the system following real-world software development practices.")