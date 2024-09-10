import streamlit as st

# Function for List Comprehensions
def list_comprehensions():
    st.subheader("List Comprehensions")
    st.write("""
    List comprehensions provide a concise way to create lists. They allow you to generate new lists by applying an expression to each item in an existing list.

    **Basic Example:**
    ```python
    # Create a list of squares of numbers from 0 to 4
    squares = [x**2 for x in range(5)]
    print(squares)  # Output: [0, 1, 4, 9, 16]
    ```

    **Filtering Example:**
    ```python
    # Filter out non-numeric items from a list and convert the remaining to integers
    items = ['10', '20', 'a', '30', 'b', '40']
    only_digits = [int(item) for item in items if item.isdigit()]
    print(only_digits)  # Output: [10, 20, 30, 40]
    ```

    **Nested List Comprehensions:**
    ```python
    # Flatten a list of lists
    lists = [[1, 2, 3], [4, 5], [6]]
    flat_list = [item for sublist in lists for item in sublist]
    print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
    ```

    **Using `zip()` to Combine Lists:**
    ```python
    # Combine two lists into a list of strings
    numbers = [1, 2, 3]
    words = ['one', 'two', 'three']
    combined = [f"{num}: {word}" for num, word in zip(numbers, words)]
    print(combined)
    # Output: ['1: one', '2: two', '3: three']
    ```
    """)

# Function for Dict Comprehensions
def dict_comprehensions():
    st.subheader("Dict Comprehensions")
    st.write("""
    Dict comprehensions create dictionaries in a single line. They can be used to generate new dictionaries by applying an expression to each key-value pair in an existing dictionary.

    **Basic Example:**
    ```python
    # Create a dictionary with numbers and their squares
    squares = {x: x**2 for x in range(5)}
    print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    ```

    **Converting Keys to Lowercase:**
    ```python
    # Convert all keys in a dictionary to lowercase
    original = {'Name': 'Alice', 'AGE': 30}
    lowercased = {key.lower(): value for key, value in original.items()}
    print(lowercased)
    # Output: {'name': 'Alice', 'age': 30}
    ```

    **Nested Dict Comprehensions:**
    ```python
    # Use nested comprehensions to invert a dictionary
    original = {'a': 1, 'b': 2, 'c': 3}
    inverted = {value: key for key, value in original.items()}
    print(inverted)
    # Output: {1: 'a', 2: 'b', 3: 'c'}
    ```

    """)

# Function for Set Comprehensions
def set_comprehensions():
    st.subheader("Set Comprehensions")
    st.write("""
    Set comprehensions are used to create sets, which are collections of unique items.

    **Basic Example:**
    ```python
    # Create a set of unique numbers from a list
    numbers = [1, 2, 2, 3, 4, 4, 4]
    unique_numbers = {num for num in numbers}
    print(unique_numbers)  # Output: {1, 2, 3, 4}
    ```

    **Filtering Example:**
    ```python
    # Create a set of even numbers from a list
    numbers = [1, 2, 3, 4, 5, 6]
    evens = {num for num in numbers if num % 2 == 0}
    print(evens)  # Output: {2, 4, 6}
    ```
    """)

# Function for Defining Functions
def defining_functions():
    st.subheader("Defining Functions")
    st.write("""
    Functions in Python are blocks of code that perform a specific task. They are defined using the `def` keyword.

    **Basic Function:**
    ```python
    # Function to greet someone
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Alice"))  # Output: Hello, Alice!
    ```

    **Using Default Arguments:**
    ```python
    # Function with a default greeting
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    print(greet("Alice"))  # Output: Hello, Alice!
    print(greet("Bob", "Hi"))  # Output: Hi, Bob!
    ```

    **Variable-Length Arguments:**
    ```python
    # Function to sum any number of values
    def add_numbers(*numbers):
        return sum(numbers)

    print(add_numbers(1, 2, 3))  # Output: 6
    print(add_numbers(5, 10, 15, 20))  # Output: 50
    ```

    **Using Keyword Arguments:**
    ```python
    # Function with keyword arguments
    def print_info(name, **info):
        print(f"Name: {name}")
        for key, value in info.items():
            print(f"{key}: {value}")

    print_info("Alice", age=30, city="New York")
    # Output:
    # Name: Alice
    # age: 30
    # city: New York
    ```
    """)

# Function for Instructional Activity: Code Enrichment
def code_enrichment():
    st.subheader("Instructional Activity: Code Enrichment")
    st.write("""
    **Activity Description:**
    This activity involves improving a simple Python script related to managing a list of items. The goal is to enhance the script by adding new features or making it more efficient.

    **Initial Code:**
    ```python
    # Initial script for managing a list of items
    items = ['apple', 'banana', 'cherry']
    
    # Add a new item
    items.append('date')
    
    # Remove an item
    items.remove('banana')
    
    # Print all items
    for item in items:
        print(item)
    ```

    **Enhanced Code:**
    ```python
    # Improved script with additional features
    items = ['apple', 'banana', 'cherry']

    # Add a new item
    items.append('date')

    # Remove an item if it exists
    item_to_remove = 'banana'
    if item_to_remove in items:
        items.remove(item_to_remove)

    # Print all items with their positions
    for index, item in enumerate(items):
        print(f"Item {index + 1}: {item}")
    ```

    **Instructions:**
    - **Understand the Initial Code:** Review the provided script that manages a list of items.
    - **Identify Enhancements:** Consider how you can improve the script. For example, add features like checking if an item exists before removing it or displaying item positions.
    - **Implement Enhancements:** Update the code based on your ideas.
    - **Test the Code:** Run the enhanced script to ensure it works correctly.

    **Discussion Points:**
    - How did the enhancements improve the script?
    - What difficulties did you face, and how did you overcome them?
    """)

# Function for Participatory Learning: Role Play
def role_play():
    st.subheader("Participatory Learning: Role Play")
    st.write("""
    **Activity Description:**
    Engage in role-play scenarios to understand different applications of Python functions and comprehensions in various contexts.

    **Instructions:**
    - **Divide into Small Groups:** Form groups and assign each group a scenario.
    - **Role-Play Scenarios:**
        1. **Student Portal:** Create a Python function that retrieves and displays a student's grades.
        2. **Faculty Portal:** Develop a Python function to update faculty details in a simple data structure.
        3. **Admin Portal:** Use comprehensions to generate a summary report of user activities.
    - **Develop Solutions:** Use Python functions and comprehensions to solve the scenarios.
    - **Present Your Solution:** Each group presents their solution and explains how they applied Python concepts.
    - **Discussion:** Discuss the effectiveness of each solution and potential improvements.

    **Example Code for Student Portal:**
    ```python
    # Function to display student grades
    def display_grades(name, grades):
        print(f"{name}'s grades: {', '.join(map(str, grades))}")

    display_grades("Alice", [85, 90, 88])
    # Output: Alice's grades: 85, 90, 88
    ```

    **Discussion Points:**
    - How did you choose which Python concepts to use?
    - What were the challenges in implementing the scenarios?
    """)

# Function for Participatory Learning: Case Study
def case_study():
    st.subheader("Participatory Learning: Case Study")
    st.write("""
    **Activity Description:**
    Analyze a case study that demonstrates the use of Python comprehensions and functions in a practical application.

    **Instructions:**
    - **Review the Case Study:** Read through the case study describing how Python comprehensions and functions are used in a real-world application.
    - **Analyze the Case Study:** Identify and discuss how these concepts are applied.
    - **Discuss Applications:** Explore how similar techniques can be used in other scenarios.
    - **Present Your Findings:** Share your analysis and discuss possible adaptations.

    **Example Case Study:**
    **Case Study:** A store wants to calculate the total cost of products bought by customers and list the product names.

    ```python
    # List of purchases
    purchases = [
        {'product': 'Laptop', 'price': 1200},
        {'product': 'Mouse', 'price': 25},
        {'product': 'Keyboard', 'price': 75}
    ]

    # Calculate total cost
    total_cost = sum(purchase['price'] for purchase in purchases)
    print(f"Total Cost: ${total_cost}")

    # List of product names
    product_names = [purchase['product'] for purchase in purchases]
    print(f"Products Purchased: {', '.join(product_names)}")
    ```

    **Discussion Points:**
    - How were comprehensions and functions used effectively in this case study?
    - How can these techniques be applied to other real-world scenarios?
    """)

# Main function to create Streamlit app with tabs
def main():
    st.title("Python Unit-4 Concepts and Activities")
    
    # Create tabs
    tabs = st.tabs(["List Comprehensions", "Dict Comprehensions", "Set Comprehensions", "Functions", "Instructional Activity", "Participatory Learning"])
    
    with tabs[0]:
        list_comprehensions()
    
    with tabs[1]:
        dict_comprehensions()
    
    with tabs[2]:
        set_comprehensions()
    
    with tabs[3]:
        defining_functions()
    
    with tabs[4]:
        code_enrichment()
    
    with tabs[5]:
        role_play()
        case_study()

if __name__ == "__main__":
    main()