import streamlit as st
import pandas as pd
def class_lectures():
    st.header("What is Pandas?")
    st.write("Pandas is a Python library used for data manipulation and analysis. It provides easy-to-use data structures and functions, making it powerful for working with structured data.")
    st.header("Basic Elements of Pandas")
    st.subheader("1. DataFrame")
    st.write("DataFrame is a two-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or SQL table.")
    st.code("import pandas as pd\n\n# Create DataFrame\ndata = {'Name': ['John', 'Emma', 'Peter'], 'Age': [25, 30, 35]}\ndf = pd.DataFrame(data)")
    st.subheader("2. Series")
    st.write("Series is a one-dimensional labeled array capable of holding any data type.")
    st.code("import pandas as pd\n\n# Create Series\ns = pd.Series([10, 20, 30, 40, 50])")
    st.subheader("3. Index")
    st.write("Index is a unique identifier for rows in a DataFrame or labels for elements in a Series.")
    st.code("import pandas as pd\n\n# Create DataFrame with custom index\ndata = {'Name': ['John', 'Emma', 'Peter'], 'Age': [25, 30, 35]}\ndf = pd.DataFrame(data, index=['A', 'B', 'C'])")
    st.header("Object Data Indexing")
    st.write("Pandas provides various methods for indexing and selecting data in a DataFrame or Series.")
    st.subheader("DataFrame.loc[]")
    st.write("Access a group of rows and columns by labels.")
    st.code("df.loc['A']  # Select row with index 'A'")

    st.subheader("DataFrame.iloc[]")
    st.write("Access a group of rows and columns by integer position.")
    st.code("df.iloc[0]  # Select row at position 0")

    st.header("Selection Operating")
    st.write("Pandas offers powerful operations for selecting, filtering, and modifying data.")

    st.subheader("Filtering Data")
    st.write("Filter rows based on certain conditions.")
    st.code("df[df['Age'] > 30]  # Filter rows where Age is greater than 30")

    st.subheader("Modifying Data")
    st.write("Update values in a DataFrame.")
    st.code("df.loc['A', 'Age'] = 26  # Change the Age value for row 'A' to 26")
def load_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    return df

def explore_data(df):
    st.header("Exploring the Election Bonds and Donations Dataset")
    
    # Display the first few rows of the dataset
    st.subheader("First Few Rows")
    st.write(df.head())

    # Get information about the columns and data types
    st.subheader("Data Information")
    st.write(df.info())

    # Summary statistics of numerical columns
    st.subheader("Summary Statistics")
    st.write(df.describe())

def filter_and_modify_data(df):
    st.header("Filtering and Modifying Data")
    
    # Filtering Data
    st.subheader("Filtering Data")
    party_to_filter = st.selectbox("Select a Party to Filter:", df['Party'].unique())
    filtered_data = df[df['Party'] == party_to_filter]
    st.write(filtered_data)

    # Modifying Data
    st.subheader("Modifying Data")
    column_to_update = st.selectbox("Select a Column to Update:", df.columns)
    update_value = st.number_input(f"Enter the New Value for {column_to_update}:")
    df[column_to_update] = update_value
    st.write("Data Updated Successfully!")
    st.write(df.head())

def assignments():
    st.subheader("Assignment: Exploring Real-Time Current Affairs Dataset")

    st.write("""
    #### Objective:
    This assignment aims to provide students with practical experience in exploring and analyzing real-time current affairs datasets using Python and Streamlit. By applying data analysis techniques, students will gain insights into recent events, trends, or issues, enhancing their understanding of current affairs topics.

    #### Instructions:
    1. **Load and Explore Dataset**: 
       - Load the current affairs dataset using Python's Pandas library.
       - Explore the dataset by displaying the first few rows, examining data information, and summarizing statistics.

    2. **Filtering and Modifying Data**:
       - Allow users to filter the dataset based on relevant criteria (e.g., party name, event type).
       - Provide functionality for modifying data by updating specific columns with new values.

    3. **Data Visualization**:
       - Create interactive visualizations to illustrate key findings or trends in the dataset.
       - Utilize charts, graphs, and plots to enhance the presentation of data exploration results.

    4. **Documentation and Reporting**:
       - Document the analysis process, including dataset exploration, filtering, and visualization techniques used.
       - Prepare a concise report summarizing the main insights and observations from the dataset analysis.

    #### Submission Guidelines:
    - Students should submit their Python script or Streamlit application code along with any necessary data files.
    - The code should be well-commented and structured to facilitate understanding and reproducibility.
    - Submissions should include a brief summary or README file explaining the analysis approach and key findings.

    #### Evaluation Criteria:
    - Completeness and effectiveness of dataset exploration and analysis.
    - Functionality and usability of the filtering and modification features.
    - Quality and clarity of data visualizations in conveying insights.
    - Documentation quality and coherence of the analysis report.

    #### Additional Notes:
    - Encourage students to explore datasets related to current events, politics, economics, or other areas of interest.
    - Provide guidance on using Streamlit for interactive data visualization and user interface development.
    - Encourage experimentation and creativity in applying data analysis techniques to real-world datasets.

    By following these instructions, students will gain practical experience in exploring and analyzing real-time current affairs datasets, enhancing their data analysis skills and understanding of current events.
    """)


def practicals():
    st.subheader("Exercise 8: Construct a Script for Inner Join Operation")

    st.write("""
    #### Aim:
    The aim of this exercise is to develop a Python script that simulates the functionality of a SQL inner join operation for an internal data structure. This exercise will provide students with hands-on experience in implementing data manipulation techniques using Python.

    #### Algorithm:
    1. Define two data structures (e.g., lists, dictionaries) representing the tables to be joined.
    2. Implement a function to perform the inner join operation on the specified columns.
    3. Iterate through the rows of both tables and match records based on the join condition.
    4. Combine matching records into a new data structure representing the result of the inner join.
    5. Return the resulting data structure containing the inner join output.

    #### Program Guidelines:
    - Define two data structures representing the tables to be joined, ensuring they contain relevant columns for the join operation.
    - Implement a function to perform the inner join operation, taking input parameters for the two data structures and the columns to join on.
    - Handle cases where there are multiple matches or no matches for a given join condition.
    - Test the script with different datasets and join conditions to ensure its correctness and robustness.
    - Document the code with clear comments and explanations to aid understanding.

    #### Expected Output:
    - The output of the script should be a data structure containing the result of the inner join operation, representing the combined information from both tables based on the specified join condition.
    - The output should accurately reflect the matching records from both tables, demonstrating the functionality of the inner join operation.

    By completing this exercise, students will gain a deeper understanding of data manipulation techniques and the inner workings of SQL join operations, enhancing their programming skills in Python.
    """)



def main():
    st.title("UNIT-4: Introduction to Pandas")

    # Load the dataset
    file_path = "election_bonds_dataset.csv"
    df = load_data(file_path)

    # Sidebar tabs and hyperlinks
    st.sidebar.title('Unit-4: Quick Navigation')
    tab = st.sidebar.radio('Go to', ['Contents', 'Class Lectures', 'Examples', 'Assignments', 'Practicals'])

    if tab == 'Contents':
        st.subheader("File Handling in Python")
        st.write("Writing and Reading Binary Data, Writing and Parsing Text Files, Writing and Parsing XML Files.")
        st.subheader("Pandas Library in Python")
        st.write('Introduction to Pandas Objects-Data indexing and Selection-Operating on Data in Pandas-Handling Missing Data-Hierarchical Indexing.')
        st.subheader("Practical Exercises")
        st.write("7.Write a script to perform CRUD operations using corresponding SQL statements and load the data into the internal Data Structure.")
        st.write("8.Construct a script to work like a SQL Inner Join for an internal Data Structure")
        
    elif tab == 'Class Lectures':
        class_lectures()
    elif tab == 'Examples':
        # Explore the dataset
        explore_data(df)
        # Filter and Modify Data
        filter_and_modify_data(df)

    elif tab == 'Assignments':
        assignments()

    elif tab == 'Practicals':
        practicals()

if __name__ == "__main__":
    main()
