import streamlit as st

def main():
    st.title("Digital Mission 2024 Program")

    tabs = st.tabs([
        "Overview",
        "Courses",
        "Train the Trainers",
        "Feedback & Plans",
        "CSA Activities",
        "Class Structure"
    ])

    with tabs[0]:
        overview_tab()

    with tabs[1]:
        courses_tab()

    with tabs[2]:
        train_the_trainers_tab()

    with tabs[3]:
        feedback_and_plans_tab()

    with tabs[4]:
        csa_activities_tab()

    with tabs[5]:
        class_structure_tab()

def overview_tab():
    st.header("Program Overview")
    st.write("Mission: CHRIST is a nurturing ground for an individual's holistic development to make effective contribution to the society in a dynamic environment")
    st.write("Vision: Excellence and Service")
    st.write("Core Values: Faith in God | Moral Uprightness | Love of Fellow Beings | Social Responsibility | Pursuit of Excellence")

def courses_tab():
    st.header("Digital Mission Courses")
    st.subheader("Existing Courses")
    st.table({
        "Level": ["ESSENTIALS", "ESSENTIALS", "ESSENTIALS", "ESSENTIALS", "ENTERPRISE", "ENTERPRISE", "ENTERPRISE", "ENTERPRISE", "ENTERPRISE"],
        "Course Code": ["CSC989", "CSC990", "CSC991", "CSC992", "CSC993", "CSC994", "CSC995", "CSC996", "CSC997"],
        "Course Name": ["Google Workspace", "Formulas & Design", "Essentials for handling images", "Fundamentals of Programming", "Automating Spreadsheets", "Automating Google Workspace", "Automate using Python", "Visualizing Data", "Cloud Literacy"],
        "Hours": [15, 15, 15, 15, 15, 15, 15, 15, 15]
    })
    
    st.subheader("Newly Added Courses")
    st.table({
        "Level": ["ESSENTIALS", "ESSENTIALS", "ENTERPRISE"],
        "Course Code": ["CSC988", "CSC998", "CSC999"],
        "Course Name": ["Cybersecurity Essentials", "AI Essentials", "GENERATIVE AI"],
        "Hours": [15, 15, 15]
    })

def train_the_trainers_tab():
    st.header("Train the Trainers Session")
    st.write("Session Overview: July 1st 2024 (1st Batch), August 1st 2024 (2nd Batch)")
    st.write("Purpose: To improve teaching methodologies and enhance faculty expertise")
    st.write("Outcomes:")
    st.write("- Improved teaching methodologies")
    st.write("- Enhanced faculty expertise")

def feedback_and_plans_tab():
    st.header("Feedback and Plans for Improvement")
    st.subheader("Last Year's Achievements")
    st.write("- Successful completion of AY 2023-24 with more than 1500 student accomplishments")
    st.write("- Consistent student engagement and feedback")
    st.write("- Completion rates above 95%")
    
    st.subheader("Suggestions for Improvement")
    suggestions = [
        "Enhance the course with more practical-driven sessions",
        "Increase elaboration on topics",
        "Tailor the course content to be more specific to the field",
        "Introduce more workshops and interactive activities",
        "Foster more interaction between the instructor and students",
        "Teach digital courses that can bring up finance, calculation of figures, and analysis",
        "Emphasize integration or relevance of coding with finance",
        "Add more new and complex topics",
        "Include interactive videos and practical classes"
    ]
    for suggestion in suggestions:
        st.write(f"- {suggestion}")

def csa_activities_tab():
    st.header("CSA Activities Planned")
    
    st.subheader("Collaborations with Sightsavers")
    st.write("Objective: Support and empower physically and visually challenged students")
    st.write("Activities:")
    st.write("- Specialized digital literacy programs")
    st.write("- Assistive technology training")
    st.write("- Inclusive education resources")
    
    st.subheader("Digital Literacy for Villages/Govt. Schools")
    st.write("Objective: Educate villagers with basic digital literacy")
    st.write("Activities:")
    st.write("- Introduction to digital devices")
    st.write("- Basic internet skills")
    st.write("- Using digital tools for daily tasks")
    st.write("- Training on creating simple business plans")
    st.write("- Digital marketing basics")
    st.write("- Online business opportunities")

def class_structure_tab():
    st.header("Class Structure and Guidelines")
    st.write("Total Duration: 30 hours of Digital Mission classes")
    st.write("Course Distribution:")
    st.write("- 15 hours for Essentials")
    st.write("- 15 hours for Enterprise or Two Essential courses")
    
    st.subheader("Class Conduct Guidelines")
    guidelines = [
        "Be strict about attendance",
        "Insist students bring laptops to every class",
        "Address disciplinary issues promptly",
        "Foster a positive and respectful classroom environment",
        "Monitor student progress and provide timely assistance",
        "Start and end classes on time",
        "Be interactive",
        "Provide domain-specific examples",
        "Give simple explanations and complex problems to solve",
        "Adapt teaching methods to suit diverse learning styles",
        "Regularly update students on their progress",
        "Foster a culture of continuous learning and improvement",
        "Conduct regular recap sessions to reinforce learning"
    ]
    for guideline in guidelines:
        st.write(f"- {guideline}")

if __name__ == "__main__":
    main()