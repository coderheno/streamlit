import streamlit as st
from functools import reduce

# Set page configuration
st.set_page_config(page_title="Unit 5 - Functional Programming ", page_icon=":computer:")

# Custom module example - a simple math module to import later
def math_module():
    st.code("""
    # File: mymathmodule.py
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y if y != 0 else "Division by zero!"
    """, language="python")

# Page Title and Introduction
st.title("Functional Programming - Unit 5")
st.markdown("### Welcome to your interactive ICT tool for learning Functional Programming!")
st.write("This tool is designed to help first-time learners understand key concepts related to Lambda functions, Higher-order functions, Map, Filter, Reduce, and Modules, Packages, and Namespaces.")

# Navigation Bar
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Lecture", "Activities", "Programs", "Calculator", "Domain-Based Calculator", "Additional Resources"])

# Lecture Section
if section == "Lecture":
    st.header("Lecture: Functional Programming Concepts")

    st.subheader("1. Lambda Functions")
    st.write("""
    A **lambda function** is a small anonymous function defined with the keyword `lambda`. It can take any number of arguments, but only one expression.
    **Example:**
    ```python
    add = lambda x, y: x + y
    print(add(2, 3))  # Output: 5
    ```
    """)

    st.subheader("2. Higher-Order Functions")
    st.write("""
    A **higher-order function** is a function that takes another function as an argument or returns a function.
    **Example:**
    ```python
    def apply_func(func, x):
        return func(x)

    def square(n):
        return n * n

    result = apply_func(square, 5)
    print(result)  # Output: 25
    ```
    """)

    st.subheader("3. Map, Filter, Reduce")
    st.write("""
    **Map** applies a function to each item in an input list.
    **Example:**
    ```python
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16]
    ```

    **Filter** extracts elements from a list that satisfy a given condition.
    **Example:**
    ```python
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # Output: [2, 4, 6]
    ```

    **Reduce** applies a rolling computation to sequential pairs in a list.
    **Example:**
    ```python
    from functools import reduce
    numbers = [1, 2, 3, 4]
    result = reduce(lambda x, y: x * y, numbers)
    print(result)  # Output: 24
    ```
    """)

    st.subheader("4. Modules, Packages, and Namespaces")
    st.write("""
    - A **module** is a file containing Python code that defines functions, classes, and variables.
    - A **package** is a collection of modules.
    - **Namespace** is a space that holds the mapping between names and objects.

    **Example of importing a module:**
    ```python
    import math
    print(math.sqrt(16))  # Output: 4.0
    ```
    """)

# Activities Section
elif section == "Activities":
    st.header("Activities")

    st.subheader("Activity 1: Lambda Function")
    st.write("""
    Create a lambda function that multiplies two numbers and test it with different values.
    """)

    st.subheader("Activity 2: Higher-Order Function")
    st.write("""
    Write a higher-order function that applies any function passed to it, and test it with a function that returns the cube of a number.
    """)

    st.subheader("Activity 3: Map, Filter, and Reduce")
    st.write("""
    - Use **map()** to convert a list of numbers into their cubes.
    - Use **filter()** to extract only the odd numbers from a list.
    - Use **reduce()** to find the sum of all numbers in a list.
    """)

# Programs Section
elif section == "Programs":
    st.header("Programs")

    st.subheader("Example 1: Lambda Function for Addition")
    st.code("""
    # Lambda function to add two numbers
    add = lambda x, y: x + y
    print(add(10, 20))  # Output: 30
    """, language='python')

    st.subheader("Example 2: Map, Filter, and Reduce with Lambda")
    st.code("""
    # Map example: Square of numbers
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, numbers))
    print(squared_numbers)

    # Filter example: Even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

    # Reduce example: Product of numbers
    from functools import reduce
    product = reduce(lambda x, y: x * y, numbers)
    print(product)
    """, language='python')

    st.subheader("Example 3: Creating and Importing a Module")
    st.code("""
    # File: mymodule.py
    def greet(name):
        return f"Hello, {name}!"

    # Main program
    import mymodule
    print(mymodule.greet('Alice'))  # Output: Hello, Alice!
    """, language='python')

# Calculator Section
elif section == "Calculator":
    st.header("Lambda Calculator")
    st.write("This calculator uses **lambda functions** to perform basic arithmetic operations.")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0, step=0.1)
    num2 = st.number_input("Enter the second number", value=0.0, step=0.1)

    # Dropdown to select operation
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Lambda functions for the operations
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    multiply = lambda x, y: x * y
    divide = lambda x, y: x / y if y != 0 else "Division by zero!"

    # Perform calculation based on selected operation
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    # Display the result
    st.write(f"The result of {operation.lower()}ing {num1} and {num2} is: **{result}**")

# Domain-Based Calculator Section
elif section == "Domain-Based Calculator":
    st.header("Domain-Based Calculator Implementation")

    st.subheader("Step 1: Use Lambda Functions")
    st.write("""
    We'll create basic arithmetic operations using lambda functions for addition, subtraction, multiplication, and division.
    """)

    st.code("""
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    multiply = lambda x, y: x * y
    divide = lambda x, y: x / y if y != 0 else "Division by zero!"
    """, language="python")

    st.subheader("Step 2: Use map(), filter(), and reduce()")
    st.write("""
    We'll demonstrate the use of `map()`, `filter()`, and `reduce()` in our domain-based calculator.
    """)

    st.code("""
    # Using map to square all numbers
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(lambda x: x**2, numbers))

    # Using filter to find even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    # Using reduce to multiply all numbers together
    product_of_numbers = reduce(lambda x, y: x * y, numbers)

    print(squared_numbers)  # Output: [1, 4, 9, 16]
    print(even_numbers)  # Output: [2, 4]
    print(product_of_numbers)  # Output: 24
    """, language="python")

    st.subheader("Step 3: Implement a Custom Module")
    st.write("""
    Create a separate Python file as a module, e.g., `mymathmodule.py`, that contains custom functions for arithmetic operations. This can then be imported and used within the main calculator program.
    """)

    math_module()

    st.write("""
    To import and use this module in the main program:
    ```python
    import mymathmodule

    result = mymathmodule.add(10, 5)
    print(result)  # Output: 15
    ```
    """)

# Additional Resources Section
elif section == "Additional Resources":
    st.header("Additional Learning Resources")
    st.markdown("""
    - [Python Official Documentation](https://docs.python.org/3/tutorial/modules.html)
    - [Learn about Functional Programming in Python](https://realpython.com/python-functional-programming/)
    - [Lambda Functions Guide](https://www.w3schools.com/python/python_lambda.asp)
    """)

# Footer
st.markdown("---")
st.markdown("Developed as an ICT Tool for BCA263-3 Introduction to Python course.")
