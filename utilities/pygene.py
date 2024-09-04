import streamlit as st

# Title of the course
st.title("PyGene: Python for Genomics with Python Basics - Revision Quiz")

# Section 1: Quiz - Difference Between Languages and Programming Languages
st.header("1. Quiz: Understanding the Difference Between Languages and Programming Languages")

# Quiz Question 1
st.write("Question 1: Which of the following are examples of human languages?")
q1 = st.radio("Select the correct answer:", 
              ("Python", "Java", "English", "C++"), key="q1")

if q1:
    if q1 == "English":
        st.success("Correct! English is a human language.")
    else:
        st.error("Incorrect. English is the correct answer.")

# Quiz Question 2
st.write("Question 2: Which of the following best describes programming languages?")
q2 = st.radio("Select the correct answer:", 
              ("Used for communication between humans", 
               "Have grammar and vocabulary like natural languages", 
               "Used to give instructions to computers", 
               "Involves spoken and written communication"), key="q2")

if q2:
    if q2 == "Used to give instructions to computers":
        st.success("Correct! Programming languages are used to instruct computers.")
    else:
        st.error("Incorrect. Programming languages are used to give instructions to computers.")

# Section 2: Quiz - Introduction to Python
st.header("2. Quiz: Introduction to Python")

# Quiz Question 3
st.write("Question 3: What year was Python first released?")
q3 = st.radio("Select the correct answer:", 
              ("1991", "1989", "2000", "2015"), key="q3")

if q3:
    if q3 == "1991":
        st.success("Correct! Python was first released in 1991.")
    else:
        st.error("Incorrect. Python was first released in 1991.")

# Quiz Question 4
st.write("Question 4: Why is Python named 'Python'?")
q4 = st.radio("Select the correct answer:", 
              ("Named after the Python snake", 
               "Named after the British comedy show 'Monty Python's Flying Circus'", 
               "Named after its creator Guido van Rossum", 
               "Named to sound tech-savvy"), key="q4")

if q4:
    if q4 == "Named after the British comedy show 'Monty Python's Flying Circus'":
        st.success("Correct! Python is named after the comedy show.")
    else:
        st.error("Incorrect. Python is named after the British comedy show.")

# Section 3: Quiz - Python Installation and Setup
st.header("3. Quiz: Python Installation and Setup")

# Quiz Question 5
st.write("Question 5: Which command verifies the Python installation?")
q5 = st.radio("Select the correct answer:", 
              ("python --version", "python install", "python setup", "python check"), key="q5")

if q5:
    if q5 == "python --version":
        st.success("Correct! The command to verify Python installation is 'python --version'.")
    else:
        st.error("Incorrect. The correct command is 'python --version'.")

# Section 4: Quiz - Python Libraries
st.header("4. Quiz: Python Libraries for Genomics")

# Quiz Question 6
st.write("Question 6: Which Python library is specifically designed for biological computations?")
q6 = st.radio("Select the correct answer:", 
              ("NumPy", "Pandas", "BioPython", "Matplotlib"), key="q6")

if q6:
    if q6 == "BioPython":
        st.success("Correct! BioPython is used for biological computations.")
    else:
        st.error("Incorrect. The correct answer is BioPython.")

# Quiz Question 7
st.write("Question 7: Which library is used for data manipulation and analysis?")
q7 = st.radio("Select the correct answer:", 
              ("NumPy", "Pandas", "BioPython", "Matplotlib"), key="q7")

if q7:
    if q7 == "Pandas":
        st.success("Correct! Pandas is used for data manipulation and analysis.")
    else:
        st.error("Incorrect. The correct answer is Pandas.")

# Section 5: Writing Your First Python Program
st.header("5. Writing Your First Python Program")

# Quiz Question 8
st.write("Question 8: What is the output of the following Python program?")
st.code("""
print("Hello, World!")
""", language="python")

q8 = st.radio("Select the correct answer:", 
              ("Hello, Python!", "Hello, World!", "Python Program", "Error"), key="q8")

if q8:
    if q8 == "Hello, World!":
        st.success("Correct! The output of the program is 'Hello, World!'.")
    else:
        st.error("Incorrect. The correct output is 'Hello, World!'.")

# Final Section: Summary
st.header("Summary")
st.write("""
- We revised the difference between languages and programming languages.
- We explored Python, its origin, and its installation.
- We discussed Python libraries used in genomics.
- We wrote a simple Python program and learned about its output.
""")
