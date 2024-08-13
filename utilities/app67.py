import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Python Learning Hub", layout="wide")

# Create the tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Recap", "Lecture Notes", "Lab Exercises", "Activities", "List vs Tuple vs Set"])

# Tab 1: Recap
with tab1:
    st.header("Python List vs Tuple - The Great Debate")
    
    st.write("Get ready for a hilarious showdown: Python Lists vs Tuples, set in the world of **'Bollywood Stars vs Cricket Legends'**!")

    st.subheader("Debate Guidelines")
    st.write("""
    - **Teams**: Divide into two teams: **Bollywood Fans (Lists)** and **Cricket Fans (Tuples)**.
    - **Preparation**: Each team prepares arguments supporting their data structure. 
    - **Focus Areas**: Versatility, stability, and performance under pressure. For instance, why might a Bollywood star (List) need to take on different roles, or why a cricket legend (Tuple) prefers consistency?
    - **Time Limit**: Each team gets 3 minutes to present their arguments.
    - **Rebuttal**: After presentations, each team gets 2 minutes for rebuttal.
    """)

    st.subheader("Rubrics")
    st.write("""
    - **Wittiness (10 points)**: How cleverly you can blend Python with Bollywood or cricket references.
    - **Python Knowledge (10 points)**: Your depth of understanding of Python Lists and Tuples.
    - **Audience Engagement (10 points)**: How well you keep your audience entertained.
    - **Bollywood/Cricket Reference Bonus (5 points)**: Use iconic Bollywood dialogues or cricket commentary to strengthen your arguments.
    """)

    st.subheader("Punishments")
    st.write("""
    - **Losing Team Punishment**: The losing team must recreate a popular Movie dance, but explain each step as if it's a Python function.
    - **Most Over-the-top Argument**: The person with the most exaggerated argument must explain the difference between Lists and Tuples using cricket commentary or a comedy monologue.
    - **Forgot to Use a Python Term**: Anyone who forgets a crucial Python term during the debate has to write it 10 times on the whiteboard in binary or Hindi.
    """)


# Tab 2: Lecture Notes
with tab2:
    st.header("Lecture Notes: Sets and Dictionaries")
    
    st.subheader("Sets")
    st.write("""
    **Definition**: A set is an unordered collection of unique elements. 
    **Example**:
    ```python
    my_set = {1, 2, 3, 4, 5}
    ```
    
    **Built-in Methods**:
    - `add()`: Adds an element to the set.
        ```python
        my_set.add(6)
        ```
    - `remove()`: Removes an element from the set.
        ```python
        my_set.remove(3)
        ```
    - `union()`: Combines elements from two sets.
        ```python
        another_set = {4, 5, 6, 7}
        combined_set = my_set.union(another_set)
        ```
    
    **Basic Set Operations**:
    - **Union**: Combines all elements.
    - **Intersection**: Finds common elements.
    - **Difference**: Finds elements only in one set.
    
    **Mathematical Set Operations**:
    - `A | B`: Union of sets A and B.
    - `A & B`: Intersection of sets A and B.
    - `A - B`: Difference between sets A and B.
    
    **Variety of Sets**:
    - **Empty Set**: `empty_set = set()`
    - **Finite Set**: `finite_set = {1, 2, 3}`
    - **Infinite Set**: `infinite_set = set(range(1, 1000000))`
    """)

    st.subheader("Dictionaries")
    st.write("""
    **Definition**: A dictionary is a collection of key-value pairs.
    **Example**:
    ```python
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
    ```
    
    **Accessing Elements**:
    - `my_dict['name']` returns `'Alice'`
    
    **Basic Operations**:
    - **Add**: Add a new key-value pair.
        ```python
        my_dict['occupation'] = 'Adventurer'
        ```
    - **Update**: Update an existing value.
        ```python
        my_dict['age'] = 26
        ```
    - **Delete**: Remove a key-value pair.
        ```python
        del my_dict['city']
        ```
    
    **Methods**:
    - `keys()`: Returns a list of keys.
        ```python
        list(my_dict.keys())
        ```
    - `values()`: Returns a list of values.
        ```python
        list(my_dict.values())
        ```
    - `items()`: Returns a list of tuples (key, value).
        ```python
        list(my_dict.items())
        ```
    """)

# Tab 3: Lab Exercises
with tab3:
    st.header("Lab Exercises: Set and Dictionary Implementation")
    
    st.subheader("Program 5: Implement Dictionary - Movie Database")
    st.write("**Objective**: Create a dictionary to manage a simple movie database where users can add, update, and delete movies.")
    
    st.write("**Steps**:")
    st.write("""
    1. **Define the Dictionary**: Start by defining a dictionary with movie names as keys and release years as values.
        ```python
        movie_db = {'Inception': 2010, 'The Matrix': 1999, 'Interstellar': 2014}
        ```
    2. **Add Movies**: Allow users to add a new movie to the database.
        ```python
        movie_db['Avatar'] = 2009
        ```
    3. **Update Movies**: Provide functionality to update the release year of a movie.
        ```python
        movie_db['The Matrix'] = 1999
        ```
    4. **Delete Movies**: Enable users to delete a movie from the database.
        ```python
        del movie_db['Inception']
        ```
    5. **Display Database**: Print the entire database in a user-friendly format.
        ```python
        for movie, year in movie_db.items():
            print(f'{movie}: Released in {year}')
        ```

    **Expected Output**: A functional movie database that allows managing movies efficiently.
    """)

    st.subheader("Program 6: Implement Set - Superhero Abilities")
    st.write("**Objective**: Create a set to manage a superhero's abilities, including adding, removing, and performing operations like union and intersection.")

    st.write("**Steps**:")
    st.write("""
    1. **Define the Set**: Start by defining a set with initial superhero abilities.
        ```python
        abilities = {'Flying', 'Strength', 'Invisibility'}
        ```
    2. **Add Abilities**: Allow users to add a new ability to the set.
        ```python
        abilities.add('Speed')
        ```
    3. **Remove Abilities**: Provide functionality to remove an ability.
        ```python
        abilities.remove('Invisibility')
        ```
    4. **Union of Abilities**: Combine abilities from another superhero.
        ```python
        more_abilities = {'Telepathy', 'Strength'}
        combined_abilities = abilities.union(more_abilities)
        ```
    5. **Intersection of Abilities**: Find common abilities with another superhero.
        ```python
        common_abilities = abilities.intersection(more_abilities)
        ```

    **Expected Output**: A functional set representing a superhero's abilities with the ability to execute various operations.
    """)

# Tab 4: Activities
with tab4:
    st.header("Experiential and Participatory Learning Activities")
    
    st.subheader("Experiential Learning: Code Review Session")
    st.write("""
    **Objective**: Engage in a code review session where students review each other's code, focusing on readability, efficiency, and Python best practices.
    
    **Guidelines**:
    - **Pair Up**: Students should pair up with a partner.
    - **Review Criteria**: Focus on code readability, efficiency, and adherence to Python conventions.
    - **Feedback**: Provide constructive feedback, highlighting both strengths and areas for improvement.
    - **Follow-Up**: Students should make the necessary changes based on feedback and submit a revised version.
    
    **Task**:
    - Review a partner's code for a dictionary implementation, focusing on edge cases and error handling.
    """)

    st.subheader("Participatory Learning: Think-Pair-Share Activities")
    st.write("""
    **Objective**: Foster collaborative problem-solving by having students think about a problem individually, pair up to discuss, and then share their solutions with the class.
    
    **Guidelines**:
    - **Think**: Each student considers the problem independently for 5 minutes.
    - **Pair**: Students pair up with a classmate and discuss their solutions for 10 minutes.
    - **Share**: Pairs present their combined solution to the class.
    
    **Task**:
    - Problem: "Given two dictionaries, combine them into one, handling overlapping keys by summing their values."
    - Expected Outcome: A combined dictionary with correctly summed values for overlapping keys.
    """)
with tab5:
    st.header("Comprehensive Comparison: List vs Tuple vs Set")
    
    st.subheader("Overview")
    st.write("""
    Python offers three common data structures: **Lists**, **Tuples**, and **Sets**. Each has its unique properties, use cases, and behaviors. Understanding the differences and similarities can help you choose the right structure for your tasks.
    """)

    st.subheader("1. Types and Definitions")
    st.write("""
    - **List**: An ordered, mutable collection of elements.
    - **Tuple**: An ordered, immutable collection of elements.
    - **Set**: An unordered, mutable collection of unique elements.
    """)

    st.subheader("2. Common Use Cases")
    st.write("""
    - **List**: Best when you need an ordered collection that you can modify. Commonly used for storing sequences, such as a list of items.
    - **Tuple**: Best for storing fixed collections of items that should not be changed. Often used for records or fixed data.
    - **Set**: Best for membership tests and eliminating duplicates. Ideal for storing unique items and performing set operations.
    """)

    st.subheader("3. Examples")
    st.write("""
    **List Example**:
    ```python
    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
    ```

    **Tuple Example**:
    ```python
    my_tuple = (1, 2, 3, 4, 5)
    print(my_tuple)  # Output: (1, 2, 3, 4, 5)
    ```

    **Set Example**:
    ```python
    my_set = {1, 2, 3, 4, 5}
    my_set.add(6)
    print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
    ```
    """)

    st.subheader("4. Key Properties")
    st.write("""
    - **List**:
        - **Order**: Maintains the order of elements.
        - **Mutability**: Elements can be changed, added, or removed.
        - **Duplicates**: Allows duplicate elements.
    - **Tuple**:
        - **Order**: Maintains the order of elements.
        - **Mutability**: Immutable; elements cannot be changed after creation.
        - **Duplicates**: Allows duplicate elements.
    - **Set**:
        - **Order**: Does not maintain any order of elements.
        - **Mutability**: Mutable; elements can be added or removed, but no duplicates are allowed.
        - **Duplicates**: Does not allow duplicate elements.
    """)

    st.subheader("5. Common Functions and Methods")
    st.write("""
    **List Functions and Methods**:
    - `append()`: Adds an element to the end.
        ```python
        my_list.append(7)
        ```
    - `remove()`: Removes the first occurrence of a specified value.
        ```python
        my_list.remove(3)
        ```
    - `sort()`: Sorts the list in place.
        ```python
        my_list.sort()
        ```

    **Tuple Functions and Methods**:
    - `count()`: Returns the number of occurrences of a specified value.
        ```python
        my_tuple.count(3)
        ```
    - `index()`: Returns the index of the first occurrence of a specified value.
        ```python
        my_tuple.index(4)
        ```

    **Set Functions and Methods**:
    - `add()`: Adds an element to the set.
        ```python
        my_set.add(7)
        ```
    - `remove()`: Removes a specified element from the set.
        ```python
        my_set.remove(2)
        ```
    - `union()`: Returns a new set with elements from both sets.
        ```python
        another_set = {8, 9}
        union_set = my_set.union(another_set)
        ```
    """)

    st.subheader("6. Performance Considerations")
    st.write("""
    - **Lists**: Accessing elements by index is O(1). Insertion and deletion (at the end) are O(1); inserting or deleting in the middle is O(n).
    - **Tuples**: Similar to lists, but since they are immutable, they can be more memory-efficient.
    - **Sets**: Membership tests are O(1) on average, making sets efficient for lookups.
    """)

    st.subheader("7. Conclusion")
    st.write("""
    - Use **Lists** when you need a versatile, ordered collection that can grow and shrink.
    - Use **Tuples** for data that should not change and where order matters.
    - Use **Sets** for unique collections where order is not important, and you need fast membership tests.
    """)

