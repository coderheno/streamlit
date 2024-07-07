import streamlit as st
from streamlit_option_menu import option_menu

# Create the option menu for navigation
with st.sidebar:
    selected = option_menu("Menu", ["BMI Calculator (Tkinter)", "BMI Calculator (Streamlit)", "Lecture", "EL- Voice Login"],
                           icons=["calculator", "calculator", "book", "book"],
                           default_index=0)

# BMI Calculator using Tkinter (Explanation Only)
if selected == "BMI Calculator (Tkinter)":
    st.title("BMI Calculator using Tkinter")

    st.write("""
    ### Steps to Create a Simple BMI Calculator in Tkinter
    1. **Set Up the Environment**:
        - Ensure you have Python installed on your computer.
        - Install Tkinter if it's not already installed (it usually comes with Python).
    2. **Create the Main Window**:
        ```python
        import tkinter as tk
        root = tk.Tk()
        root.title("BMI Calculator")
        ```
    3. **Add Labels and Entry Widgets**:
        ```python
        label_weight = tk.Label(root, text="Weight (kg):")
        label_weight.pack(padx=10, pady=5)
        entry_weight = tk.Entry(root)
        entry_weight.pack(padx=10, pady=5)
        
        label_height = tk.Label(root, text="Height (cm):")
        label_height.pack(padx=10, pady=5)
        entry_height = tk.Entry(root)
        entry_height.pack(padx=10, pady=5)
        ```
    4. **Add a Button to Trigger BMI Calculation**:
        ```python
        button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
        button_calculate.pack(pady=20)
        ```
    5. **Add a Label to Display the Result**:
        ```python
        label_result = tk.Label(root, text="BMI: ")
        label_result.pack(pady=10)
        ```
    6. **Implement the BMI Calculation Logic**:
        ```python
        def calculate_bmi():
            weight = float(entry_weight.get())
            height = float(entry_height.get()) / 100  # Convert height to meters
            bmi = weight / (height ** 2)
            label_result.config(text=f'BMI: {bmi:.2f}')
        
        button_calculate.config(command=calculate_bmi)
        ```
    7. **Run the Application**:
        ```python
        root.mainloop()
        ```
    """)

# BMI Calculator using Streamlit
elif selected == "BMI Calculator (Streamlit)":
    st.title("BMI Calculator using Streamlit")
    st.write("""
    ### Steps to Create a Simple BMI Calculator in Streamlit
    1. **Set Up the Environment**:
        - Ensure you have Python installed on your computer.
        - Install Streamlit if it's not already installed.
    2. **Add Streamlit Library**:
        ```python
        import streamlit as st
        ```
    3. **Add Inputs - Height and Weight**:
        ```python
        weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
        height = st.number_input("Height (cm)", min_value=0.0, format="%.2f")
        ```
    4. **Add a Button to Trigger BMI Calculation**:
        ```python
        if st.button("Calculate BMI"):
            height_m = height / 100  # Convert height to meters
            bmi = weight / (height_m ** 2)
            st.write(f"BMI: {bmi:.2f}")
        ```
    5. **Run the Application**:
        ```bash
        streamlit run app25.py
        ```
    """)

    weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Height (cm)", min_value=0.0, format="%.2f")

    calculate = st.button("Calculate BMI")

    if calculate:
        height_m = height / 100  # Convert height to meters
        bmi = weight / (height_m ** 2)
        st.write(f"BMI: {bmi:.2f}")

# Explanations of Programming Concepts
elif selected == "Lecture":
    st.title("Explanations")

    st.header("Operators, Precedence, and Associativity")
    st.write("""
    **Operators**: Operators are symbols that perform operations on variables and values.
    
    **Precedence**: Operator precedence determines the order in which operators are evaluated.
    
    **Associativity**: Operator associativity determines the order in which operators of the same precedence are evaluated.
    
    Examples:
    ```python
    result = 10 + 20 * 30  # Multiplication has higher precedence than addition
    result = (10 + 20) * 30  # Parentheses change the order of evaluation
    ```

    **Precedence Order (highest to lowest)**:
    1. Parentheses `()`
    2. Exponentiation `**`
    3. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
    4. Addition `+`, Subtraction `-`
    5. Comparison `<`, `<=`, `>`, `>=`
    6. Equality `==`, `!=`
    7. Logical AND `and`
    8. Logical OR `or`
    """)

    st.header("Decision Control Structures")
    st.write("""
    Decision control structures allow the flow of execution to change based on conditions.

    **if Statement**:
    ```python
    if condition:
        # Code to execute if condition is true
    ```

    **if-else Statement**:
    ```python
    if condition:
        # Code to execute if condition is true
    else:
        # Code to execute if condition is false
    ```

    **if-elif-else Statement**:
    ```python
    if condition1:
        # Code to execute if condition1 is true
    elif condition2:
        # Code to execute if condition2 is true
    else:
        # Code to execute if all conditions are false
    ```
    """)

    st.header("Looping Structures")
    st.write("""
    Looping structures allow repeating a set of statements multiple times.

    **for Loop**:
    ```python
    for variable in iterable:
        # Code to execute for each item in the iterable
    ```

    **while Loop**:
    ```python
    while condition:
        # Code to execute while the condition is true
    ```

    **Example**:
    ```python
    for i in range(5):
        print(i)  # Prints numbers from 0 to 4

    i = 0
    while i < 5:
        print(i)  # Prints numbers from 0 to 4
        i += 1
    ```
    """)

    st.header("Console Input and Output")
    st.write("""
    **Input**:
    ```python
    name = input("Enter your name: ")  # Reads a string from the console
    age = int(input("Enter your age: "))  # Reads an integer from the console
    ```

    **Output**:
    ```python
    print("Hello, World!")  # Prints the string to the console
    print("Your age is:", age)  # Prints a string followed by the value of age
    ```

    **Example**:
    ```python
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello, {name}. You are {age} years old.")
    ```
    """)

elif selected == "EL- Voice Login":
    st.title("EL- Voice Login")
    st.write("This section will be implemented later.")
