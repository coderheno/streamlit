import streamlit as st
import datetime
import time

# Function to display system time with changing seconds
def display_system_time():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        st.write("Current Time: ", current_time)
        time.sleep(1)
        st.empty()  # Clear the output to avoid stacking multiple time displays

# Main function to run the Streamlit app
def main():
    st.title("System Time Display")
    st.write("This app displays the system time with changing seconds.")

    display_system_time()  # Call the function to display system time

if __name__ == "__main__":
    main()
