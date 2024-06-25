import streamlit as st

def python_fundamentals():
    st.header("Python Fundamentals")
    st.write("""
    **Python Fundamentals** covers the basic concepts and features of the Python programming language, including:
    
    - **Syntax and Semantics:** Python uses indentation to define code blocks, making it easy to read and write.
    - **Variables and Data Types:** Python supports various data types like integers, floats, strings, lists, tuples, and dictionaries.
    - **Control Structures:** Python includes standard control structures like if statements, for and while loops, and error handling with try/except blocks.
    - **Functions and Modules:** Python allows for the creation of reusable code through functions and modularity through modules and packages.
    - **Standard Library:** Python comes with a rich standard library that includes modules for regular expressions, file I/O, threading, and more.
    """)

def features_of_python():
    st.header("Features of Python")
    st.write("""
    **Features of Python** include several characteristics that make Python a powerful and popular programming language:
    
    - **Simple and Easy to Learn:** Python's syntax is clear and readable, making it an excellent language for beginners.
    - **Interpreted Language:** Python code is executed line by line, which makes debugging easier and faster.
    - **Dynamically Typed:** Python does not require explicit declaration of data types; the interpreter infers the type at runtime.
    - **High-Level Language:** Python abstracts many complex details of the computer, making it easier to write complex programs.
    - **Extensive Libraries and Frameworks:** Python has a vast ecosystem of libraries and frameworks for various tasks, such as web development (Django, Flask), data science (Pandas, NumPy), machine learning (TensorFlow, scikit-learn), and more.
    - **Portability:** Python code can run on any machine with a Python interpreter, making it highly portable across different operating systems.
    """)

def components_of_python_program():
    st.header("Components of a Python Program")
    st.write("""
**Components of a Python Program** consist of various elements that work together to form a complete Python application:
    
    - **Modules:** Files containing Python code that can be imported and used in other Python scripts. Modules help in organizing code logically.
    - **Statements and Expressions:** Basic building blocks of a Python program. Statements perform actions, and expressions evaluate to values.
    - **Functions:** Defined using the `def` keyword, functions encapsulate reusable blocks of code.
    - **Classes and Objects:** Python supports object-oriented programming with classes and objects, allowing for the creation of complex data structures and behavior.
    - **Exception Handling:** Python uses `try`, `except`, `finally`, and `else` blocks to handle errors gracefully.
    - **Comments and Docstrings:** Comments (`#`) and docstrings (`" " "`) are used to document the code, making it more readable and maintainable.
    - **Input/Output:** Python provides functions like `print()` for output and `input()` for taking user input, along with more advanced I/O operations using file handling.
""")

def understanding_the_interpreter():
    st.header("Understanding the Interpreter")
    st.write("""
    **Understanding the Interpreter** involves knowing how Python code is executed:
    
    - **Execution Process:** Python code is executed by the Python interpreter, which reads the source code, compiles it to bytecode, and then executes it.
    - **Interactive Mode:** The interpreter can be used in interactive mode, where commands are executed one at a time, useful for testing and debugging.
    - **Script Mode:** Python code can be written in files (scripts) and executed all at once, which is useful for larger programs.
    - **Virtual Environments:** The interpreter supports virtual environments, allowing for the management of dependencies for different projects without conflicts.
    - **Python Versions:** Different versions of the Python interpreter (e.g., Python 2.x vs. Python 3.x) may have differences in syntax and behavior, so it’s important to use the appropriate version for your code.
    """)

def python_basics():
    st.header("PYTHON BASICS: Identifiers, Basic Types")
    st.write("""
    **Python Basics: Identifiers, Basic Types** covers the fundamental building blocks of Python programming:
    
    - **Identifiers:** Names used to identify variables, functions, classes, modules, and other objects. Rules for identifiers include:
        - Must start with a letter (A-Z, a-z) or an underscore (_).
        - Can be followed by letters, digits (0-9), or underscores.
        - Case-sensitive (e.g., `myVariable` and `myvariable` are different).
        - Cannot be a reserved keyword (e.g., `if`, `else`, `while`).
    
    - **Basic Types:** The core data types in Python include:
        - **Integers (`int`):** Whole numbers without a fractional component (e.g., `42`, `-3`).
        - **Floats (`float`):** Numbers with a fractional component (e.g., `3.14`, `-0.001`).
        - **Strings (`str`):** Immutable sequences of characters (e.g., `"hello"`, `'world'`).
        - **Booleans (`bool`):** Represents `True` or `False`.
        - **Lists (`list`):** Ordered, mutable collections of items (e.g., `[1, 2, 3]`).
        - **Tuples (`tuple`):** Ordered, immutable collections of items (e.g., `(1, 2, 3)`).
        - **Dictionaries (`dict`):** Unordered, mutable collections of key-value pairs (e.g., `{'a': 1, 'b': 2}`).
        - **Sets (`set`):** Unordered collections of unique items (e.g., `{1, 2, 3}`).
    """)

def addition_basic_python():
    st.subheader("Simple Addition Program without GUI (Basic Python)")

    code_basic_python = """
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
    """

    st.code(code_basic_python, language='python')

def addition_with_tkinter():
    st.subheader("Simple Addition Program with Tkinter GUI")

    code_tkinter = """
import tkinter as tk
root = tk.Tk()
root.title("Simple Addition Program")
def add_numbers():
    num1 = float(entry_a.get())
    num2 = float(entry_b.get())
    result = num1 + num2
    result_label.config(text=f"The sum is: {result}")

label_a = tk.Label(root, text="Enter number a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()
label_b = tk.Label(root, text="Enter number b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

button_add = tk.Button(root, text="Add Numbers", command=add_numbers)
button_add.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

    """

    st.code(code_tkinter, language='python')

def addition_with_streamlit():
    st.subheader("Simple Addition Program with Streamlit")

    code_streamlit = """
import streamlit as st

st.title("Simple Addition Program with Streamlit")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

st.button("Add Numbers")
result = num1 + num2
st.success(f"The sum of {num1} and {num2} is: {result}")
    """

    st.code(code_streamlit, language='python')

# Streamlit app layout
st.title("Python Programming Guide")

st.sidebar.title("Week-2: Navigation")
option = st.sidebar.radio("Go to", ('Python Fundamentals', 'Features of Python', 'Components of a Python Program', 'Understanding the Interpreter', 'Identifiers, Basic Types', 'Experiential Learning: Program-2'))

if option == 'Python Fundamentals':
    python_fundamentals()
elif option == 'Features of Python':
    features_of_python()
elif option == 'Components of a Python Program':
    components_of_python_program()
elif option == 'Understanding the Interpreter':
    understanding_the_interpreter()
elif option == 'Identifiers, Basic Types':
    python_basics()
elif option == 'Experiential Learning: Program-2':
    addition_basic_python()
    addition_with_tkinter()
    addition_with_streamlit()