import streamlit as st
import pandas as pd

# Helper function to generate the attendance slip
def generate_attendance_slip(attendance_type, date, teacher_code, class_name, time, subject_name, start_reg_no, absentees_list):
    slip = f"""
    Attendance Type: {attendance_type}
    Date: {date}
    Teacher's Code: {teacher_code}
    Class: {class_name}
    Time: {time}
    Subject Name: {subject_name}
    Starting Register Number: {start_reg_no}
    Absentees List: {absentees_list}
    """
    return slip

# Main Application
def main():
    st.sidebar.title("Navigation")
    tab = st.sidebar.radio("Go to", [
        "Digital Mission 2024 Program", 
        "Newly Added Courses and Syllabus", 
        "AI Essentials Material- Unit I (Theory)", 
        "AI Essentials Material- Unit I (Practical)",
        "Attendance",
        "Useful Links"
    ])

    if tab == "Digital Mission 2024 Program":
        digital_mission_2024_program()
    elif tab == "Newly Added Courses and Syllabus":
        newly_added_courses_tab()
    elif tab == "AI Essentials Material- Unit I (Theory)":
        ai_essentials_material_tab()
    elif tab == "AI Essentials Material- Unit I (Practical)":
         ai_essentials_practical_tab()
    elif tab == "Attendance":
        attendance_tab()
    elif tab == "Useful Links":
        display_links()

# Function definitions
def digital_mission_2024_program():
    st.title("Digital Mission 2024 Program")
    tabs = st.tabs([
        "Overview",
        "Courses",
        "Feedback & Plans",
        "Social Activities",
        "Class Structure", 
        "Trainers Schedule"
    ])

    with tabs[0]:
        overview_tab()
        train_the_trainers_tab()
    with tabs[1]:
        courses_tab()
    with tabs[2]:
        feedback_and_plans_tab()
    with tabs[3]:
        csa_activities_tab()
    with tabs[4]:
        class_structure_tab()
    with tabs[5]:
        faculty()

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

def faculty():
    pass
def display_links():
    st.header("Useful Links")
    st.subheader("Batch-1 Schedule")
    st.markdown("[Batch-1 Schedule](https://docs.google.com/document/d/1I1jIiy-y1SsyF-xFr-KyAl-k7GL6fS1e/edit?usp=sharing&ouid=109717452376599156061&rtpof=true&sd=true)")
    st.subheader("Course contents (Old)")
    st.markdown("[Course contents (Old)](https://drive.google.com/file/d/1m06TR37VW0m-9oF_GNBu4g6f-XK6Eta7/view?usp=drive_link)")
    st.subheader("Course contents (New)")
    st.markdown("[Course contents (New)](https://drive.google.com/file/d/1Vy4MacXOsR75xC9kOxfZU2R3JcGxKI4T/view?usp=drive_link)")
    st.subheader("Day-1 Orientation Slide")
    st.markdown("[Orientation Slides](https://docs.google.com/presentation/d/1hNDKo4M6nXC1OwZJD7fspOWc1S6DPE2m/edit?usp=drive_link&ouid=105423989768943296319&rtpof=true&sd=true)")
    st.subheader("Cloud Literacy- Materials")
    st.markdown("[Unit-1](https://docs.google.com/presentation/d/1oVTTE40gptVj6aGuTBEVMqlvmCX7i0MD/edit?usp=drive_link&ouid=105423989768943296319&rtpof=true&sd=true)")
    st.subheader("Class Activities/ Labs")
    st.markdown("[Cloud Literacy - Activities](https://drive.google.com/drive/folders/1JySsRUX_EkqerHvP2-zShHusKetK9unW?usp=drive_link)")
    st.subheader("Cybersecurity Essentials")
    st.markdown("[Cybersecurity Mindfulness](https://docs.google.com/presentation/d/1nvX2MeZu7mMc5Vvb6G-ePR5oM7JD-Sbs/edit?usp=drive_link&ouid=105423989768943296319&rtpof=true&sd=true)")
    st.subheader("Cybersecurity Lab")
    st.markdown("[Lab Program-1](https://docs.google.com/document/d/1KjdFik4_cTA0yobxzyJ03yQ0UZErB8WC/edit?usp=drive_link&ouid=105423989768943296319&rtpof=true&sd=true)")

def newly_added_courses_tab():
    st.title("Newly Added Courses and Syllabus")

    st.markdown("""
    **CS192 – FUNDAMENTALS OF PROGRAMMING**

    [Click here to view syllabus](https://drive.google.com/file/d/1pm9QxIvBnqlVVU5WTv-g4GfBcVkI1tp_/view?usp=drive_link)

    **CS194 – AI ESSENTIALS**

    [Click here to view syllabus](https://drive.google.com/file/d/11yQbxN2AtUcE-LoOy1uo57ReEbA-ULrs/view?usp=drive_link)
    """)

def ai_essentials_material_tab():
    st.title("AI Essentials Materials")

    # UNIT 1: Introduction to Artificial Intelligence
    st.header("UNIT 1: Introduction to Artificial Intelligence")

    st.subheader("Introduction and History of AI")
    st.markdown("""
    Artificial Intelligence (AI) is the branch of computer science that aims to create machines capable of performing tasks that would typically require human intelligence. The concept of AI dates back to the 1950s when Alan Turing proposed the idea of a machine that could simulate any human reasoning process. Over the decades, AI has evolved from simple rule-based systems to complex machine learning models that can perform tasks like image recognition, natural language processing, and even playing complex games.

    **History of AI**:
    - **1950s**: Alan Turing introduces the Turing Test, a measure of a machine's ability to exhibit intelligent behavior.
    - **1960s**: Development of the first AI programs like ELIZA, which could mimic human conversation.
    - **1980s**: Introduction of machine learning, allowing computers to learn from data.
    - **2000s**: Breakthroughs in deep learning and neural networks, enabling AI to perform tasks like image and speech recognition with high accuracy.
    """)

    st.subheader("What is AI? Overview and Scope")
    st.markdown("""
    Artificial Intelligence refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. AI can be classified into two broad categories:

    - **Narrow AI**: AI systems that are designed to perform a narrow task (e.g., facial recognition, internet searches).
    - **General AI**: AI systems that possess the ability to perform any intellectual task that a human can do (still theoretical).

    **Example**: 
    A virtual assistant like Siri or Google Assistant is an example of Narrow AI. It can perform specific tasks like setting reminders, answering queries, or playing music.

    **Case Study**:
    AI is used in personalized recommendation systems, such as those used by Netflix or Amazon. These systems analyze user behavior and preferences to suggest movies or products that a user is likely to enjoy.
    """)

    st.subheader("Key Techniques in AI: Machine Learning and Deep Learning")
    st.markdown("""
    **Machine Learning**:
    Machine Learning (ML) is a subset of AI that enables a machine to automatically learn from past data without programming it explicitly. ML focuses on the development of algorithms that can analyze and learn from data to make decisions or predictions.

    **Example**:
    A spam email filter is a simple example of ML. The filter learns from a dataset of emails labeled as spam or not spam and then uses this knowledge to classify new emails.

    **Deep Learning**:
    Deep Learning is a subfield of machine learning that deals with neural networks with many layers (hence "deep"). It is particularly effective in tasks like image and speech recognition.

    **Example**:
    Image recognition systems, such as those used by Google Photos, can automatically tag people in photos by learning to recognize their faces.

    **Case Study**:
    **AI in Healthcare**: IBM Watson for Oncology uses AI and machine learning to help oncologists develop treatment plans for cancer patients. Watson analyzes large amounts of data from medical literature, patient records, and clinical trials to recommend treatment options.
    """)

    st.subheader("Real-World Applications of AI")
    st.markdown("""
    AI has a wide range of applications across various industries:

    - **Healthcare**: AI is used for predictive analytics, diagnostics, and personalized medicine.
    - **Finance**: AI algorithms are used for fraud detection, trading, and risk management.
    - **Transportation**: Self-driving cars and traffic management systems rely on AI for decision-making.
    - **Entertainment**: AI powers recommendation engines in platforms like Netflix and Spotify.

    **Example**:
    AI is used in predictive maintenance for industrial equipment. By analyzing sensor data, AI can predict when a machine is likely to fail, allowing for timely maintenance and reducing downtime.

    **Case Study**:
    **Self-Driving Cars**: Companies like Tesla use AI for autonomous driving. The AI systems in these cars process data from cameras, radar, and other sensors to make real-time driving decisions.
    """)

    st.subheader("Example: Basic Python Program to Simulate a Simple Decision-Making Process")
    st.code("""
def simple_decision_making(weather):
    if weather == 'sunny':
        return 'Go for a walk'
    elif weather == 'rainy':
        return 'Stay indoors'
    else:
        return 'Check the weather again'

# Example usage
decision = simple_decision_making('sunny')
print(decision)  # Output: Go for a walk
    """, language="python")

    st.markdown("""
    This simple Python program simulates a basic decision-making process. Based on the input (weather), it returns a suggestion for an activity.
    """)

    st.subheader("Case Study: Application of AI in Healthcare (IBM Watson)")
    st.markdown("""
    **IBM Watson for Oncology**:
    IBM Watson is an AI platform that assists oncologists in developing treatment plans for cancer patients. Watson analyzes large datasets from medical literature, clinical trials, and patient records to provide evidence-based treatment options. The AI system is designed to augment the decision-making process by offering insights that might not be immediately apparent to human doctors. This application of AI helps in making more informed treatment decisions, potentially leading to better patient outcomes.
    """)
# AI Essentials Material - Unit I (Practical)
def ai_essentials_practical_tab():
    st.title("AI Essentials Materials - Unit I (Practical)")

    # Python Basics
    st.header("Python Basics")

    st.subheader("Hello World Program")
    st.code("""
# Hello World Program in Python
print("Hello, World!")
    """, language="python")
    st.markdown("""
    This is the simplest Python program that prints "Hello, World!" to the screen. It's often the first program beginners write when learning a new programming language.
    """)

    st.subheader("Variables and Data Types")
    st.code("""
# Variables and Data Types in Python
name = "John Doe"
age = 25
height = 5.9
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")
    """, language="python")
    st.markdown("""
    Python allows you to store different types of data in variables, such as strings, integers, floats, and booleans. The `f` string is used to format the output.
    """)

    st.subheader("Basic Input and Output")
    st.code("""
# Input and Output in Python
name = input("Enter your name: ")
print(f"Hello, {name}!")
    """, language="python")
    st.markdown("""
    This program takes input from the user and then prints a greeting message. The `input()` function is used to capture user input as a string.
    """)

    # AI-Related Libraries Introduction
    st.header("Introduction to AI-Related Libraries")

    st.subheader("Installing and Importing Libraries")
    st.code("""
# Installing AI Libraries
# Run these commands in your terminal or command prompt
!pip install numpy
!pip install pandas
!pip install scikit-learn
!pip install tensorflow

# Importing Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
    """, language="python")
    st.markdown("""
    This code snippet shows how to install and import essential AI-related libraries:
    
    - **Numpy**: For numerical operations.
    - **Pandas**: For data manipulation and analysis.
    - **Scikit-learn**: For machine learning algorithms.
    - **TensorFlow**: For deep learning models.
    """)

    # Interactive Program: Simple Decision Making
    st.header("Simple Interactive Program: Decision Making")
    st.code("""
def simple_response_system(user_input):
    if user_input.lower() == "hello":
        return "Hi there!"
    elif user_input.lower() == "how are you?":
        return "I'm doing great, thank you!"
    elif user_input.lower() == "bye":
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

# Example Usage
user_input = input("Say something to the AI: ")
response = simple_response_system(user_input)
print(response)
    """, language="python")
    st.markdown("""
    This program simulates a simple interaction where the AI responds based on the user's input. The `simple_response_system` function checks the input and returns a corresponding response.
    """)

    st.subheader("AI in Action: Basic Data Handling")
    st.code("""
# Basic Data Handling with Pandas
import pandas as pd

# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22],
    "Score": [88, 92, 85]
}

df = pd.DataFrame(data)

# Display DataFrame
print(df)

# Example: Filter students with a score above 85
high_scorers = df[df["Score"] > 85]
print(high_scorers)
    """, language="python")
    st.markdown("""
    This example demonstrates how to create and manipulate data using the Pandas library. The code creates a DataFrame with student names, ages, and scores, and then filters out students with scores above 85.
    """)

    st.subheader("Simple AI Example: Linear Regression with Scikit-learn")
    st.code("""
from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict
predictions = model.predict(X)
print("Predictions:", predictions)
    """, language="python")
    st.markdown("""
    This basic AI example uses Scikit-learn's `LinearRegression` model to fit a simple dataset. The model is trained on the data and then used to make predictions. This example helps students understand how a basic AI model works.
    """)
def attendance_tab():
    st.title("Extraordinary Attendance Entry")
    attendance_type = st.selectbox("Type of Attendance", ["Regular", "Extraordinary"])
    date = st.date_input("Date")
    teacher_code = "4116"
    class_name = st.selectbox("Class", [
        "I BBA FIB A", "I BBA FIB B", "SBA A", "SBA B", "BBA Tourism", 
        "BBA F&E", "1 BCom FI A", "1 BCom FI B", "1 BCOM A", "1 BCOM B", 
        "1 BCOM C", "1 BCOM D", "1 BCOM F", "1 BCOM AT", "1 BCOM AFA", 
        "1 BCOM SFH"
    ])
    time = st.time_input("Class Time")
    subject_name = st.selectbox("Subject Name", ["cs192-Fundamentals of Programming", "cs194 - AI Essentials"])
    start_reg_no = st.text_input("Starting Register Number")
    absentees_list = st.text_area("Absentees List (comma-separated)")
    
    if st.button("Generate Attendance Slip"):
        slip = generate_attendance_slip(attendance_type, date, teacher_code, class_name, time, subject_name, start_reg_no, absentees_list)
        st.success("Attendance slip generated.")
        st.download_button("Download Slip", slip, file_name="attendance_slip.pdf")

if __name__ == "__main__":
    main()