import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

st.set_page_config(page_title='Data Visualization App')
st.title('Data Visualization App')

st.subheader('Data')
st.write(data)

st.subheader('Age Distribution')
fig, ax = plt.subplots()
ax.hist(data['Age'], bins=10)
ax.set_xlabel('Age')
ax.set_ylabel('Count')
ax.set_title('Age Distribution')
st.pyplot(fig)

st.subheader('Interactive Visualization')
selected_column = st.selectbox('Select a column', data.columns)
fig, ax = plt.subplots()
ax.hist(data[selected_column], bins=10)
ax.set_xlabel(selected_column)
ax.set_ylabel('Count')
ax.set_title(f'{selected_column} Distribution')
st.pyplot(fig)

if __name__ == '__main__':
    st.write('Running the Streamlit app...')
    st.write('Please wait for the app to open in your browser.')
    st.stop()