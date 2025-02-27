import streamlit as st
import pandas as pd

def python_streamlit_ba():
    st.title("🚀 Why Include Python and Streamlit in Business Analytics?")
    
    # Introduction
    st.subheader("Why Include Python and Streamlit?")
    st.write("""
    Python is one of the most widely used languages in business analytics due to its extensive libraries:
    - **Data Cleaning & Preprocessing** (Pandas, NumPy)
    - **Statistical Analysis & Hypothesis Testing** (Statsmodels)
    - **Machine Learning & Predictive Analytics** (Scikit-learn, TensorFlow)
    - **Data Visualization** (Matplotlib, Seaborn)
    - **Automation of Repetitive Tasks** (Scripting & APIs)
    
    Streamlit is an open-source framework that helps create interactive business applications quickly:
    - **Rapid Deployment** of business dashboards
    - **Interactive Visualizations** for real-time decision-making
    - **Seamless ML Integration** for predictive analytics
    """)

    # Business Analytics Tools Table
    st.subheader("📊 Updated List of Business Analytics Tools")
    data = {
        "Category": [
            "Spreadsheet-Based Tools", "Statistical & Predictive Analytics",
            "Data Mining & Machine Learning", "Data Visualization",
            "Big Data & Cloud Analytics", "Programming & Development"
        ],
        "Tools": [
            "MS Excel, Google Sheets",
            "SPSS, SAS, R, MATLAB, Stata, Salford Systems",
            "Python (Pandas, Scikit-learn, TensorFlow), KXEN, RapidMiner",
            "Tableau, Power BI, Streamlit, Python (Matplotlib, Seaborn)",
            "Apache Spark, Google BigQuery, AWS SageMaker",
            "Python, R, Julia, SQL"
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    # Advantages of Python & Streamlit
    st.subheader("🚀 Advantages of Python and Streamlit in Business Analytics")
    advantages = [
        "✅ **Open-source & Cost-effective** – Unlike SAS & SPSS, Python & Streamlit are free.",
        "✅ **Scalability** – Python efficiently handles large datasets, unlike Excel.",
        "✅ **Real-time Analytics** – Streamlit enables interactive dashboards for business insights.",
        "✅ **AI/ML Integration** – Python supports ML models, unlike traditional tools."
    ]
    for adv in advantages:
        st.markdown(adv)

    # Optional Comparison Table Prompt
    st.write("Would you like a **comparison table** showing how Python and Streamlit compare to traditional tools? 🚀")
    if st.button("Generate Comparison"):
        comparison_data = {
            "Feature": ["Cost", "Scalability", "AI/ML Support", "Real-Time Dashboards", "Ease of Use"],
            "Python & Streamlit": ["Free & Open Source", "High", "Yes", "Yes", "User-friendly"],
            "Traditional Tools (Excel, SPSS, SAS)": ["Paid", "Limited", "Limited", "No", "Requires Training"]
        }
        comparison_df = pd.DataFrame(comparison_data)
        st.table(comparison_df)

# Run Function
if __name__ == "__main__":
    python_streamlit_ba()
