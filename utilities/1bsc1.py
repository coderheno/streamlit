import streamlit as st

st.set_page_config(page_title="Windows Applications & Event-Driven Programming", layout="wide")

st.title("Windows Applications & Event-Driven Programming")
st.write("Detailed, Practical & Application-Oriented Study Material")

# Sidebar Menu (kept simple to avoid duplicate ID issues)
menu = st.sidebar.selectbox(
    "Select Topic",
    (
        "Introduction & Event-Driven Programming",
        "Windows Forms & Common Controls",
        "ListView, TreeView & ProgressBar",
        "Timer, ErrorProvider & Components",
        "Menus, Toolbars & Dialog Boxes",
        "Custom Controls & VB.NET–C# Interoperability",
        "Lab-3: Calculator",
        "Lab-4: Drawing App (Paint)"
    )
)

# --------------------------------------------------
if menu == "Introduction & Event-Driven Programming":
    st.header("1. Windows Applications & Event-Driven Programming")

    st.markdown("""
    ### Windows Applications
    Windows Applications are **GUI-based desktop applications** developed to run on the Windows Operating System.
    They allow users to interact through **visual components** instead of typing commands.

    **Common GUI Controls:**
    - Button – triggers an action
    - TextBox – accepts user input
    - Label – displays text
    - RadioButton / CheckBox – selection options
    - Timer – performs actions at fixed intervals

    **Real-Time Examples:**
    - **Calculator** – Buttons for numbers and operators
    - **Notepad** – TextBox for typing text
    - **Paint** – Mouse events for drawing
    - **Stopwatch** – Timer control updates time
    - **Login Form** – Button click validates username/password
    """)

    st.markdown("""
    ### Event-Driven Programming
    In event-driven programming, the **program does not execute line by line**.
    Instead, it **waits for an event** (user action or system action) and responds to it.

    #### What is an Event?
    An **event** is an action that occurs when the user interacts with the application or when the system triggers it.

    | User Action | Event Name |
    |------------|-----------|
    | Clicking a button | Click |
    | Typing in TextBox | TextChanged |
    | Opening the form | Load |
    | Moving the mouse | MouseMove |
    | Timer interval | Tick |

    **Event Execution Flow:**
    ```
    User Action → Event → Event Handler → Application Response
    ```
    """)

    st.markdown("""
    ### Simple Example – Button Click Event

    #### Scenario:
    When the user clicks a button, a message should be displayed.

    #### VB.NET Example:
    ```vbnet
    Private Sub btnHello_Click(sender As Object, e As EventArgs) Handles btnHello.Click
        MessageBox.Show("Hello, Welcome to Windows Application!")
    End Sub
    ```

    **Explanation:**
    - `btnHello_Click` is the **event handler**
    - `Handles btnHello.Click` connects the button to the event
    - Code executes **only when the button is clicked**

    #### C#.NET Example:
    ```csharp
    private void btnHello_Click(object sender, EventArgs e)
    {
        MessageBox.Show("Hello, Welcome to Windows Application!");
    }
    ```

    **Explanation:**
    - Method runs automatically when `btnHello` is clicked
    - `sender` refers to the control that triggered the event
    """)

    st.markdown("""
    ### Real-Time Event Mapping Examples

    - **Calculator App**
      - Number Button → `Click`
      - Equals Button → `Click`

    - **Quiz Application**
      - RadioButton selection → `CheckedChanged`
      - Submit Button → `Click`

    - **Stopwatch**
      - Timer → `Tick`
      - Start/Stop Button → `Click`

    - **Paint Application**
      - Mouse movement → `MouseMove`
      - Mouse click → `MouseDown`

    ✔️ Each action happens **only when its event is triggered**, making applications responsive and efficient.
    """)

    st.info("👉 Key Idea: Event-driven programming reacts to user actions instead of running continuously.")

# --------------------------------------------------
elif menu == "Windows Forms & Common Controls":
    st.header("2. Windows Forms Development & Common Controls")

    st.markdown("""
    ### Windows Forms (WinForms)
    Windows Forms is a .NET framework used to create **desktop GUI applications** using C# or VB.NET.

    A **Form** acts as the main window of the application.
    """)

    st.subheader("Button (Calculator / Quiz)")
    st.write("Used to perform actions when clicked.")
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
    st.markdown("""
    Used to accept user input.
    - `Multiline = true` → Notepad
    - `ReadOnly = true` → Display-only
    """)

    st.subheader("Label (Stopwatch Display)")
    st.write("Used to display output like time, result, messages.")

    st.subheader("RadioButton (Quiz App)")
    st.code("""
If RadioButton1.Checked Then
    score = score + 1
End If
""", language="vbnet")

    st.subheader("CheckBox (Settings / Quiz)")
    st.write("Allows multiple selections.")

# --------------------------------------------------
elif menu == "ListView, TreeView & ProgressBar":
    st.header("3. ListView, TreeView & ProgressBar")

    st.subheader("ListView")
    st.markdown("""
    Displays items in a list format.

    **Real Applications:**
    - File Explorer
    - Quiz Results
    - Browser History
    """)

    st.code("""
listView1.Items.Add("Student1 - 8/10");
""", language="csharp")

    st.subheader("TreeView")
    st.markdown("""
    Displays **hierarchical data**.

    **Example:** Folder structure, Menu structure
    """)

    st.subheader("ProgressBar")
    st.markdown("""
    Shows progress of a task.

    **Examples:**
    - Quiz progress
    - File download
    - Installation
    """)

    st.code("""
progressBar1.Value += 10; // Each question
""", language="csharp")

# --------------------------------------------------
elif menu == "Timer, ErrorProvider & Components":
    st.header("4. Timer, ErrorProvider & Components")

    st.subheader("Timer (Stopwatch / Quiz)")
    st.markdown("Timer triggers code at fixed intervals.")

    st.code("""
private void timer1_Tick(object sender, EventArgs e)
{
    seconds++;
    lblTime.Text = seconds.ToString();
}
""", language="csharp")

    st.subheader("ErrorProvider (Validation)")
    st.markdown("Used to show validation errors in forms.")

    st.code("""
If TextBox1.Text = "" Then
    ErrorProvider1.SetError(TextBox1, "Required field")
End If
""", language="vbnet")

# --------------------------------------------------
elif menu == "Menus, Toolbars & Dialog Boxes":
    st.header("5. Menus, Toolbars & Dialog Boxes")

    st.subheader("MenuStrip (Notepad)")
    st.write("File → New | Open | Save | Exit")

    st.subheader("ToolStrip (Paint)")
    st.write("Icons for brush, eraser, color picker")

    st.subheader("Dialog Boxes")
    st.markdown("""
    - OpenFileDialog
    - SaveFileDialog
    - ColorDialog
    - FontDialog
    """)

    st.code("""
OpenFileDialog dlg = new OpenFileDialog();
dlg.ShowDialog();
""", language="csharp")

# --------------------------------------------------
elif menu == "Custom Controls & VB.NET–C# Interoperability":
    st.header("6. Custom Controls & Interoperability")

    st.subheader("Custom Controls")
    st.markdown("""
    A custom control is a **user-defined control** created by combining existing controls.

    **Example:**
    - Stopwatch control
    - Calculator keypad
    """)

    st.subheader("VB.NET & C# Interoperability")
    st.markdown("""
    Allows using VB.NET code inside C# projects and vice versa.

    **Example:**
    - Business logic in C# DLL
    - UI in VB.NET
    """)

# --------------------------------------------------
elif menu == "Lab-3: Calculator":
    st.header("🧪 Lab-3: Windows Forms Calculator")

    st.subheader("Aim")
    st.write("To create a simple calculator using Windows Forms in VB.NET / C#")

    st.subheader("Algorithm / Steps")
    st.markdown("""
    1. Create Windows Forms Application
    2. Add two TextBoxes for input
    3. Add Buttons for arithmetic operations
    4. Add Label to display result
    5. Write Click event code
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
    st.write("Calculator performs addition, subtraction, multiplication and division")

# --------------------------------------------------
elif menu == "Lab-4: Drawing App (Paint)":
    st.header("🧪 Lab-4: Drawing App (Paint)")

    st.subheader("Aim")
    st.write("To create a simple Paint application using mouse events")

    st.subheader("Algorithm / Steps")
    st.markdown("""
    1. Create Windows Forms Application
    2. Handle MouseDown, MouseMove, MouseUp events
    3. Use Graphics and Pen classes
    4. Add ColorDialog for color selection
    """)

    st.subheader("Sample Code (C#)")
    st.code("""
private void Form1_MouseMove(object sender, MouseEventArgs e)
{
    if (e.Button == MouseButtons.Left)
    {
        Graphics g = this.CreateGraphics();
        g.FillEllipse(Brushes.Black, e.X, e.Y, 4, 4);
    }
}
""", language="csharp")

    st.subheader("Expected Output")
    st.write("User can draw freely on the form similar to MS Paint")
