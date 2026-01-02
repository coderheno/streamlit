import streamlit as st

st.set_page_config(page_title="Windows Applications & Event-Driven Programming", layout="wide")

st.title("🪟 Windows Applications & Event-Driven Programming")
st.subheader("Practical-Based Learning using Streamlit")

# Sidebar Navigation
menu = st.sidebar.radio(
    "Select Topic",
    [
        "Introduction & Event-Driven Programming",
        "Common Controls (with Examples)",
        "Timer & ProgressBar",
        "Menus & Dialog Boxes",
        "Mini Apps Overview",
        "Lab-3: Calculator",
        "Lab-4: Drawing App (Paint)",
    ]
)

# -------------------------------------------------
if menu == "Introduction & Event-Driven Programming":
    st.header("1️⃣ Windows Applications & Event-Driven Programming")

    st.markdown("""
    **Windows Applications** are GUI-based programs that respond to user actions.

    ### Event-Driven Programming
    - Program execution depends on **events**
    - Example events: Button Click, Timer Tick, Mouse Move

    **Real-Time Examples:**
    - Calculator → Button Click
    - Quiz App → RadioButton Change
    - Stopwatch → Timer Tick

    **Event Flow:**
    ```
    User Action → Event → Event Handler → Output
    ```
    """)

# -------------------------------------------------
elif menu == "Common Controls (with Examples)":
    st.header("2️⃣ Common Controls – Practical Examples")

    st.subheader("Button (Calculator / Quiz)")
    st.code("""
// C# Button Click Event
private void btnAdd_Click(object sender, EventArgs e)
{
    int a = int.Parse(txtA.Text);
    int b = int.Parse(txtB.Text);
    lblResult.Text = (a + b).ToString();
}
""", language="csharp")

    st.subheader("TextBox (Notepad)")
    st.markdown("- Multiline TextBox is used to type notes")

    st.subheader("RadioButton (Quiz App)")
    st.code("""
If RadioButton1.Checked Then
    score += 1
End If
""", language="vbnet")

    st.subheader("ListView (Quiz Result / File List)")
    st.code("""
listView1.Items.Add("Student1 - 8/10");
""", language="csharp")

# -------------------------------------------------
elif menu == "Timer & ProgressBar":
    st.header("3️⃣ Timer & ProgressBar")

    st.subheader("Timer – Stopwatch / Quiz Timer")
    st.code("""
private void timer1_Tick(object sender, EventArgs e)
{
    seconds++;
    lblTime.Text = seconds.ToString();
}
""", language="csharp")

    st.subheader("ProgressBar – Quiz Progress")
    st.code("""
progressBar1.Value += 10; // Each question = 10%
""", language="csharp")

    st.markdown("**Expected Output:** Time increments every second, progress fills gradually")

# -------------------------------------------------
elif menu == "Menus & Dialog Boxes":
    st.header("4️⃣ Menus, Toolbars & Dialog Boxes")

    st.subheader("MenuStrip – Notepad")
    st.markdown("- File → New, Open, Save, Exit")

    st.subheader("OpenFileDialog Example")
    st.code("""
OpenFileDialog ofd = new OpenFileDialog();
ofd.ShowDialog();
""", language="csharp")

    st.subheader("ColorDialog – Paint App")
    st.markdown("Used to select drawing color")

# -------------------------------------------------
elif menu == "Mini Apps Overview":
    st.header("5️⃣ Mini Applications")

    st.markdown("""
    ### Quiz Application
    - Controls: Label, RadioButton, Button, Timer, ProgressBar

    ### Stopwatch
    - Controls: Label, Button, Timer

    ### Notepad
    - Controls: TextBox (Multiline), MenuStrip, Dialog Boxes

    ### Simple Web Browser
    ```csharp
    webBrowser1.Navigate(txtURL.Text);
    ```
    """)

# -------------------------------------------------
elif menu == "Lab-3: Calculator":
    st.header("🧪 Lab-3: Windows Forms Calculator")

    st.subheader("Aim")
    st.write("To create a calculator using Windows Forms in VB.NET / C#")

    st.subheader("Steps")
    st.markdown("""
    1. Create a new Windows Forms Application
    2. Add two TextBoxes for input
    3. Add Buttons for operations (+, -, *, /)
    4. Add Label to display result
    5. Write event handlers for buttons
    """)

    st.subheader("Sample Code (VB.NET)")
    st.code("""
Private Sub btnAdd_Click(sender As Object, e As EventArgs)
    Dim a As Integer = Val(TextBox1.Text)
    Dim b As Integer = Val(TextBox2.Text)
    Label1.Text = a + b
End Sub
""", language="vbnet")

    st.subheader("Expected Output")
    st.write("Calculator performs arithmetic operations")

# -------------------------------------------------
elif menu == "Lab-4: Drawing App (Paint)":
    st.header("🧪 Lab-4: Drawing App (Paint)")

    st.subheader("Aim")
    st.write("To create a simple paint application using mouse events")

    st.subheader("Steps")
    st.markdown("""
    1. Create Windows Forms Application
    2. Handle MouseDown, MouseMove, MouseUp events
    3. Use Graphics class to draw
    4. Add ColorDialog for color selection
    """)

    st.subheader("Sample Code (C#)")
    st.code("""
Graphics g;
Pen pen = new Pen(Color.Black);

private void Form1_MouseMove(object sender, MouseEventArgs e)
{
    if (e.Button == MouseButtons.Left)
    {
        g = this.CreateGraphics();
        g.DrawEllipse(pen, e.X, e.Y, 2, 2);
    }
}
""", language="csharp")

    st.subheader("Expected Output")
    st.write("User can draw freely on the form like Paint")
import streamlit as st

st.set_page_config(page_title="Windows Applications & Event-Driven Programming", layout="wide")

st.title("🪟 Windows Applications & Event-Driven Programming")
st.subheader("Practical-Based Learning using Streamlit")

# Sidebar Navigation
menu = st.sidebar.radio(
    "Select Topic",
    [
        "Introduction & Event-Driven Programming",
        "Common Controls (with Examples)",
        "Timer & ProgressBar",
        "Menus & Dialog Boxes",
        "Mini Apps Overview",
        "Lab-3: Calculator",
        "Lab-4: Drawing App (Paint)",
    ]
)

# -------------------------------------------------
if menu == "Introduction & Event-Driven Programming":
    st.header("1️⃣ Windows Applications & Event-Driven Programming")

    st.markdown("""
    **Windows Applications** are GUI-based programs that respond to user actions.

    ### Event-Driven Programming
    - Program execution depends on **events**
    - Example events: Button Click, Timer Tick, Mouse Move

    **Real-Time Examples:**
    - Calculator → Button Click
    - Quiz App → RadioButton Change
    - Stopwatch → Timer Tick

    **Event Flow:**
    ```
    User Action → Event → Event Handler → Output
    ```
    """)

# -------------------------------------------------
elif menu == "Common Controls (with Examples)":
    st.header("2️⃣ Common Controls – Practical Examples")

    st.subheader("Button (Calculator / Quiz)")
    st.code("""
// C# Button Click Event
private void btnAdd_Click(object sender, EventArgs e)
{
    int a = int.Parse(txtA.Text);
    int b = int.Parse(txtB.Text);
    lblResult.Text = (a + b).ToString();
}
""", language="csharp")

    st.subheader("TextBox (Notepad)")
    st.markdown("- Multiline TextBox is used to type notes")

    st.subheader("RadioButton (Quiz App)")
    st.code("""
If RadioButton1.Checked Then
    score += 1
End If
""", language="vbnet")

    st.subheader("ListView (Quiz Result / File List)")
    st.code("""
listView1.Items.Add("Student1 - 8/10");
""", language="csharp")

# -------------------------------------------------
elif menu == "Timer & ProgressBar":
    st.header("3️⃣ Timer & ProgressBar")

    st.subheader("Timer – Stopwatch / Quiz Timer")
    st.code("""
private void timer1_Tick(object sender, EventArgs e)
{
    seconds++;
    lblTime.Text = seconds.ToString();
}
""", language="csharp")

    st.subheader("ProgressBar – Quiz Progress")
    st.code("""
progressBar1.Value += 10; // Each question = 10%
""", language="csharp")

    st.markdown("**Expected Output:** Time increments every second, progress fills gradually")

# -------------------------------------------------
elif menu == "Menus & Dialog Boxes":
    st.header("4️⃣ Menus, Toolbars & Dialog Boxes")

    st.subheader("MenuStrip – Notepad")
    st.markdown("- File → New, Open, Save, Exit")

    st.subheader("OpenFileDialog Example")
    st.code("""
OpenFileDialog ofd = new OpenFileDialog();
ofd.ShowDialog();
""", language="csharp")

    st.subheader("ColorDialog – Paint App")
    st.markdown("Used to select drawing color")

# -------------------------------------------------
elif menu == "Mini Apps Overview":
    st.header("5️⃣ Mini Applications")

    st.markdown("""
    ### Quiz Application
    - Controls: Label, RadioButton, Button, Timer, ProgressBar

    ### Stopwatch
    - Controls: Label, Button, Timer

    ### Notepad
    - Controls: TextBox (Multiline), MenuStrip, Dialog Boxes

    ### Simple Web Browser
    ```csharp
    webBrowser1.Navigate(txtURL.Text);
    ```
    """)

# -------------------------------------------------
elif menu == "Lab-3: Calculator":
    st.header("🧪 Lab-3: Windows Forms Calculator")

    st.subheader("Aim")
    st.write("To create a calculator using Windows Forms in VB.NET / C#")

    st.subheader("Steps")
    st.markdown("""
    1. Create a new Windows Forms Application
    2. Add two TextBoxes for input
    3. Add Buttons for operations (+, -, *, /)
    4. Add Label to display result
    5. Write event handlers for buttons
    """)

    st.subheader("Sample Code (VB.NET)")
    st.code("""
Private Sub btnAdd_Click(sender As Object, e As EventArgs)
    Dim a As Integer = Val(TextBox1.Text)
    Dim b As Integer = Val(TextBox2.Text)
    Label1.Text = a + b
End Sub
""", language="vbnet")

    st.subheader("Expected Output")
    st.write("Calculator performs arithmetic operations")

# -------------------------------------------------
elif menu == "Lab-4: Drawing App (Paint)":
    st.header("🧪 Lab-4: Drawing App (Paint)")

    st.subheader("Aim")
    st.write("To create a simple paint application using mouse events")

    st.subheader("Steps")
    st.markdown("""
    1. Create Windows Forms Application
    2. Handle MouseDown, MouseMove, MouseUp events
    3. Use Graphics class to draw
    4. Add ColorDialog for color selection
    """)

    st.subheader("Sample Code (C#)")
    st.code("""
Graphics g;
Pen pen = new Pen(Color.Black);

private void Form1_MouseMove(object sender, MouseEventArgs e)
{
    if (e.Button == MouseButtons.Left)
    {
        g = this.CreateGraphics();
        g.DrawEllipse(pen, e.X, e.Y, 2, 2);
    }
}
""", language="csharp")

    st.subheader("Expected Output")
    st.write("User can draw freely on the form like Paint")
