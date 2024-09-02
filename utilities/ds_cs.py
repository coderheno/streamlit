import streamlit as st

def python_data_structures_guide():
    st.title("Python Data Structures Cheat Sheet")

    st.sidebar.title("Select a Tab")
    option = st.sidebar.radio("Choose one", [
        'Lists', 
        'Tuples', 
        'Sets', 
        'Dictionaries', 
        'Strings',
        'Advanced Topics',
        'Real-World Examples',
        'Performance and Error Handling',
        'Quizzes and Exercises',
        'Resources and Conclusion'
    ])

    if option == 'Lists':
        # Basic Lists Information
        st.header("Lists")
        st.write("""
        **Definition**: An ordered, mutable collection that can hold items of different types.
        **Syntax**: `list_name = [item1, item2, item3, ...]`
        """)
        
        st.subheader("Common List Operations and Methods")
        st.markdown("""
        - **Create a List**: `my_list = [1, 2, 3]`
        - **Access Elements**: `my_list[0]` (Accesses the first element)
        - **Negative Indexing**: `my_list[-1]` (Accesses the last element)
        - **Slicing**: `my_list[1:3]` (Returns a sublist `[2, 3]`)
        - **Length**: `len(my_list)` (Returns the number of elements)
        - **Check Existence**: `3 in my_list` (Returns `True` if 3 exists in the list)
        - **Concatenation**: `my_list + [4, 5]` (Returns `[1, 2, 3, 4, 5]`)
        - **Repetition**: `my_list * 2` (Returns `[1, 2, 3, 1, 2, 3]`)
        """)
        
        st.subheader("List Methods with Examples")
        st.code("""
# Create a List
my_list = [1, 2, 3]

# Append
my_list.append(4)  # my_list becomes [1, 2, 3, 4]

# Extend
my_list.extend([5, 6])  # my_list becomes [1, 2, 3, 4, 5, 6]

# Insert
my_list.insert(1, 'a')  # my_list becomes [1, 'a', 2, 3, 4, 5, 6]

# Remove
my_list.remove(3)  # my_list becomes [1, 'a', 2, 4, 5, 6]

# Pop
last_item = my_list.pop()  # Removes and returns 6, my_list becomes [1, 'a', 2, 4, 5]

# Index
index_of_a = my_list.index('a')  # Returns 1

# Count
count_of_2 = my_list.count(2)  # Returns 1

# Sort
numeric_list = [3, 1, 4, 2]
numeric_list.sort()  # numeric_list becomes [1, 2, 3, 4]

# Reverse
numeric_list.reverse()  # numeric_list becomes [4, 3, 2, 1]
        """, language='python')

        st.subheader("Streamlit Example - Working with Lists")
        list_example = [1, 2, 3, 4, 5]
        element = st.number_input("Enter a number to add to the list:", value=0, step=1)
        if st.button("Add to List"):
            list_example.append(element)
        st.write("Updated List:", list_example)

    elif option == 'Tuples':
        # Tuples Information
        st.header("Tuples")
        st.write("""
        **Definition**: An ordered, immutable collection. Tuples are used for fixed collections of items.
        **Syntax**: `tuple_name = (item1, item2, item3, ...)`
        """)

        st.subheader("Common Tuple Operations")
        st.markdown("""
        - **Create a Tuple**: `my_tuple = (1, 2, 3)`
        - **Single Element Tuple**: `single = (1,)` (Note the comma)
        - **Access Elements**: `my_tuple[0]` (Accesses the first element)
        - **Negative Indexing**: `my_tuple[-1]` (Accesses the last element)
        - **Slicing**: `my_tuple[1:3]` (Returns a sub-tuple `(2, 3)`)
        - **Length**: `len(my_tuple)` (Returns the number of elements)
        - **Check Existence**: `3 in my_tuple` (Returns `True` if 3 exists in the tuple)
        - **Concatenation**: `my_tuple + (4, 5)` (Returns `(1, 2, 3, 4, 5)`)
        - **Repetition**: `my_tuple * 2` (Returns `(1, 2, 3, 1, 2, 3)`)
        """)

        st.subheader("Tuple Methods with Examples")
        st.code("""
# Create a Tuple
my_tuple = (1, 2, 3, 4, 5)

# Count occurrences
count_of_2 = my_tuple.count(2)  # Returns 1

# Index of an element
index_of_4 = my_tuple.index(4)  # Returns 3
        """, language='python')

        st.subheader("Streamlit Example - Working with Tuples")
        st.write("Tuples are immutable. Here's a fixed tuple example:")
        tuple_example = (1, 2, 3, 4, 5)
        st.write("Tuple:", tuple_example)

    elif option == 'Sets':
        # Sets Information
        st.header("Sets")
        st.write("""
        **Definition**: An unordered collection of unique elements. Sets do not allow duplicate items.
        **Syntax**: `set_name = {item1, item2, item3, ...}`
        """)

        st.subheader("Common Set Operations")
        st.markdown("""
        - **Create a Set**: `my_set = {1, 2, 3}`
        - **Add Element**: `my_set.add(4)` (Adds `4` to the set)
        - **Remove Element**: `my_set.remove(3)` (Removes `3` from the set)
        - **Length**: `len(my_set)` (Returns the number of elements)
        - **Check Existence**: `2 in my_set` (Returns `True` if 2 exists in the set)
        - **Union**: `set1 | set2` or `set1.union(set2)` (Returns a set with all elements from both sets)
        - **Intersection**: `set1 & set2` or `set1.intersection(set2)` (Returns a set with common elements)
        - **Difference**: `set1 - set2` or `set1.difference(set2)` (Returns a set with elements in `set1` but not in `set2`)
        - **Symmetric Difference**: `set1 ^ set2` or `set1.symmetric_difference(set2)` (Returns a set with elements in either set but not both)
        """)

        st.subheader("Set Methods with Examples")
        st.code("""
# Create a Set
my_set = {1, 2, 3, 4, 5}

# Add
my_set.add(6)  # my_set becomes {1, 2, 3, 4, 5, 6}

# Remove
my_set.remove(2)  # my_set becomes {1, 3, 4, 5, 6}

# Discard (no error if element is not present)
my_set.discard(10)  # my_set remains {1, 3, 4, 5, 6}

# Pop (removes and returns an arbitrary element)
popped_element = my_set.pop()  # my_set becomes {3, 4, 5, 6}

# Clear
my_set.clear()  # my_set becomes set()
        """, language='python')

        st.subheader("Streamlit Example - Working with Sets")
        set_example = {1, 2, 3, 4, 5}
        element = st.number_input("Enter a number to add to the set:", value=0, step=1)
        if st.button("Add to Set"):
            set_example.add(element)
        st.write("Updated Set:", set_example)

    elif option == 'Dictionaries':
        # Dictionaries Information
        st.header("Dictionaries")
        st.write("""
        **Definition**: An unordered collection of key-value pairs. Each key must be unique.
        **Syntax**: `dict_name = {key1: value1, key2: value2, ...}`
        """)

        st.subheader("Common Dictionary Operations")
        st.markdown("""
        - **Create a Dictionary**: `my_dict = {'a': 1, 'b': 2, 'c': 3}`
        - **Access Value**: `my_dict['a']` (Returns `1`)
        - **Add/Update Value**: `my_dict['d'] = 4` (Adds a new key-value pair or updates the value if the key exists)
        - **Remove Key**: `del my_dict['b']` (Removes the key `'b'`)
        - **Length**: `len(my_dict)` (Returns the number of key-value pairs)
        - **Check Key Existence**: `'a' in my_dict` (Returns `True` if `'a'` is a key)
        - **Get Keys**: `my_dict.keys()` (Returns a view of all keys)
        - **Get Values**: `my_dict.values()` (Returns a view of all values)
        - **Get Key-Value Pairs**: `my_dict.items()` (Returns a view of all key-value pairs)
        """)

        st.subheader("Dictionary Methods with Examples")
        st.code("""
# Create a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Get Value
value_a = my_dict.get('a')  # Returns 1

# Pop
value_c = my_dict.pop('c')  # Removes 'c' and returns 3

# Pop Item (removes and returns an arbitrary key-value pair)
key_value = my_dict.popitem()  # Example Output: ('b', 2)

# Clear
my_dict.clear()  # my_dict becomes {}

# Update
my_dict.update({'d': 4, 'e': 5})  # Adds/updates keys 'd' and 'e'
        """, language='python')

        st.subheader("Streamlit Example - Working with Dictionaries")
        dict_example = {'a': 1, 'b': 2, 'c': 3}
        key = st.text_input("Enter a key to add/update")
        value = st.number_input("Enter a value", value=0, step=1)
        if st.button("Add/Update Dictionary"):
            dict_example[key] = value
        st.write("Updated Dictionary:", dict_example)

    elif option == 'Strings':
        # Strings Information
        st.header("Strings")
        st.write("""
        **Definition**: An immutable sequence of characters.
        **Syntax**: `string_name = "Your string here"`
        """)

        st.subheader("Common String Operations and Methods")
        st.markdown("""
        - **Create a String**: `my_string = "Hello, World!"`
        - **Access Character**: `my_string[0]` (Returns `'H'`)
        - **Negative Indexing**: `my_string[-1]` (Returns `'!'`)
        - **Slicing**: `my_string[0:5]` (Returns `'Hello'`)
        - **Length**: `len(my_string)` (Returns the number of characters)
        - **Concatenation**: `my_string + " How are you?"` (Returns `'Hello, World! How are you?'`)
        - **Repetition**: `my_string * 2` (Returns `'Hello, World!Hello, World!'`)
        - **Check Substring**: `'Hello' in my_string` (Returns `True`)
        """)

        st.subheader("String Methods with Examples")
        st.code("""
# Create a String
my_string = "Hello, World!"

# Upper
upper_string = my_string.upper()  # Returns 'HELLO, WORLD!'

# Lower
lower_string = my_string.lower()  # Returns 'hello, world!'

# Find
position = my_string.find('World')  # Returns 7

# Replace
replaced_string = my_string.replace('World', 'There')  # Returns 'Hello, There!'

# Strip (removes leading/trailing whitespace)
trimmed_string = my_string.strip()

# Split (splits into a list by separator)
split_list = my_string.split(', ')  # Returns ['Hello', 'World!']

# Join (joins elements of a list into a single string)
joined_string = '-'.join(['Hello', 'World'])  # Returns 'Hello-World'

# Count occurrences
count_of_l = my_string.count('l')  # Returns 3
        """, language='python')

        st.subheader("Streamlit Example - Working with Strings")
        string_example = "Hello, World!"
        replace_word = st.text_input("Replace 'World' with:", "There")
        modified_string = string_example.replace("World", replace_word)
        st.write("Updated String:", modified_string)

    elif option == 'Advanced Topics':
        # Advanced Topics Information
        st.header("Advanced Topics")
        st.write("Explore advanced operations and techniques for Python data structures.")
        
        st.subheader("List Comprehensions")
        st.write("List comprehensions provide a concise way to create lists.")
        st.code("""
# List Comprehension Example
squares = [x ** 2 for x in range(10)]  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        """, language='python')
        
        st.subheader("Tuple Unpacking")
        st.write("Tuples can be used to assign multiple variables in a single statement.")
        st.code("""
# Tuple Unpacking Example
person = ('John', 'Doe', 30)
first_name, last_name, age = person
        """, language='python')
        
        st.subheader("Dictionary Comprehensions")
        st.write("Like list comprehensions, dictionary comprehensions provide a quick way to create dictionaries.")
        st.code("""
# Dictionary Comprehension Example
squares = {x: x ** 2 for x in range(6)}  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        """, language='python')
        
        st.subheader("Frozen Sets")
        st.write("Frozen sets are immutable sets and can be used as keys in dictionaries.")
        st.code("""
# Frozen Set Example
frozen_set = frozenset([1, 2, 3, 4])
        """, language='python')
        
        st.subheader("String Formatting")
        st.write("Python offers multiple ways to format strings.")
        st.code("""
name = "Alice"
age = 30

# Using f-strings
formatted_string = f"{name} is {age} years old."  # Output: 'Alice is 30 years old.'

# Using str.format()
formatted_string = "{} is {} years old.".format(name, age)

# Using %-formatting
formatted_string = "%s is %d years old." % (name, age)
        """, language='python')

    elif option == 'Real-World Examples':
        # Real-World Examples
        st.header("Real-World Examples")
        st.write("See how data structures can be applied in real-world scenarios.")
        
        st.subheader("Using Lists for Task Management")
        st.write("Lists can be used to manage a to-do list:")
        st.code("""
tasks = ["buy groceries", "clean the house", "pay bills"]
tasks.append("call mom")
tasks.remove("pay bills")
        """, language='python')
        
        st.subheader("Using Tuples for GPS Coordinates")
        st.write("Tuples can store immutable data like GPS coordinates:")
        st.code("""
coordinates = (40.7128, -74.0060)  # New York City
        """, language='python')
        
        st.subheader("Using Sets for Removing Duplicates")
        st.write("Sets are useful for storing unique items and removing duplicates:")
        st.code("""
items = ["apple", "orange", "apple", "pear"]
unique_items = set(items)  # Output: {'apple', 'orange', 'pear'}
        """, language='python')
        
        st.subheader("Using Dictionaries for a Contact Book")
        st.write("Dictionaries can be used to store key-value pairs, such as names and phone numbers:")
        st.code("""
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
phone_number = contacts["Alice"]
        """, language='python')

    elif option == 'Performance and Error Handling':
        # Performance and Error Handling
        st.header("Performance and Error Handling")
        st.write("Learn about the performance implications of using different data structures and how to handle common errors.")
        
        st.subheader("Performance Considerations")
        st.write("Understand the time complexity of common operations:")
        st.markdown("""
        - **Lists**: Accessing elements is O(1), but inserting/removing elements can be O(n).
        - **Tuples**: Similar to lists, but immutable. Good for fixed collections.
        - **Sets**: Fast membership tests O(1), but order is not preserved.
        - **Dictionaries**: Fast lookup, insertion, and deletion O(1) due to hash tables.
        """)
        
        st.subheader("Common Errors and How to Handle Them")
        
        st.write("**List Index Out of Range**")
        st.code("""
my_list = [1, 2, 3]
try:
    element = my_list[5]
except IndexError:
    print("Index out of range")
        """, language='python')
        
        st.write("**Tuple TypeError (immutability)**")
        st.code("""
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 5
except TypeError:
    print("Tuples are immutable")
        """, language='python')
        
        st.write("**Set KeyError**")
        st.code("""
my_set = {1, 2, 3}
try:
    my_set.remove(4)
except KeyError:
    print("Element not found in set")
        """, language='python')
        
        st.write("**Dictionary KeyError**")
        st.code("""
my_dict = {'a': 1, 'b': 2}
try:
    value = my_dict['c']
except KeyError:
    print("Key not found in dictionary")
        """, language='python')

    elif option == 'Quizzes and Exercises':
        # Quizzes and Exercises
        st.header("Quizzes and Exercises")
        st.write("Test your knowledge with these interactive quizzes and exercises.")
        
        st.subheader("Quiz: Understanding Lists")
        st.write("What is the output of the following code?")
        st.code("""
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
        """, language='python')
        answer = st.text_input("Your Answer:", "")
        if answer == "[1, 2, 3, 4]":
            st.success("Correct!")
        else:
            st.error("Try again!")
        
        st.subheader("Exercise: Working with Tuples")
        st.write("Create a tuple with the values `(1, 2, 3, 4)` and find the index of the number `3`.")
        st.code("""
my_tuple = (1, 2, 3, 4)
index_of_3 = my_tuple.index(3)
        """, language='python')
        
        st.subheader("Quiz: Understanding Sets")
        st.write("What will be the output of the following code?")
        st.code("""
my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.add(3)
print(len(my_set))
        """, language='python')
        answer = st.text_input("Your Answer (Sets):", "")
        if answer == "5":
            st.success("Correct!")
        else:
            st.error("Try again!")
        
        st.subheader("Exercise: Working with Dictionaries")
        st.write("Create a dictionary with keys `a`, `b`, and `c` with values `1`, `2`, and `3`. Then, update the value for key `b` to `20`.")
        st.code("""
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['b'] = 20
        """, language='python')

    elif option == 'Resources and Conclusion':
        # Resources and Conclusion
        st.header("Resources and Conclusion")
        st.write("Review key concepts and find additional resources to continue learning.")
        
        st.subheader("Summary of Data Structures")
        st.write("Each data structure has its unique properties and use cases:")
        st.markdown("""
        - **Lists**: Ordered, mutable, and allows duplicates. Good for sequential data.
        - **Tuples**: Ordered, immutable, and allows duplicates. Useful for fixed collections.
        - **Sets**: Unordered, mutable, and only allows unique items. Great for membership tests.
        - **Dictionaries**: Unordered, mutable, and maps keys to values. Ideal for key-value pairs.
        - **Strings**: Immutable sequences of characters. Essential for text processing.
        """)
        
        st.subheader("Further Reading and Resources")
        st.write("Expand your knowledge with these resources:")
        st.markdown("""
        - [Python Official Documentation](https://docs.python.org/3/tutorial/datastructures.html)
        - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
        - [Python for Everybody](https://www.py4e.com/)
        - [Real Python](https://realpython.com/)
        """)
        
        st.subheader("Conclusion")
        st.write("Understanding Python data structures is crucial for efficient programming. They provide the foundation for organizing and manipulating data effectively, enabling the development of powerful and scalable applications.")

if __name__ == "__main__":
    python_data_structures_guide()
