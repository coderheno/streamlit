import streamlit as st

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Full Stack Development - Unit 1",
    page_icon="🌐",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title("🌐 Full Stack Development")
st.subheader("Unit 1 Overview and Foundations")

st.markdown("""
Welcome to the Unit 1 Learning Portal.

This module provides an overview of the key concepts required
to build modern responsive web applications using HTML5,
CSS, Tailwind CSS, GitHub, JavaScript, and HTML5 APIs.

Use the navigation menu to explore the topics.
""")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📚 Unit 1 Topics")

topic = st.sidebar.radio(
    "Select Topic",
    [
        "Full Stack Development",
        "HTML5 Semantic Elements",
        "Responsive Web Design",
        "Tailwind CSS",
        "HTML5 Canvas",
        "HTML Media",
        "Font Awesome Icons",
        "Git Commit",
        "Git Rollback",
        "Remote Repository (GitHub)",
        "Merge Conflict",
        "CSS Specificity",
        "Pseudo Selectors",
        "Media Queries",
        "CSS Transitions",
        "Advanced Flexbox",
        "Tailwind Responsive Grid",
        "Navbar Component",
        "Hero Component",
        "Table Component",
        "Modal Component",
        "Carousel Component",
        "Core JavaScript",
        "DOM Manipulation",
        "HTML5 APIs",
        "Mini Project",
        "Unit 1 Summary",
        "Important Viva Questions"
    ]
)

# =====================================================
# FULL STACK DEVELOPMENT
# =====================================================

if topic == "Full Stack Development":

    st.header("What is Full Stack Development?")

    st.markdown("""
Full Stack Development refers to the development of both
the frontend and backend components of a web application.

A Full Stack Developer works with:

### Frontend
The user-facing part of a website.

Examples:

- HTML
- CSS
- Tailwind CSS
- JavaScript
- React

### Backend

Responsible for:

- Business Logic
- Authentication
- Data Processing
- APIs

Examples:

- Node.js
- Express.js
- Python
- PHP

### Database

Stores application data.

Examples:

- MySQL
- MongoDB
- PostgreSQL
""")

    st.subheader("Real World Example")

    st.markdown("""
### Instagram

Frontend

- Login Page
- Feed
- Profile Page
- Reels

Backend

- User Authentication
- Post Upload
- Messaging System

Database

- Users
- Posts
- Comments
- Followers
""")

    st.success(
        "A Full Stack Developer can work across all layers of an application."
    )

    st.subheader("Technology Stack")

    st.code(
"""
Frontend:
HTML + CSS + JavaScript + React

Backend:
Node.js + Express.js

Database:
MongoDB

Deployment:
GitHub + Cloud Platforms
""",
        language="text"
    )

    st.subheader("Why Learn Full Stack Development?")

    st.markdown("""
✔ Build complete applications

✔ Better career opportunities

✔ Startup and freelancing potential

✔ Ability to develop end-to-end solutions

✔ Strong problem-solving skills
""")

    st.subheader("Activity")

    st.markdown("""
Identify three applications you use daily.

For each application, identify:

1. Frontend Features
2. Backend Features
3. Data Stored in Database
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is Full Stack Development?

2. What is the difference between frontend and backend?

3. Name some frontend technologies.

4. Name some backend technologies.

5. What is a database?
""")

# =====================================================
# HTML5 SEMANTIC ELEMENTS
# =====================================================

elif topic == "HTML5 Semantic Elements":

    st.header("HTML5 Semantic Elements")

    st.markdown("""
Semantic elements clearly describe the purpose of content.

They make webpages:

- More readable
- SEO friendly
- Accessible
- Easier to maintain
""")

    st.subheader("Common Semantic Elements")

    st.code(
"""
<header>
<nav>
<main>
<section>
<article>
<aside>
<footer>
""",
        language="html"
    )

    st.subheader("Element Descriptions")

    st.markdown("""
### header
Represents introductory content.

### nav
Contains navigation links.

### main
Contains primary webpage content.

### section
Groups related content.

### article
Represents self-contained content.

### aside
Contains supplementary information.

### footer
Contains copyright and contact details.
""")

    st.subheader("Example Page Structure")

    st.code(
"""
<header>
    <nav>
    </nav>
</header>

<main>

    <section>

        <article>

        </article>

    </section>

</main>

<footer>

</footer>
""",
        language="html"
    )

    st.subheader("Benefits")

    st.markdown("""
### Search Engine Optimization

Search engines understand page structure better.

### Accessibility

Screen readers can interpret content correctly.

### Code Readability

Developers can understand structure easily.

### Maintainability

Makes large projects easier to manage.
""")

    st.info(
        "Avoid excessive use of div elements when semantic alternatives exist."
    )

    st.subheader("Activity")

    st.markdown("""
Convert a webpage created using only div elements into semantic HTML.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What are semantic elements?

2. Why is semantic HTML important?

3. Difference between section and article?

4. What is the purpose of nav?

5. What is the purpose of footer?
""")

# =====================================================
# RESPONSIVE WEB DESIGN
# =====================================================

elif topic == "Responsive Web Design":

    st.header("Responsive Web Design")

    st.markdown("""
Responsive Web Design allows webpages to adapt to
different screen sizes and devices.

Devices include:

- Mobile Phones
- Tablets
- Laptops
- Desktop Computers
""")

    st.subheader("Why Responsive Design?")

    st.markdown("""
### Better User Experience

Users can access websites comfortably.

### Mobile Usage

Most users browse using smartphones.

### Improved Accessibility

Content remains readable.

### Professional Websites

Modern websites must support multiple devices.
""")

    st.subheader("Responsive Layout Example")

    st.code(
"""
<div
class="
grid
grid-cols-1
md:grid-cols-2
lg:grid-cols-3
">
</div>
""",
        language="html"
    )

    st.subheader("Responsive Design Principles")

    st.markdown("""
1. Mobile First Design

2. Flexible Layouts

3. Responsive Images

4. Media Queries

5. Flexible Grids
""")

    st.subheader("Common Breakpoints")

    st.table({
        "Prefix":[
            "sm",
            "md",
            "lg",
            "xl",
            "2xl"
        ],
        "Screen Size":[
            "640px",
            "768px",
            "1024px",
            "1280px",
            "1536px"
        ]
    })

    st.success(
        "Responsive design is a mandatory skill for modern web developers."
    )

    st.subheader("Activity")

    st.markdown("""
Open any website on:

- Mobile
- Tablet
- Laptop

Observe how the layout changes.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is Responsive Web Design?

2. Why is it important?

3. What are breakpoints?

4. What is Mobile First Design?

5. What is a responsive grid?
""")

# =====================================================
# TAILWIND CSS
# =====================================================

elif topic == "Tailwind CSS":

    st.header("Tailwind CSS")

    st.markdown("""
Tailwind CSS is a utility-first CSS framework.

Instead of writing custom CSS,
developers use predefined utility classes.

Example:

Traditional CSS:

.button{
background:blue;
padding:10px;
}

Tailwind CSS:

class="bg-blue-500 p-3"
""")

    st.subheader("Advantages")

    st.markdown("""
✔ Faster Development

✔ Responsive Utilities

✔ Consistent Design

✔ Reusable Components

✔ Easy Maintenance
""")

    st.subheader("Common Utility Classes")

    st.table({
        "Class":[
            "bg-blue-500",
            "text-white",
            "p-4",
            "m-4",
            "rounded-lg",
            "font-bold"
        ],
        "Purpose":[
            "Background Color",
            "Text Color",
            "Padding",
            "Margin",
            "Border Radius",
            "Bold Text"
        ]
    })

    st.subheader("Example")

    st.code(
"""
<div
class="
bg-blue-500
text-white
p-4
rounded-lg
">

Welcome to Tailwind CSS

</div>
""",
        language="html"
    )

    st.subheader("Tailwind CDN")

    st.code(
"""
<script src="https://cdn.tailwindcss.com"></script>
""",
        language="html"
    )

    st.info(
        "Tailwind allows developers to build responsive interfaces rapidly."
    )

    st.subheader("Activity")

    st.markdown("""
Create a simple card using:

- Background Color
- Text Color
- Padding
- Border Radius
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is Tailwind CSS?

2. What is a utility class?

3. Give examples of utility classes.

4. What are the advantages of Tailwind?

5. What is the purpose of Tailwind CDN?
""")
# =====================================================
# HTML5 CANVAS
# =====================================================

elif topic == "HTML5 Canvas":

    st.header("HTML5 Canvas")

    st.markdown("""
HTML5 Canvas provides a drawing surface that allows developers
to create graphics using JavaScript.

Canvas is widely used in:

- Games
- Drawing Applications
- Charts
- Digital Signatures
- Image Editing Tools
- Data Visualization
""")

    st.subheader("Canvas Element")

    st.code(
"""
<canvas
id="myCanvas"
width="400"
height="200">
</canvas>
""",
        language="html"
    )

    st.subheader("Drawing a Rectangle")

    st.code(
"""
const canvas =
document.getElementById(
"myCanvas"
);

const ctx =
canvas.getContext("2d");

ctx.fillStyle = "blue";

ctx.fillRect(
50,
50,
150,
100
);
""",
        language="javascript"
    )

    st.info(
        "Canvas drawings are created using JavaScript."
    )

    st.subheader("Applications")

    st.markdown("""
✔ Games

✔ Signature Pad

✔ Online Whiteboards

✔ Dashboards

✔ Graph Visualization
""")

    st.subheader("Activity")

    st.markdown("""
Draw:

1. Rectangle

2. Circle

3. Text

using Canvas API.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is Canvas?

2. Why is Canvas used?

3. Which language is used to draw on Canvas?

4. Name some Canvas applications.
""")

# =====================================================
# HTML MEDIA
# =====================================================

elif topic == "HTML Media":

    st.header("HTML Media")

    st.markdown("""
HTML5 provides built-in support for multimedia content.

Developers can directly embed:

- Audio
- Video

without external plugins.
""")

    st.subheader("Audio Element")

    st.code(
"""
<audio controls>

<source
src="audio.mp3"
type="audio/mpeg">

</audio>
""",
        language="html"
    )

    st.subheader("Video Element")

    st.code(
"""
<video
width="500"
controls>

<source
src="video.mp4"
type="video/mp4">

</video>
""",
        language="html"
    )

    st.subheader("Advantages")

    st.markdown("""
✔ Native Browser Support

✔ No Flash Required

✔ Mobile Friendly

✔ Easy Integration
""")

    st.subheader("Applications")

    st.markdown("""
- E-Learning Portals

- YouTube Alternatives

- Podcasts

- Online Courses

- Product Demonstrations
""")

    st.subheader("Activity")

    st.markdown("""
Create a webpage containing:

- One Audio Player

- One Video Player

- Description Section
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is HTML Media?

2. Difference between Audio and Video tags?

3. What is the purpose of controls attribute?

4. Give real-world applications.
""")

# =====================================================
# FONT AWESOME
# =====================================================

elif topic == "Font Awesome Icons":

    st.header("Font Awesome Icons")

    st.markdown("""
Font Awesome is a popular icon library used in modern websites.

Icons help improve:

- User Experience
- Navigation
- Visual Appeal
""")

    st.subheader("CDN Integration")

    st.code(
"""
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
""",
        language="html"
    )

    st.subheader("Examples")

    st.code(
"""
<i class="fas fa-home"></i>

<i class="fas fa-user"></i>

<i class="fas fa-envelope"></i>

<i class="fas fa-laptop-code"></i>
""",
        language="html"
    )

    st.subheader("Applications")

    st.markdown("""
✔ Navigation Menus

✔ Feature Cards

✔ Dashboards

✔ Contact Pages

✔ Social Media Links
""")

    st.subheader("Activity")

    st.markdown("""
Design a feature section using:

- Laptop Icon

- Cloud Icon

- Robot Icon

using Font Awesome.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is Font Awesome?

2. Why are icons used?

3. What is CDN?

4. Give examples of Font Awesome icons.
""")

# =====================================================
# GIT COMMIT
# =====================================================

elif topic == "Git Commit":

    st.header("Git Commit")

    st.markdown("""
Git is a Version Control System.

It helps developers:

- Track Changes
- Maintain Versions
- Collaborate with Teams
- Restore Previous Work
""")

    st.subheader("Initialize Repository")

    st.code(
"""
git init
""",
        language="bash"
    )

    st.subheader("Add Files")

    st.code(
"""
git add .
""",
        language="bash"
    )

    st.subheader("Commit Changes")

    st.code(
"""
git commit -m "Initial Commit"
""",
        language="bash"
    )

    st.success(
        "A commit represents a saved version of the project."
    )

    st.subheader("Activity")

    st.markdown("""
Create a webpage and make:

1. Initial Commit

2. Second Commit

3. Third Commit
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is Git?

2. What is a commit?

3. Why are commits important?

4. Difference between add and commit?
""")

# =====================================================
# GIT ROLLBACK
# =====================================================

elif topic == "Git Rollback":

    st.header("Git Rollback")

    st.markdown("""
Rollback allows developers to restore
previous versions of a project.
""")

    st.subheader("View Commit History")

    st.code(
"""
git log
""",
        language="bash"
    )

    st.subheader("Checkout Previous Commit")

    st.code(
"""
git checkout commit_id
""",
        language="bash"
    )

    st.markdown("""
Benefits:

✔ Recover mistakes

✔ Compare versions

✔ Restore deleted content
""")

    st.subheader("Activity")

    st.markdown("""
Create 3 commits.

Restore the project to Commit 1.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is rollback?

2. Why is rollback useful?

3. What is git log?
""")

# =====================================================
# REMOTE REPOSITORY
# =====================================================

elif topic == "Remote Repository (GitHub)":

    st.header("Remote Repository")

    st.markdown("""
A Remote Repository is an online repository.

GitHub is the most popular Git hosting platform.
""")

    st.subheader("Connect Repository")

    st.code(
"""
git remote add origin URL
""",
        language="bash"
    )

    st.subheader("Push Project")

    st.code(
"""
git push -u origin main
""",
        language="bash"
    )

    st.subheader("Benefits")

    st.markdown("""
✔ Online Backup

✔ Collaboration

✔ Portfolio Building

✔ Version Control
""")

    st.subheader("Activity")

    st.markdown("""
Upload your landing page project to GitHub.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is GitHub?

2. What is a remote repository?

3. Why do developers use GitHub?

4. What is git push?
""")
elif topic == "Merge Conflict":

    st.header("Merge Conflict")

    st.markdown("""
A Merge Conflict occurs when Git cannot automatically merge
changes because multiple developers modified the same section
of a file.

Merge conflicts are common in collaborative software development.
""")

    st.subheader("Example Scenario")

    st.markdown("""
Developer A changes:

```html
<h1>TechLearn Academy</h1>
```

Developer B changes:

```html
<h1>TechLearn Platform</h1>
```

When merging, Git detects conflicting changes.
""")

    st.subheader("Conflict Markers")

    st.code("""
<<<<<<< HEAD

<h1>TechLearn Academy</h1>

=======

<h1>TechLearn Platform</h1>

>>>>>>> branch-name
""", language="html")

    st.subheader("Resolution Steps")

    st.markdown("""
Review conflicting code
Decide which version to keep
Remove conflict markers
Save the file

Commit the resolved version
""")

    st.subheader("Activity")

    st.markdown("""
Create two versions of the same HTML file and simulate a merge conflict.
""")

    st.subheader("Viva Questions")

    st.markdown("""
What is a Merge Conflict?
Why do Merge Conflicts occur?
How can Merge Conflicts be resolved?
What is collaboration in Git?
""")

elif topic == "CSS Specificity":

    st.header("CSS Specificity Rules")

    st.markdown("""
CSS Specificity determines which CSS rule will be applied
when multiple rules target the same element.
""")

    st.subheader("Priority Order")

    st.markdown("""
Highest Priority

Inline Style
ID Selector
Class Selector
Element Selector

Lowest Priority
""")

    st.subheader("Example")

    st.code("""
#title{
color:red;
}

.heading{
color:blue;
}

h1{
color:green;
}
""", language="css")

    st.code("""
<h1 id="title" class="heading"> Welcome </h1>
""", language="html")

    st.success("""
Output Color: Red

Reason:
ID Selector has higher priority than Class Selector and Element Selector.
""")

    st.subheader("Why Specificity Matters")

    st.markdown("""
Prevents styling conflicts
Improves maintainability

Helps debugging CSS issues
""")

    st.subheader("Activity")

    st.markdown("""
Predict the output color for different CSS specificity examples.
""")

    st.subheader("Viva Questions")

    st.markdown("""
What is CSS Specificity?
Which selector has highest priority?
Which selector has lowest priority?
Why is specificity important?
""")

elif topic == "Pseudo Selectors":

    st.header("Pseudo Selectors")

    st.markdown("""
Pseudo Selectors define special states of HTML elements.
""")

    st.subheader("Common Pseudo Selectors")

    st.code("""
:hover
:focus
:active
:first-child
:last-child
:nth-child()
""", language="css")

    st.subheader("Hover Example")

    st.code("""
button:hover{
background-color:green;
color:white;
}
""", language="css")

    st.subheader("Focus Example")

    st.code("""
input:focus{
border:2px solid blue;
}
""", language="css")

    st.subheader("First Child Example")

    st.code("""
li:first-child{
color:red;
}
""", language="css")

    st.subheader("Applications")

    st.markdown("""
✔ Navigation Menus

✔ Forms

✔ Buttons

✔ Interactive User Interfaces
""")

    st.subheader("Activity")

    st.markdown("""
Create a menu using:

hover
first-child

last-child
""")

    st.subheader("Viva Questions")

    st.markdown("""
What is a pseudo selector?
What is :hover?
What is :focus?
Give two applications of pseudo selectors.
""")

elif topic == "Media Queries":

    st.header("Media Queries")

    st.markdown("""
Media Queries allow websites to adapt to different screen sizes.

They are one of the core technologies behind Responsive Web Design.
""")

    st.subheader("Syntax")

    st.code("""
@media (max-width:768px){

body{
    background:red;
}

}
""", language="css")

    st.subheader("Common Breakpoints")

    st.table({
        "Device":[
            "Mobile",
            "Tablet",
            "Laptop",
            "Desktop"
        ],
        "Width":[
            "576px",
            "768px",
            "992px",
            "1200px"
        ]
    })

    st.subheader("Responsive Example")

    st.code("""
.container{
width:1200px;
}

@media(max-width:768px){

.container{
width:100%;
}

}
""", language="css")

    st.subheader("Applications")

    st.markdown("""
✔ Mobile Websites

✔ Responsive Navigation

✔ Responsive Dashboards

✔ Adaptive Layouts
""")

    st.subheader("Activity")

    st.markdown("""
Create separate layouts for:

Mobile
Tablet

Desktop
""")

    st.subheader("Viva Questions")

    st.markdown("""
What is a Media Query?
Why are Media Queries important?
What is a breakpoint?
What is Responsive Design?
""")

elif topic == "CSS Transitions":

    st.header("CSS Transitions")

    st.markdown("""
Transitions allow smooth animation between CSS property changes.
""")

    st.subheader("Basic Example")

    st.code("""
button{

background:blue;

transition:0.5s;

}

button:hover{

background:red;

}
""", language="css")

    st.subheader("Transition Properties")

    st.code("""
transition-property

transition-duration

transition-delay

transition-timing-function
""", language="css")

    st.subheader("Advanced Example")

    st.code("""
.card{

transition:0.5s;

}

.card:hover{

transform:scale(1.1);

}
""", language="css")

    st.subheader("Benefits")

    st.markdown("""
✔ Better User Experience

✔ Smooth Interactions

✔ Professional Interfaces

✔ Improved Visual Feedback
""")

    st.subheader("Activity")

    st.markdown("""
Create:

Animated Button
Animated Card

using transitions.
""")

    st.subheader("Viva Questions")

    st.markdown("""
What is a Transition?
Why are transitions used?
What properties can be animated?
Difference between transition and animation?
""")

elif topic == "Advanced Flexbox":

    st.header("Advanced Flexbox")

    st.markdown("""
Flexbox is a one-dimensional layout system
used to arrange elements efficiently.
""")

    st.subheader("Create Flex Container")

    st.code("""
.container{

display:flex;

}
""", language="css")

    st.subheader("Direction")

    st.code("""
flex-direction:row;

flex-direction:column;
""", language="css")

    st.subheader("Horizontal Alignment")

    st.code("""
justify-content:flex-start;

justify-content:center;

justify-content:space-between;

justify-content:space-around;
""", language="css")

    st.subheader("Vertical Alignment")

    st.code("""
align-items:flex-start;

align-items:center;

align-items:flex-end;
""", language="css")

    st.subheader("Tailwind Example")

    st.code("""
<div class="flex justify-center items-center h-screen">

Content

</div>
""", language="html")

    st.subheader("Applications")

    st.markdown("""
✔ Navbar

✔ Hero Section

✔ Cards

✔ Dashboard Layouts

✔ Forms
""")

    st.subheader("Activity")

    st.markdown("""
Build a responsive navbar using:

flex
justify-between

items-center
""")

    st.subheader("Viva Questions")

    st.markdown("""
What is Flexbox?
What is justify-content?
What is align-items?
Difference between row and column?

Where is Flexbox commonly used?
""")

    st.success(
        "Part 3 Completed: Merge Conflict, CSS Specificity, Pseudo Selectors, Media Queries, CSS Transitions and Advanced Flexbox."
    )

elif topic == "Tailwind Responsive Grid":


    st.header("Tailwind Responsive Grid")

    st.markdown("""
Tailwind Grid Layout helps developers create
responsive multi-column layouts easily.

Instead of manually writing CSS Grid properties,
Tailwind provides utility classes.
""")

    st.subheader("Basic Grid")

    st.code("""
<div class="grid grid-cols-3 gap-4">

    <div>Card 1</div>

    <div>Card 2</div>

    <div>Card 3</div>

</div>
""", language="html")

    st.subheader("Responsive Grid")

    st.code("""
<div
class="
grid
grid-cols-1
md:grid-cols-2
lg:grid-cols-3
gap-6
">

</div>
""", language="html")

    st.info("""
Mobile → 1 Column

Tablet → 2 Columns

Desktop → 3 Columns
""")

    st.subheader("Applications")

    st.markdown("""
✔ Feature Cards

✔ Product Listings

✔ Dashboards

✔ Photo Galleries

✔ Admin Panels
""")

    st.subheader("Activity")

    st.markdown("""
Create a responsive 6-card dashboard
using Tailwind Grid.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is Grid Layout?

2. Difference between Grid and Flexbox?

3. What is grid-cols-3?

4. Why use responsive grids?
""")

# =====================================================
# NAVBAR COMPONENT
# =====================================================

elif topic == "Navbar Component":

    st.header("Navbar Component")

    st.markdown("""
Navbar is one of the most commonly used
UI components in websites.

It helps users navigate between pages.
""")

    st.subheader("Tailwind Navbar")

    st.code("""
<nav
class="
bg-blue-700
text-white
p-4
flex
justify-between
items-center
">

<h1>
TechLearn
</h1>

<ul
class="
flex
gap-6
">

<li>Home</li>
<li>Courses</li>
<li>Projects</li>
<li>Contact</li>

</ul>

</nav>
""", language="html")

    st.subheader("Features")

    st.markdown("""
✔ Branding

✔ Navigation Links

✔ Responsive Layout

✔ Mobile Friendly
""")

    st.subheader("Activity")

    st.markdown("""
Create a responsive navbar
for your project domain.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is a Navbar?

2. Why is navigation important?

3. Which Tailwind classes are used?
""")

# =====================================================
# HERO COMPONENT
# =====================================================

elif topic == "Hero Component":

    st.header("Hero Component")

    st.markdown("""
A Hero Section is the first section
users see on a webpage.

It introduces the product,
service or application.
""")

    st.subheader("Example Hero Section")

    st.code("""
<section
class="
text-center
py-20
bg-gray-100
">

<h1
class="
text-5xl
font-bold
">

Learn Full Stack Development

</h1>

<p
class="
mt-4
text-gray-600
">

Build modern web applications.

</p>

<button
class="
mt-6
bg-blue-600
text-white
px-6
py-3
rounded
">

Get Started

</button>

</section>
""", language="html")

    st.subheader("Hero Section Elements")

    st.markdown("""
✔ Heading

✔ Description

✔ Call To Action Button

✔ Background Image (Optional)

✔ Illustration (Optional)
""")

    st.subheader("Activity")

    st.markdown("""
Create a Hero Section
for your selected project domain.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is a Hero Section?

2. Why is it important?

3. What is a CTA button?
""")

# =====================================================
# TABLE COMPONENT
# =====================================================

elif topic == "Table Component":

    st.header("Table Component")

    st.markdown("""
Tables are used to display
structured data.
""")

    st.subheader("Example")

    st.code("""
<table
class="
table-auto
border-collapse
border
w-full
">

<tr>

<th>Name</th>

<th>Course</th>

<th>Marks</th>

</tr>

<tr>

<td>John</td>

<td>FSD</td>

<td>90</td>

</tr>

</table>
""", language="html")

    st.subheader("Applications")

    st.markdown("""
✔ Student Records

✔ Employee Data

✔ Product Listings

✔ Reports
""")

    st.subheader("Activity")

    st.markdown("""
Create a Student Marks Table.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is a table?

2. Difference between th and td?

3. Give real-world applications.
""")

# =====================================================
# MODAL COMPONENT
# =====================================================

elif topic == "Modal Component":

    st.header("Modal Component")

    st.markdown("""
A Modal is a popup dialog
displayed above webpage content.
""")

    st.subheader("Applications")

    st.markdown("""
✔ Login Forms

✔ Registration Forms

✔ Confirmations

✔ Notifications
""")

    st.subheader("Basic Structure")

    st.code("""
<div
class="
fixed
inset-0
flex
justify-center
items-center
">

<div
class="
bg-white
p-6
rounded
shadow
">

<h2>
Login
</h2>

</div>

</div>
""", language="html")

    st.subheader("Advantages")

    st.markdown("""
✔ Better User Experience

✔ Focused Interaction

✔ Space Saving
""")

    st.subheader("Activity")

    st.markdown("""
Design a Login Modal
for your application.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is a Modal?

2. Why are Modals used?

3. Give examples of Modal usage.
""")

# =====================================================
# CAROUSEL COMPONENT
# =====================================================

elif topic == "Carousel Component":

    st.header("Carousel Component")

    st.markdown("""
A Carousel is used to display
multiple images or content
in a sliding format.
""")

    st.subheader("Applications")

    st.markdown("""
✔ Product Showcase

✔ Image Gallery

✔ Advertisements

✔ Portfolio Websites
""")

    st.subheader("Basic Structure")

    st.code("""
<div class="carousel">

<img src="img1.jpg">

<img src="img2.jpg">

<img src="img3.jpg">

</div>
""", language="html")

    st.subheader("Benefits")

    st.markdown("""
✔ Attractive UI

✔ Better Content Presentation

✔ Improved Engagement
""")

    st.subheader("Popular Carousel Libraries")

    st.markdown("""
- Swiper.js

- Slick Carousel

- Bootstrap Carousel
""")

    st.subheader("Activity")

    st.markdown("""
Create an image carousel
for your domain project.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is a Carousel?

2. Where are Carousels used?

3. Name some Carousel libraries.
""")

    st.success(
        "Part 4 Completed: Tailwind Responsive Grid, Navbar, Hero, Table, Modal and Carousel Components."
    )
# =====================================================
# INTRODUCTION TO CORE JAVASCRIPT
# =====================================================

elif topic == "Core JavaScript":

    st.header("Introduction to Core JavaScript")

    st.markdown("""
JavaScript is the programming language of the web.

HTML provides structure.

CSS provides styling.

JavaScript provides interaction and behavior.
""")

    st.subheader("Why JavaScript?")

    st.markdown("""
✔ User Interaction

✔ Form Validation

✔ Dynamic Content

✔ API Integration

✔ Animations

✔ Web Applications
""")

    st.subheader("JavaScript in HTML")

    st.code("""
<script>

alert("Hello World");

</script>
""", language="html")

    st.subheader("Variables")

    st.code("""
let name = "John";

const age = 20;

var city = "Bangalore";
""", language="javascript")

    st.subheader("Data Types")

    st.code("""
String

Number

Boolean

Array

Object
""", language="javascript")

    st.subheader("Functions")

    st.code("""
function greet(){

    alert("Welcome");

}
""", language="javascript")

    st.subheader("Events")

    st.code("""
<button onclick="greet()">

Click Me

</button>
""", language="html")

    st.subheader("Activity")

    st.markdown("""
Create a button that displays
a welcome message using JavaScript.
""")

    st.subheader("Viva Questions")

    st.markdown("""
1. What is JavaScript?

2. Why is JavaScript used?

3. What is a variable?

4. What is a function?

5. What is an event?
""")

# =====================================================
# DOM MANIPULATION
# =====================================================

elif topic == "DOM Manipulation":

    st.header("DOM Manipulation")

    st.markdown("""
DOM stands for Document Object Model.

JavaScript can access and modify HTML elements dynamically.
""")

    st.subheader("Selecting Elements")

    st.code("""
document.getElementById()

document.querySelector()

document.querySelectorAll()
""", language="javascript")

    st.subheader("Example")

    st.code("""
<p id="demo">

Hello

</p>

<script>

document.getElementById(
"demo"
).innerHTML =

"Welcome Students";

</script>
""", language="html")

    st.subheader("Applications")

    st.markdown("""
✔ Dynamic Content

✔ Form Validation

✔ Interactive UI

✔ Dashboard Updates
""")

    st.subheader("Activity")

    st.markdown("""
Create a button that changes
the text of a paragraph.
""")

# =====================================================
# HTML5 APIS
# =====================================================

elif topic == "HTML5 APIs":

    st.header("Introduction to HTML5 APIs")

    st.markdown("""
HTML5 introduced powerful APIs
that allow web applications to access
browser features and device capabilities.
""")

    st.subheader("Popular HTML5 APIs")

    st.markdown("""
✔ Geolocation API

✔ Local Storage API

✔ Audio API

✔ Video API

✔ Canvas API

✔ Drag and Drop API

✔ Clipboard API

✔ Notifications API
""")

    st.info("""
Exercise-2 requires students
to integrate suitable APIs
based on their selected domain.
""")

# =====================================================
# GEOLOCATION API
# =====================================================

    st.subheader("1. Geolocation API")

    st.markdown("""
Geolocation API retrieves
the user's current location.
""")

    st.code("""
navigator.geolocation.getCurrentPosition(

function(position){

console.log(
position.coords.latitude
);

console.log(
position.coords.longitude
);

}

);
""", language="javascript")

    st.markdown("""
Applications:

- Travel Apps

- Food Delivery

- Smart Campus

- Emergency Services
""")

# =====================================================
# LOCAL STORAGE API
# =====================================================

    st.subheader("2. Local Storage API")

    st.markdown("""
Local Storage stores data
inside the browser.
""")

    st.code("""
localStorage.setItem(
"name",
"John"
);

localStorage.getItem(
"name"
);
""", language="javascript")

    st.markdown("""
Applications:

- User Preferences

- Shopping Cart

- Theme Settings

- Login Information
""")

# =====================================================
# AUDIO API
# =====================================================

    st.subheader("3. Audio API")

    st.code("""
<audio controls>

<source
src="audio.mp3">

</audio>
""", language="html")

    st.markdown("""
Applications:

- Podcasts

- Music Platforms

- E-Learning Systems
""")

# =====================================================
# VIDEO API
# =====================================================

    st.subheader("4. Video API")

    st.code("""
<video controls>

<source
src="video.mp4">

</video>
""", language="html")

    st.markdown("""
Applications:

- Tutorials

- Online Courses

- Product Demonstrations
""")

# =====================================================
# CANVAS API
# =====================================================

    st.subheader("5. Canvas API")

    st.code("""
<canvas
id="canvas"
width="300"
height="200">
</canvas>
""", language="html")

    st.code("""
const canvas =

document.getElementById(
"canvas"
);

const ctx =

canvas.getContext(
"2d"
);

ctx.fillRect(
50,
50,
100,
100
);
""", language="javascript")

    st.markdown("""
Applications:

- Games

- Drawing Tools

- Charts

- Signatures
""")

# =====================================================
# DRAG AND DROP API
# =====================================================

    st.subheader("6. Drag and Drop API")

    st.markdown("""
Allows users to drag
and drop elements.
""")

    st.code("""
draggable="true"
""", language="html")

    st.markdown("""
Applications:

- Kanban Boards

- File Upload Systems

- Project Management Tools
""")

# =====================================================
# DOMAIN EXAMPLES
# =====================================================

    st.subheader("HTML5 APIs in Real Projects")

    st.table({
        "Domain":[
            "Smart Campus",
            "Parking App",
            "Food Sharing",
            "Service Request",
            "Healthcare"
        ],
        "Possible APIs":[
            "Geolocation, Storage",
            "Geolocation",
            "Storage, Notifications",
            "Storage, Audio",
            "Geolocation, Video"
        ]
    })

# =====================================================
# MINI PROJECT
# =====================================================

elif topic == "Mini Project":

    st.header("Unit 1 Mini Project")

    st.markdown("""
Build a responsive domain-based
web application prototype.
""")

    st.subheader("Requirements")

    st.markdown("""
The application must include:

✔ HTML5 Semantic Elements

✔ Tailwind CSS

✔ Responsive Design

✔ Navbar

✔ Hero Section

✔ Feature Cards

✔ Footer

✔ Font Awesome Icons

✔ GitHub Repository

✔ JavaScript Interactions

✔ Minimum 3 HTML5 APIs
""")

    st.subheader("Suggested Domains")

    st.markdown("""
- Smart Campus

- Service Request System

- Food Sharing Platform

- Parking Management

- NGO Portal

- Healthcare Portal

- Alumni Portal
""")

# =====================================================
# UNIT 1 SUMMARY
# =====================================================

elif topic == "Unit 1 Summary":

    st.header("Unit 1 Summary")

    st.success("""
Congratulations!

You have completed Unit 1.
""")

    st.markdown("""
Topics Covered:

✔ Full Stack Development

✔ HTML5 Semantic Elements

✔ Responsive Web Design

✔ Tailwind CSS

✔ Canvas

✔ HTML Media

✔ Font Awesome

✔ Git Commit

✔ Git Rollback

✔ Remote Repository

✔ Merge Conflict

✔ CSS Specificity

✔ Pseudo Selectors

✔ Media Queries

✔ CSS Transitions

✔ Flexbox

✔ Responsive Grid

✔ Components

✔ Core JavaScript

✔ HTML5 APIs
""")

    st.subheader("Learning Outcomes")

    st.markdown("""
Students should now be able to:

- Build responsive webpages

- Use Tailwind CSS

- Create reusable UI components

- Work with Git and GitHub

- Write basic JavaScript

- Integrate HTML5 APIs

- Develop domain-based prototypes
""")

# =====================================================
# IMPORTANT VIVA QUESTIONS
# =====================================================

elif topic == "Important Viva Questions":

    st.header("Important Viva Questions")

    st.markdown("""
1. What is Full Stack Development?

2. What are Semantic Elements?

3. What is Responsive Web Design?

4. Difference between Flexbox and Grid?

5. What is Tailwind CSS?

6. What is Git Commit?

7. What is Rollback?

8. What is a Remote Repository?

9. What is a Merge Conflict?

10. What is CSS Specificity?

11. What are Pseudo Selectors?

12. What are Media Queries?

13. What are CSS Transitions?

14. What is JavaScript?

15. What is DOM?

16. What is an HTML5 API?

17. Explain Geolocation API.

18. Explain Local Storage API.

19. Explain Canvas API.

20. Explain Audio and Video APIs.
""")

    st.success(
        "🎉 Full Unit 1 Streamlit Learning Portal Completed."
    )