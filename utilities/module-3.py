import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Module 3 - Machine Learning Application Development",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Module 3: Machine Learning Application Development")
st.markdown("---")

# Sidebar Navigation
st.sidebar.title("📚 Module 3 Contents")

topic = st.sidebar.radio(
    "Select a Topic",
    [
        "Module Overview",
        "1. Introduction to Machine Learning",
        "2. Loading Pre-trained Models",
        "3. User Input Validation",
        "4. Building Prediction Applications",
        "5. Classification Applications",
        "6. Model Evaluation",
        "7. Result Interpretation",
        "8. End-to-End ML Applications",
        "9. Deployment Considerations",
        "10. Real-World Case Studies",
        "Module Summary"
    ]
)

# Module Overview
if topic == "Module Overview":

    st.header("Module Overview")

    st.write("""
    Machine Learning (ML) enables computers to learn from data and make
    predictions or decisions without being explicitly programmed.
    In this module, learners will explore how Machine Learning models
    can be integrated into Streamlit applications to create intelligent,
    interactive, and user-friendly solutions.
    """)

    st.success("Learning Outcomes")

    st.markdown("""
    - Understand Machine Learning concepts.
    - Load and use pre-trained ML models.
    - Validate user inputs.
    - Develop prediction and classification systems.
    - Evaluate ML model performance.
    - Build end-to-end ML applications using Streamlit.
    """)

# Topic 1
elif topic == "1. Introduction to Machine Learning":

    st.header("1. Introduction to Machine Learning")

    st.write("""
    Machine Learning is a branch of Artificial Intelligence that enables
    systems to learn patterns from data and make decisions.
    """)

    st.subheader("Types of Machine Learning")

    st.markdown("""
    ### Supervised Learning
    - Uses labeled data
    - Prediction and classification tasks

    ### Unsupervised Learning
    - Uses unlabeled data
    - Clustering and pattern discovery

    ### Reinforcement Learning
    - Learns through rewards and penalties
    """)

# Topic 2
elif topic == "2. Loading Pre-trained Models":

    st.header("2. Loading Pre-trained Models")

    st.write("""
    Trained machine learning models can be saved and reused in Streamlit applications.
    """)

    st.code("""
import pickle

model = pickle.load(
    open("model.pkl", "rb")
)
""", language="python")

    st.info("""
    Pickle is commonly used to save and load machine learning models.
    """)

# Topic 3
elif topic == "3. User Input Validation":

    st.header("3. User Input Validation")

    st.write("""
    User input validation ensures that the application receives correct data.
    """)

    st.code("""
age = st.number_input(
    "Enter Age",
    min_value=1,
    max_value=120
)
""", language="python")

    st.code("""
if age <= 0:
    st.error("Invalid Age")
""", language="python")

# Topic 4
elif topic == "4. Building Prediction Applications":

    st.header("4. Building Prediction Applications")

    st.write("""
    Prediction applications use machine learning models to forecast outcomes.
    """)

    st.code("""
import streamlit as st

income = st.number_input(
    "Enter Income"
)

if st.button("Predict"):

    prediction = model.predict(
        [[income]]
    )

    st.success(
        f"Prediction: {prediction[0]}"
    )
""", language="python")

# Topic 5
elif topic == "5. Classification Applications":

    st.header("5. Classification Applications")

    st.write("""
    Classification models categorize data into predefined classes.
    """)

    st.markdown("""
    Examples:
    - Spam Detection
    - Disease Diagnosis
    - Student Performance Prediction
    - Sentiment Analysis
    """)

    st.code("""
result = model.predict(
    [[feature1, feature2]]
)

st.write(result)
""", language="python")

# Topic 6
elif topic == "6. Model Evaluation":

    st.header("6. Model Evaluation")

    st.write("""
    Model evaluation measures how well a machine learning model performs.
    """)

    st.subheader("Common Metrics")

    st.markdown("""
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - Mean Squared Error
    """)

    st.code("""
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(accuracy)
""", language="python")

# Topic 7
elif topic == "7. Result Interpretation":

    st.header("7. Result Interpretation")

    st.write("""
    Model predictions should be interpreted carefully to support
    informed decision-making.
    """)

    st.markdown("""
    Good interpretation helps:
    - Identify trends
    - Detect anomalies
    - Improve business decisions
    - Enhance user trust
    """)

# Topic 8
elif topic == "8. End-to-End ML Applications":

    st.header("8. End-to-End ML Applications")

    st.write("""
    An end-to-end ML application includes:
    """)

    st.markdown("""
    1. Data Collection
    2. Data Preprocessing
    3. Model Training
    4. Model Saving
    5. Streamlit Interface
    6. Prediction Output
    """)

    st.code("""
User Input
      ↓
Preprocessing
      ↓
ML Model
      ↓
Prediction
      ↓
Result Display
""")

# Topic 9
elif topic == "9. Deployment Considerations":

    st.header("9. Deployment Considerations")

    st.write("""
    Deployment makes ML applications accessible to users through the web.
    """)

    st.markdown("""
    Common Deployment Platforms:
    - Streamlit Community Cloud
    - Render
    - Hugging Face Spaces
    - AWS
    - Azure
    """)

    st.code("""
streamlit run app.py
""", language="bash")

# Topic 10
elif topic == "10. Real-World Case Studies":

    st.header("10. Real-World Case Studies")

    st.markdown("""
    ### Healthcare
    Disease Prediction Systems

    ### Education
    Student Performance Analytics

    ### Banking
    Loan Approval Prediction

    ### Agriculture
    Crop Yield Prediction

    ### Retail
    Sales Forecasting
    """)

# Module Summary
elif topic == "Module Summary":

    st.header("Module Summary")

    st.success("""
    Congratulations! You have completed Module 3.
    """)

    st.markdown("""
    ### Key Concepts Covered

    ✅ Introduction to Machine Learning

    ✅ Loading Pre-trained Models

    ✅ User Input Validation

    ✅ Prediction Systems

    ✅ Classification Systems

    ✅ Model Evaluation

    ✅ Result Interpretation

    ✅ End-to-End ML Applications

    ✅ Deployment Considerations

    ✅ Real-World Applications
    """)

    st.info("""
    Course Outcome Addressed:

    CO3: Develop and integrate machine learning models
    into Streamlit applications for predictive analytics
    and decision support.
    """)

    st.markdown("""
    ### Skills Acquired

    - Machine Learning Fundamentals
    - Model Integration
    - Prediction System Development
    - Classification Techniques
    - Model Evaluation
    - Streamlit ML Deployment
    """)

    st.success("""
    🚀 Next Module: Version Control and Project Deployment using GitHub
    """)