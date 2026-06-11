import streamlit as st

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Session 5 - JavaScript & HTML5 APIs",
    page_icon="⚡",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title(
    "⚡ Session 5: Introduction to Core JavaScript & HTML5 APIs"
)

st.markdown("""
Welcome to Session 5.

In this session we will learn how to make webpages interactive using JavaScript.

Until now:

HTML = Structure

CSS/Tailwind = Styling

Today:

JavaScript = Behavior and Interaction

By the end of this session you will be able to:

✔ Create Variables

✔ Use Data Types

✔ Perform Calculations

✔ Write Functions

✔ Handle Events

✔ Manipulate Webpages

✔ Work with HTML5 APIs
""")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title(
    "📚 Session Topics"
)

topic = st.sidebar.radio(
    "Select Topic",
    [
        "Introduction to JavaScript",
        "Variables",
        "Data Types",
        "Operators",
        "Conditional Statements",
        "Loops",
        "Functions",
        "Event Handling",
        "DOM Manipulation",
        "HTML5 APIs",
        "Cluster Challenge",
        "Viva Battle",
        "Badge System",
        "Mini Project"
    ]
)

# =====================================================
# INTRODUCTION TO JAVASCRIPT
# =====================================================

if topic == "Introduction to JavaScript":

    st.header(
        "Introduction to JavaScript"
    )

    st.markdown("""
JavaScript is the programming language of the web.

HTML creates the structure.

CSS creates the design.

JavaScript creates the behavior.

Without JavaScript:

- Buttons do nothing
- Forms cannot be validated
- Pages remain static

With JavaScript:

- Buttons respond to clicks
- Forms can be validated
- Content can change dynamically
- APIs can be accessed
""")

    st.subheader(
        "Role of JavaScript"
    )

    st.markdown("""
### HTML

Creates:

- Heading
- Paragraph
- Button

### CSS

Styles:

- Colors
- Layout
- Typography

### JavaScript

Adds:

- Click Events
- Validation
- Animations
- Interactions
""")

    st.subheader(
        "First JavaScript Program"
    )

    st.code(
"""
<script>

alert(
"Hello World"
);

</script>
""",
        language="html"
    )

    st.subheader(
        "Expected Output"
    )

    st.info(
        "A popup box displaying 'Hello World'"
    )

    st.subheader(
        "Applications of JavaScript"
    )

    st.markdown("""
✔ Websites

✔ Web Applications

✔ Games

✔ Mobile Apps

✔ AI Applications

✔ Dashboards

✔ E-Commerce Platforms
""")

    st.subheader(
        "Activity"
    )

    st.markdown("""
Identify 5 websites that use JavaScript.

Example:

- YouTube
- Instagram
- Amazon
- Netflix
- Swiggy
""")

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is JavaScript?

2. Why is JavaScript used?

3. Difference between HTML, CSS and JavaScript?

4. Can a webpage work without JavaScript?

5. Name some applications of JavaScript.
""")

# =====================================================
# VARIABLES
# =====================================================

elif topic == "Variables":

    st.header(
        "Variables"
    )

    st.markdown("""
Variables are containers used to store data.

Think of a variable as a labelled box.

Example:

Name Box → Vijay

Age Box → 21

City Box → Bangalore
""")

    st.subheader(
        "Variable Declaration"
    )

    st.code(
"""
let name = "Vijay";

const college =
"Christ University";

var city =
"Bangalore";
""",
        language="javascript"
    )

    st.subheader(
        "Types of Variables"
    )

    st.table({
        "Keyword":[
            "let",
            "const",
            "var"
        ],
        "Purpose":[
            "Value can change",
            "Value cannot change",
            "Old style declaration"
        ]
    })

    st.subheader(
        "Example"
    )

    st.code(
"""
let age = 20;

age = 21;

console.log(age);
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.success(
        "21"
    )

    st.subheader(
        "Rules for Naming Variables"
    )

    st.markdown("""
✔ Use meaningful names

✔ Start with letters

✔ Use camelCase

Examples:

studentName

totalMarks

courseCode

Avoid:

123name

my-name
""")

    st.subheader(
        "Activity"
    )

    st.markdown("""
Create variables for:

- Name
- Age
- College
- Course
- City
""")

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is a variable?

2. Difference between let and const?

3. What is var?

4. What are naming conventions?
""")

# =====================================================
# DATA TYPES
# =====================================================

elif topic == "Data Types":

    st.header(
        "Data Types"
    )

    st.markdown("""
Data Types define the type of information
stored inside a variable.
""")

    st.subheader(
        "Common Data Types"
    )

    st.table({
        "Type":[
            "String",
            "Number",
            "Boolean",
            "Array",
            "Object"
        ],
        "Example":[
            '"Hello"',
            "100",
            "true",
            "[1,2,3]",
            "{name:'John'}"
        ]
    })

    st.subheader(
        "String Example"
    )

    st.code(
"""
let name =
"John";
""",
        language="javascript"
    )

    st.subheader(
        "Number Example"
    )

    st.code(
"""
let marks = 95;
""",
        language="javascript"
    )

    st.subheader(
        "Boolean Example"
    )

    st.code(
"""
let passed =
true;
""",
        language="javascript"
    )

    st.subheader(
        "Array Example"
    )

    st.code(
"""
let colors =

[
"Red",
"Blue",
"Green"
];
""",
        language="javascript"
    )

    st.subheader(
        "Object Example"
    )

    st.code(
"""
let student = {

name:"John",

age:20

};
""",
        language="javascript"
    )

    st.subheader(
        "Activity"
    )

    st.markdown("""
Identify the data type:

1. 100

2. "Christ"

3. false

4. [10,20,30]

5. {id:1}
""")

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is a Data Type?

2. What is a String?

3. What is a Boolean?

4. What is an Array?

5. What is an Object?
""")

# =====================================================
# OPERATORS
# =====================================================

elif topic == "Operators":

    st.header(
        "Operators"
    )

    st.markdown("""
Operators perform calculations
and comparisons.
""")

    st.subheader(
        "Arithmetic Operators"
    )

    st.code(
"""
let a = 10;

let b = 5;

console.log(a+b);

console.log(a-b);

console.log(a*b);

console.log(a/b);
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.code(
"""
15

5

50

2
""",
        language="text"
    )

    st.subheader(
        "Comparison Operators"
    )

    st.code(
"""
a > b

a < b

a == b

a != b
""",
        language="javascript"
    )

    st.subheader(
        "Logical Operators"
    )

    st.code(
"""
&&

||

!
""",
        language="javascript"
    )

    st.subheader(
        "Applications"
    )

    st.markdown("""
✔ Decision Making

✔ Form Validation

✔ Calculators

✔ Business Logic
""")

    st.subheader(
        "Activity"
    )

    st.markdown("""
Create a simple calculator
that performs:

- Addition

- Subtraction

- Multiplication

- Division
""")

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is an operator?

2. What are arithmetic operators?

3. What are logical operators?

4. Give examples of comparison operators.
""")

    st.success(
        "Part 1 Completed: Introduction, Variables, Data Types and Operators."
    )
# =====================================================
# CONDITIONAL STATEMENTS
# =====================================================

elif topic == "Conditional Statements":

    st.header(
        "Conditional Statements"
    )

    st.markdown("""
Conditional Statements help programs
make decisions based on conditions.

Real Life Examples:

- If marks > 40 → Pass

- If age >= 18 → Eligible to Vote

- If password is correct → Login
""")

    st.subheader(
        "if Statement"
    )

    st.code(
"""
let age = 20;

if(age >= 18){

    console.log(
    "Eligible to Vote"
    );

}
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.success(
        "Eligible to Vote"
    )

    st.subheader(
        "if else Statement"
    )

    st.code(
"""
let marks = 35;

if(marks >= 40){

    console.log(
    "Pass"
    );

}
else{

    console.log(
    "Fail"
    );

}
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.error(
        "Fail"
    )

    st.subheader(
        "if else if"
    )

    st.code(
"""
let score = 85;

if(score >= 90){

    console.log("A");

}
else if(score >= 75){

    console.log("B");

}
else{

    console.log("C");

}
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.success(
        "B"
    )

    st.subheader(
        "switch Statement"
    )

    st.code(
"""
let day = 1;

switch(day){

case 1:

console.log(
"Monday"
);

break;

case 2:

console.log(
"Tuesday"
);

break;

default:

console.log(
"Invalid Day"
);

}
""",
        language="javascript"
    )

    st.subheader(
        "Applications"
    )

    st.markdown("""
✔ Login Systems

✔ Grade Calculation

✔ Voting Eligibility

✔ Form Validation

✔ E-Commerce Logic
""")

    st.subheader(
        "Activity"
    )

    st.markdown("""
Write a program to check:

- Pass / Fail

- Even / Odd

- Positive / Negative Number
""")

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is a Conditional Statement?

2. Difference between if and if else?

3. Why use switch?

4. Give a real-world example.
""")

# =====================================================
# LOOPS
# =====================================================

elif topic == "Loops":

    st.header(
        "Loops"
    )

    st.markdown("""
Loops are used when we need
to repeat a task multiple times.

Instead of writing:

print(1)

print(2)

print(3)

print(4)

print(5)

we use loops.
""")

    st.subheader(
        "for Loop"
    )

    st.code(
"""
for(
let i=1;
i<=5;
i++
){

console.log(i);

}
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.code(
"""
1
2
3
4
5
""",
        language="text"
    )

    st.subheader(
        "while Loop"
    )

    st.code(
"""
let i = 1;

while(i<=5){

console.log(i);

i++;

}
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.code(
"""
1
2
3
4
5
""",
        language="text"
    )

    st.subheader(
        "do while Loop"
    )

    st.code(
"""
let i = 1;

do{

console.log(i);

i++;

}
while(i<=5);
""",
        language="javascript"
    )

    st.subheader(
        "Applications"
    )

    st.markdown("""
✔ Number Printing

✔ Table Generation

✔ Repeating Tasks

✔ Data Processing

✔ Iterating Arrays
""")

    st.subheader(
        "Activity"
    )

    st.markdown("""
Write programs to:

1. Print numbers 1 to 10

2. Print even numbers

3. Print multiplication table of 5
""")

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is a loop?

2. Why are loops used?

3. Difference between for and while?

4. What is do while?
""")

# =====================================================
# FUNCTIONS
# =====================================================

elif topic == "Functions":

    st.header(
        "Functions"
    )

    st.markdown("""
Functions are reusable blocks of code.

Benefits:

✔ Reusability

✔ Better Organization

✔ Easy Maintenance

✔ Reduced Code Duplication
""")

    st.subheader(
        "Simple Function"
    )

    st.code(
"""
function greet(){

alert(
"Welcome Students"
);

}
""",
        language="javascript"
    )

    st.subheader(
        "Function Call"
    )

    st.code(
"""
greet();
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.success(
        "Welcome Students"
    )

    st.subheader(
        "Function with Parameters"
    )

    st.code(
"""
function add(a,b){

return a+b;

}
""",
        language="javascript"
    )

    st.code(
"""
add(10,20);
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.success(
        "30"
    )

    st.subheader(
        "Function with Return Value"
    )

    st.code(
"""
function square(num){

return num*num;

}

let result =

square(5);

console.log(result);
""",
        language="javascript"
    )

    st.subheader(
        "Expected Output"
    )

    st.success(
        "25"
    )

    st.subheader(
        "Real World Examples"
    )

    st.markdown("""
Functions are used in:

✔ Login Systems

✔ Payment Systems

✔ Search Features

✔ Calculators

✔ Web Applications
""")

    st.subheader(
        "Activity"
    )

    st.markdown("""
Create functions for:

1. Addition

2. Subtraction

3. Multiplication

4. Area of Circle

5. Student Grade Calculator
""")

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is a Function?

2. Why are Functions used?

3. What are Parameters?

4. What is a Return Value?

5. Give examples of Functions.
""")

# =====================================================
# PART 2 SUMMARY
# =====================================================

    st.success(
        "Part 2 Completed: Conditional Statements, Loops and Functions."
    )
# =====================================================
# EVENT HANDLING
# =====================================================

elif topic == "Event Handling":

    st.header(
        "Event Handling"
    )

    st.markdown("""
Events occur whenever a user interacts
with a webpage.

Examples:

✔ Clicking a Button

✔ Typing in a Textbox

✔ Hovering over an Element

✔ Selecting an Option

✔ Submitting a Form

JavaScript listens to these events and
performs actions accordingly.
""")

    st.subheader(
        "Popular Events"
    )

    st.table({
        "Event":[
            "onclick",
            "onchange",
            "onmouseover",
            "onmouseout",
            "onkeyup",
            "onsubmit"
        ],
        "Purpose":[
            "Button Click",
            "Value Changed",
            "Mouse Hover",
            "Mouse Leave",
            "Keyboard Input",
            "Form Submission"
        ]
    })

    st.subheader(
        "onclick Example"
    )

    st.code(
"""
<button
onclick="showMessage()">

Click Me

</button>

<script>

function showMessage(){

alert(
"Welcome Students"
);

}

</script>
""",
        language="html"
    )

    st.subheader(
        "Expected Output"
    )

    st.success(
        "A popup appears when the button is clicked."
    )

    st.subheader(
        "onmouseover Example"
    )

    st.code(
"""
<div
onmouseover="changeColor()">

Hover Over Me

</div>

<script>

function changeColor(){

document.body.style.background =
"yellow";

}

</script>
""",
        language="html"
    )

    st.subheader(
        "onchange Example"
    )

    st.code(
"""
<select
onchange="displayCourse()">

<option>BCA</option>

<option>BSc</option>

</select>
""",
        language="html"
    )

    st.subheader(
        "onkeyup Example"
    )

    st.code(
"""
<input
type="text"
onkeyup="showText()">
""",
        language="html"
    )

    st.subheader(
        "Real World Applications"
    )

    st.markdown("""
✔ Login Forms

✔ Search Boxes

✔ Shopping Carts

✔ Online Exams

✔ Registration Forms
""")

    st.subheader(
        "Mini Activity"
    )

    st.markdown("""
Create:

1. Button Click Event

2. Hover Event

3. Text Input Event

4. Dropdown Selection Event
""")

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is an Event?

2. What is Event Handling?

3. Difference between onclick and onchange?

4. Give examples of Events.
""")

# =====================================================
# DOM MANIPULATION
# =====================================================

elif topic == "DOM Manipulation":

    st.header(
        "DOM Manipulation"
    )

    st.markdown("""
DOM stands for:

Document Object Model

The DOM represents a webpage as a tree
of objects.

JavaScript can:

✔ Read Content

✔ Modify Content

✔ Modify Styles

✔ Create Elements

✔ Delete Elements
""")

    st.subheader(
        "DOM Structure"
    )

    st.code(
"""
HTML

|
|-- Head

|
|-- Body

    |
    |-- H1

    |
    |-- P

    |
    |-- Button
""",
        language="text"
    )

    st.subheader(
        "Selecting an Element"
    )

    st.code(
"""
document.getElementById(
"demo"
);
""",
        language="javascript"
    )

    st.subheader(
        "Change Text Example"
    )

    st.code(
"""
<p id="demo">

Hello Students

</p>

<button
onclick="changeText()">

Click

</button>

<script>

function changeText(){

document.getElementById(
"demo"
).innerHTML =

"Welcome to JavaScript";

}

</script>
""",
        language="html"
    )

    st.subheader(
        "Expected Output"
    )

    st.success(
        "Text changes after button click."
    )

    st.subheader(
        "Change Style Example"
    )

    st.code(
"""
function changeColor(){

document.getElementById(
"demo"
).style.color =

"red";

}
""",
        language="javascript"
    )

    st.subheader(
        "Hide Element"
    )

    st.code(
"""
document.getElementById(
"demo"
).style.display =

"none";
""",
        language="javascript"
    )

    st.subheader(
        "Show Element"
    )

    st.code(
"""
document.getElementById(
"demo"
).style.display =

"block";
""",
        language="javascript"
    )

    st.subheader(
        "Real World Applications"
    )

    st.markdown("""
✔ Dynamic Dashboards

✔ Online Shopping Sites

✔ Student Portals

✔ Banking Systems

✔ Social Media Platforms
""")

# =====================================================
# INTERACTIVE DEMO 1
# =====================================================

    st.subheader(
        "Interactive Demo: Live Text Updater"
    )

    st.code(
"""
<input
type="text"
id="nameBox">

<button
onclick="showName()">

Display

</button>

<p id="output"></p>

<script>

function showName(){

let name =

document.getElementById(
"nameBox"
).value;

document.getElementById(
"output"
).innerHTML =

name;

}

</script>
""",
        language="html"
    )

    st.markdown("""
### Output

User enters:

Vijay

After clicking Display

Output:

Vijay
""")

# =====================================================
# INTERACTIVE DEMO 2
# =====================================================

    st.subheader(
        "Interactive Demo: Dark Mode"
    )

    st.code(
"""
<button
onclick="darkMode()">

Dark Mode

</button>

<script>

function darkMode(){

document.body.style.background =
"black";

document.body.style.color =
"white";

}

</script>
""",
        language="html"
    )

    st.markdown("""
### Output

Page switches to dark theme.
""")

# =====================================================
# INTERACTIVE DEMO 3
# =====================================================

    st.subheader(
        "Interactive Demo: Click Counter"
    )

    st.code(
"""
let count = 0;

function increaseCount(){

count++;

document.getElementById(
"counter"
).innerHTML =

count;

}
""",
        language="javascript"
    )

    st.markdown("""
Applications:

✔ Like Button

✔ Visitor Counter

✔ Voting System
""")

# =====================================================
# EVENT HANDLING VS DOM
# =====================================================

    st.subheader(
        "Event Handling vs DOM Manipulation"
    )

    st.table({
        "Concept":[
            "Event Handling",
            "DOM Manipulation"
        ],
        "Purpose":[
            "Detect User Action",
            "Modify Webpage Content"
        ]
    })

# =====================================================
# CLASS CHALLENGE PREPARATION
# =====================================================

    st.subheader(
        "Class Challenge Preparation"
    )

    st.markdown("""
Tomorrow your cluster may challenge
another cluster to develop:

✔ Background Color Changer

✔ Live Character Counter

✔ Dark Mode Toggle

✔ Student Grade Calculator

✔ Simple Calculator

✔ Dynamic Greeting System

✔ Traffic Light Simulator

✔ Quiz Application

✔ Attendance Counter

✔ Theme Switcher
""")

# =====================================================
# ACTIVITY
# =====================================================

    st.subheader(
        "Hands-on Activity"
    )

    st.markdown("""
Develop the following using JavaScript:

1. Change Paragraph Text

2. Change Text Color

3. Hide and Show Content

4. Button Click Counter

5. Dark Mode Toggle

6. Live Input Display
""")

# =====================================================
# VIVA QUESTIONS
# =====================================================

    st.subheader(
        "Viva Questions"
    )

    st.markdown("""
1. What is DOM?

2. What is Event Handling?

3. What is getElementById()?

4. What is innerHTML?

5. How can we change CSS using JavaScript?

6. Difference between Event and Event Handler?

7. What is onclick?

8. What is onkeyup?

9. What is DOM Manipulation?

10. Give real-world applications.
""")

    st.success(
        "Part 3 Completed: Event Handling and DOM Manipulation."
    )
# =====================================================
# CLUSTER CHALLENGE
# =====================================================

elif topic == "Cluster Challenge":

    st.header(
        "🏆 Cluster Challenge"
    )

    st.markdown("""
The class will be divided into
three clusters.

🔵 Cluster A

🟢 Cluster B

🟠 Cluster C

Each cluster will challenge
another cluster to develop
a JavaScript-based solution.

Points will be awarded based on:

✔ Correctness

✔ Creativity

✔ Code Quality

✔ Presentation

✔ Explanation
""")

    st.subheader(
        "Round 1 - Event Handling Challenge"
    )

    st.markdown("""
Example Challenges:

✔ Change Background Color

✔ Display Welcome Message

✔ Live Character Counter

✔ Theme Switcher

✔ Dynamic Greeting System

✔ Traffic Light Simulator

✔ Quiz Button
""")

    st.subheader(
        "Scoring"
    )

    st.table({
        "Criteria":[
            "Working Solution",
            "Code Explanation",
            "Creativity",
            "Presentation"
        ],
        "Points":[
            5,
            3,
            2,
            2
        ]
    })

    st.subheader(
        "Round 2 - DOM Challenge"
    )

    st.markdown("""
Examples:

✔ Change Text

✔ Change Color

✔ Hide Content

✔ Show Content

✔ Dynamic Table

✔ Student Profile Generator
""")

    st.subheader(
        "Round 3 - API Challenge"
    )

    st.markdown("""
Examples:

✔ Save User Name

✔ Store Preferences

✔ Display Location

✔ Audio Controller

✔ Video Controller
""")

    st.subheader(
        "Bonus Round"
    )

    st.markdown("""
Develop something useful
for your selected project domain
within 10 minutes.
""")

    st.success(
        "Winning Cluster earns bonus points and badges."
    )

# =====================================================
# VIVA BATTLE
# =====================================================

elif topic == "Viva Battle":

    st.header(
        "⚔️ JavaScript Viva Battle"
    )

    st.markdown("""
Each cluster asks questions
to another cluster.

Correct answers earn points.

Incorrect answers allow
other clusters to steal points.
""")

    st.subheader(
        "Round 1 - JavaScript Basics"
    )

    st.markdown("""
1. What is JavaScript?

2. Difference between HTML and JavaScript?

3. Difference between let and const?

4. What is a variable?

5. What is a data type?
""")

    st.subheader(
        "Round 2 - Conditions and Loops"
    )

    st.markdown("""
1. What is an if statement?

2. Difference between if and switch?

3. What is a loop?

4. Difference between for and while?

5. Give one real-world use of loops.
""")

    st.subheader(
        "Round 3 - Functions"
    )

    st.markdown("""
1. What is a function?

2. Why are functions used?

3. What are parameters?

4. What is a return value?

5. Give one example function.
""")

    st.subheader(
        "Round 4 - Events"
    )

    st.markdown("""
1. What is an event?

2. What is onclick?

3. What is onchange?

4. What is onkeyup?

5. Give examples of event handling.
""")

    st.subheader(
        "Round 5 - DOM"
    )

    st.markdown("""
1. What is DOM?

2. What is innerHTML?

3. What is getElementById()?

4. How can we change CSS using JavaScript?

5. Give a DOM example.
""")

    st.subheader(
        "Scoring Rules"
    )

    st.table({
        "Task":[
            "Correct Answer",
            "Bonus Explanation",
            "Counter Question"
        ],
        "Points":[
            2,
            1,
            1
        ]
    })

# =====================================================
# BADGE SYSTEM
# =====================================================

elif topic == "Badge System":

    st.header(
        "🏅 Session Badges"
    )

    st.markdown("""
Students and clusters can earn
badges throughout the session.
""")

    st.subheader(
        "Available Badges"
    )

    st.markdown("""
🥇 JavaScript Champion

Awarded for best overall performance.

---

⚡ Event Master

Awarded for excellent event handling solutions.

---

🎯 DOM Ninja

Awarded for DOM manipulation expertise.

---

🚀 API Explorer

Awarded for creative use of APIs.

---

🛠 Debugging Hero

Awarded for fixing challenging bugs.

---

💡 Innovation Star

Awarded for unique ideas and implementations.
""")

    st.subheader(
        "Recognition"
    )

    st.markdown("""
Winning clusters may receive:

✔ Bonus Activity Points

✔ Classroom Recognition

✔ Digital Badge

✔ Hall of Fame Mention
""")

# =====================================================
# MINI PROJECT
# =====================================================

elif topic == "Mini Project":

    st.header(
        "🚀 Session Mini Project"
    )

    st.markdown("""
Build an Interactive Student Profile Page
using JavaScript.
""")

    st.subheader(
        "Project Features"
    )

    st.markdown("""
Mandatory:

✔ Variables

✔ Data Types

✔ Conditional Statements

✔ Functions

✔ Event Handling

✔ DOM Manipulation

Optional:

✔ Local Storage

✔ Geolocation

✔ Dark Mode

✔ Theme Switcher
""")

    st.subheader(
        "Suggested Inputs"
    )

    st.markdown("""
Student Name

Register Number

Course

Department

Favorite Subject
""")

    st.subheader(
        "Expected Output"
    )

    st.markdown("""
Display a formatted
student profile card.

Allow:

✔ Updating Details

✔ Changing Theme

✔ Showing Greetings

✔ Interactive Buttons
""")

    st.subheader(
        "Advanced Ideas"
    )

    st.markdown("""
1. Student Grade Calculator

2. Attendance Tracker

3. Quiz Application

4. Expense Calculator

5. Event Registration Form

6. To-Do List

7. Student Feedback System

8. Campus Navigation Tool
""")

    st.subheader(
        "Learning Outcomes"
    )

    st.markdown("""
After completing this project,
students should be able to:

✔ Write JavaScript programs

✔ Create Functions

✔ Handle Events

✔ Manipulate DOM Elements

✔ Build Interactive Web Pages
""")

# =====================================================
# SESSION SUMMARY
# =====================================================

elif topic == "Session Summary":

    st.header(
        "📚 Session Summary"
    )

    st.success("""
Congratulations!

You have completed
Introduction to Core JavaScript.
""")

    st.markdown("""
Topics Covered:

✔ Introduction to JavaScript

✔ Variables

✔ Data Types

✔ Operators

✔ Conditional Statements

✔ Loops

✔ Functions

✔ Event Handling

✔ DOM Manipulation

✔ HTML5 APIs Overview

✔ Cluster Challenge

✔ Viva Battle

✔ Badge System

✔ Mini Project
""")

    st.subheader(
        "Key Takeaway"
    )

    st.markdown("""
HTML creates the structure.

CSS creates the design.

JavaScript creates the interaction.

Together they form the foundation
of modern web development.
""")

    st.success(
        "🎉 Session 5 Completed Successfully!"
    )