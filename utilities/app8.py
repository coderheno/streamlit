import streamlit as st
import numpy as np

# Title
st.title("NumPy Tutorial")

# Option selection
option = st.sidebar.selectbox(
    "Select Content Option",
    ("NUMPY Computation", "Aggregations", "Computation on Arrays", "Comparisons, Masks, and Boolean Arrays", 
     "Fancy Indexing", "Sorting Arrays", "Structured Data: NumPy’s Structured Array")
)

# Option content
if option == "NUMPY Computation":
    st.header("NUMPY Computation on NumPy")
    st.write("""
    - Introduction to NumPy library for numerical computations in Python.
    - Basic array operations such as creation, reshaping, and accessing elements.
    - Aggregation functions like sum, mean, max, and min for array analysis.
    - Performing mathematical computations on arrays using built-in functions.
    """)
    
    # Example: Basic array creation and aggregation
    st.subheader("Example: Basic Array Creation and Aggregation")
    arr = np.array([1, 2, 3, 4, 5])
    st.write("Array:", arr)
    st.write("Sum:", np.sum(arr))
    st.write("Mean:", np.mean(arr))
    st.write("Max:", np.max(arr))
    st.write("Min:", np.min(arr))
    
elif option == "Aggregations":
    st.header("Aggregations")
    st.write("""
    - Understanding the concept of aggregation in NumPy.
    - Performing aggregation operations like sum, mean, max, and min on arrays.
    - Exploring the axis parameter to specify the axis along which the aggregation is applied.
    - Using aggregation functions to analyze data and extract statistical information.
    """)
    
    # Example: Aggregation with axis parameter
    st.subheader("Example: Aggregation with Axis Parameter")
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    st.write("Array:", arr)
    st.write("Sum along axis 0:", np.sum(arr, axis=0))
    st.write("Sum along axis 1:", np.sum(arr, axis=1))
    
elif option == "Computation on Arrays":
    st.header("Computation on Arrays")
    st.write("""
    - Performing element-wise mathematical operations on NumPy arrays.
    - Exploring arithmetic operations such as addition, subtraction, multiplication, and division.
    - Broadcasting feature for performing operations on arrays of different shapes.
    - Utilizing universal functions (ufuncs) for efficient element-wise computations.
    """)
    
    # Example: Element-wise arithmetic operations
    st.subheader("Example: Element-wise Arithmetic Operations")
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])
    st.write("Array 1:", arr1)
    st.write("Array 2:", arr2)
    st.write("Addition:", arr1 + arr2)
    st.write("Subtraction:", arr1 - arr2)
    st.write("Multiplication:", arr1 * arr2)
    st.write("Division:", arr1 / arr2)
    
elif option == "Comparisons, Masks, and Boolean Arrays":
    st.header("Comparisons, Masks, and Boolean Arrays")
    st.write("""
    - Conducting element-wise comparisons between arrays.
    - Creating boolean arrays based on comparison results.
    - Using boolean indexing to filter and manipulate array elements.
    - Applying masks to perform conditional operations on arrays.
    """)
    
    # Example: Boolean indexing
    st.subheader("Example: Boolean Indexing")
    arr = np.array([1, 2, 3, 4, 5])
    mask = arr > 2
    st.write("Array:", arr)
    st.write("Mask:", mask)
    st.write("Filtered Array:", arr[mask])
    
elif option == "Fancy Indexing":
    st.header("Fancy Indexing")
    st.write("""
    - Introduction to fancy indexing as a powerful mechanism for accessing array elements.
    - Performing indexing using arrays of indices or boolean arrays.
    - Exploring advanced indexing techniques to extract specific elements or subarrays.
    - Understanding the difference between basic and fancy indexing and their respective applications.
    """)
    
    # Example: Fancy indexing
    st.subheader("Example: Fancy Indexing")
    arr = np.array([10, 20, 30, 40, 50])
    indices = np.array([0, 2, 4])
    st.write("Array:", arr)
    st.write("Selected Elements:", arr[indices])
    
elif option == "Sorting Arrays":
    st.header("Sorting Arrays")
    st.write("""
    - Sorting NumPy arrays in ascending or descending order.
    - Utilizing the sort() function for in-place sorting of arrays.
    - Sorting multi-dimensional arrays along specified axes.
    - Exploring different sorting algorithms and their performance characteristics.
    """)
    
    # Example: Sorting arrays
    st.subheader("Example: Sorting Arrays")
    arr = np.array([3, 1, 5, 2, 4])
    st.write("Original Array:", arr)
    st.write("Sorted Array:", np.sort(arr))
    
elif option == "Structured Data: NumPy’s Structured Array":
    st.header("Structured Data: NumPy’s Structured Array")
    st.write("""
    - Introduction to structured arrays in NumPy for handling structured data.
    - Defining structured arrays with custom data types and field names.
    - Accessing and manipulating structured array elements using field names.
    - Performing operations and analyses on structured data using NumPy's structured array functionality.
    """)
    
    # Example: Structured array
    st.subheader("Example: Structured Array")
    data = np.array([(1, 'John', 25), (2, 'Jane', 30), (3, 'Doe', 35)], dtype=[('id', int), ('name', 'U10'), ('age', int)])
    st.write("Structured Array:", data)

