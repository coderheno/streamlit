import streamlit as st
import random
# Define the list of names
names = [
    "MOSMI S", "MUGILARASAN A", "NIGAM M J", "NIKITA SHARMA", "NILESH VIDHANI",
    "NISHTHA JAIN", "PRIYADHARSHINI B", "REBEKAH DAVID", "ROHAAN D KOTHARI",
    "RUCHAK KHATRI", "SACHIN K", "SACHIN YADAV", "SAHANA S REDDY", "SAI KRISHNAN B",
    "SAMRUDH S BANGERA", "SANDHYA M", "SANIDHYA SRIVASTAVA", "SARA RAJESH KOTIAN",
    "SEBASTIAN JOSE", "SHINEY ARORA", "SHREEDHAR ANANT MODI", "SHREENITHI U",
    "SHUBHAM KUNDU", "SREELAKSHMI K", "SURAMYA DIDWANIA", "SURYA VAMSHI S",
    "SUYASH MASKARA", "THOMAS DENNIS", "VAIBHAV KAPOOR", "VANSHIKA KOTHARI",
    "YASH BABULAL SINGHAL", "YUG SURYA", "HANNAH MARIAM MATHEW", "DINESH J",
    "HARIHARAN P", "SHARON SUSAN THOMAS"
]

# Define the list of funny tasks
funny_tasks = [
    "Do an animal sound (e.g., roar like a lion)",
    "Tell your favorite crush you like them",
    "Call your mom/dad and say 'I love you'",
    "Reveal a Chinese secret with your frnds",
    "Recite the alphabet backwards",
    "Tell us your dad's phone number",
    "Do a trending dance",
    "Speak in a made-up language",
    "Tell a joke about yourself",
    "2 Truths and 1 Lie about you",
    "Do a silly impression of a famous person",
    "Do a magic trick",
    "Tell a funny sorry to your friend",
    "Do an impression of your favorite character",
    "Sing a song with your mouth closed",
    "Pretend to be a anchor and report a funny reel",
    "Truth or Dare",
    "Truth or Dare"
]


def tuple_ict_tool():
    st.title("Unit-2: Learning Tuples in Python")

    # Define tabs
    tabs = st.selectbox("Select a Topic", ["Introduction", "Lecture", "Activities", "Lab Program","Tuple Matching Game"])

    if tabs == "Introduction":
        st.header("Introduction to Tuples")
        st.write("""
        Tuples are a built-in data type in Python that allows you to store a collection of items. Unlike lists, tuples are immutable, meaning their content cannot be changed once created. They are often used to group related data together.

        ### Comparison with Other Languages:

        - **Java**: In Java, tuples are not natively supported. Instead, similar functionality can be achieved using classes or pairs of values through libraries like `Apache Commons Lang`. Java does not provide built-in tuple types, so creating a tuple-like structure requires custom classes.

        - **C++**: C++ has a `std::tuple` class introduced in C++11. It allows storing elements of different types in a single object. Tuples in C++ are mutable and provide methods to access and modify the elements. The syntax is slightly more complex compared to Python's tuples.

        - **JavaScript**: JavaScript does not have a native tuple type. Instead, arrays or objects are commonly used to achieve similar results. Arrays can be used to store multiple values, but they are mutable, unlike Python tuples.

        Tuples in Python offer simplicity and ease of use for grouping and accessing related data, which can be more intuitive than the alternatives in other languages.
        """)
    elif tabs == "Tuple Matching Game":
        tuple_matching_game()
    elif tabs == "Lecture":
        st.header("Lecture on Tuples")
        
        # Working with Tuple Elements
        st.subheader("1. Working with Tuple Elements")
        st.write("""
        To work with tuple elements, you need to understand how to access and manipulate them. You can access elements in a tuple using indexing, similar to lists. Tuples support both positive and negative indexing.
        """)
        st.code("""
        # Example Tuple
        my_tuple = (1, 2, 3, 4, 5)
        
        # Accessing Elements
        first_element = my_tuple[0]  # Output: 1
        last_element = my_tuple[-1]  # Output: 5
        """)
        
        st.subheader("2. Basic Tuple Operations")
        st.write("""
        Tuples support various operations including concatenation and repetition. You can combine tuples using the `+` operator and repeat tuples using the `*` operator.
        """)
        st.code("""
        # Concatenation
        tuple1 = (1, 2, 3)
        tuple2 = (4, 5, 6)
        combined_tuple = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)
        
        # Repetition
        repeated_tuple = tuple1 * 2  # Output: (1, 2, 3, 1, 2, 3)
        """)
        
        st.subheader("3. Tuple Methods")
        st.write("""
        Tuples have a limited set of methods compared to lists. They include methods like `count` and `index`.
        """)
        st.code("""
        # Example Tuple
        my_tuple = (1, 2, 3, 1, 2, 1)
        
        # Count Method
        count_of_1 = my_tuple.count(1)  # Output: 3
        
        # Index Method
        index_of_2 = my_tuple.index(2)  # Output: 1
        """)
        
        st.subheader("4. Type of Tuples")
        st.write("""
        Tuples can be categorized based on their content and usage. For example, a single-element tuple requires a trailing comma to distinguish it from a simple value.
        """)
        st.code("""
        # Single-element Tuple
        single_element_tuple = (1,)  # Must include a comma
        
        # Nested Tuples
        nested_tuple = ((1, 2), (3, 4))
        """)

    elif tabs == "Activities":
        st.header("Activities")
        
        # Activity 1: Accessing Tuple Elements
        st.subheader("Activity 1: Accessing Tuple Elements")
        st.write("""
        Create a tuple with 5 elements and write code to access the first, last, and middle elements. Use indexing to achieve this.
        """)
        my_tuple = st.text_input("Enter a tuple (e.g., (0, 1, 2, 3, 4)):", "(0, 1, 2, 3, 4)")
        if my_tuple:
            try:
                my_tuple = eval(my_tuple)  # Convert string input to tuple
                if isinstance(my_tuple, tuple):
                    first_element = my_tuple[0]
                    last_element = my_tuple[-1]
                    middle_element = my_tuple[len(my_tuple) // 2]
                    st.write(f"First Element: {first_element}")
                    st.write(f"Last Element: {last_element}")
                    st.write(f"Middle Element: {middle_element}")
                else:
                    st.error("Please enter a valid tuple.")
            except:
                st.error("Invalid input. Please enter a tuple in the correct format.")
        
        # Activity 2: Performing Tuple Operations
        st.subheader("Activity 2: Performing Tuple Operations")
        tuple1_input = st.text_input("Enter the first tuple (e.g., (1, 2)):", "(1, 2)")
        tuple2_input = st.text_input("Enter the second tuple (e.g., (3, 4)):", "(3, 4)")
        if tuple1_input and tuple2_input:
            try:
                tuple1 = eval(tuple1_input)
                tuple2 = eval(tuple2_input)
                if isinstance(tuple1, tuple) and isinstance(tuple2, tuple):
                    combined_tuple = tuple1 + tuple2
                    repeated_tuple = combined_tuple * 3
                    st.write(f"Combined Tuple: {combined_tuple}")
                    st.write(f"Repeated Tuple: {repeated_tuple}")
                else:
                    st.error("Please enter valid tuples.")
            except:
                st.error("Invalid input. Please enter tuples in the correct format.")
        
        # Activity 3: Using Tuple Methods
        st.subheader("Activity 3: Using Tuple Methods")
        tuple_input = st.text_input("Enter a tuple with repeated elements (e.g., (5, 6, 7, 5, 5, 6)):", "(5, 6, 7, 5, 5, 6)")
        if tuple_input:
            try:
                my_tuple = eval(tuple_input)
                if isinstance(my_tuple, tuple):
                    count_of_5 = my_tuple.count(5)
                    index_of_6 = my_tuple.index(6)
                    st.write(f"Count of 5: {count_of_5}")
                    st.write(f"Index of 6: {index_of_6}")
                else:
                    st.error("Please enter a valid tuple.")
            except:
                st.error("Invalid input. Please enter a tuple in the correct format.")
        
        # Activity 4: Working with Different Tuple Types
        st.subheader("Activity 4: Working with Different Tuple Types")
        single_element_tuple = st.text_input("Enter a single-element tuple (e.g., (10,)):", "(10,)")
        nested_tuple = st.text_input("Enter a nested tuple (e.g., ((1, 2), (3, 4))):", "((1, 2), (3, 4))")
        if single_element_tuple and nested_tuple:
            try:
                single_element_tuple = eval(single_element_tuple)
                nested_tuple = eval(nested_tuple)
                if isinstance(single_element_tuple, tuple) and isinstance(nested_tuple, tuple):
                    first_element_of_nested = nested_tuple[0]
                    st.write(f"Single-element Tuple: {single_element_tuple}")
                    st.write(f"First Element of Nested Tuple: {first_element_of_nested}")
                else:
                    st.error("Please enter valid tuples.")
            except:
                st.error("Invalid input. Please enter tuples in the correct format.")

    elif tabs == "Lab Program":
        st.header("Lab Program: Implementing Tuples in a Specific Domain")
        
        st.write("""
        In this lab program, we will implement tuples in a specific domain. For example, consider a scenario where we use tuples to represent data related to employees in a company. Each employee can be represented as a tuple containing their ID, name, and department. 

        ### Example:
        
        1. **Define Employee Data**:
        ```python
        # Define a tuple for each employee
        employee1 = (101, 'Alice', 'HR')
        employee2 = (102, 'Bob', 'Engineering')
        employee3 = (103, 'Charlie', 'Marketing')
        ```

        2. **Access and Manipulate Employee Data**:
        ```python
        # List of employees
        employees = [employee1, employee2, employee3]

        # Accessing data
        for emp in employees:
            emp_id, name, dept = emp
            st.write(f"Employee ID: {emp_id}, Name: {name}, Department: {dept}")

        # Example: Filtering employees by department
        hr_employees = [emp for emp in employees if emp[2] == 'HR']
        st.write(f"HR Employees: {hr_employees}")
        ```

        ### Interactive Example:
        """)

        # Define and display employee data
        employees = [
            (101, 'Alice', 'HR'),
            (102, 'Bob', 'Engineering'),
            (103, 'Charlie', 'Marketing')
        ]
        
        # Display employees
        st.subheader("Employee Data")
        for emp in employees:
            emp_id, name, dept = emp
            st.write(f"Employee ID: {emp_id}, Name: {name}, Department: {dept}")

        # Filter by department
        selected_department = st.selectbox("Select Department to Filter", ["All", "HR", "Engineering", "Marketing"])
        if selected_department != "All":
            filtered_employees = [emp for emp in employees if emp[2] == selected_department]
            st.write(f"Employees in {selected_department}: {filtered_employees}")
        else:
            st.write("All Employees:", employees)
    

# Define the Tuple Matching Game content
def tuple_matching_game():
    st.title("Tuple Truth or Dare")
    st.write("Get ready for some fun! Each student will perform a random task based on their tuple.")

    # Randomly assign tasks to names
    random.shuffle(funny_tasks)
    assigned_tasks = {name: funny_tasks[i % len(funny_tasks)] for i, name in enumerate(names)}

    # Display tasks for each student
    for name in names:
        st.subheader(f"{name}'s Turn")
        st.write(f"Task: {assigned_tasks[name]}")
        st.write("Perform this task and have fun!")

    # Instructions for game
    st.write("Take turns performing your tasks. Enjoy the laughter and fun!")

# Run the app
if __name__ == "__main__":
    tuple_ict_tool()
