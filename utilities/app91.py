import streamlit as st
import random

def generate_team_name():
    adjectives = ['Swift', 'Brave', 'Clever', 'Witty', 'Bold']
    animals = ['Tigers', 'Eagles', 'Sharks', 'Wolves', 'Lions']
    return f"{random.choice(adjectives)} {random.choice(animals)}"

# Main application
st.title("Lecture Series: Sets and Dictionaries in Python")

# Tab structure
tabs = ["Lecture Topics", "Activities", "Lab Exercise"]
tab_choice = st.sidebar.selectbox("Select a tab", tabs)

# Lecture Topics
if tab_choice == "Lecture Topics":
    st.header("Sets")
    
    st.subheader("Definition")
    st.write("""
    A set is an unordered collection of unique elements in Python. 
    Unlike lists or tuples, sets do not allow duplicate values. 
    Sets are mutable, meaning their contents can be changed after creation, 
    but the elements themselves must be immutable.
    """)
    
    st.subheader("Set Elements")
    st.write("""
    Elements in a set must be immutable types like numbers, strings, or tuples. 
    You can add elements using the `add()` method or remove them using `remove()` or `discard()`. 
    Sets automatically remove any duplicate elements, ensuring that each element is unique.
    """)
    
    st.subheader("Built-in Methods")
    st.write("""
    Python provides several built-in methods for sets, including:
    - `add(elem)`: Adds an element to the set.
    - `remove(elem)`: Removes a specified element. Raises a KeyError if the element is not found.
    - `discard(elem)`: Removes a specified element. Does not raise an error if the element is not found.
    - `clear()`: Removes all elements from the set.
    - `union(set1, set2)`: Returns a new set with elements from both sets.
    - `intersection(set1, set2)`: Returns a new set with elements common to both sets.
    - `difference(set1, set2)`: Returns a new set with elements in the first set but not in the second.
    """)
    
    st.subheader("Basic Set Operations")
    st.write("""
    Sets support basic mathematical operations like union, intersection, difference, and symmetric difference:
    - **Union** (`|`): Combines elements from two sets, removing duplicates.
    - **Intersection** (`&`): Finds common elements between two sets.
    - **Difference** (`-`): Finds elements present in one set but not in another.
    - **Symmetric Difference** (`^`): Finds elements present in either of the sets but not in both.
    """)
    
    st.subheader("Mathematical Set Operations")
    st.write("""
    Sets also support several mathematical operations:
    - **Subset** (`<=`): Checks if one set is a subset of another.
    - **Superset** (`>=`): Checks if one set is a superset of another.
    - **Disjoint** (`isdisjoint()`): Checks if two sets have no elements in common.
    """)
    
    st.subheader("Variety of Sets")
    st.write("""
    Different types of sets include:
    - **Empty Set**: A set with no elements, defined as `set()`.
    - **Singleton Set**: A set with a single element, like `{1}`.
    - **Finite Set**: A set with a finite number of elements, like `{1, 2, 3}`.
    - **Infinite Set**: A set with an infinite number of elements, typically theoretical in programming contexts.
    """)
    
    st.header("Dictionaries")
    
    st.subheader("Defining a Dictionary")
    st.write("""
    A dictionary in Python is a collection of key-value pairs. 
    Each key must be unique and immutable (like a string, number, or tuple), 
    while the values can be of any data type. Dictionaries are defined using curly braces `{}`.
    """)
    
    st.subheader("Accessing Elements")
    st.write("""
    You can access elements in a dictionary by using their keys. For example, 
    if `d = {'key1': 'value1', 'key2': 'value2'}`, then `d['key1']` returns `'value1'`. 
    If you try to access a key that doesn't exist, Python raises a `KeyError`.
    """)
    
    st.subheader("Basic Operations")
    st.write("""
    Basic operations on dictionaries include:
    - **Adding/Updating**: Add a new key-value pair or update an existing key's value using `d[key] = value`.
    - **Deleting**: Remove a key-value pair using `del d[key]`.
    - **Checking Existence**: Use `key in d` to check if a key exists in the dictionary.
    """)
    
    st.subheader("Methods")
    st.write("""
    Python dictionaries offer several useful methods:
    - `keys()`: Returns a view object containing the dictionary’s keys.
    - `values()`: Returns a view object containing the dictionary’s values.
    - `items()`: Returns a view object containing key-value pairs.
    - `get(key, default)`: Returns the value for the specified key if it exists; otherwise, returns the default value.
    - `pop(key)`: Removes and returns the value for the specified key.
    - `update(dict)`: Updates the dictionary with elements from another dictionary.
    """)
    
    st.subheader("Real-time Examples")
    st.write("""
    1. **Set Example**: Use a set to store unique hashtags in a social media application.
       ```python
       hashtags = {"#learning", "#python", "#coding"}
       hashtags.add("#streamlit")
       print(hashtags)  # Output: {'#coding', '#streamlit', '#python', '#learning'}
       ```
       
    2. **Dictionary Example**: Use a dictionary to store and retrieve user profiles.
       ```python
       users = {"john_doe": {"age": 30, "email": "john@example.com"},
                "jane_doe": {"age": 25, "email": "jane@example.com"}}
       print(users["john_doe"]["email"])  # Output: john@example.com
       ```
    """)

# Activities
elif tab_choice == "Activities":
    st.header("Experiential Learning: Code Review Session")
    st.write("**Activity:** Form teams of 4-6 students, each assigned a randomly generated team name.")
    if st.button("Generate Team Name"):
        st.write(f"Your Team Name: {generate_team_name()}")
    st.write("""
    The moderator will randomly select a student from each team to start writing a program. 
    Each subsequent student continues the program. The team’s final output will be assessed 
    for logical correctness. Peer assessment will be conducted via WhatsApp voting based on 
    the final output's correctness and creativity.
    """)

    st.header("Participatory Learning: Think-Pair-Share Activities")
    st.write("**Guidelines:**")
    st.write("""
    1. **Think:** Each student reflects individually on a thought-provoking question related to the lesson. 
       Example question: "How would you use sets to optimize search queries in a database?"
    2. **Pair:** Students pair up to discuss their ideas. In this stage, students should focus on both explaining 
       their thought process and challenging each other's ideas in a humorous and constructive manner.
    3. **Share:** Pairs share their discussion results with the larger group. Presentations should be engaging, 
       and students are encouraged to use creative analogies or examples. Each pair should be prepared to answer 
       questions from their peers.
    """)

# Lab Exercise
elif tab_choice == "Lab Exercise":
    st.header("Lab Exercise: Implement Set for Social Media Tagging")

    st.subheader("Aim")
    st.write("""
    The objective of this lab exercise is to develop a Python program that uses sets 
    to manage and analyze unique social media tags, optimizing the process for 
    content categorization and trend analysis in a social media platform.
    """)

    st.subheader("Steps")
    st.write("""
    1. **Initialization**: Start by creating an empty set to store tags.
       ```python
       tags = set()
       ```
    2. **Adding Tags**: Implement functionality to add new tags to the set.
       ```python
       def add_tag(tag):
           tags.add(tag)
       add_tag("#Python")
       add_tag("#AI")
       ```
    3. **Check for Duplicates**: Ensure that no duplicate tags are added.
       ```python
       add_tag("#Python")  # This will not create a duplicate entry
       print(tags)  # Output: {'#AI', '#Python'}
       ```
    4. **Tag Analysis**: Develop functions to analyze tag trends.
       ```python
       def common_tags(other_tags):
           return tags.intersection(other_tags)
       print(common_tags({"#Python", "#DataScience"}))  # Output: {'#Python'}
       ```
    5. **Suggest Tags**: Create a feature to suggest new tags based on trends.
       ```python
       def suggest_tags(trending_tags):
           popular_tags = {"#AI", "#MachineLearning", "#BigData", "#IoT"}
           return trending_tags.difference(popular_tags)
       current_tags = {"#AI", "#Python", "#HealthTech"}
       print(suggest_tags(current_tags))  # Output: {'#python', '#healthtech'}
       ```

    """)

    st.subheader("Tentative Output")
    st.write("""
    **Expected Output**:
    - The program successfully tracks, manages, and displays unique tags.
    - Users receive real-time suggestions based on trending tags.
    - The system ensures efficient management of tags without duplicates.

    **Sample Output**:
    ```
    Unique Tags Used:
    #ai
    #healthtech
    #python

    Suggested New Tags:
    #healthtech
    ```
    """)

# Running the app
st.sidebar.title("Lecture Series Menu")
st.sidebar.info("Choose a section to explore")
st.sidebar.success("Interactive Learning Awaits!")
