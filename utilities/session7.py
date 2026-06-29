import streamlit as st

st.set_page_config(
    page_title="JavaScript Foundations for Full Stack Development",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 JavaScript Foundations for Full Stack Development")
st.markdown("### Unit 2 Learning Portal")

module = st.sidebar.radio(
    "Select Topic",
    [
        "JavaScript Objects",
        "Forms",
        "Events & Event Handling",
        "Async / Await",
        "Fetch API",
        "Navigator & Storage",
        "Login Workflow"
    ]
)

# =====================================================
# MODULE 1
# =====================================================

if module == "JavaScript Objects":

    st.header("📦 JavaScript Objects")

    st.subheader("What is an Object?")

    st.write("""
Objects help us store related information together.

Examples:
- Student
- Product
- Employee
- Course
""")

    st.code("""
const student = {

    name:"John",

    course:"BCA",

    age:20

};

console.log(student.name);
""", language="javascript")

    st.success("Output: John")

    st.subheader("Interactive Demo")

    name = st.text_input("Student Name")

    course = st.text_input("Course")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100
    )

    if st.button("Generate Object"):

        student = {

            "name": name,
            "course": course,
            "age": age

        }

        st.json(student)

    st.subheader("Activity")

    st.write("""
Create an object for:
- Student
- Product
- Employee
""")

# =====================================================
# MODULE 2
# =====================================================

elif module == "Forms":

    st.header("📝 JavaScript Forms")

    st.write("""
Forms collect information from users.

Examples:
- Login
- Registration
- Booking
- Service Request
""")

    st.code("""
<input type="text">

<input type="email">

<button>Submit</button>
""", language="html")

    st.subheader("Student Registration Form")

    name = st.text_input("Name")

    email = st.text_input("Email")

    course = st.selectbox(
        "Course",
        ["BCA", "BSc", "MCA", "MBA"]
    )

    if st.button("Submit Registration"):

        st.success("Registration Submitted")

        st.json({
            "name": name,
            "email": email,
            "course": course
        })

    st.subheader("Activity")

    st.write("""
Design a form for your selected domain.
""")

# =====================================================
# MODULE 3
# =====================================================

elif module == "Events & Event Handling":

    st.header("⚡ Events & Event Handling")

    st.write("""
Events occur when users interact with a webpage.
""")

    events = {

        "Event": [

            "click",
            "input",
            "change",
            "submit"

        ],

        "Purpose": [

            "Button Click",
            "Typing",
            "Selection Change",
            "Form Submission"

        ]
    }

    st.table(events)

    st.subheader("Click Event Demo")

    if st.button("Click Me"):

        st.success("Click Event Triggered")

    st.subheader("Input Event Demo")

    text = st.text_input("Type Something")

    if text:

        st.info(f"You Typed: {text}")

    st.subheader("Change Event Demo")

    color = st.selectbox(
        "Select Color",
        ["Red", "Blue", "Green"]
    )

    st.success(f"Selected: {color}")

    st.subheader("Activity")

    st.write("""
Implement at least 3 events in your project.
""")

# =====================================================
# MODULE 4
# =====================================================

elif module == "Async / Await":

    st.header("⏳ Async / Await")

    st.write("""
Some operations take time.

Examples:
- API Calls
- Database Queries
- File Uploads
""")

    st.code("""
console.log("A");

setTimeout(()=>{

console.log("B");

},3000);

console.log("C");
""", language="javascript")

    st.success("""
Output:

A

C

B
""")

    st.code("""
async function load(){

const response =

await fetch(url);

}
""", language="javascript")

    st.info("""
await means:

Wait until the result arrives.
""")

    st.subheader("Activity")

    st.write("""
Identify 3 situations where waiting is required.
""")

# =====================================================
# MODULE 5
# =====================================================

elif module == "Fetch API":

    st.header("🌐 Fetch API")

    st.write("""
Fetch API allows JavaScript to communicate with servers.
""")

    st.code("""
const response =

await fetch(url);

const data =

await response.json();
""", language="javascript")

    st.markdown("""
```text
Browser
   ↓
Server
   ↓
Response
```
""")

    st.subheader("GET Request")

    st.code("""
fetch("/students");
""", language="javascript")

    st.subheader("POST Request")

    st.code("""
fetch("/login",{
    method:"POST"
});
""", language="javascript")

    st.subheader("Activity")

    st.write("""
Identify where Fetch API can be used in your domain project.
""")

# =====================================================
# MODULE 6
# =====================================================

elif module == "Navigator & Storage":

    st.header("🌍 Navigator API & Browser Storage")

    st.subheader("Geolocation")

    st.code("""
navigator.geolocation
.getCurrentPosition(...);
""", language="javascript")

    st.write("""
Useful for:
- Travel
- Tourism
- Delivery Services
""")

    st.subheader("Local Storage")

    st.code("""
localStorage.setItem(
    "name",
    "John"
);
""", language="javascript")

    comparison = {
        "Feature": [
            "Cookies",
            "Local Storage",
            "Session Storage"
        ],
        "Purpose": [
            "Authentication",
            "Preferences",
            "Temporary Data"
        ]
    }

    st.table(comparison)

    st.subheader("Activity")

    st.write("""
Suggest one browser feature that can enhance your project.
""")

# =====================================================
# MODULE 7
# =====================================================

elif module == "Login Workflow":

    st.header("🚀 Complete Login Workflow")

st.markdown("""
Form
   ↓
Event
   ↓
Object
   ↓
JSON
   ↓
Fetch API
   ↓
Express Server
   ↓
Response
   ↓
UI Update

""")

st.subheader("Frontend Example")

st.code("""

const loginData = {

username,

password

};

await fetch(

"/login",

{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(loginData)

}

);
""", language="javascript")

st.subheader("Backend Example")

st.code("""

app.post(

"/login",

(req,res)=>{

res.json({

success:true,

message:"Login Successful"

});

}

);
""", language="javascript")

st.subheader("Full Stack Architecture")

st.markdown("""
HTML Form
     ↓
JavaScript Event
     ↓
Fetch API
     ↓
Express Route
     ↓
Validation
     ↓
JSON Response
     ↓
DOM Update

""")

st.success("""

This is the foundation of Full Stack Development.
""")

st.subheader("Mini Project")

st.write("""

Build a domain-specific prototype.

Requirements:

✅ Responsive UI

✅ Form

✅ Event Handling

✅ JavaScript Object

✅ Async/Await

✅ Fetch API

Optional:

✅ Navigator API

✅ Local Storage
""")

st.balloons()

st.success("""

Congratulations!

You have completed:

✅ Objects

✅ Forms

✅ Events

✅ Async/Await

✅ Fetch API

✅ Navigator API

✅ Browser Storage

✅ Login Workflow

Ready for:

🚀 Express.js

🚀 REST APIs

🚀 MongoDB

🚀 React
""")