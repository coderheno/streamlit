import streamlit as st

def python_basics():
    st.header("Python Basics")
    
    st.subheader("Data Types")
    st.write("In Python, data types include integers, floats, strings, lists, tuples, dictionaries, and sets.")
    
    st.subheader("Numbers")
    st.code("""
# Integer
x = 10

# Float
y = 10.5

# Complex
z = 1 + 2j
""")
    st.write("Example:")
    st.code("""
x = 10       # Integer
y = 10.5     # Float
z = 1 + 2j   # Complex

print(x)     # Output: 10
print(y)     # Output: 10.5
print(z)     # Output: (1+2j)
""")

    st.subheader("Strings")
    st.code("""
# Single quotes
s = 'Hello'

# Double quotes
t = "World"

# Multiline string
u = '''This is a 
multiline string'''
""")
    st.write("Example:")
    st.code("""
s = 'Hello'
t = "World"
u = '''This is a 
multiline string'''

print(s)     # Output: Hello
print(t)     # Output: World
print(u)     # Output: This is a 
             #          multiline string
""")

    st.subheader("Lists")
    st.code("""
lst = [1, 2, 3, 4, 5]
""")
    st.write("Example:")
    st.code("""
lst = [1, 2, 3, 4, 5]
print(lst)   # Output: [1, 2, 3, 4, 5]
""")

    st.subheader("Tuples")
    st.code("""
tpl = (1, 2, 3, 4, 5)
""")
    st.write("Example:")
    st.code("""
tpl = (1, 2, 3, 4, 5)
print(tpl)   # Output: (1, 2, 3, 4, 5)
""")

    st.subheader("Dictionaries")
    st.code("""
dct = {'one': 1, 'two': 2, 'three': 3}
""")
    st.write("Example:")
    st.code("""
dct = {'one': 1, 'two': 2, 'three': 3}
print(dct)  # Output: {'one': 1, 'two': 2, 'three': 3}
""")

    st.subheader("Sets")
    st.code("""
st = {1, 2, 3, 4, 5}
""")
    st.write("Example:")
    st.code("""
st = {1, 2, 3, 4, 5}
print(st)   # Output: {1, 2, 3, 4, 5}
""")

    st.subheader("Variables")
    st.code("""
# Single assignment
a = 5

# Multiple assignments
x, y, z = 1, 2, 3
""")
    st.write("Example:")
    st.code("""
a = 5
x, y, z = 1, 2, 3

print(a)    # Output: 5
print(x)    # Output: 1
print(y)    # Output: 2
print(z)    # Output: 3
""")

    st.subheader("Input and Output Statements")
    st.write("**Input**: The `input()` function is used to take input from the user.")
    st.code("""
variable = input("Prompt message")
""")
    st.write("Example:")
    st.code("""
name = input("Enter your name: ")
print("Hello, " + name + "!")
# If user inputs "Alice", output: Hello, Alice!
""")

    st.write("**Output**: The `print()` function is used to output data to the console.")
    st.code("""
print(value)
""")
    st.write("Example:")
    st.code("""
print("Hello, World!")
# Output: Hello, World!
""")

    st.subheader("Conditional Statements")
    st.write("**Conditional statements** control the flow of the program based on conditions.")
    st.code("""
if condition:
    # Code block if condition is True
elif another_condition:
    # Code block if another_condition is True
else:
    # Code block if all conditions are False
""")
    st.write("Example:")
    st.code("""
a = 10
if a > 0:
    print("a is positive")
elif a == 0:
    print("a is zero")
else:
    print("a is negative")
# Output: a is positive
""")

    st.subheader("Looping Statements")
    st.write("**For Loop**: Iterate over a sequence of items.")
    st.code("""
for item in sequence:
    # Code block
""")
    st.write("Example:")
    st.code("""
for i in range(5):
    print(i)
# Output: 
# 0
# 1
# 2
# 3
# 4
""")

    st.write("**While Loop**: Execute as long as a condition is true.")
    st.code("""
while condition:
    # Code block
""")
    st.write("Example:")
    st.code("""
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 
# 0
# 1
# 2
# 3
# 4
""")

    st.subheader("Example Code Combining All Concepts")
    st.code("""
# Data types
num = 10
flt = 10.5
string = "Hello"
lst = [1, 2, 3]
tpl = (1, 2, 3)
dct = {'a': 1, 'b': 2}
st = {1, 2, 3}

# Variables
a, b, c = 5, 'Hello', 3.14

# Input
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Conditional statements
if a > 0:
    print('a is positive')
elif a == 0:
    print('a is zero')
else:
    print('a is negative')

# For loop
for i in range(3):
    print(lst[i])

# While loop
count = 0
while count < 3:
    print(tpl[count])
    count += 1
""")

def streamlit_basics():
    st.header("Streamlit Basics")

    st.subheader("Data Types")
    st.write("Streamlit handles data types similarly to standard Python, including integers, floats, strings, lists, tuples, dictionaries, and sets.")

    st.subheader("Numbers")
    st.code("""
# Integer
x = 10

# Float
y = 10.5

# Complex
z = 1 + 2j
""")
    st.write("Example:")
    st.code("""
x = 10       # Integer
y = 10.5     # Float
z = 1 + 2j   # Complex

print(x)     # Output: 10
print(y)     # Output: 10.5
print(z)     # Output: (1+2j)
""")

    st.subheader("Strings")
    st.code("""
# Single quotes
s = 'Hello'

# Double quotes
t = "World"

# Multiline string
u = '''This is a 
multiline string'''
""")
    st.write("Example:")
    st.code("""
s = 'Hello'
t = "World"
u = '''This is a 
multiline string'''

print(s)     # Output: Hello
print(t)     # Output: World
print(u)     # Output: This is a 
             #          multiline string
""")

    st.subheader("Lists")
    st.code("""
lst = [1, 2, 3, 4, 5]
""")
    st.write("Example:")
    st.code("""
lst = [1, 2, 3, 4, 5]
print(lst)   # Output: [1, 2, 3, 4, 5]
""")

    st.subheader("Tuples")
    st.code("""
tpl = (1, 2, 3, 4, 5)
""")
    st.write("Example:")
    st.code("""
tpl = (1, 2, 3, 4, 5)
print(tpl)   # Output: (1, 2, 3, 4, 5)
""")

    st.subheader("Dictionaries")
    st.code("""
dct = {'one': 1, 'two': 2, 'three': 3}
""")
    st.write("Example:")
    st.code("""
dct = {'one': 1, 'two': 2, 'three': 3}
print(dct)  # Output: {'one': 1, 'two': 2, 'three': 3}
""")

    st.subheader("Sets")
    st.code("""
st = {1, 2, 3, 4, 5}
""")
    st.write("Example:")
    st.code("""
st = {1, 2, 3, 4, 5}
print(st)   # Output: {1, 2, 3, 4, 5}
""")

    st.subheader("Variables")
    st.code("""
# Single assignment
a = 5

# Multiple assignments
x, y, z = 1, 2, 3
""")
    st.write("Example:")
    st.code("""
a = 5
x, y, z = 1, 2, 3

print(a)    # Output: 5
print(x)    # Output: 1
print(y)    # Output: 2
print(z)    # Output: 3
""")

    st.subheader("Input and Output Statements")
    st.write("**Input**: The `st.text_input()` and `st.number_input()` functions are used to take input from the user.")
    st.code("""
temperature = st.number_input("Enter the temperature:", format="%.2f")
conversion_type = st.text_input("Convert from (C or F):").strip().upper()
""")
    st.write("Example:")
    st.code("""
name = st.text_input("Enter your name:")
st.write("Hello, " + name + "!")
""")

    st.write("**Output**: The `st.write()` function is used to output data to the app.")
    st.code("""
st.write(value)
""")
    st.write("Example:")
    st.code("""
st.write("Hello, World!")
""")

    st.subheader("Conditional Statements")
    st.code("""
if condition:
    # Code block if condition is True
elif another_condition:
    # Code block if another_condition is True
else:
    # Code block if all conditions are False
""")
    st.write("Example:")
    st.code("""
a = 10
if a > 0:
    st.write("a is positive")
elif a == 0:
    st.write("a is zero")
else:
    st.write("a is negative")
""")

    st.subheader("Looping Statements")
    st.write("**For Loop**: Iterate over a sequence of items.")
    st.code("""
for item in sequence:
    # Code block
""")
    st.write("Example:")
    st.code("""
for i in range(5):
    st.write(i)
""")

    st.write("**While Loop**: Execute as long as a condition is true.")
    st.code("""
while condition:
    # Code block
""")
    st.write("Example:")
    st.code("""
count = 0
while count < 5:
    st.write(count)
    count += 1
""")

    st.subheader("Example Code Combining All Concepts")
    st.code("""
# Data types
num = 10
flt = 10.5
string = "Hello"
lst = [1, 2, 3]
tpl = (1, 2, 3)
dct = {'a': 1, 'b': 2}
st = {1, 2, 3}

# Variables
a, b, c = 5, 'Hello', 3.14

# Input
name = st.text_input("Enter your name:")
st.write("Hello, " + name + "!")

# Conditional statements
if a > 0:
    st.write('a is positive')
elif a == 0:
    st.write('a is zero')
else:
    st.write('a is negative')

# For loop
for i in range(3):
    st.write(lst[i])

# While loop
count = 0
while count < 3:
    st.write(tpl[count])
    count += 1
""")

def quiz():
    st.header("Quiz")
    
    st.subheader("Test Your Knowledge")
    st.write("Answer the following questions:")
    
    # Question 1
    st.write("1. What is the output of `print(5 + 3)`?")
    answer_1 = st.text_input("Your answer for Question 1:")
    if st.button("Submit Answer 1"):
        if answer_1.strip() == "8":
            st.write("Correct!")
        else:
            st.write("Incorrect. The correct answer is 8.")
    
    # Question 2
    st.write("2. How do you declare a list in Python?")
    answer_2 = st.text_input("Your answer for Question 2:")
    if st.button("Submit Answer 2"):
        if "list" in answer_2.lower() and "[" in answer_2 and "]" in answer_2:
            st.write("Correct!")
        else:
            st.write("Incorrect. You declare a list using square brackets, e.g., `[1, 2, 3]`.")

def problem_solving():
    st.header("Problem Solving")
    
    st.subheader("Solve the Following Problems:")
    
    st.write("1. **Calculate the Sum of Numbers**: Enter a range of numbers and find their sum.")
    
    # Input range of numbers
    start = st.number_input("Start of range:", value=1)
    end = st.number_input("End of range:", value=10)
    
    if st.button("Calculate Sum"):
        if end >= start:
            total_sum = sum(range(start, end + 1))
            st.write(f"The sum of numbers from {start} to {end} is {total_sum}.")
        else:
            st.write("End of range should be greater than or equal to start.")
    
    st.write("2. **Simple Arithmetic Quiz**: Enter two numbers and select an operation to perform.")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.write("Error: Division by zero is not allowed.")
                result = None

        if result is not None:
            st.write(f"The result of {operation} is {result:.2f}")

# Create tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["Python Basics", "Streamlit Basics", "Quiz", "Problem Solving"])

with tab1:
    python_basics()

with tab2:
    streamlit_basics()

with tab3:
    quiz()

with tab4:
    problem_solving()
