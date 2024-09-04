import streamlit as st

# Title of the Course
st.title("PyGene: Python for Genomics with Python Basics")

# Section 1: Difference Between Languages and Programming Languages
st.header("1. Difference Between Languages and Programming Languages")

st.write("""
**Human Languages** are systems of communication used by humans. They can be spoken, written, or signed and are used to convey thoughts, ideas, emotions, and information.

Key characteristics of human languages include:
- Grammar, syntax, and vocabulary
- They allow for natural communication between humans
- Examples include: English, Hindi, Tamil, etc.

**Programming Languages**, on the other hand, are formal languages used to communicate with computers. These languages consist of instructions designed to produce various outputs and perform specific tasks.

Key characteristics of programming languages include:
- Strict syntax and rules
- Used for computational tasks
- Examples include: Python, Java, C++, and JavaScript
""")

# Section 2: Introduction to Python
st.header("2. Introduction to Python")

st.write("""
**Python** is an interpreted, high-level, general-purpose programming language created by Guido van Rossum and first released in 1991. Python is known for its simplicity, readability, and versatility, making it one of the most popular languages for beginners and professionals alike.

### Key Features of Python:
- Easy-to-understand syntax that is similar to plain English
- Extensive standard library and ecosystem of third-party libraries
- Wide usage in areas such as web development, data science, artificial intelligence, and genomics

Python's flexibility and ease of use have made it an industry standard for scientific research and data analysis, particularly in the field of genomics.
""")

# Expandable section for Python's name origin
with st.expander("Why is Python called Python?"):
    st.write("""
    Python is named after the British comedy show 'Monty Python's Flying Circus.' Guido van Rossum, the creator of Python, was a fan of the show and chose the name because it was short, unique, and slightly mysterious.
    """)

# Section 3: Python Installation and Setup
st.header("3. Python Installation and Setup")

st.write("""
To start writing Python programs, the first step is to install Python on your system and set up a suitable development environment.
""")

# Using radio buttons to present a step-by-step installation guide in a structured format
installation_step = st.radio("Python Installation Steps:", 
                             ["Step 1: Download Python", "Step 2: Install Visual Studio Code", "Step 3: Verify Installation", "Step 4: Create a Python File"])

if installation_step == "Step 1: Download Python":
    st.write("""
    1. Visit the official Python website: [python.org](https://www.python.org).
    2. Download the latest version of Python compatible with your operating system (Windows, macOS, or Linux).
    3. Follow the installation instructions provided on the website.
    """)
elif installation_step == "Step 2: Install Visual Studio Code":
    st.write("""
    1. Download Visual Studio Code (VS Code) from the official site: [code.visualstudio.com](https://code.visualstudio.com).
    2. Install VS Code on your system by following the installation instructions.
    3. Open VS Code and install the Python extension for an enhanced coding experience.
    """)
elif installation_step == "Step 3: Verify Installation":
    st.write("""
    1. Open a terminal (or command prompt).
    2. Type the following command to check if Python is installed correctly:
    ```
    python --version
    ```
    3. The terminal should display the installed Python version, confirming that Python has been successfully installed.
    """)
elif installation_step == "Step 4: Create a Python File":
    st.write("""
    1. Open VS Code and create a new file with the `.py` extension (e.g., `hello.py`).
    2. Write a simple Python program, such as:
    ```
    print("Hello, World!")
    ```
    3. Save the file and run it to verify that your Python environment is correctly set up.
    """)

# Section 4: Choosing an Editor for Python Development
st.header("4. Choosing an Editor for Python Development")

st.write("""
To write Python programs efficiently, you need a code editor or Integrated Development Environment (IDE). Below are some popular options:
""")

# Dropdown for selecting a Python editor
editor_choice = st.selectbox("Select a Python Editor to Learn More:", 
                             ["IDLE", "VS Code", "PyCharm", "Jupyter Notebook"])

if editor_choice == "IDLE":
    st.write("""
    **IDLE**: This is the default editor that comes with Python. It is a simple and lightweight editor, ideal for beginners working on small projects.
    """)
elif editor_choice == "VS Code":
    st.write("""
    **Visual Studio Code (VS Code)**: A lightweight but powerful code editor that supports multiple languages, including Python. It is widely used due to its flexibility and support for extensions that enhance the coding experience.
    """)
elif editor_choice == "PyCharm":
    st.write("""
    **PyCharm**: A full-featured, professional IDE for Python development. It is widely used by developers working on large-scale projects due to its powerful features and advanced tools.
    """)
elif editor_choice == "Jupyter Notebook":
    st.write("""
    **Jupyter Notebook**: An open-source web application widely used in data science and scientific research. It allows users to create and share documents that contain live code, equations, visualizations, and explanatory text.
    """)

# Section 5: Python Libraries for Genomics
st.header("5. Python Libraries for Genomics")

st.write("""
Python has an extensive collection of libraries that enhance its capabilities in various domains, including genomics. Below are some key libraries that are widely used in the field of genomics and data science:
""")

# Multiselect for selecting libraries to learn more about
selected_libraries = st.multiselect("Select Libraries to Learn About:", 
                                    ["NumPy", "Pandas", "BioPython", "Matplotlib", "Streamlit", "Tkinter"])

if "NumPy" in selected_libraries:
    st.write("""
    **NumPy**: A fundamental package for numerical computing in Python. It provides support for large multidimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
    """)
if "Pandas" in selected_libraries:
    st.write("""
    **Pandas**: A powerful data manipulation and analysis library. It provides data structures such as Series and DataFrames, which make handling structured data intuitive and efficient.
    """)
if "BioPython" in selected_libraries:
    st.write("""
    **BioPython**: A set of tools for biological computation. It provides functionalities to work with sequences, perform genome analysis, and read various biological file formats.
    """)
if "Matplotlib" in selected_libraries:
    st.write("""
    **Matplotlib**: A 2D plotting library used for creating static, animated, and interactive visualizations in Python. It is especially useful for scientific data visualization.
    """)
if "Streamlit" in selected_libraries:
    st.write("""
    **Streamlit**: A framework for building interactive web applications. It allows data scientists and machine learning engineers to quickly build and deploy web applications for their models and analyses.
    """)
if "Tkinter" in selected_libraries:
    st.write("""
    **Tkinter**: The standard Python interface to the Tk GUI toolkit. It is used for creating graphical user interface (GUI) applications.
    """)

# Section 6: Writing Your First Python Program
st.header("6. Writing Your First Python Program")

st.write("""
Let’s write and run your first Python program. Below is the code for a simple program that prints a message to the screen:
""")

# Displaying Python code
st.code("""
# This is your first Python program
print("Hello, World!")
""", language="python")

st.write("""
1. Open your chosen editor (e.g., VS Code).
2. Create a new file and name it `hello.py`.
3. Copy the code above into your file.
4. Run the file to see the output: `Hello, World!`
""")

# Section 7: Summary
st.header("Summary")

st.write("""
In this module, we have covered:
1. The difference between human languages and programming languages.
2. An introduction to Python and its key features.
3. Step-by-step instructions for installing Python and setting up your development environment.
4. Various editors for Python development and their use cases.
5. Important Python libraries for genomics and scientific computing.
6. Writing and running your first Python program.
""")
