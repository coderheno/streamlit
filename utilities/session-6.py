import streamlit as st

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="JavaScript Interactive Learning Portal",
    page_icon="📘",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main-header{
    font-size:42px;
    font-weight:bold;
    color:#2563eb;
}

.sub-header{
    font-size:24px;
    color:#374151;
}

.topic-box{
    background:#f8fafc;
    padding:20px;
    border-radius:10px;
    border-left:6px solid #2563eb;
    margin-bottom:15px;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("📘 JavaScript Portal")

module = st.sidebar.selectbox(
    "Select Topic",
    [
        "🏠 Home",
        "1. Events & Event Handling",
        "2. Async & Await",
        "3. JavaScript Navigator",
        "4. JavaScript Cookies",
        "5. Quiz",
        "6. AI Tutor"
    ]
)

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------

if module == "🏠 Home":

    st.markdown(
        "<div class='main-header'>JavaScript Interactive Learning Portal</div>",
        unsafe_allow_html=True
    )

    st.write("")

  

    st.write("")

    st.markdown("""
Welcome to the **JavaScript Interactive Learning Portal**.

This portal has been designed to help students understand JavaScript concepts
through theory, demonstrations, coding activities, real-world examples,
mini projects, quizzes, and viva preparation.

Instead of memorizing syntax, students will learn by building
interactive web applications.
""")

    st.divider()

    st.subheader("🎯 Course Learning Outcomes")

    st.success("""
After completing this module, students will be able to:

✅ Understand JavaScript Event Handling

✅ Develop interactive webpages

✅ Implement Asynchronous Programming

✅ Use Browser APIs

✅ Store information using Cookies

✅ Integrate JavaScript with HTML5 applications
""")

    st.divider()

    st.subheader("📚 Module Structure")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
### Module 1

📌 Events & Event Handling

• Event Introduction

• Mouse Events

• Keyboard Events

• Form Events

• Window Events

• Event Listeners

• Demonstrations

• Activities
""")

        st.info("""
### Module 2

📌 Async & Await

• Synchronous Programming

• Asynchronous Programming

• Callback

• Promise

• Async Function

• Await Keyword

• Fetch API

• Demonstrations
""")

    with col2:

        st.info("""
### Module 3

📌 JavaScript Navigator

• Browser Information

• User Agent

• Platform

• Language

• Online Status

• Geolocation

• Cookies Enabled
""")

        st.info("""
### Module 4

📌 Cookies

• Cookie Basics

• CRUD Operations

• Session Cookies

• Persistent Cookies

• Local Storage Comparison

• Security
""")

    st.divider()

    st.subheader("📖 Teaching Methodology")

    st.markdown("""
Each topic follows the same learning structure:

1. Introduction

2. Why do we need it?

3. Theory

4. Syntax

5. Live Demonstration

6. Code Walkthrough

7. Real-world Applications

8. Best Practices

9. Classroom Activity

10. Lab Exercise

11. Viva Questions

12. MCQs

13. Mini Challenge
""")

    st.divider()

    st.subheader("🛠 Software Requirements")

    st.write("""
- Visual Studio Code

- Google Chrome

- Git

- GitHub

- Tailwind CSS

- JavaScript

- HTML5
""")

    st.divider()

    st.subheader("🌍 Real-world Applications")

    st.markdown("""
JavaScript powers almost every modern website.

Examples include:

- Gmail

- Google Maps

- YouTube

- Amazon

- Flipkart

- Netflix

- Instagram

- Swiggy

- Zomato

- Microsoft Teams
""")

    st.divider()

    st.subheader("🚀 Learning Approach")

    st.write("""
✔ Learn Concepts

✔ Watch Demonstrations

✔ Read Sample Code

✔ Perform Activities

✔ Complete Lab Exercises

✔ Solve MCQs

✔ Build Mini Projects
""")

    st.divider()

    st.success(
        "Use the navigation panel on the left to begin with Module 1: Events & Event Handling."
    )

    st.markdown(
        "<div class='footer'>© 2026 Full Stack Development | CHRIST (Deemed to be University)</div>",
        unsafe_allow_html=True
    )
# ---------------------------------------------------
# MODULE 1 : EVENTS & EVENT HANDLING
# ---------------------------------------------------
# ---------------------------------------------------
# AI TUTOR
# ---------------------------------------------------

elif module == "6. AI Tutor":

    st.title("🤖 AI Tutor")

    st.markdown("""
### Full Stack Development AI Tutor

Ask questions related to:

- HTML5
- Tailwind CSS
- JavaScript
- Async & Await
- Git & GitHub
- Browser APIs
- Full Stack Development

Click the button below to launch the AI Tutor.
""")

    st.link_button(
        "🚀 Open AI Tutor",
        "https://fscbot.streamlit.app/"
    )

    st.info(
        "The AI Tutor will open in a new browser tab."
    )
elif module == "1. Events & Event Handling":

    st.title("🖱️ JavaScript Events & Event Handling")

    st.write("")

    st.markdown("""
An **event** is an action or occurrence that happens in the browser,
which JavaScript can detect and respond to.

Events make web pages **interactive**.

Without events, webpages become static and cannot respond to user actions.
""")

    st.divider()

    st.subheader("🎯 Learning Outcomes")

    st.success("""
After completing this chapter, you will be able to:

✅ Understand Event Driven Programming

✅ Identify different JavaScript Events

✅ Use Event Handlers

✅ Use addEventListener()

✅ Build Interactive Web Applications
""")

    st.divider()

    st.subheader("🌍 Real-world Examples")

    col1,col2 = st.columns(2)

    with col1:

        st.info("""
### Gmail

✔ Click Send

✔ Type Email

✔ Hover Buttons

✔ Submit Forms
""")

        st.info("""
### Amazon

✔ Add to Cart

✔ Search Products

✔ Hover Products

✔ Filter Categories
""")

    with col2:

        st.info("""
### YouTube

✔ Play Video

✔ Pause Video

✔ Volume Change

✔ Full Screen
""")

        st.info("""
### Google Maps

✔ Drag Map

✔ Zoom

✔ Search Location

✔ Detect Current Location
""")

    st.divider()

    st.subheader("⚙️ What is Event Driven Programming?")

    st.markdown("""
Traditional programs execute line by line.

JavaScript waits for an event to occur.

When an event occurs,

↓

JavaScript executes the associated function.
""")

    st.code("""

User Action

      ↓

Browser detects Event

      ↓

JavaScript Event Listener

      ↓

Function Executes

      ↓

Output Displayed

""")

    st.divider()

    st.subheader("📚 Event Categories")

    event_data = {
        "Category":[
            "Mouse Events",
            "Keyboard Events",
            "Form Events",
            "Window Events",
            "Clipboard Events",
            "Drag & Drop"
        ],

        "Examples":[
            "click, mouseover, mouseout",
            "keydown, keyup",
            "input, submit, change",
            "load, resize, scroll",
            "copy, paste",
            "drag, drop"
        ]
    }

    st.table(event_data)

    st.divider()

    st.subheader("🧩 Common Events")

    st.code("""

Mouse Events

click

dblclick

mouseover

mouseout

mousemove

-------------------------

Keyboard Events

keydown

keyup

keypress

-------------------------

Form Events

focus

blur

change

submit

input

-------------------------

Window Events

load

resize

scroll

""")

    st.divider()

    st.subheader("💻 Syntax")

    st.code("""

element.addEventListener(

    "event",

    function(){

        // JavaScript Code

    }

);

""",language="javascript")

    st.divider()

    st.subheader("📌 Example 1")

    st.code("""

<button id="btn">

Click Me

</button>

<script>

document.getElementById(

"btn"

).addEventListener(

"click",

function(){

alert("Button Clicked");

}

);

</script>

""",language="html")

    st.info("""
Explanation

button → HTML Element

click → Event

addEventListener() → Registers the Event

function() → Executes when event occurs
""")

    st.divider()

    st.subheader("🎮 Interactive Demonstration")

    user_name = st.text_input(
        "Enter your name"
    )

    if user_name:

        st.success(
            f"Welcome {user_name}"
        )

        st.write("""
This demonstrates an **Input Event**.

Every time you type,

JavaScript detects the event and updates the output.
""")

    st.divider()

    st.subheader("📋 Activity")

    st.markdown("""
Build a webpage demonstrating any **five events**.

Suggested Events:

- input

- mouseover

- mouseout

- resize

- focus

Display meaningful output for each event.
""")

    st.divider()

    st.subheader("💡 Best Practices")

    st.write("""

✔ Use addEventListener()

✔ Keep functions small

✔ Avoid inline JavaScript

✔ Give meaningful function names

✔ Validate user input

✔ Improve User Experience

""")

    st.divider()

    st.subheader("❓ Viva Questions")

    st.markdown("""

1. What is an Event?

2. What is Event Handling?

3. What is Event Driven Programming?

4. What is addEventListener()?

5. Name five Mouse Events.

6. Name three Keyboard Events.

7. Difference between keydown and keyup.

8. Difference between mouseover and mouseout.

9. What is an Event Listener?

10. Why are Events important?

""")

    st.divider()

    st.subheader("📝 Mini Challenge")

    st.warning("""
Develop a Student Registration Form implementing:

✔ input

✔ focus

✔ blur

✔ submit

✔ change

Display appropriate messages whenever each event occurs.
""")
# ---------------------------------------------------
# MOUSE EVENTS
# ---------------------------------------------------

    st.divider()

    st.header("🖱 Mouse Events")

    st.markdown("""
Mouse events occur whenever the user interacts with the mouse.

Examples include:

- click
- dblclick
- mouseover
- mouseout
- mousemove

Mouse events improve user interaction and provide instant visual feedback.
""")

    st.divider()

    st.subheader("1. Mouse Over Event")

    st.markdown("""
### What is Mouse Over?

The **mouseover** event occurs whenever the mouse pointer enters an element.

### Real World Examples

✔ Amazon Product Cards

✔ Netflix Movie Posters

✔ Navigation Menus

✔ Image Galleries
""")

    st.code("""
<div id="box">

Hover over me

</div>

<script>

document.getElementById("box")

.addEventListener(

"mouseover",

function(){

this.style.background="orange";

});

</script>
""", language="html")

    hover = st.checkbox("Hover Simulation")

    if hover:

        st.success("Mouse entered the element.")

        st.info("Background changes when mouse enters.")

    else:

        st.write("Move the mouse over an HTML element to trigger this event.")

    st.divider()

    st.subheader("2. Mouse Out Event")

    st.markdown("""
The **mouseout** event occurs when the mouse pointer leaves an element.

Usually used to restore the original appearance.
""")

    st.code("""
element.addEventListener(

"mouseout",

function(){

this.style.background="white";

});

""", language="javascript")

    leave = st.checkbox("Mouse Left Element")

    if leave:

        st.warning("Mouse left the element.")

    st.divider()

    st.subheader("3. Double Click Event")

    st.markdown("""
The **dblclick** event occurs when the user double-clicks an element.

### Applications

✔ Zoom Images

✔ Edit Records

✔ Open Files

✔ Full Screen Mode
""")

    st.code("""
element.addEventListener(

"dblclick",

function(){

alert("Double Click");

});

""", language="javascript")

    dbl = st.button("Double Click Simulation")

    if dbl:

        st.success("Imagine this action is triggered by a double click.")

    st.divider()

    st.subheader("4. Mouse Move Event")

    st.markdown("""
The **mousemove** event occurs whenever the mouse moves over an element.

Applications

✔ Drawing Applications

✔ Games

✔ Image Magnifier

✔ Coordinate Tracking
""")

    st.code("""
element.addEventListener(

"mousemove",

function(event){

console.log(

event.clientX,

event.clientY

);

});

""", language="javascript")

    x = st.slider("Mouse X Coordinate",0,1000,300)

    y = st.slider("Mouse Y Coordinate",0,800,200)

    st.write("Current Position")

    st.code(f"""

X : {x}

Y : {y}

""")

    st.divider()

    st.subheader("📊 Mouse Event Comparison")

    st.table({

        "Event":[
            "mouseover",
            "mouseout",
            "dblclick",
            "mousemove"
        ],

        "Purpose":[
            "Pointer enters element",
            "Pointer leaves element",
            "User double clicks",
            "Pointer movement"
        ]

    })

    st.divider()

    st.subheader("🌍 Real-world Scenario")

    st.info("""
Imagine an E-Commerce Website.

mouseover

↓

Highlight Product

mouseout

↓

Restore Product Card

dblclick

↓

Quick View Product

mousemove

↓

Image Zoom Effect
""")

    st.divider()

    st.subheader("🎯 Activity")

    st.markdown("""
Develop an interactive product card.

Requirements

✔ Mouse Over

Increase card size.

✔ Mouse Out

Restore original size.

✔ Double Click

Display product information.

✔ Mouse Move

Display current coordinates.
""")

    st.divider()

    st.subheader("💡 Best Practices")

    st.write("""

✔ Avoid excessive animations

✔ Keep transitions smooth

✔ Provide visual feedback

✔ Do not overload users

✔ Maintain accessibility

""")

    st.divider()

    st.subheader("❓ Viva Questions")

    st.markdown("""

1. What is Mouse Event?

2. Difference between mouseover and mousemove.

3. Difference between mouseover and mouseout.

4. What is dblclick?

5. Name four applications of mouse events.

6. Which event tracks cursor position?

7. How do you register mouse events?

8. What object provides mouse coordinates?

""")

    st.divider()

    st.success("Mouse Events Completed ✅")
# ---------------------------------------------------
# KEYBOARD EVENTS
# ---------------------------------------------------

    st.divider()

    st.header("⌨️ Keyboard Events")

    st.markdown("""
Keyboard events occur whenever the user presses or releases keys.

Common Keyboard Events

• keydown

• keyup

• keypress (Deprecated)

Keyboard events are widely used in:

✔ Login Forms

✔ Search Bars

✔ Shortcuts

✔ Games

✔ Editors
""")

    st.subheader("1. Key Down")

    st.code("""
<input id="txt">

<script>

document.getElementById("txt")

.addEventListener(

"keydown",

function(){

console.log("Key Pressed");

});

</script>
""", language="html")

    key = st.text_input(
        "Type something"
    )

    if key:

        st.success(
            f"Key Down Event Triggered : {key}"
        )

    st.divider()

    st.subheader("2. Key Up")

    st.markdown("""
The keyup event occurs after a key is released.

Applications

✔ Search Suggestions

✔ Live Validation

✔ Character Counter
""")

    st.code("""
element.addEventListener(

"keyup",

function(){

});

""", language="javascript")

    st.divider()

# ---------------------------------------------------
# FORM EVENTS
# ---------------------------------------------------

    st.header("📝 Form Events")

    st.markdown("""
Form events improve user interaction and validation.
""")

    st.table({

        "Event":[
            "focus",
            "blur",
            "input",
            "change",
            "submit"
        ],

        "Purpose":[
            "Input Selected",
            "Input Lost Focus",
            "User Typing",
            "Value Changed",
            "Form Submission"
        ]

    })

    st.divider()

    st.subheader("Focus Event")

    st.code("""
<input

onfocus="highlight()">

""", language="html")

    st.info("""
Real World

✔ Highlight Login Box

✔ Highlight Search Box

✔ Cursor Placement
""")

    st.divider()

    st.subheader("Blur Event")

    st.code("""
<input

onblur="validate()">

""", language="html")

    st.info("""
Real World

✔ Email Validation

✔ Password Validation

✔ Required Field Checking
""")

    st.divider()

    st.subheader("Input Event")

    name = st.text_input(
        "Student Name"
    )

    st.write(
        "Characters :",
        len(name)
    )

    st.code("""
input.addEventListener(

"input",

function(){

});

""", language="javascript")

    st.divider()

    st.subheader("Change Event")

    course = st.selectbox(

        "Select Course",

        [
            "BCA",
            "MCA",
            "BSc CS"
        ]

    )

    st.success(
        f"Selected : {course}"
    )

    st.divider()

    st.subheader("Submit Event")

    with st.form("student"):

        email = st.text_input(
            "Email"
        )

        submit = st.form_submit_button(
            "Submit"
        )

    if submit:

        st.success(
            "Form Submitted Successfully"
        )

# ---------------------------------------------------
# WINDOW EVENTS
# ---------------------------------------------------

    st.divider()

    st.header("🖥 Window Events")

    st.markdown("""
Window events occur on the browser window.

Examples

✔ load

✔ resize

✔ scroll
""")

    st.code("""
window.addEventListener(

"load",

function(){

});

""", language="javascript")

    width = st.slider(
        "Resize Simulation",
        300,
        1920,
        1024
    )

    st.write(
        f"Current Width : {width}px"
    )

    progress = st.slider(
        "Scroll Position",
        0,
        100,
        20
    )

    st.progress(
        progress
    )

# ---------------------------------------------------
# CLIPBOARD EVENTS
# ---------------------------------------------------

    st.divider()

    st.header("📋 Clipboard Events")

    st.markdown("""
Clipboard Events

✔ copy

✔ cut

✔ paste

Applications

✔ Copy Text

✔ Paste Validation

✔ Security
""")

    st.code("""
element.addEventListener(

"copy",

function(){

});

element.addEventListener(

"paste",

function(){

});

""", language="javascript")

# ---------------------------------------------------
# EVENT SUMMARY
# ---------------------------------------------------

    st.divider()

    st.header("📊 Summary")

    st.table({

        "Category":[

            "Mouse",

            "Keyboard",

            "Form",

            "Window",

            "Clipboard"

        ],

        "Examples":[

            "mouseover",

            "keydown",

            "submit",

            "resize",

            "copy"

        ]

    })

# ---------------------------------------------------
# CLASSROOM ACTIVITY
# ---------------------------------------------------

    st.divider()

    st.header("🎯 Classroom Activity")

    st.markdown("""

Develop a Student Registration Page.

Implement

✔ keydown

✔ input

✔ focus

✔ blur

✔ change

✔ submit

Display meaningful messages for every event.

""")

# ---------------------------------------------------
# MINI PROJECT
# ---------------------------------------------------

    st.divider()

    st.header("🚀 Mini Project")

    st.success("""

Develop an Interactive Course Registration System.

Features

✔ Live Character Counter

✔ Email Validation

✔ Password Validation

✔ Course Selection

✔ Form Submission

✔ Responsive UI

✔ Tailwind CSS

""")

# ---------------------------------------------------
# VIVA QUESTIONS
# ---------------------------------------------------

    st.divider()

    st.header("❓ Viva Questions")

    st.markdown("""

1. What is Event Handling?

2. Difference between keydown and keyup.

3. Difference between focus and blur.

4. What is input event?

5. Difference between input and change.

6. What is submit event?

7. Difference between mouseover and mousemove.

8. Name three Window Events.

9. What is Clipboard Event?

10. Why is Event Driven Programming important?

""")

# ---------------------------------------------------
# MINI QUIZ
# ---------------------------------------------------

    st.divider()

    st.header("📝 Quick Quiz")

    answer = st.radio(

        "Which event occurs when typing inside a textbox?",

        [

            "mouseover",

            "input",

            "resize",

            "load"

        ]

    )

    if answer == "input":

        st.success("Correct!")

    elif answer:

        st.error("Incorrect. Correct answer is input.")

    st.success("🎉 Congratulations! You have completed JavaScript Event Handling.")
# ---------------------------------------------------
# MODULE 2 : ASYNC & AWAIT
# ---------------------------------------------------

elif module == "2. Async & Await":

    st.title("⚡ JavaScript Async & Await")

    st.write("")

    st.markdown("""
Modern web applications perform many tasks in the background without freezing the webpage.

Imagine opening YouTube.

✔ Videos load in the background.

✔ Comments load separately.

✔ Recommendations appear later.

✔ Advertisements load independently.

All of this is possible because of **Asynchronous Programming**.
""")

    st.divider()

    st.subheader("🎯 Learning Outcomes")

    st.success("""

After completing this module, you will be able to

✅ Understand Synchronous Programming

✅ Understand Asynchronous Programming

✅ Explain Callback Functions

✅ Explain Promises

✅ Write Async Functions

✅ Use Await

✅ Fetch Data from APIs

""")

    st.divider()

    st.subheader("🌍 Real-world Examples")

    col1,col2 = st.columns(2)

    with col1:

        st.info("""

### Netflix

Movie loads...

↓

Subtitle loads...

↓

Recommendations load...

""")

        st.info("""

### Swiggy

Order Placed

↓

Restaurant Accepts

↓

Delivery Assigned

↓

Live Tracking

""")

    with col2:

        st.info("""

### Google Maps

Load Map

↓

Current Location

↓

Traffic

↓

Nearby Places

""")

        st.info("""

### Amazon

Product Page

↓

Reviews

↓

Ratings

↓

Recommended Products

""")

    st.divider()

    st.subheader("🤔 Why Async Programming?")

    st.markdown("""

Suppose you click **Submit Assignment**.

Uploading may take 10 seconds.

Should the browser freeze for 10 seconds?

❌ No.

Instead,

JavaScript continues executing other tasks while the upload happens in the background.

This is called **Asynchronous Programming**.

""")

    st.divider()

    st.subheader("🍽 Restaurant Analogy")

    st.code("""

Customer Orders Food

        ↓

Chef Starts Cooking

        ↓

Customer Waits

        ↓

Meanwhile...

Other Customers Place Orders

Bills are Generated

Tables are Cleaned

        ↓

Food Ready

""")

    st.success("""

The restaurant never stops working.

JavaScript behaves the same way.

""")

    st.divider()

    st.subheader("📚 Synchronous Programming")

    st.markdown("""

Synchronous code executes one statement after another.

Next statement waits until the previous statement finishes.

""")

    st.code("""

console.log("Start");

console.log("Loading");

console.log("Finish");

""",language="javascript")

    st.info("""

Execution Order

Start

↓

Loading

↓

Finish

""")

    st.divider()

    st.subheader("📚 Asynchronous Programming")

    st.markdown("""

Asynchronous code allows long-running operations to execute in the background.

The browser remains responsive.

""")

    st.code("""

console.log("Start");

setTimeout(function(){

console.log("Loading Completed");

},3000);

console.log("Finish");

""",language="javascript")

    st.success("""

Output

Start

Finish

Loading Completed

""")

    st.divider()

    st.subheader("🧪 Live Demonstration")

    seconds = st.slider(

        "Simulate Loading Time",

        1,

        10,

        3

    )

    if st.button("Run Simulation"):

        with st.spinner("Loading Data..."):

            import time

            time.sleep(seconds)

        st.success("Task Completed Successfully!")

    st.divider()

    st.subheader("⚖ Comparison")

    st.table({

        "Synchronous":[

            "Runs Sequentially",

            "Waits",

            "Can Block UI",

            "Simple Execution"

        ],

        "Asynchronous":[

            "Runs Independently",

            "Does Not Wait",

            "Responsive UI",

            "Better Performance"

        ]

    })

    st.divider()

    st.subheader("🎯 Classroom Activity")

    st.markdown("""

Think of five real-world applications that use asynchronous programming.

Examples

✔ Food Delivery

✔ Banking

✔ Chat Applications

✔ Social Media

✔ Online Shopping

Discuss why synchronous programming would fail in these systems.

""")

    st.divider()

    st.subheader("❓ Viva Questions")

    st.markdown("""

1. What is Synchronous Programming?

2. What is Asynchronous Programming?

3. Why is Async Programming needed?

4. Give five real-world examples.

5. Why does JavaScript use asynchronous programming?

""")
    # ---------------------------------------------------
    # CALLBACK FUNCTIONS
    # ---------------------------------------------------

    st.divider()

    st.header("📞 Callback Functions")

    st.markdown("""

A **callback** is a function that is passed as an argument to another function.

Instead of executing immediately, the callback executes **after another task finishes**.

""")

    st.subheader("🏪 Real World Example")

    st.info("""

Restaurant

↓

Customer Places Order

↓

Chef Cooks Food

↓

Food Ready

↓

Waiter Serves Food

The waiter only serves **after** the chef finishes cooking.

The waiter acts like a Callback Function.

""")

    st.code("""

function greet(name){

    console.log("Hello " + name);

}

function process(callback){

    callback("Vijay");

}

process(greet);

""",language="javascript")

    st.success("""

Output

Hello Vijay

""")

    st.divider()

    st.subheader("🎮 Callback Demonstration")

    if st.button("Prepare Coffee"):

        st.info("Preparing Coffee...")

        import time

        time.sleep(2)

        st.success("☕ Coffee Ready!")

        st.balloons()

    st.divider()

    st.subheader("✅ Advantages")

    st.write("""

✔ Executes after another function

✔ Useful for asynchronous tasks

✔ Event Handling

✔ API Requests

✔ File Reading

""")

    st.divider()

    st.subheader("❌ Disadvantages")

    st.error("""

Too many callbacks make code difficult to read.

This is called

Callback Hell

""")

    st.divider()

    st.header("😵 Callback Hell")

    st.markdown("""

Imagine ordering food online.

Step 1

Restaurant Accepts

↓

Step 2

Chef Starts Cooking

↓

Step 3

Delivery Assigned

↓

Step 4

Driver Picks Food

↓

Step 5

Delivery Completed

If every step depends on the previous step using callbacks,

the code becomes deeply nested.

""")

    st.code("""

login(function(){

    loadProfile(function(){

        loadOrders(function(){

            loadPayments(function(){

                loadNotifications(function(){

                    console.log("Completed");

                });

            });

        });

    });

});

""",language="javascript")

    st.warning("""

This is called Callback Hell.

Problems

❌ Difficult to Read

❌ Difficult to Debug

❌ Difficult to Maintain

""")

    st.divider()

    st.header("🤝 Promise")

    st.markdown("""

A Promise represents the eventual completion (or failure)

of an asynchronous operation.

Instead of nesting callbacks,

JavaScript introduced Promises.

""")

    st.subheader("📦 Promise States")

    st.table({

        "State":[

            "Pending",

            "Fulfilled",

            "Rejected"

        ],

        "Meaning":[

            "Still Processing",

            "Completed Successfully",

            "Failed"

        ]

    })

    st.divider()

    st.subheader("🌍 Real World Example")

    st.info("""

Online Shopping

↓

Order Placed

↓

Processing...

↓

Delivered ✔

or

Cancelled ❌

""")

    st.divider()

    st.subheader("Promise Syntax")

    st.code("""

let promise = new Promise(

function(resolve,reject){

    resolve("Success");

}

);

""",language="javascript")

    st.divider()

    st.subheader("Promise Example")

    st.code("""

let order = new Promise(

function(resolve,reject){

    let payment=true;

    if(payment){

        resolve("Order Confirmed");

    }

    else{

        reject("Payment Failed");

    }

}

);

order

.then(result=>console.log(result))

.catch(error=>console.log(error));

""",language="javascript")

    st.divider()

    st.subheader("🎮 Promise Simulation")

    choice = st.radio(

        "Payment Status",

        [

            "Successful",

            "Failed"

        ]

    )

    if st.button("Process Payment"):

        with st.spinner("Processing..."):

            import time

            time.sleep(2)

        if choice=="Successful":

            st.success("✅ Promise Resolved")

            st.success("Order Confirmed")

        else:

            st.error("❌ Promise Rejected")

            st.error("Payment Failed")

    st.divider()

    st.subheader("📊 Callback vs Promise")

    st.table({

        "Callback":[

            "Nested",

            "Hard to Maintain",

            "Callback Hell",

            "Less Readable"

        ],

        "Promise":[

            "Cleaner",

            "Easy to Read",

            "Chainable",

            "Better Error Handling"

        ]

    })

    st.divider()

    st.subheader("🎯 Activity")

    st.markdown("""

Think of five real-world systems where promises are useful.

Examples

✔ Online Banking

✔ Railway Ticket Booking

✔ Movie Ticket Booking

✔ Shopping

✔ Food Delivery

""")

    st.divider()

    st.subheader("❓ Viva Questions")

    st.markdown("""

1. What is a Callback?

2. Why are Callbacks used?

3. What is Callback Hell?

4. What problems arise due to Callback Hell?

5. What is a Promise?

6. Name the three states of a Promise.

7. Difference between Callback and Promise.

8. Why are Promises preferred?

""")
    # ---------------------------------------------------
    # ASYNC FUNCTIONS
    # ---------------------------------------------------

    st.divider()

    st.header("🚀 Async Functions")

    st.markdown("""

JavaScript introduced the **async** keyword to simplify asynchronous programming.

Instead of writing multiple callbacks or chaining promises,
we can write asynchronous code that looks like normal sequential code.

""")

    st.subheader("Why Async?")

    st.info("""

Problems with Callbacks

❌ Nested Functions

❌ Difficult to Read

❌ Difficult to Debug

Problems with Promises

❌ Long .then() chains

Async/Await solves both problems.

""")

    st.divider()

    st.subheader("Syntax")

    st.code("""

async function functionName(){

}

""",language="javascript")

    st.markdown("""

An async function **always returns a Promise**.

""")

    st.divider()

    st.subheader("Simple Example")

    st.code("""

async function greet(){

    return "Welcome Students";

}

greet().then(

result=>console.log(result)

);

""",language="javascript")

    st.success("""

Output

Welcome Students

""")

    st.divider()

    st.header("⏳ Await Keyword")

    st.markdown("""

The **await** keyword pauses the execution of an async function
until a Promise is completed.

It makes asynchronous code easier to understand.

""")

    st.code("""

async function demo(){

    let response = await fetch(url);

}

""",language="javascript")

    st.divider()

    st.subheader("Restaurant Example")

    st.info("""

Customer Orders Pizza

↓

Chef Starts Preparing

↓

await

↓

Pizza Ready

↓

Serve Pizza

The waiter waits only for the pizza.

Other restaurant activities continue normally.

""")

    st.divider()

    st.subheader("Flow Diagram")

    st.code("""

Start

↓

Call Async Function

↓

Wait using await

↓

Promise Completed

↓

Continue Execution

↓

Finish

""")

    st.divider()

    st.subheader("Traditional Promise")

    st.code("""

fetch(url)

.then(response=>response.json())

.then(data=>console.log(data))

.catch(error=>console.log(error));

""",language="javascript")

    st.divider()

    st.subheader("Using Async Await")

    st.code("""

async function loadData(){

    try{

        let response = await fetch(url);

        let data = await response.json();

        console.log(data);

    }

    catch(error){

        console.log(error);

    }

}

""",language="javascript")

    st.success("""

Advantages

✔ Cleaner

✔ Easier to Read

✔ Easier to Debug

✔ Looks like Sequential Programming

""")

    st.divider()

    st.header("🧪 Live Demonstration")

    if st.button("Load Student Records"):

        with st.spinner("Fetching Student Records..."):

            import time

            time.sleep(3)

        students=[

            "Alice",

            "John",

            "David",

            "Maria",

            "Vijay"

        ]

        st.success("Data Loaded Successfully")

        st.table(students)

    st.divider()

    st.header("📊 Promise vs Async Await")

    st.table({

        "Promise":[

            ".then()",

            "Nested",

            "Moderate Readability",

            "More Boilerplate"

        ],

        "Async Await":[

            "await",

            "Linear",

            "Very Readable",

            "Cleaner"

        ]

    })

    st.divider()

    st.header("🌍 Real-world Applications")

    st.markdown("""

Almost every modern web application uses async/await.

Examples

✔ Gmail

✔ YouTube

✔ Google Maps

✔ Instagram

✔ Facebook

✔ Amazon

✔ Netflix

✔ Flipkart

✔ Swiggy

✔ Zomato

""")

    st.divider()

    st.header("💡 Why Full Stack Developers Love Async/Await")

    st.write("""

✔ API Calls

✔ Database Queries

✔ Login Authentication

✔ Payment Processing

✔ Image Upload

✔ Cloud Storage

✔ Notifications

✔ AI Chatbots

✔ File Downloads

✔ Real-time Dashboards

""")

    st.divider()

    st.header("🎯 Activity")

    st.markdown("""

Scenario

You are developing a Student Portal.

Requirements

✔ Load Student Details

✔ Load Marks

✔ Load Attendance

✔ Display Result

Identify where async/await should be used.

""")

    st.divider()

    st.header("❓ Viva Questions")

    st.markdown("""

1. What is an async function?

2. What does async return?

3. What is await?

4. Why is await used?

5. Difference between Promise and Async.

6. Can await be used without async?

7. What happens if Promise fails?

8. Why do we use try-catch?

9. What are the advantages of async/await?

10. Give five real-world examples.

""")

    st.divider()

    st.header("📝 Quick Quiz")

    answer = st.radio(

        "Which keyword pauses an async function until a Promise completes?",

        [

            "pause",

            "wait",

            "await",

            "hold"

        ],

        key="async_quiz"

    )

    if answer=="await":

        st.success("✅ Correct! await pauses execution until the Promise resolves.")

    elif answer:

        st.error("❌ Incorrect. The correct answer is 'await'.")

    st.success("🎉 Async & Await concepts completed successfully!")
    # ---------------------------------------------------
    # FETCH API & JSON
    # ---------------------------------------------------

    st.divider()

    st.header("🌐 Fetch API")

    st.markdown("""

The **Fetch API** is used to communicate with servers.

It allows JavaScript to:

✔ Retrieve Data

✔ Send Data

✔ Update Data

✔ Delete Data

Most modern Full Stack applications communicate with servers using Fetch.

""")

    st.subheader("Real World Applications")

    st.info("""

Amazon

↓

Fetch Product Details

Netflix

↓

Fetch Movies

Instagram

↓

Fetch Posts

Google Maps

↓

Fetch Locations

Swiggy

↓

Fetch Restaurants

""")

    st.divider()

    st.subheader("Basic Fetch Syntax")

    st.code("""

fetch(url)

.then(response=>response.json())

.then(data=>{

console.log(data);

});

""",language="javascript")

    st.divider()

    st.subheader("Fetch using Async Await")

    st.code("""

async function loadStudents(){

    const response = await fetch(url);

    const data = await response.json();

    console.log(data);

}

""",language="javascript")

    st.success("""

Notice how much cleaner this code looks compared to Promise chaining.

""")

    st.divider()

    st.header("📦 JSON")

    st.markdown("""

JSON stands for

**JavaScript Object Notation**

It is the most common format used for data exchange between

✔ Browser

✔ Server

✔ APIs

""")

    st.code("""

{

"name":"Vijay",

"department":"Computer Science",

"course":"Full Stack Development"

}

""",language="json")

    st.divider()

    st.subheader("Convert JSON")

    st.code("""

// Object → JSON

JSON.stringify(object)

// JSON → Object

JSON.parse(json)

""",language="javascript")

    st.divider()

    st.header("🌍 REST APIs")

    st.markdown("""

REST APIs allow applications to communicate over HTTP.

Most Full Stack applications consume REST APIs.

""")

    st.table({

        "Method":[

            "GET",

            "POST",

            "PUT",

            "DELETE"

        ],

        "Purpose":[

            "Read Data",

            "Insert Data",

            "Update Data",

            "Delete Data"

        ]

    })

    st.divider()

    st.header("🧪 Public APIs")

    st.markdown("""

Practice APIs

✔ JSONPlaceholder

https://jsonplaceholder.typicode.com

✔ Random User API

https://randomuser.me

✔ OpenWeather

https://openweathermap.org

✔ GitHub API

https://api.github.com

""")

    st.divider()

    st.header("⚠ Error Handling")

    st.markdown("""

Whenever we access APIs,

network failures may occur.

Always use

try...catch

""")

    st.code("""

async function loadData(){

    try{

        const response=await fetch(url);

        const data=await response.json();

        console.log(data);

    }

    catch(error){

        console.log(error);

    }

}

""",language="javascript")

    st.divider()

    st.header("🎮 Full Stack Simulation")

    api = st.selectbox(

        "Select API",

        [

            "Student Database",

            "Course Details",

            "Attendance",

            "Marks"

        ]

    )

    if st.button("Fetch Data"):

        with st.spinner("Contacting Server..."):

            import time

            time.sleep(2)

        st.success("Data Retrieved Successfully")

        st.json({

            "API":api,

            "Status":"Success",

            "Records":5

        })

    st.divider()

    st.header("🏗 Mini Project")

    st.success("""

Build a Student Information Dashboard

Requirements

✔ HTML

✔ Tailwind CSS

✔ JavaScript

✔ Async Await

✔ Fetch API

✔ JSON

✔ Error Handling

Display

• Student Details

• Attendance

• Marks

• Courses

• Profile

""")

    st.divider()

    st.header("💼 Industry Applications")

    st.markdown("""

Where is Async Await used?

✔ React

✔ Node.js

✔ Express.js

✔ MongoDB

✔ Firebase

✔ REST APIs

✔ AI Chatbots

✔ Payment Gateways

✔ Cloud Applications

✔ Authentication

""")

    st.divider()

    st.header("🎯 Classroom Activity")

    st.markdown("""

Choose any one application.

Examples

• Netflix

• Amazon

• Flipkart

• Swiggy

• Gmail

Identify

✔ What data is fetched?

✔ Which APIs might be used?

✔ Which operations are asynchronous?

Present your findings.

""")

    st.divider()

    st.header("📝 Lab Exercise")

    st.info("""

Develop a webpage that:

✔ Retrieves data from a public REST API.

✔ Displays the data dynamically.

✔ Uses Async Await.

✔ Uses try-catch for error handling.

✔ Styles the webpage using Tailwind CSS.

""")

    st.divider()

    st.header("❓ Viva Questions")

    st.markdown("""

1. What is Fetch API?

2. Why do we use Fetch?

3. What is JSON?

4. Difference between JSON.parse() and JSON.stringify().

5. What is REST API?

6. Name four HTTP methods.

7. Difference between GET and POST.

8. Why is try-catch required?

9. Give five real-world applications of Fetch API.

10. Explain Async Await using a real-world example.

""")

    st.divider()

    st.header("📝 Final Quiz")

    answer = st.radio(

        "Which HTTP method is used to retrieve data?",

        [

            "POST",

            "DELETE",

            "GET",

            "PUT"

        ],

        key="fetch_quiz"

    )

    if answer=="GET":

        st.success("✅ Correct! GET retrieves data from the server.")

    elif answer:

        st.error("❌ Incorrect. The correct answer is GET.")

    st.success("🎉 Congratulations! You have completed Module 2: Async & Await.")