import streamlit as st
import numpy as np

# Title
st.title("NumPy Tutorial")

# Option selection
option = st.sidebar.selectbox(
    "Select Content Option",
    ("NUMPY Basics", "Array Creation", "Array Indexing and Slicing", "Array Operations", 
     "Random Number Generation", "Linear Algebra Operations", "File Input and Output")
)

# Option content
if option == "NUMPY Basics":
    st.header("NUMPY Basics")
    st.write("""
    - Introduction to NumPy library for numerical computations in Python.
    - Basic array operations such as creation, reshaping, and accessing elements.
    - Data types and attributes of NumPy arrays.
    - Universal functions (ufuncs) and broadcasting.
    """)
    
    # Example: Basic array creation and attributes
    st.subheader("Example: Basic Array Creation and Attributes")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    st.write("Array:", arr)
    st.write("Shape:", arr.shape)
    st.write("Data Type:", arr.dtype)
    st.write("Number of Dimensions:", arr.ndim)
    st.write("Size:", arr.size)
    
elif option == "Array Creation":
    st.header("Array Creation")
    st.write("""
    - Different methods for creating NumPy arrays (e.g., np.array(), np.zeros(), np.ones()).
    - Creating arrays with specified data types and dimensions.
    - Generating sequences and ranges with np.arange(), np.linspace(), and np.random.
    """)
    
    # Example: Creating arrays with np.arange() and np.random
    st.subheader("Example: Creating Arrays")
    arr1 = np.arange(1, 10, 2)  # Array with values from 1 to 9 with step 2
    arr2 = np.random.rand(3, 3)  # 3x3 array of random numbers
    st.write("Array 1:", arr1)
    st.write("Array 2:", arr2)
    
elif option == "Array Indexing and Slicing":
    st.header("Array Indexing and Slicing")
    st.write("""
    - Accessing and modifying individual elements of arrays.
    - Slicing arrays to extract subarrays and manipulate data.
    - Advanced indexing techniques like boolean indexing and fancy indexing.
    """)
    
    # Example: Array indexing and slicing
    st.subheader("Example: Array Indexing and Slicing")
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    st.write("Array:", arr)
    st.write("Element at position (1, 1):", arr[1, 1])
    st.write("First column:", arr[:, 0])
    st.write("Subarray:", arr[:2, 1:])
    
elif option == "Array Operations":
    st.header("Array Operations")
    st.write("""
    - Performing arithmetic operations, aggregation, and broadcasting on arrays.
    - Applying mathematical functions and universal functions (ufuncs) to arrays.
    - Manipulating arrays with reshape, transpose, and concatenation operations.
    """)
    
    # Example: Array operations
    st.subheader("Example: Array Operations")
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    st.write("Array 1:", arr1)
    st.write("Array 2:", arr2)
    st.write("Sum:", np.sum(arr1))
    st.write("Element-wise product:", arr1 * arr2)
    st.write("Matrix multiplication:", np.dot(arr1, arr2))
    
elif option == "Random Number Generation":
    st.header("Random Number Generation")
    st.write("""
    - Generating random numbers and arrays with various distributions.
    - Seeding random number generators for reproducibility.
    - Sampling from random distributions and shuffling arrays.
    """)
    
    # Example: Random number generation
    st.subheader("Example: Random Number Generation")
    rand_num = np.random.randint(1, 100)  # Random integer between 1 and 100
    rand_arr = np.random.rand(3, 3)  # 3x3 array of random numbers between 0 and 1
    st.write("Random Number:", rand_num)
    st.write("Random Array:", rand_arr)
    
elif option == "Linear Algebra Operations":
    st.header("Linear Algebra Operations")
    st.write("""
    - Performing matrix and vector operations like addition, multiplication, and inversion.
    - Solving linear equations and computing matrix decompositions.
    - Applying linear algebra functions for eigenvalues, singular values, and norms.
    """)
    
    # Example: Linear algebra operations
    st.subheader("Example: Linear Algebra Operations")
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 6])
    x = np.linalg.solve(A, b)  # Solve Ax = b
    st.write("Matrix A:", A)
    st.write("Vector b:", b)
    st.write("Solution x:", x)
    
elif option == "File Input and Output":
    st.header("File Input and Output")
    st.write("""
    - Reading and writing NumPy arrays from/to files in various formats.
    - Handling CSV, text, binary, and compressed files with NumPy functions.
    - Saving and loading arrays using np.save(), np.load(), and np.savetxt().
    """)
    
    # Example: File input and output
    st.subheader("Example: File Input and Output")
    data = np.array([[1, 2, 3], [4, 5, 6]])
    np.save("example.npy", data)  # Save array to .npy file
    loaded_data = np.load("example.npy")  # Load array from .npy file
    st.write("Saved Array:", data)
    st.write("Loaded Array:", loaded_data)
