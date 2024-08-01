import streamlit as st

def main():
    st.title("Introduction to Python Data Types and Structures")

    # Create tabs
    tabs = st.tabs([
        "Introduction",
        "Lists: Accessing Elements",
        "Basic List Operations",
        "Built-in Methods",
        "Activities"
    ])

    # Introduction Tab
    with tabs[0]:
        st.title("Introduction to Python Data Types and Data Structures")
        st.write("""
            Python has various data types and data structures that are essential for programming. 
            Understanding these is crucial for efficient coding and data manipulation. This section covers:
            - Basic data types: int, float, str, bool
            - Data structures: list, tuple, set, dict
            - Their usage and operations
        """)
        compare_lists_and_arrays()

    # Lists: Accessing Elements Tab
    with tabs[1]:
        st.header("Lists: Accessing Elements")
        st.write("""
            Lists are one of the most versatile data structures in Python. You can access elements in a list using indexing.
            
            **Indexing:**
            Python lists use zero-based indexing. The first element has index 0, the second has index 1, and so on. Negative indexing allows access from the end of the list.
            
            **Examples:**
            ```python
            # Creating a list
            my_list = [10, 20, 30, 40, 50]

            # Accessing elements
            first_element = my_list[0]   # 10
            second_element = my_list[1]  # 20
            third_element = my_list[2]   # 30

            # Negative indexing
            last_element = my_list[-1]   # 50
            second_last_element = my_list[-2]  # 40
            ```
            
            **Slicing Lists:**
            Slicing allows you to access a subset of the list.
            
            **Examples:**
            ```python
            # Slicing a list
            subset = my_list[1:4]    # [20, 30, 40] (elements from index 1 to 3)
            subset_end = my_list[:3] # [10, 20, 30] (elements from start to index 2)
            subset_start = my_list[2:] # [30, 40, 50] (elements from index 2 to end)
            ```
            
            **Step in Slicing:**
            You can also specify a step to skip elements.
            
            **Examples:**
            ```python
            # Step in slicing
            stepped = my_list[::2]   # [10, 30, 50] (every second element)
            reversed_list = my_list[::-1]  # [50, 40, 30, 20, 10] (reversed list)
            ```
        """)

    # Basic List Operations Tab
    with tabs[2]:
        st.header("Basic List Operations")
        st.write("""
            Lists support a variety of operations for adding, removing, and modifying elements.
            
            **Examples:**
            ```python
            # Creating a list
            my_list = [10, 20, 30]

            # Append an element
            my_list.append(40)       # [10, 20, 30, 40]

            # Insert an element at a specific position
            my_list.insert(1, 15)    # [10, 15, 20, 30, 40]

            # Remove an element by value
            my_list.remove(20)       # [10, 15, 30, 40]

            # Remove an element by index
            popped_element = my_list.pop(2)  # 30, my_list = [10, 15, 40]

            # Length of the list
            length = len(my_list)   # 3

            # Extend the list with another list
            my_list.extend([50, 60])  # [10, 15, 40, 50, 60]

            # Concatenate lists
            another_list = [70, 80]
            combined_list = my_list + another_list  # [10, 15, 40, 50, 60, 70, 80]

            # Repeat elements
            repeated_list = my_list * 2  # [10, 15, 40, 50, 60, 10, 15, 40, 50, 60]
            ```

            **List Comprehensions:**
            A concise way to create lists based on existing lists.

            **Examples:**
            ```python
            # List comprehension to create a new list with squared values
            squared_list = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

            # Filtering with list comprehension
            even_numbers = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
            ```
        """)

    # Built-in List Methods Tab
    with tabs[3]:
        st.header("Built-in List Methods")
        st.write("""
            Python provides several built-in methods to work with lists.
            
            **Examples:**
            ```python
            # Creating a list
            my_list = [10, 20, 30, 20]

            # Count occurrences of an element
            count = my_list.count(20)  # 2

            # Find index of an element
            index = my_list.index(30)  # 2

            # Sort the list in ascending order
            my_list.sort()  # [10, 20, 20, 30]

            # Reverse the list
            my_list.reverse()  # [30, 20, 20, 10]

            # Copy the list
            copied_list = my_list.copy()  # [30, 20, 20, 10]

            # Clear all elements from the list
            my_list.clear()  # []
            ```

            **More Advanced Operations:**
            ```python
            # Sort list in descending order
            my_list = [10, 30, 20, 40]
            my_list.sort(reverse=True)  # [40, 30, 20, 10]

            # Removing and returning last item
            last_item = my_list.pop()  # 10, my_list = [40, 30, 20]

            # Removing all occurrences of an element
            while 30 in my_list:
                my_list.remove(30)  # [40, 20]
            ```
        """)
   
    # Activities Tab
    with tabs[4]:
        st.header("Activities")
        st.write("Here are some fun and engaging activities to enhance your understanding of Python lists:")

        # Poster Presentation
        st.subheader("Poster Presentation: 'Python Lists in the Real World'")
        st.write("""
            **Objective:** Create and present a poster that demonstrates the use of Python lists in a real-world application.
            
            **Guidelines:**
            1. Choose a Real-World Scenario:
               - **E-Commerce:** Managing shopping carts or tracking orders.
               - **Social Media:** Handling posts, comments, or followers.
               - **Healthcare:** Tracking patient records or appointments.
               - **Finance:** Managing transactions or investment portfolios.
            2. Create a Poster:
               - Describe the chosen scenario.
               - Explain how Python lists are used.
               - Include sample code and visuals.
            3. Present and Discuss:
               - Present your poster and discuss its applications.
               - Share insights and answer questions.
        """)

        # Brainstorming
        st.subheader("Brainstorming: 'Innovative Uses of Lists Across Domains'")
        st.write("""
            **Objective:** Brainstorm creative uses of Python lists across different domains.
            
            **Guidelines:**
            1. Form Groups and Choose Domains:
               - **Education:** Tracking progress, class schedules, interactive tools.
               - **Travel:** Planning itineraries, booking, expense management.
               - **Sports:** Tracking statistics, game scores, team rosters.
               - **Entertainment:** Managing playlists, favorite movies, reviews.
            2. Generate and Share Ideas:
               - Discuss practical and innovative uses of lists.
               - Prepare a brief presentation of your ideas.
            3. Document Insights:
               - Record key ideas and applications.
               - Highlight unique uses of lists discovered during the session.
        """)


def compare_lists_and_arrays():
    st.header("Comparison: Python Lists vs C Arrays")

    st.write("""
    Python lists and C arrays are both data structures used to store collections of elements, but they have some key differences:
    """)

    # Declaration
    st.subheader("1. Declaration")
    st.write("""
    - **Python lists:** No explicit declaration needed. Create a list by assigning a value to a variable, e.g., `my_list = [1, 2, 3]`.
    - **C arrays:** Must be explicitly declared with a fixed size, e.g., `int my_array[3] = {1, 2, 3};`.
    """)

    # Size
    st.subheader("2. Size")
    st.write("""
    - **Python lists:** Dynamic size, can grow or shrink as elements are added or removed.
    - **C arrays:** Fixed size, determined at compile time.
    """)

    # Data Type
    st.subheader("3. Data Type")
    st.write("""
    - **Python lists:** Can store elements of any data type, including mixed types.
    - **C arrays:** Elements must be of the same data type.
    """)

    # Memory Allocation
    st.subheader("4. Memory Allocation")
    st.write("""
    - **Python lists:** Memory is managed automatically by Python's memory manager.
    - **C arrays:** Memory is manually managed by the programmer using pointers.
    """)

    # Indexing
    st.subheader("5. Indexing")
    st.write("""
    - **Python lists:** Support indexing, slicing, and negative indexing.
    - **C arrays:** Support indexing, but no slicing or negative indexing.
    """)

    # Operations
    st.subheader("6. Operations")
    st.write("""
    - **Python lists:** Support various methods like append, insert, remove, sort, etc.
    - **C arrays:** No built-in methods; operations must be implemented manually.
    """)

    st.subheader("Examples of Python List Operations")
    st.write("""
    **1. Adding Elements:**
    ```python
    my_list = [1, 2, 3]
    my_list.append(4)  # Adds 4 to the end of the list
    print(my_list)  # Output: [1, 2, 3, 4]
    ```

    **2. Inserting Elements:**
    ```python
    my_list = [1, 2, 3]
    my_list.insert(1, 'a')  # Inserts 'a' at index 1
    print(my_list)  # Output: [1, 'a', 2, 3]
    ```

    **3. Removing Elements:**
    ```python
    my_list = [1, 2, 3, 4, 2]
    my_list.remove(2)  # Removes the first occurrence of 2
    print(my_list)  # Output: [1, 3, 4, 2]
    ```

    **4. Popping Elements:**
    ```python
    my_list = [1, 2, 3, 4]
    popped_element = my_list.pop(2)  # Removes and returns the element at index 2
    print(popped_element)  # Output: 3
    print(my_list)  # Output: [1, 2, 4]
    ```

    **5. Slicing Lists:**
    ```python
    my_list = [1, 2, 3, 4, 5]
    sliced_list = my_list[1:4]  # Extracts elements from index 1 to 3 (4 is not included)
    print(sliced_list)  # Output: [2, 3, 4]
    ```

    **6. Reversing a List:**
    ```python
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()  # Reverses the list in place
    print(my_list)  # Output: [5, 4, 3, 2, 1]
    ```

    **7. Sorting a List:**
    ```python
    my_list = [3, 1, 4, 2, 5]
    my_list.sort()  # Sorts the list in ascending order
    print(my_list)  # Output: [1, 2, 3, 4, 5]
    ```

    **8. List Comprehensions:**
    ```python
    my_list = [1, 2, 3, 4, 5]
    squared_list = [x**2 for x in my_list]  # Creates a new list with the squares of each element
    print(squared_list)  # Output: [1, 4, 9, 16, 25]
    ```

    **9. Clearing a List:**
    ```python
    my_list = [1, 2, 3, 4]
    my_list.clear()  # Removes all elements from the list
    print(my_list)  # Output: []
    ```

    **10. Checking for Element Existence:**
    ```python
    my_list = [1, 2, 3, 4, 5]
    print(3 in my_list)  # Output: True
    print(6 in my_list)  # Output: False
    ```
    """)

    st.write("Let me know if you'd like me to elaborate on any of these points!")


if __name__ == "__main__":
    main()
