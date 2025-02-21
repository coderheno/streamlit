import streamlit as st
import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_fresh_random_data(df, num_rows):
    random_data = []
    for _ in range(num_rows):
        row = {}
        for col in df.columns:
            if "time" in col.lower():
                row[col] = fake.date_time()
            elif "email" in col.lower():
                row[col] = fake.email()
            elif "name" in col.lower():
                row[col] = fake.name()
            elif df[col].dtype == 'int64':
                row[col] = random.randint(1, 100)
            elif df[col].dtype == 'float64':
                row[col] = round(random.uniform(1.0, 100.0), 2)
            else:
                row[col] = fake.sentence()
        random_data.append(row)
    return pd.DataFrame(random_data)

def main():
    st.title("Fresh Random Data Generator from Uploaded File")
    
    uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["csv", "xlsx"])
    
    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1]
        
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, sheet_name=0)  # Read first sheet
        
        st.write("### Preview of Uploaded Data")
        st.dataframe(df.head())
        
        num_rows = st.number_input("Enter the number of fresh random rows to generate:", min_value=1, step=1)
        
        if st.button("Generate Fresh Random Data"):
            random_df = generate_fresh_random_data(df, num_rows)
            st.write("### Generated Fresh Random Data")
            st.dataframe(random_df)
            
            # Provide download link
            csv = random_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, "fresh_random_data.csv", "text/csv")
            
if __name__ == "__main__":
    main()
