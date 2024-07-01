import streamlit as st
import pandas as pd
def main():
    st.title("Digital Mission 2024 Program")

    tabs = st.tabs([
        "Overview",
        "Courses",
        "Feedback & Plans",
        "Social Activities",
        "Class Structure", 
        "Trainers Schedule",
        "Useful Links"
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
        time_tab()
    with tabs[6]:
        display_links()
    
        
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


# Data for the schedule
data_commerce = [
    {"Class": "III BCom FI A", "Room No": "4506, 5TH FLOOR, BLOCK IV", "Schedule": "Monday 10:30 AM to 11:30 AM", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Shravan K (4MDA)"},
    {"Class": "III BCom FI A", "Room No": "4506, 5TH FLOOR, BLOCK IV", "Schedule": "Thursday 11:30 AM to 12:30 PM", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Shravan K (4MDA)"},
    {"Class": "III BCom FI B", "Room No": "4507, 5TH FLOOR, BLOCK IV", "Schedule": "Tuesday 10:30 AM to 11:30 AM", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Shravan K (4MDA)"},
    {"Class": "III BCom FI B", "Room No": "4507, 5TH FLOOR, BLOCK IV", "Schedule": "Friday 10:30 AM to 11:30 AM", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Shravan K (4MDA)"},
    {"Class": "III BCOM A", "Room No": "4607, 6TH FLOOR, BLOCK IV", "Schedule": "Wednesday 8:00 AM to 9:00 AM", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Priyadarsh P (5 CME)"},
    {"Class": "III BCOM A", "Room No": "4607, 6TH FLOOR, BLOCK IV", "Schedule": "Thursday 9:30 AM to 10:30 AM", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Priyadarsh P (5 CME)"},
    {"Class": "III BCOM B", "Room No": "4608, 6TH FLOOR, BLOCK IV", "Schedule": "Tuesday 8:00 AM to 9:00 AM", "Trainer-1": "Maanav (BCOM)", "Trainer-2": "Shalini Sosa (5 CME)"},
    {"Class": "III BCOM B", "Room No": "4608, 6TH FLOOR, BLOCK IV", "Schedule": "Wednesday 8:00 AM to 9:00 AM", "Trainer-1": "Maanav (BCOM)", "Trainer-2": "Shalini Sosa (5 CME)"},
    {"Class": "III BCOM C", "Room No": "4609, 6TH FLOOR, BLOCK IV", "Schedule": "Tuesday 9:30 AM to 10:30 AM", "Trainer-1": "Radhika (PhD Scholar)", "Trainer-2": "Meenu Hani (4 MDA)"},
    {"Class": "III BCOM C", "Room No": "4609, 6TH FLOOR, BLOCK IV", "Schedule": "Friday 10:30 AM to 11:30 AM", "Trainer-1": "Radhika (PhD Scholar)", "Trainer-2": "Meenu Hani (4 MDA)"},
    {"Class": "III BCOM D", "Room No": "4610, 6TH FLOOR, BLOCK IV", "Schedule": "Monday 11:30 AM to 12:30 AM", "Trainer-1": "Kiran Kumar", "Trainer-2": "Zainab Khan (5 CME)"},
    {"Class": "III BCOM D", "Room No": "4610, 6TH FLOOR, BLOCK IV", "Schedule": "Wednesday 8:00 AM to 9:00 AM", "Trainer-1": "Kiran Kumar", "Trainer-2": "Zainab Khan (5 CME)"},
    {"Class": "III BCOM F", "Room No": "726, 2ND FLOOR, BLOCK II", "Schedule": "Tuesday 8:00 AM to 9:00 AM", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Antoniette Figeredo (5 CME)"},
    {"Class": "III BCOM F", "Room No": "726, 2ND FLOOR, BLOCK II", "Schedule": "Thursday 8:00 AM to 9:00 AM", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Antoniette Figeredo (5 CME)"},
    {"Class": "III BCOM AT", "Room No": "4602, 6TH FLOOR, BLOCK IV", "Schedule": "Wednesday 9:30 AM to 10:30 AM", "Trainer-1": "Anjana (PhD Scholar)", "Trainer-2": "Nirupama L (4MDA)"},
    {"Class": "III BCOM AT", "Room No": "4602, 6TH FLOOR, BLOCK IV", "Schedule": "Thursday 11:30 AM to 12:30 PM", "Trainer-1": "Anjana (PhD Scholar)", "Trainer-2": "Nirupama L (4MDA)"},
    {"Class": "III BCOM AFA", "Room No": "4604, 6TH FLOOR, BLOCK IV", "Schedule": "Monday 2:30 PM to 3:30 PM", "Trainer-1": "Neha (PhD Scholar)", "Trainer-2": "Ahanya Mariam (6BCA)"},
    {"Class": "III BCOM AFA", "Room No": "4604, 6TH FLOOR, BLOCK IV", "Schedule": "Wednesday 9:30 AM to 10:30 AM", "Trainer-1": "Neha (PhD Scholar)", "Trainer-2": "Ahanya Mariam (6BCA)"},
    {"Class": "III SEM BCOM SFH", "Room No": "4412, 4TH FLOOR, BLOCK IV", "Schedule": "Thursday 11:30 AM to 12:30 PM", "Trainer-1": "Sushmitha R (4MDA)", "Trainer-2": "Arjun Ajithan (6BCA)"},
    {"Class": "III SEM BCOM SFH", "Room No": "4412, 4TH FLOOR, BLOCK IV", "Schedule": "Friday 10:30 AM to 11:30 AM", "Trainer-1": "Sushmitha R (4MDA)", "Trainer-2": "Arjun Ajithan (6BCA)"},
]

data_international_studies = [
    {"Class": "1 BAHP", "Module": "Google Workspace", "Schedule": "Tuesday 1:30 to 3:30 PM", "Trainer-1": "Kavaskar (4MCA)", "Trainer-2": "Sakshee Priya (6BCA)"},
    {"Class": "1 BAHP", "Module": "Google Workspace", "Schedule": "Friday 2:30 to 3:30 PM", "Trainer-1": "Kavaskar (4MCA)", "Trainer-2": "Sakshee Priya (6BCA)"},
    {"Class": "5 HEP", "Module": "Visualizing Data", "Schedule": "Thursday 2:30 to 3:30 PM", "Trainer-1": "Kalpana N (4MCA)", "Trainer-2": "Brito Jaison (6BCA)"},
    {"Class": "5 HEP", "Module": "Visualizing Data", "Schedule": "Friday 2:30 to 3:30 PM", "Trainer-1": "Kalpana N (4MCA)", "Trainer-2": "Brito Jaison (6BCA)"},
    {"Class": "3BAHP", "Module": "Visualizing Data", "Schedule": "Tuesday 10:30 to 12:30 PM", "Trainer-1": "Sushmitha R (4MDA)", "Trainer-2": "Jessica Shirley (4MDA)"},
    {"Class": "1MAIS", "Module": "Formulas and design", "Schedule": "Wednesday 2:30 to 3:30 PM", "Trainer-1": "Likitha Yadav G (4MCA)", "Trainer-2": "Nayana K Benny (6BCA)"},
    {"Class": "1MAIS", "Module": "Formulas and design", "Schedule": "Friday 2:30 to 3:30 PM", "Trainer-1": "Likitha Yadav G (4MCA)", "Trainer-2": "Nayana K Benny (6BCA)"},
    {"Class": "3MAIS", "Module": "Formulas and design", "Schedule": "Tuesday 11:30 to 12:30 PM", "Trainer-1": "Sujana (PhD Scholar)", "Trainer-2": "Nirupama L (4MDA)"},
    {"Class": "3MAIS", "Module": "Formulas and design", "Schedule": "Friday 10:30 to 11:30 AM", "Trainer-1": "Sujana (PhD Scholar)", "Trainer-2": "Nirupama L (4MDA)"},
]

data_psychology = [
    {"Class": "1BA PENG", "Module": "Digital Skills Essentials - Google Workspace", "Room No": "Room No.524, Ground Floor, Block 2", "Schedule": "Monday 11:30-12:30", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Amritha S Nair"},
    {"Class": "1BA PENG", "Module": "Digital Skills Essentials - Google Workspace", "Room No": "Room No.524, Ground Floor, Block 2", "Schedule": "Tuesday 2:30-3:30", "Trainer-1": "Gadhiya Shreya (MSc CSA)", "Trainer-2": "Amritha S Nair"},
    {"Class": "1BA PECO", "Module": "Digital Skills Essentials - Google Workspace", "Room No": "Room No.527, Ground Floor, Block 2", "Schedule": "Tuesday 2:30-3:30", "Trainer-1": "Arunoth Symen", "Trainer-2": "Shreyans Jain"},
    {"Class": "1BA PECO", "Module": "Digital Skills Essentials - Google Workspace", "Room No": "Room No.527, Ground Floor, Block 2", "Schedule": "Monday 2:30-3:30 PM", "Trainer-1": "Arunoth Symen", "Trainer-2": "Shreyans Jain"},
    {"Class": "3PENG", "Module": "Cybersecurity - Essentials", "Room No": "Room No.605, Ground Floor, Block 2", "Schedule": "Monday 10:30 - 11:30", "Trainer-1": "Jessica Shirley (4MDA)", "Trainer-2": "Nirupama L (4MDA)"},
    {"Class": "3PENG", "Module": "Cybersecurity - Essentials", "Room No": "Room No.605, Ground Floor, Block 2", "Schedule": "Tuesday 10:30-11:30", "Trainer-1": "Jessica Shirley (4MDA)", "Trainer-2": "Nirupama L (4MDA)"},
    {"Class": "3PECO", "Module": "Cybersecurity - Essentials", "Room No": "Room No.505, Ground Floor, Block 2", "Schedule": "Tuesday 10:30 - 11:30 AM", "Trainer-1": "Meenu Hani (4MDA)", "Trainer-2": "Aruna (4MDA)"},
    {"Class": "3PECO", "Module": "Cybersecurity - Essentials", "Room No": "Room No.505, Ground Floor, Block 2", "Schedule": "Wednesday 10:30 - 11:30", "Trainer-1": "Meenu Hani (4MDA)", "Trainer-2": "Aruna (4MDA)"},
]

data_education = [
    {"Class": "1 PG", "Module": "Digital Skills Essentials", "Schedule": "Saturday 8 to 10 AM", "Trainer-1": "Kiran", "Trainer-2": "Shubam"},
    {"Class": "2 PG", "Module": "Digital Skills Essentials", "Schedule": "Saturday 8 to 10 AM", "Trainer-1": "Alby", "Trainer-2": "Gavin"},
]

trainers_contact = [
    {"Name": "Dr. Vijay Arputhraj", "Contact": "+91 9677188654", "Remarks": "Coordinator/ In-charge"},
    {"Name": "Ms. Kaleeshwari", "Contact": "+91 87921 32388"},
    {"Name": "Ms. Gadhiya Shreya", "Contact": "+91 94284 06333"},
    {"Name": "Ms. Maanav", "Contact": "+91 6362 512 601"},
    {"Name": "Ms. Radhika", "Contact": ""},
    {"Name": "Ms. Anjana", "Contact": "+91 83018 73780"},
    {"Name": "Ms. Neha Singh", "Contact": "+91 83103 79475"},
    {"Name": "Mr. Kiran Kumar", "Contact": "+91 70226 41150"},
    {"Name": "Mr. Priyadarsh P", "Contact": "+91 79945 93685"},
    {"Name": "Ms. Shalini Sosa", "Contact": ""},
    {"Name": "Ms. Zainab Khan", "Contact": ""},
    {"Name": "Ms. Antoniette Figeredo", "Contact": ""},
    {"Name": "Ms. Ahanya Mariam", "Contact": ""},
    {"Name": "Mr. Arjun Ajithan", "Contact": ""},
]

# Combine all data into a single DataFrame
data = data_commerce + data_international_studies + data_psychology + data_education

df = pd.DataFrame(data)

# Create a function to generate the timetable for a specific trainer
def generate_timetable(trainer_name):
    timetable = df[(df["Trainer-1"].str.contains(trainer_name)) | (df["Trainer-2"].str.contains(trainer_name))]
    return timetable


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
    st.markdown("[Cloud  Literacy - Activities](https://drive.google.com/drive/folders/1JySsRUX_EkqerHvP2-zShHusKetK9unW?usp=drive_link)")



    

# Streamlit interface
def time_tab():
    st.title("Faculty Wise Timetable Generator")

    trainer_name = st.text_input("Enter the trainer's name:", "Gadhiya Shreya (MSc CSA)")
    
    if trainer_name:
        timetable = generate_timetable(trainer_name)
        st.write(f"Timetable for {trainer_name}:")
        st.table(timetable)
    else:
        st.write("Please enter a trainer's name to generate the timetable.")

    st.title("Trainers Contact Details")
    contact_df = pd.DataFrame(trainers_contact)
    st.table(contact_df)



if __name__ == "__main__":
    main()