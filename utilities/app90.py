import streamlit as st
import random
import pandas as pd
import base64

def display_groups():
    # Input for names and number of groups
    names_input = st.text_input("Enter names separated by commas")
    num_groups = st.number_input("Enter number of groups", min_value=1, step=1)
    
    # Split the names and shuffle them randomly
    names = [name.strip() for name in names_input.split(",") if name.strip()]
    random.shuffle(names)
    
    # Funny food names for groups
    food_names = [
        "Biriyani", "Tandori", "Samosas", "Pizza", "Sushi",
        "Burgers", "Chicken Tikka", "Frenc fries", "Noodles", "Curd rice"
    ]
    random.shuffle(food_names)
    
    # Initialize the groups dictionary
    groups = {f"{food_names[i % len(food_names)]} (Group {i+1})": [] for i in range(num_groups)}
    
    # Assign names to groups randomly
    for i, name in enumerate(names):
        group_key = f"{food_names[i % len(food_names)]} (Group {(i % num_groups) + 1})"
        groups[group_key].append(name)
    
    # Create a DataFrame for displaying in Streamlit
    df = pd.DataFrame(groups.values(), index=groups.keys()).transpose()
    
    # Display the table using Streamlit
    st.write("Groups and Members:")
    st.table(df)
    
    # Shout out for each group
    for group in groups:
        st.success(f"Shout out to the {group}!")
    
    # Save the groups to a CSV file
    save_option = st.checkbox("Save groups to CSV file")
    if save_option:
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="groups.csv">Download CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)

def main():
    # Set the title for the workshop
    st.set_page_config(page_title="Building and Deploying Interactive Web Apps with Streamlit")

    # Create tabs for the app
    tabs = st.tabs(["Home", "Streamlit Basics", "GitHub Desktop", "Streamlit Sharing & VSCode", "Live Activities"])

    # Home Tab
    with tabs[0]:
        st.title("Welcome to the Workshop!")
        st.header("Workshop Title: Building and Deploying Interactive Web Apps with Streamlit")
        st.subheader("Objective:")
        st.write("""
        The objective of this workshop is to equip participants with the skills to build and deploy interactive web applications using Streamlit. 
        The workshop covers the basics of Streamlit, the importance of version control with GitHub, and how to deploy Streamlit apps using various tools like GitHub, VSCode, and more.
        """)
        
        st.subheader("Outcomes:")
        st.write("""
        By the end of this workshop, participants will be able to:
        - Understand the fundamentals of Streamlit and how to create interactive web applications.
        - Utilize GitHub Desktop for version control and collaboration.
        - Deploy Streamlit applications using various platforms.
        - Integrate Python examples and understand the importance of tools like VSCode.
        - Participate in live coding activities and group exercises.
        """)
        
        st.subheader("Trainer Details:")
        st.write("""
        **Trainer:** Vijay, Computer Science Professor with 15 years of teaching experience, expert in Streamlit, Python, and web development.
        - **Phone:** +91 9677188654
        - **Email:** phdvij@gmail.com
        - **Linked
        - **Specializations:** Streamlit, Python, Web Development, Educational Technology, and Disaster Management.
        """)

    # Streamlit Basics Tab
    with tabs[1]:
        st.header("Streamlit Basics")
        st.write("""
        Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. 
        With just a few lines of code, you can build and deploy powerful web applications.
        """)
        st.subheader("Key Features:")
        st.write("""
        - **Ease of Use:** Simple and intuitive syntax that allows for rapid app development.
        - **Interactivity:** Create interactive widgets like sliders, buttons, and more with minimal effort.
        - **Real-Time Feedback:** Changes are reflected immediately in the app as you code.
        - **Data Integration:** Seamlessly integrate with popular Python libraries like Pandas, Matplotlib, and Plotly for data visualization.
        """)
        st.subheader("Getting Started:")
        st.code("""
        import streamlit as st
        
        st.title("Hello, Streamlit!")
        st.write("This is a simple Streamlit app.")
        """, language="python")
        st.subheader("Running Your App:")
        st.write("""
        To run your Streamlit app, save your Python script and use the following command in your terminal:
        
        ```
        streamlit run your_app.py
        ```
        
        This will start a local server and open your app in the browser.
        """)

    # GitHub Desktop Tab
    with tabs[2]:
        st.header("GitHub Desktop Overview and Importance")
        st.write("""
        GitHub Desktop is a user-friendly interface for Git that allows you to manage your repositories and collaborate with others without using the command line. 
        It's an excellent tool for beginners and helps simplify the process of version control.
        """)
        st.subheader("Key Benefits:")
        st.write("""
        - **Ease of Use:** No need to remember Git commands; everything is done through an intuitive interface.
        - **Visual Interface:** See your changes, commits, and history visually.
        - **Collaboration:** Easily manage pull requests and branch merges.
        """)
        st.subheader("Getting Started with GitHub Desktop:")
        st.write("""
        1. Download and install [GitHub Desktop](https://desktop.github.com/).
        2. Clone your repository or create a new one.
        3. Make changes, commit them, and push them to GitHub with a few clicks.
        4. Collaborate with others by creating branches and pull requests.
        """)

    # Streamlit Sharing & VSCode Tab
    with tabs[3]:
        st.header("Streamlit Sharing, VSCode, and Python Examples")
        st.write("""
        Deploying your Streamlit apps can be done using various platforms, with Streamlit Sharing being one of the simplest.
        Visual Studio Code (VSCode) is a powerful code editor that integrates well with Python and GitHub, making it easier to develop and deploy applications.
        """)
        st.subheader("Deploying with Streamlit Sharing:")
        st.write("""
        1. Push your Streamlit app to GitHub.
        2. Log in to Streamlit Sharing and link your GitHub repository.
        3. Deploy your app with a single click.
        """)
        st.subheader("Python Examples and Importance:")
        st.write("""
        Python's versatility makes it an ideal language for web development, data analysis, and more. Examples can range from simple data visualization apps to complex machine learning dashboards.
        """)
        st.code("""
        import streamlit as st
        import matplotlib.pyplot as plt
        
        st.title("Simple Plot Example")
        
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 30, 40, 50]
        
        plt.plot(x, y)
        st.pyplot(plt)
        """, language="python")
        st.subheader("Using VSCode with Streamlit:")
        st.write("""
        1. Install [Visual Studio Code](https://code.visualstudio.com/).
        2. Install Python and Streamlit extensions for enhanced development experience.
        3. Develop your app, run it locally, and deploy it seamlessly using GitHub and Streamlit Sharing.
        """)

    # Live Activities Tab
    with tabs[4]:
        st.header("Live Activities and Group Exercise")
        st.write("Let's get hands-on with some activities!")
        
        st.subheader("Step 1: Group Formation and Shout Out")
        st.write("Form groups with funny food names and give a shout out to each group.")

        # Call the group generator function
        display_groups()

        st.subheader("Step 2: Live Demo on App Deployment")
        st.write("""
        - **Live demo:** We will go through the entire process of deploying a Streamlit app.
        - **Tools:** We'll use Visual Studio Code (VSCode) with Python, Streamlit, and GitHub for version control and collaboration.
        - **Authorization:** Authorize your GitHub account using GitHub Desktop.
        - **Deployment:** Finally, deploy the app using Streamlit Sharing.
        """)

        st.subheader("Step 3: Install the Required Tools")
        st.write("""
        - **Step 3.1:** Install [Visual Studio Code](https://code.visualstudio.com/).
        - **Step 3.2:** Install Python (if not already installed).
        - **Step 3.3:** Install Streamlit using the command `pip install streamlit`.
        """)

        st.subheader("Step 4: Create GitHub Accounts and Collaborate")
        st.write("""
        - **Step 4.1:** Create GitHub accounts if you don’t have one.
        - **Step 4.2:** Set up repositories and collaborate with others on a shared project.
        """)

        st.subheader("Step 5: Install GitHub Desktop and Authorize")
        st.write("""
        - **Step 5.1:** Download and install [GitHub Desktop](https://desktop.github.com/).
        - **Step 5.2:** Authorize your account and start using it for version control.
        """)

        st.subheader("Step 6: Deploying to Streamlit Sharing")
        st.write("""
        - **Step 6.1:** Push your code to GitHub.
        - **Step 6.2:** Deploy your app using [Streamlit Sharing](https://share.streamlit.io/).
        """)

if __name__ == "__main__":
    main()
