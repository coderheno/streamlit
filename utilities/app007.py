import streamlit as st

def python_genomics_app():
    st.title("Introduction to Python: Genomics Applications")
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Home", "Syntax Basics", "Data Types", "Activities"])

    if choice == "Home":
        st.header("Welcome to Python for Genomics")
        st.write("""
        This app provides an introduction to Python syntax, data types, and their applications in genomics.
        Navigate through the sections using the sidebar!
        """)

    elif choice == "Syntax Basics":
        st.header("Python Syntax Basics")
        st.subheader("Key Features")
        st.write("""
        - **Emphasis on Readability**: Python syntax is designed to be easy to read.
        - **Indentation**: Indentation is used to define code blocks, improving clarity.
        - **Dynamic Typing**: Variables do not require explicit type declarations.
        """)
        st.subheader("Example: Indentation and Variables")
        code = """
        def greet(name):
            print(f"Hello, {name}!")

        greet("Genomics Researcher")
        """
        st.code(code, language="python")
        if st.button("Run Syntax Example"):
            st.write("Output: Hello, Genomics Researcher!")

    elif choice == "Data Types":
        st.header("Python Data Types")
        st.subheader("Overview")
        st.write("""
        Python supports various data types such as integers, floats, strings, lists, tuples, and dictionaries.
        Each type is tailored for specific tasks in programming and data analysis.
        """)
        st.subheader("Interactive Example: Lists")
        numbers = st.text_input("Enter a list of numbers (comma-separated):", "1, 2, 3, 4")
        if numbers:
            num_list = list(map(int, numbers.split(',')))
            st.write("Your List:", num_list)
            st.write("Sum of Numbers:", sum(num_list))

    elif choice == "Activities":
        st.header("Interactive Activities")
        st.subheader("Code Review Session")
        st.write("""
        Work in teams to review the following code snippet. Suggest improvements:
        ```python
        x = 10
        y = 20
        if x > y:
            print("x is greater")
        else:
            print("y is greater")
        ```
        """)
        st.subheader("Quiz: Python Operators")
        question = st.radio(
            "What is the output of `5 ** 2` in Python?",
            options=["10", "25", "5", "None"]
        )
        if st.button("Submit Answer"):
            if question == "25":
                st.success("Correct!")
            else:
                st.error("Try again!")

if __name__ == "__main__":
    python_genomics_app()
