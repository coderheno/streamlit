import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('data1.csv')

# Title
st.title('Gender Performance Analysis')

# Data preview
st.subheader('Data Preview')
st.write(data.head())

# Gender distribution
st.subheader('Gender Distribution')
gender_counts = data['Gender'].value_counts()
fig, ax = plt.subplots()
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
ax.axis('equal')
ax.set_title('Gender Distribution')
st.pyplot(fig)

# Gender-wise marking distribution
st.subheader('Gender-wise Marking Distribution')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Gender', y='CIA1 (20)', data=data, ax=ax)
ax.set_title('Gender-wise Marking Distribution')
st.pyplot(fig)

# Correlation between assignment and test scores
st.subheader('Correlation between Assignment and Test Scores')
corr = data['Assignment (10)'].corr(data['Test (10)'])
st.write(f'The correlation between assignment and test scores is: {corr:.2f}')

# Marking chart
st.subheader('Marking Chart')
marking_chart = data[['Student Name', 'Gender', 'Assignment (10)', 'Test (10)', 'CIA1 (20)']].sort_values(by='CIA1 (20)', ascending=False)
st.write(marking_chart)

# Marking distribution histogram
st.subheader('Marking Distribution Histogram')
fig, ax = plt.subplots()
ax.hist(data['CIA1 (20)'], bins=20, edgecolor='black')
ax.set_xlabel('CIA1 Marks')
ax.set_ylabel('Count')
ax.set_title('Marking Distribution Histogram')
st.pyplot(fig)