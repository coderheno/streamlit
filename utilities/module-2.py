import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Module 2 - Data Handling and Visualization",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Module 2: Data Handling and Visualization")
st.markdown("---")

# Sidebar
st.sidebar.title("📚 Module 2 Contents")

topic = st.sidebar.radio(
    "Select a Topic",
    [
        "Module Overview",
        "1. Introduction to Data Handling",
        "2. Reading and Writing Text Files",
        "3. Working with CSV Files",
        "4. Working with JSON Files",
        "5. File Upload and Download",
        "6. Data Cleaning and Preprocessing",
        "7. Displaying DataFrames and Tables",
        "8. Data Visualization in Streamlit",
        "9. Interactive Charts using Plotly",
        "10. Building Data-Driven Applications",
        "Module Summary"
    ]
)

# Module Overview
if topic == "Module Overview":

    st.header("Module Overview")

    st.write("""
    Data is the backbone of modern applications. In this module,
    learners will explore techniques for reading, processing,
    cleaning, visualizing, and managing data using Python and Streamlit.
    """)

    st.success("Learning Outcomes")

    st.markdown("""
    - Read and write Text, CSV, and JSON files.
    - Upload and process files in Streamlit.
    - Clean and preprocess datasets.
    - Display data using tables and DataFrames.
    - Create visualizations and dashboards.
    - Build data-driven applications.
    """)

# Topic 1
elif topic == "1. Introduction to Data Handling":

    st.header("1. Introduction to Data Handling")

    st.write("""
    Data handling involves collecting, storing, processing,
    and presenting information effectively.
    """)

    st.subheader("Importance of Data Handling")

    st.markdown("""
    - Data Analysis
    - Business Intelligence
    - Machine Learning
    - Reporting and Dashboards
    - Decision Making
    """)

    st.subheader("Common Data Formats")

    st.table({
        "Format": ["Text", "CSV", "JSON"],
        "Extension": [".txt", ".csv", ".json"],
        "Usage": [
            "Simple text storage",
            "Tabular data",
            "Structured data exchange"
        ]
    })

# Topic 2
elif topic == "2. Reading and Writing Text Files":

    st.header("2. Reading and Writing Text Files")

    st.subheader("Reading a Text File")

    st.code("""
with open("sample.txt","r") as file:
    content = file.read()

st.write(content)
""", language="python")

    st.subheader("Writing to a Text File")

    st.code("""
with open("sample.txt","w") as file:
    file.write("Welcome to Streamlit")
""", language="python")

    st.info("Text files are lightweight and easy to manage.")

# Topic 3
elif topic == "3. Working with CSV Files":

    st.header("3. Working with CSV Files")

    st.write("""
    CSV files are widely used for storing structured tabular data.
    """)

    st.code("""
import pandas as pd

df = pd.read_csv("students.csv")

st.dataframe(df)
""", language="python")

    st.subheader("Writing CSV")

    st.code("""
df.to_csv("output.csv", index=False)
""", language="python")

# Topic 4
elif topic == "4. Working with JSON Files":

    st.header("4. Working with JSON Files")

    st.write("""
    JSON (JavaScript Object Notation) is commonly used
    for web applications and APIs.
    """)

    st.code("""
import json

with open("data.json") as file:
    data = json.load(file)

st.write(data)
""", language="python")

    st.subheader("Writing JSON")

    st.code("""
with open("output.json","w") as file:
    json.dump(data,file)
""", language="python")

# Topic 5
elif topic == "5. File Upload and Download":

    st.header("5. File Upload and Download")

    st.subheader("Uploading Files")

    st.code("""
uploaded_file = st.file_uploader(
    "Choose a file"
)

if uploaded_file:
    st.write(uploaded_file.name)
""", language="python")

    st.subheader("Reading Uploaded CSV")

    st.code("""
import pandas as pd

file = st.file_uploader(
    "Upload CSV"
)

if file:
    df = pd.read_csv(file)
    st.dataframe(df)
""", language="python")

    st.subheader("Download Button")

    st.code("""
st.download_button(
    label="Download",
    data="Hello Streamlit",
    file_name="sample.txt"
)
""", language="python")

# Topic 6
elif topic == "6. Data Cleaning and Preprocessing":

    st.header("6. Data Cleaning and Preprocessing")

    st.write("""
    Real-world datasets often contain missing values,
    duplicates, and inconsistencies.
    """)

    st.subheader("Checking Missing Values")

    st.code("""
df.isnull().sum()
""", language="python")

    st.subheader("Removing Missing Values")

    st.code("""
df.dropna()
""", language="python")

    st.subheader("Replacing Missing Values")

    st.code("""
df.fillna(0)
""", language="python")

    st.subheader("Removing Duplicates")

    st.code("""
df.drop_duplicates()
""", language="python")

# Topic 7
elif topic == "7. Displaying DataFrames and Tables":

    st.header("7. Displaying DataFrames and Tables")

    st.subheader("Table Display")

    st.code("""
st.table(df)
""", language="python")

    st.subheader("Interactive DataFrame")

    st.code("""
st.dataframe(df)
""", language="python")

    st.subheader("Metrics")

    st.code("""
st.metric(
    "Total Students",
    500
)
""", language="python")

# Topic 8
elif topic == "8. Data Visualization in Streamlit":

    st.header("8. Data Visualization in Streamlit")

    st.write("""
    Data visualization helps users understand trends
    and patterns quickly.
    """)

    st.subheader("Line Chart")

    st.code("""
st.line_chart(df)
""", language="python")

    st.subheader("Bar Chart")

    st.code("""
st.bar_chart(df)
""", language="python")

    st.subheader("Area Chart")

    st.code("""
st.area_chart(df)
""", language="python")

# Topic 9
elif topic == "9. Interactive Charts using Plotly":

    st.header("9. Interactive Charts using Plotly")

    st.write("""
    Plotly provides advanced interactive charts.
    """)

    st.code("""
pip install plotly
""", language="bash")

    st.code("""
import plotly.express as px

fig = px.bar(
    df,
    x="Name",
    y="Marks"
)

st.plotly_chart(fig)
""", language="python")

    st.success("""
    Plotly charts support zooming,
    hovering, filtering, and exporting.
    """)

# Topic 10
elif topic == "10. Building Data-Driven Applications":

    st.header("10. Building Data-Driven Applications")

    st.write("""
    Data-driven applications collect,
    process, analyze, and visualize data.
    """)

    st.code("""
import streamlit as st
import pandas as pd

st.title("CSV Analyzer")

file = st.file_uploader(
    "Upload CSV"
)

if file:

    df = pd.read_csv(file)

    st.dataframe(df)

    st.bar_chart(
        df.select_dtypes(
            include="number"
        )
    )
""", language="python")

    st.subheader("Workflow")

    st.markdown("""
    User Uploads Data

    ↓

    Data Processing

    ↓

    Data Cleaning

    ↓

    Visualization

    ↓

    Insights
    """)

# Summary
elif topic == "Module Summary":

    st.header("Module Summary")

    st.success("""
    Congratulations! You have completed Module 2.
    """)

    st.markdown("""
    ### Key Concepts Learned

    ✅ Text File Handling

    ✅ CSV Processing

    ✅ JSON Processing

    ✅ File Upload and Download

    ✅ Data Cleaning

    ✅ DataFrames and Tables

    ✅ Data Visualization

    ✅ Plotly Charts

    ✅ Data-Driven Applications
    """)

    st.info("""
    Course Outcome Addressed:
    CO2 - Implement file handling, data processing,
    and visualization techniques for managing
    structured and unstructured data.
    """)

    st.markdown("""
    ### Next Module

    🚀 Module 3: Machine Learning Application Development
    """)