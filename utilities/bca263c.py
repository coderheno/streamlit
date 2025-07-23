import streamlit as st

st.set_page_config(page_title="List vs Tuple vs Set Function Comparison", layout="wide")
st.title("🔍 Python Data Structures: List vs Tuple vs Set")

# Summary Table
st.markdown("### List vs Tuple vs Set")

st.markdown("""
| **Characteristic**        | **List**               | **Tuple**              | **Set**                            |
|---------------------------|------------------------|------------------------|-------------------------------------|
| Mutable                   | ✅ Yes                 | ❌ No                  | ✅ Yes                              |
| Ordered                   | ✅ Yes                 | ✅ Yes                 | ❌ No                               |
| Allows Duplicates         | ✅ Yes                 | ✅ Yes                 | ❌ No                               |
| Indexing / Slicing        | ✅ Supported           | ✅ Supported           | ❌ Not supported                    |
| Typical Use Case          | Dynamic items          | Fixed values/records   | Unique values / Fast membership    |
""", unsafe_allow_html=True)

# Function Table
st.markdown("### 🧮 Function Comparison Table (With Examples)")
st.markdown("""
| **Function / Feature**     | **List (`[]`)**                                              | **Tuple (`()`)**                                           | **Set (`{}` or `set()`)**                                        |
|----------------------------|--------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------|
| **1. `append()`**          | `fruits.append('apple')` → `['apple']`                      | ❌ Not available                                             | `colors.add('red')` → `{'red'}`                                 |
| **2. `insert()` / `add()`**| `fruits.insert(1, 'mango')` → `['apple', 'mango']`           | ❌ Not available                                             | `colors.add('blue')`                                            |
| **3. `remove()`**          | `fruits.remove('apple')`                                     | ❌ Not available                                             | `colors.remove('blue')`                                         |
| **4. `pop()`**             | `fruits.pop()` → removes last element                        | ❌ Not available                                             | `colors.pop()` → removes arbitrary item                         |
| **5. `count()`**           | `fruits.count('apple')` → `1`                                | `nums.count(2)` → `2`                                       | ❌ Not available                                                 |
| **6. `index()`**           | `fruits.index('apple')` → `0`                                | `nums.index(3)` → `1`                                       | ❌ Not available                                                 |
| **7. `sort()` / `sorted()`**| `fruits.sort()` → sorts list in place                      | ❌ Immutable – use `sorted(tuple)`                          | `sorted(colors)` → returns sorted list                          |
| **8. `reverse()`**         | `fruits.reverse()`                                           | ❌ Not available                                             | ❌ Not available                                                 |
| **9. `copy()`**            | `new_list = fruits.copy()`                                   | `new_tuple = tuple(old_tuple)`                             | `new_set = colors.copy()`                                       |
| **10. `clear()`**          | `fruits.clear()` → empties the list                          | ❌ Not available                                             | `colors.clear()` → empties the set                              |
""", unsafe_allow_html=True)

# Divider
st.markdown("---")

st.success("✅ CO2: Apply Programming logics using Control statements and functions.")


st.markdown("---")

# Function comparisons

# List Functions
st.markdown("### 📋 List Functions and Examples")

st.code("""
fruits = ['apple', 'banana', 'cherry']

# 1. append() - add item to end
fruits.append('orange')

# 2. insert() - add at specific position
fruits.insert(1, 'grape')

# 3. remove() - delete by value
fruits.remove('banana')

# 4. pop() - remove by index (last if not specified)
last = fruits.pop()

# 5. sort() - sort alphabetically
fruits.sort()

print(fruits)
""", language='python')
st.success("Use List when you need to frequently add, remove, or update elements.")

# Tuple Functions
st.markdown("### 🔐 Tuple Functions and Examples")

st.code("""
colors = ('red', 'blue', 'green', 'blue')

# 1. count() - how many times a value occurs
print(colors.count('blue'))  # Output: 2

# 2. index() - first index of value
print(colors.index('green'))  # Output: 2

# 3. len() - total elements
print(len(colors))  # Output: 4

# 4. tuple() - convert list to tuple
new_tuple = tuple(['a', 'b'])

# 5. unpacking
r, b, g, b2 = colors
""", language='python')
st.info("Tuples are used when you don’t want to change the data after creation.")

# Set Functions
st.markdown("### 🧮 Set Functions and Examples")

st.code("""
numbers = {1, 2, 3, 4}

# 1. add() - insert value
numbers.add(5)

# 2. remove() - remove value (KeyError if not found)
numbers.remove(3)

# 3. discard() - remove safely (no error)
numbers.discard(10)

# 4. union() - combine two sets
even = {2, 4, 6}
all_numbers = numbers.union(even)

# 5. intersection() - common elements
common = numbers.intersection(even)

print(numbers)
""", language='python')
st.warning("Use Set when you need only unique elements with fast operations.")

st.markdown("---")

# Summary
st.markdown("""
## 🧠 Summary

- **List**: Best for ordered, dynamic data where duplicates are allowed.
- **Tuple**: Ideal for constant data that shouldn't change.
- **Set**: Best when only unique values are needed and order doesn’t matter.

Explore these data structures to write cleaner and more efficient Python code!
""")
