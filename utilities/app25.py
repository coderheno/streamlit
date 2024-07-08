import streamlit as st
def display_authentication_methods():
    st.title("Login Authentication Methods")

    st.header("1. Username and Password")
    st.write("""
    **Description:** The most traditional and widely used method. Users provide a unique username and a password to gain access.
    **Security Level:** Moderate, but vulnerable to various attacks like phishing, brute force, and credential stuffing.
    """)

    st.header("2. Multi-Factor Authentication (MFA)")
    st.write("""
    **Description:** Requires two or more verification methods, typically combining something the user knows (password) with something the user has (smartphone, hardware token) or something the user is (biometric).
    **Security Level:** High, significantly reduces the risk of unauthorized access.
    """)

    st.header("3. Biometric Authentication")
    st.write("""
    **Fingerprint:** Uses the unique patterns on a user's fingertip.
    **Face Recognition:** Uses the unique features of a user's face.
    **Voice Recognition:** Uses the unique characteristics of a user's voice.
    **Iris/Retina Scanning:** Uses the unique patterns in a user's iris or retina.
    **Security Level:** High, difficult to replicate, but can be affected by changes in physical characteristics or environmental conditions.
    """)

    st.header("4. Two-Factor Authentication (2FA)")
    st.write("""
    **Description:** A subset of MFA, typically involves a password and a second factor like a one-time code sent to a mobile device.
    **Security Level:** High, but slightly less secure than full MFA.
    """)

    st.header("5. Token-Based Authentication")
    st.write("""
    **Hardware Tokens:** Physical devices that generate a one-time code.
    **Software Tokens:** Apps that generate time-based one-time passwords (TOTP) or other codes.
    **Security Level:** High, as it requires possession of the token.
    """)

    st.header("6. Smart Card Authentication")
    st.write("""
    **Description:** Users authenticate by inserting a smart card into a reader and entering a PIN.
    **Security Level:** High, as it combines something the user has (smart card) with something the user knows (PIN).
    """)

    st.header("7. Single Sign-On (SSO)")
    st.write("""
    **Description:** Allows users to log in once and gain access to multiple systems without being prompted to log in again.
    **Security Level:** Varies, but can be very secure when combined with MFA.
    """)

    st.header("8. OAuth/OpenID Connect")
    st.write("""
    **Description:** Protocols that allow users to authenticate using their existing accounts from services like Google, Facebook, or Microsoft.
    **Security Level:** High, as it leverages the security of major providers.
    """)

    st.header("9. Passwordless Authentication")
    st.write("""
    **Email or SMS Links:** Sends a one-time login link to the user’s email or phone.
    **Push Notifications:** Sends a notification to a trusted device for approval.
    **Security Level:** High, as it eliminates the need for passwords, reducing the risk of password-related attacks.
    """)

    st.header("10. Behavioral Biometrics")
    st.write("""
    **Description:** Analyzes user behavior patterns, such as typing speed, mouse movements, and other interactions.
    **Security Level:** High, difficult to replicate but may require continuous monitoring.
    """)

    st.header("11. Knowledge-Based Authentication (KBA)")
    st.write("""
    **Static KBA:** Questions with pre-set answers, such as mother’s maiden name.
    **Dynamic KBA:** Questions generated from public or private data sources.
    **Security Level:** Low to Moderate, vulnerable to social engineering and data breaches.
    """)

    st.header("Activity: Domain-Based Authentication")
    st.write("""
    **Description:** Authentication that is restricted to users within a specific domain (e.g., company or organization domain). Users log in with their domain credentials.
    **Security Level:** High, as it leverages the organization's authentication policies and infrastructure.
    """)


# Create the option menu for navigation
tabs = st.tabs([
        "Lecture - Notes",
        "BMI Tkinter App",
        "BMI Streamlit APP",
        "Login Types: Activity",
        "Voice-based Login: EL", 
        "Useful Links"
    ])
# BMI Calculator using Tkinter (Explanation Only)
with tabs[1]:
    st.title("BMI Calculator using Tkinter")

    st.write("""
    ### Steps to Create a Simple BMI Calculator in Tkinter
    1. **Set Up the Environment**:
        - Ensure you have Python installed on your computer.
        - Install Tkinter if it's not already installed (it usually comes with Python).
    2. **Create the Main Window**:
        ```python
        import tkinter as tk
        root = tk.Tk()
        root.title("BMI Calculator")
        ```
    3. **Add Labels and Entry Widgets**:
        ```python
        label_weight = tk.Label(root, text="Weight (kg):")
        label_weight.pack(padx=10, pady=5)
        entry_weight = tk.Entry(root)
        entry_weight.pack(padx=10, pady=5)
        
        label_height = tk.Label(root, text="Height (cm):")
        label_height.pack(padx=10, pady=5)
        entry_height = tk.Entry(root)
        entry_height.pack(padx=10, pady=5)
        ```
    4. **Add a Button to Trigger BMI Calculation**:
        ```python
        button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
        button_calculate.pack(pady=20)
        ```
    5. **Add a Label to Display the Result**:
        ```python
        label_result = tk.Label(root, text="BMI: ")
        label_result.pack(pady=10)
        ```
    6. **Implement the BMI Calculation Logic**:
        ```python
        def calculate_bmi():
            weight = float(entry_weight.get())
            height = float(entry_height.get()) / 100  # Convert height to meters
            bmi = weight / (height ** 2)
            label_result.config(text=f'BMI: {bmi:.2f}')
        
        button_calculate.config(command=calculate_bmi)
        ```
    7. **Run the Application**:
        ```python
        root.mainloop()
        ```
    """)

# BMI Calculator using Streamlit
with tabs[2]:
    st.title("BMI Calculator using Streamlit")
    st.write("""
    ### Steps to Create a Simple BMI Calculator in Streamlit
    1. **Set Up the Environment**:
        - Ensure you have Python installed on your computer.
        - Install Streamlit if it's not already installed.
    2. **Add Streamlit Library**:
        ```python
        import streamlit as st
        ```
    3. **Add Inputs - Height and Weight**:
        ```python
        weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
        height = st.number_input("Height (cm)", min_value=0.0, format="%.2f")
        ```
    4. **Add a Button to Trigger BMI Calculation**:
        ```python
        if st.button("Calculate BMI"):
            height_m = height / 100  # Convert height to meters
            bmi = weight / (height_m ** 2)
            st.write(f"BMI: {bmi:.2f}")
        ```
    5. **Run the Application**:
        ```bash
        streamlit run app25.py
        ```
    """)

    weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Height (cm)", min_value=0.0, format="%.2f")

    calculate = st.button("Calculate BMI")

    if calculate:
        height_m = height / 100  # Convert height to meters
        bmi = weight / (height_m ** 2)
        st.write(f"BMI: {bmi:.2f}")

# Explanations of Programming Concepts
with tabs[0]:
    st.header("Operators, Precedence, and Associativity")
    st.write("""
    **Operators**: Operators are symbols that perform operations on variables and values.
    
    **Precedence**: Operator precedence determines the order in which operators are evaluated.
    
    **Associativity**: Operator associativity determines the order in which operators of the same precedence are evaluated.
    
    Examples:
    ```python
    result = 10 + 20 * 30  # Multiplication has higher precedence than addition
    result = (10 + 20) * 30  # Parentheses change the order of evaluation
    ```

    **Precedence Order (highest to lowest)**:
    1. Parentheses `()`
    2. Exponentiation `**`
    3. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
    4. Addition `+`, Subtraction `-`
    5. Comparison `<`, `<=`, `>`, `>=`
    6. Equality `==`, `!=`
    7. Logical AND `and`
    8. Logical OR `or`
    """)

    st.header("Decision Control Structures")
    st.write("""
    Decision control structures allow the flow of execution to change based on conditions.

    **if Statement**:
    ```python
    if condition:
        # Code to execute if condition is true
    ```

    **if-else Statement**:
    ```python
    if condition:
        # Code to execute if condition is true
    else:
        # Code to execute if condition is false
    ```

    **if-elif-else Statement**:
    ```python
    if condition1:
        # Code to execute if condition1 is true
    elif condition2:
        # Code to execute if condition2 is true
    else:
        # Code to execute if all conditions are false
    ```
    """)

    st.header("Looping Structures")
    st.write("""
    Looping structures allow repeating a set of statements multiple times.

    **for Loop**:
    ```python
    for variable in iterable:
        # Code to execute for each item in the iterable
    ```

    **while Loop**:
    ```python
    while condition:
        # Code to execute while the condition is true
    ```

    **Example**:
    ```python
    for i in range(5):
        print(i)  # Prints numbers from 0 to 4

    i = 0
    while i < 5:
        print(i)  # Prints numbers from 0 to 4
        i += 1
    ```
    """)

    st.header("Console Input and Output")
    st.write("""
    **Input**:
    ```python
    name = input("Enter your name: ")  # Reads a string from the console
    age = int(input("Enter your age: "))  # Reads an integer from the console
    ```

    **Output**:
    ```python
    print("Hello, World!")  # Prints the string to the console
    print("Your age is:", age)  # Prints a string followed by the value of age
    ```

    **Example**:
    ```python
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello, {name}. You are {age} years old.")
    ```
    """)

with tabs[4]:
    st.title("Voice-Based Login App - EL")

    st.markdown("""
    ### Steps and Explanation

    1. **Import Libraries:**
        - `streamlit` for creating the web app interface.
        - `speech_recognition` for recognizing speech from the microphone.

    2. **Define `recognize_speech_from_mic` Function:**
        - This function captures audio from the microphone and transcribes it into text using Google's Web Speech API.
        - **Parameters:**
          - `recognizer`: An instance of `sr.Recognizer`.
          - `microphone`: An instance of `sr.Microphone`.
        - **Functionality:**
          - Checks if the provided recognizer and microphone are valid instances.
          - Adjusts the recognizer for ambient noise and records audio.
          - Tries to transcribe the recorded audio using Google’s Web Speech API.
          - Handles errors if the API is unavailable or if the speech is not recognized.

    3. **Streamlit App Interface:**
        - The app title and instructions are displayed.
        - A button is provided for the user to press and start the recording process.
        - The recorded audio is processed and compared with a predefined passphrase to determine if the login is successful.

    ### Program Code
    ```python
    import streamlit as st
    import speech_recognition as sr

    def recognize_speech_from_mic(recognizer, microphone):
        \"\"\"Transcribe speech from recorded from `microphone`.\"\"\"
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `sr.Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `sr.Microphone` instance")

        # Adjust the recognizer sensitivity to ambient noise and record audio
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["error"] = "Unable to recognize speech"

        return response

    # Streamlit app
    st.title("Voice-Based Login")

    st.write("Press the button and say your passphrase.")

    if st.button("Record"):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with st.spinner("Listening..."):
            response = recognize_speech_from_mic(recognizer, microphone)

        if response["error"]:
            st.error("ERROR: {}".format(response["error"]))
        else:
            st.write("You said: {}".format(response["transcription"]))

            # Example authentication (replace with your actual logic)
            if response["transcription"].lower() == "hello world":
                st.success("Login successful!")
            else:
                st.error("Login failed. Try again.")
    ```
    """)

with tabs[3]: 
    display_authentication_methods()