import streamlit as st

st.set_page_config(page_title="Windows Applications & Event-Driven Programming", layout="wide")

st.title("Windows Applications & Event-Driven Programming")
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
    st.header("Windows Applications & Event-Driven Programming")

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
    st.header("2. Windows Forms Development & Working Mechanisms")

    st.markdown("""
    Windows Forms applications work on **event-driven execution** where multiple
    controls cooperate to complete a **process or workflow**.

    Below examples demonstrate **how real applications function internally**
    using the same code taught in class.
    """)

    st.markdown("""
    ---
    ### Mini Project 1: Progress Tracker – Time-Driven Processing

    **Working Principle:**
    - Application initializes on form load
    - Progress bar range is configured
    - Timer generates periodic `Tick` events
    - Progress updates automatically
    - Process stops when completion is reached

    **Controls involved:**
    - Form
    - ProgressBar
    - Timer
    - Label
    """)

    st.markdown("#### VB.NET – Initialization Phase (Form Load)")
    st.code("""
Private Sub Form3_Load(sender As Object, e As EventArgs) Handles MyBase.Load
    ProgressBar1.Minimum = 0
    ProgressBar1.Maximum = 1000
    Timer1.Enabled = True
End Sub
""", language="vbnet")

    st.markdown("#### VB.NET – Execution Phase (Timer Tick)")
    st.code("""
Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
    ProgressBar1.Value = ProgressBar1.Value + 1
    Label8.Text = (ProgressBar1.Value / 10) & " % completed"

    If ProgressBar1.Value >= 1000 Then
        Timer1.Enabled = False
    End If
End Sub
""", language="vbnet")

    st.info("""
    ✔️ This demonstrates **automation using system events**  
    ✔️ No user action required after start  
    ✔️ Commonly used in loaders, installers, file transfers
    """)

    st.markdown("""
    ---
    ### Mini Project 2: Notepad Editor – File Handling Workflow

    **Working Principle:**
    - User selects a file using dialog
    - File content is loaded into editor
    - User modifies text
    - Updated content is saved back to file

    **Controls involved:**
    - MenuStrip
    - RichTextBox
    - OpenFileDialog
    - SaveFileDialog
    """)

    st.markdown("#### VB.NET – Open & Save File Mechanism")
    st.code("""
OpenFileDialog1.ShowDialog()
RichTextBox1.Text = System.IO.File.ReadAllText(OpenFileDialog1.FileName)

SaveFileDialog1.ShowDialog()
System.IO.File.WriteAllText(SaveFileDialog1.FileName, RichTextBox1.Text)
""", language="vbnet")

    st.markdown("#### C#.NET – Menu-Driven File Operations")
    st.code("""
private void openToolStripMenuItem_Click(object sender, EventArgs e)
{
    OpenFileDialog ofd = new OpenFileDialog();
    if (ofd.ShowDialog() == DialogResult.OK)
        richTextBox1.Text = System.IO.File.ReadAllText(ofd.FileName);
}

private void saveToolStripMenuItem_Click(object sender, EventArgs e)
{
    SaveFileDialog sfd = new SaveFileDialog();
    if (sfd.ShowDialog() == DialogResult.OK)
        System.IO.File.WriteAllText(sfd.FileName, richTextBox1.Text);
}
""", language="csharp")

    st.success("""
    ✔️ Demonstrates **file I/O workflow**
    ✔️ Separates UI action from data handling
    ✔️ Real-world editor behavior
    """)

    st.markdown("""
    ---
    ### Mini Project 3: Notepad Customization – Runtime Configuration

    **Working Principle:**
    - User selects visual preferences
    - Dialog returns selected value
    - Editor appearance updates dynamically

    **Controls involved:**
    - ColorDialog
    - FontDialog
    - RichTextBox
    """)

    st.markdown("#### C#.NET – Appearance Customization")
    st.code("""
private void foregroundToolStripMenuItem_Click(object sender, EventArgs e)
{
    ColorDialog cd = new ColorDialog();
    if (cd.ShowDialog() == DialogResult.OK)
        richTextBox1.ForeColor = cd.Color;
}

private void fontToolStripMenuItem_Click(object sender, EventArgs e)
{
    FontDialog fd = new FontDialog();
    if (fd.ShowDialog() == DialogResult.OK)
        richTextBox1.Font = fd.Font;
}
""", language="csharp")

    st.markdown("""
    ✔️ Shows **runtime UI reconfiguration**
    ✔️ Used in IDEs, editors, accessibility tools
    """)

    st.markdown("""
    ---
    ### Mini Project 4: Calculator – State-Based Computation

    **Working Principle:**
    - Numbers are entered step-by-step
    - Operator selection stores state
    - Final computation occurs on action trigger

    **Controls involved:**
    - Button
    - TextBox
    """)

    st.markdown("#### C#.NET – Calculator Logic (State Handling)")
    st.code("""
int a, b, c, option;

private void button5_Click(object sender, EventArgs e)
{
    a = int.Parse(textBox1.Text);
    textBox1.Text = "";
    option = 1; // Addition
}

private void button4_Click(object sender, EventArgs e)
{
    b = int.Parse(textBox1.Text);
    textBox1.Text = "";

    if (option == 1)
    {
        c = a + b;
        textBox1.Text = c.ToString();
    }
}
""", language="csharp")

    st.warning("""
    ✔️ Demonstrates **state retention**
    ✔️ Operator logic separated from input
    ✔️ Core concept for calculators, billing apps
    """)

    st.markdown("""
    ---
    ### Overall Learning Outcome

    These examples show that **WinForms applications are process-oriented systems**:
    - Some react to **time**
    - Some manage **files**
    - Some store **state**
    - Some automate **progress**

    🎯 Controls are just tools — **logic and workflow drive the application**
    """)

# --------------------------------------------------
elif menu == "ListView, TreeView & ProgressBar":
    st.header("3. ListView, TreeView & ProgressBar – Process-Based Working")

    st.markdown("""
    In real applications, these controls are used to **organize, visualize, and track data flow**.
    The focus here is on **how the data moves and changes**, not just on displaying it.
    """)

    st.markdown("""
    ---
    ## ListView – Structured Data Management (Mini Project: Student Records)

    **Working Principle:**
    1. Configure ListView display style
    2. Define columns (structure)
    3. Create items (data objects)
    4. Add items to ListView
    5. Select and retrieve data
    6. Dynamically insert new records from input

    This mimics **tables in real applications** like:
    - Student Management System
    - Marks / Results Viewer
    - File Explorer (Details View)
    """)

    st.markdown("### Step 1: Configure ListView Layout")
    st.code("""
ListView1.View = View.Details
ListView1.FullRowSelect = True
ListView1.GridLines = True
""", language="vbnet")

    st.markdown("""
    ✔️ Sets ListView to behave like a **table**
    ✔️ Improves readability and row-based selection
    """)

    st.markdown("### Step 2: Define Columns (Data Structure)")
    st.code("""
ListView1.Columns.Add("Roll No", 100)
ListView1.Columns.Add("Name", 150)
ListView1.Columns.Add("Department", 120)
""", language="vbnet")

    st.markdown("""
    ✔️ Columns act as **field definitions**
    ✔️ Similar to attributes in a database table
    """)

    st.markdown("### Step 3 & 4: Create and Add Data Item")
    st.code("""
Dim item1 As New ListViewItem("101")
item1.SubItems.Add("Arjun")
item1.SubItems.Add("BCA")

ListView1.Items.Add(item1)
""", language="vbnet")

    st.markdown("""
    ✔️ `ListViewItem` represents **one complete record**
    ✔️ `SubItems` represent additional fields
    """)

    st.markdown("### Step 5: Access Selected Record (User Interaction)")
    st.code("""
If ListView1.SelectedItems.Count > 0 Then
    MessageBox.Show(ListView1.SelectedItems(0).Text)
End If
""", language="vbnet")

    st.markdown("""
    ✔️ Demonstrates **selection-based processing**
    ✔️ Used in delete, edit, view-details operations
    """)

    st.markdown("### Step 6: Dynamic Data Entry Using TextBoxes")
    st.code("""
Dim newItem As New ListViewItem(TextBox1.Text)
newItem.SubItems.Add(TextBox2.Text)
newItem.SubItems.Add(TextBox3.Text)

ListView1.Items.Add(newItem)

TextBox1.Clear()
TextBox2.Clear()
TextBox3.Clear()

MessageBox.Show("Data Added Successfully")
""", language="vbnet")

    st.success("""
    ✔️ Demonstrates **runtime data insertion**
    ✔️ Common in CRUD-based applications
    """)

    st.markdown("""
    ---
    ## ListView – Equivalent C#.NET Logic (For Reference)
    """)

    st.code("""
listView1.View = View.Details;
listView1.FullRowSelect = true;
listView1.GridLines = true;

listView1.Columns.Add("Roll No", 100);
listView1.Columns.Add("Name", 150);
listView1.Columns.Add("Department", 120);

ListViewItem item = new ListViewItem("101");
item.SubItems.Add("Arjun");
item.SubItems.Add("BCA");

listView1.Items.Add(item);
""", language="csharp")

    st.markdown("""
    ---
    ## TreeView – Hierarchical Data Representation

    **Working Principle:**
    - Parent nodes represent categories
    - Child nodes represent sub-items
    - Used when data follows a **tree structure**

    **Real Applications:**
    - Folder structure
    - Organization hierarchy
    - Course → Semester → Subject
    """)

    st.code("""
TreeNode root = new TreeNode("Courses");
root.Nodes.Add("BCA");
root.Nodes.Add("BSc CS");

treeView1.Nodes.Add(root);
""", language="csharp")

    st.markdown("""
    ✔️ TreeView represents **parent–child relationships**
    ✔️ Navigation-based control
    """)

    st.markdown("""
    ---
    ## ProgressBar – Task Progress Monitoring

    **Working Principle:**
    - ProgressBar reflects task completion
    - Value updated during processing
    - Often combined with Timer or loops

    **Real Applications:**
    - File upload/download
    - Quiz completion status
    - Installation process
    """)

    st.code("""
progressBar1.Value += 10;  // Progress per task
""", language="csharp")

    st.info("""
    🎯 Key Insight:
    ListView manages **structured records**,  
    TreeView manages **hierarchies**,  
    ProgressBar tracks **process completion**.
    """)


# --------------------------------------------------
elif menu == "Timer, ErrorProvider & Components":
    st.header("4. Timer, ErrorProvider & Components – Working Mechanisms")

    st.markdown("""
    Components in WinForms work **behind the scenes**.
    They do not directly interact with users but control **timing, validation,
    and application behavior**.
    """)

    st.markdown("""
    ---
    ## Timer – Time-Driven Execution (Mini Project: Stopwatch / Quiz Timer)

    **Working Principle:**
    - Timer runs in the background
    - Generates `Tick` events at fixed intervals
    - Each tick updates application logic
    - Stops automatically based on condition

    **Common Uses:**
    - Stopwatch
    - Countdown timer in quizzes
    - Auto-save
    - Progress monitoring

    **Controls involved:**
    - Timer
    - Label
    - Button
    """)

    st.markdown("### C#.NET – Stopwatch Core Mechanism")
    st.code("""
int seconds = 0;

private void timer1_Tick(object sender, EventArgs e)
{
    seconds++;
    lblTime.Text = seconds.ToString() + " sec";
}
""", language="csharp")

    st.markdown("### VB.NET – Timer Controlled Execution")
    st.code("""
Dim seconds As Integer = 0

Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
    seconds += 1
    lblTime.Text = seconds & " sec"
End Sub
""", language="vbnet")

    st.info("""
    ✔️ Demonstrates **system-generated events**
    ✔️ Code executes automatically without user action
    ✔️ Key concept for real-time applications
    """)

    st.markdown("""
    ---
    ## Timer – Quiz Countdown Example (Process Flow)

    **Working Principle:**
    - Quiz starts
    - Timer counts down
    - When time reaches zero, quiz ends automatically
    """)

    st.code("""
int timeLeft = 30;

private void timer1_Tick(object sender, EventArgs e)
{
    timeLeft--;
    lblTime.Text = timeLeft.ToString();

    if (timeLeft == 0)
    {
        timer1.Stop();
        MessageBox.Show("Time Up!");
    }
}
""", language="csharp")

    st.markdown("""
    ---
    ## ErrorProvider – Input Validation Mechanism

    **Working Principle:**
    - User enters data
    - System checks validity
    - ErrorProvider shows visual feedback
    - Error disappears once corrected

    **Used in:**
    - Registration forms
    - Login validation
    - Data entry applications
    """)

    st.markdown("### VB.NET – Required Field Validation")
    st.code("""
If TextBox1.Text = "" Then
    ErrorProvider1.SetError(TextBox1, "Required field")
Else
    ErrorProvider1.Clear()
End If
""", language="vbnet")

    st.markdown("### C#.NET – Numeric Validation Example")
    st.code("""
if (string.IsNullOrEmpty(txtAge.Text))
{
    errorProvider1.SetError(txtAge, "Age is required");
}
else
{
    errorProvider1.Clear();
}
""", language="csharp")

    st.success("""
    ✔️ Validation happens **without blocking the user**
    ✔️ Improves usability and data correctness
    """)

    st.markdown("""
    ---
    ## Components – Non-Visual Controllers

    **Definition:**
    Components are non-visual objects that:
    - Control application logic
    - Manage resources
    - Support background processing

    **Examples:**
    - Timer
    - ErrorProvider
    - BackgroundWorker
    - FileSystemWatcher
    """)

    st.markdown("""
    ---
    ### Learning Summary

    - **Timer** controls *when* code executes
    - **ErrorProvider** controls *data correctness*
    - **Components** manage application behavior behind the UI

    🎯 Controls show data, components **drive logic**
    """)


# --------------------------------------------------
elif menu == "Menus, Toolbars & Dialog Boxes":
    st.header("5. Menus, Toolbars & Dialog Boxes – Command & Interaction Flow")

    st.markdown("""
    Menus and toolbars act as **command controllers** in desktop applications.
    They do not perform work themselves but **trigger processes**
    such as file handling, formatting, and system interaction using dialog boxes.
    """)

    st.markdown("""
    ---
    ## MenuStrip – Command-Based Workflow (Mini Project: Notepad)

    **Working Principle:**
    - User selects a menu option
    - Corresponding event handler is triggered
    - Application executes required logic
    - Dialog box may appear for user input

    **Typical Menu Flow:**
    ```
    Menu Click → Event Handler → Dialog → Action → UI Update
    ```

    **Common Menu Commands:**
    - File → New / Open / Save / Exit
    - Edit → Cut / Copy / Paste
    - Format → Font / Color
    """)

    st.markdown("### C#.NET – File Open Using MenuStrip")
    st.code("""
private void openToolStripMenuItem_Click(object sender, EventArgs e)
{
    OpenFileDialog dlg = new OpenFileDialog();
    if (dlg.ShowDialog() == DialogResult.OK)
    {
        richTextBox1.Text = System.IO.File.ReadAllText(dlg.FileName);
    }
}
""", language="csharp")

    st.markdown("### VB.NET – File Save Using MenuStrip")
    st.code("""
Private Sub SaveToolStripMenuItem_Click(sender As Object, e As EventArgs)
    SaveFileDialog1.ShowDialog()
    System.IO.File.WriteAllText(SaveFileDialog1.FileName, RichTextBox1.Text)
End Sub
""", language="vbnet")

    st.info("""
    ✔️ MenuStrip acts as a **command dispatcher**
    ✔️ Used in editors, IDEs, management systems
    """)

    st.markdown("""
    ---
    ## ToolStrip – Quick Action Workflow (Mini Project: Paint / Editor)

    **Working Principle:**
    - Icons represent frequently used commands
    - Clicking an icon triggers the same logic as menu items
    - Improves speed and usability

    **Used in:**
    - Paint applications
    - Text editors
    - Design tools
    """)

    st.markdown("### C#.NET – ToolStrip Color Selection")
    st.code("""
private void toolStripButtonColor_Click(object sender, EventArgs e)
{
    ColorDialog cd = new ColorDialog();
    if (cd.ShowDialog() == DialogResult.OK)
        richTextBox1.ForeColor = cd.Color;
}
""", language="csharp")

    st.markdown("""
    ✔️ ToolStrip is a **shortcut interface**
    ✔️ Often linked to the same logic as MenuStrip
    """)

    st.markdown("""
    ---
    ## Dialog Boxes – User Interaction Mechanism

    **Working Principle:**
    - Dialog box collects user input or preference
    - Returns selected value to application
    - Application updates behavior accordingly

    **Common Dialogs:**
    - OpenFileDialog → Select file
    - SaveFileDialog → Save content
    - ColorDialog → Choose colors
    - FontDialog → Select font
    """)

    st.markdown("### C#.NET – Open File Dialog")
    st.code("""
OpenFileDialog dlg = new OpenFileDialog();
dlg.ShowDialog();
""", language="csharp")

    st.markdown("### VB.NET – Font Selection Dialog")
    st.code("""
FontDialog1.ShowDialog()
RichTextBox1.Font = FontDialog1.Font
""", language="vbnet")

    st.success("""
    ✔️ Dialogs provide **safe and standardized interaction**
    ✔️ Prevent invalid input and improve UX
    """)

    st.markdown("""
    ---
    ### Learning Summary

    - **MenuStrip** organizes application commands
    - **ToolStrip** provides quick access to actions
    - **Dialog Boxes** gather user choices securely

    🎯 Menus & dialogs **control workflow**, not data
    """)


# --------------------------------------------------
elif menu == "Custom Controls & VB.NET–C# Interoperability":
    st.header("6. Custom Controls & VB.NET–C# Interoperability – Reuse & Integration")

    st.markdown("""
    Advanced Windows Forms applications focus on **reuse, modularity, and integration**.
    Custom Controls and Interoperability help developers **avoid rewriting code**
    and **separate UI from logic**.
    """)

    st.markdown("""
    ---
    ## Custom Controls – Component Reuse Mechanism

    **What is a Custom Control?**
    A Custom Control is a **user-defined reusable component** created by
    combining multiple controls and logic into a single unit.

    **Why Custom Controls?**
    - Reduce repeated coding
    - Maintain consistent UI behavior
    - Simplify large applications
    """)

    st.markdown("""
    ### Mini Project: Stopwatch as a Custom Control

    **Working Principle:**
    - Timer controls time progression
    - Internal logic handles start/stop/reset
    - External form simply **uses** the control

    **Internal Components Used:**
    - Label
    - Button
    - Timer
    """)

    st.markdown("### C#.NET – Stopwatch Custom Control (Core Logic)")
    st.code("""
public partial class StopwatchControl : UserControl
{
    int seconds = 0;

    public StopwatchControl()
    {
        InitializeComponent();
    }

    private void timer1_Tick(object sender, EventArgs e)
    {
        seconds++;
        lblTime.Text = seconds + " sec";
    }

    public void Start()
    {
        timer1.Start();
    }

    public void Stop()
    {
        timer1.Stop();
    }
}
""", language="csharp")

    st.markdown("""
    ✔️ Control exposes **methods**, not internal UI  
    ✔️ Used like a ready-made component
    """)

    st.markdown("### VB.NET – Using Custom Control in a Form")
    st.code("""
Private Sub btnStart_Click(sender As Object, e As EventArgs) Handles btnStart.Click
    StopwatchControl1.Start()
End Sub
""", language="vbnet")

    st.success("""
    ✔️ Demonstrates **encapsulation and reusability**
    ✔️ Ideal for dashboards, timers, calculators
    """)

    st.markdown("""
    ---
    ## Custom Controls – Another Example (Calculator Keypad)

    **Working Principle:**
    - Buttons are grouped into one control
    - Key press logic handled internally
    - Main form receives final value only
    """)

    st.markdown("""
    ✔️ Used in billing systems, POS, kiosks
    """)

    st.markdown("""
    ---
    ## VB.NET & C#.NET Interoperability – Cross-Language Integration

    **What is Interoperability?**
    Interoperability allows **VB.NET and C#.NET to work together**
    within the same application using the .NET Common Language Runtime (CLR).

    **Why Interoperability?**
    - Use existing code without rewriting
    - Separate business logic from UI
    - Team flexibility (VB & C# developers)
    """)

    st.markdown("""
    ### Mini Project: Shared Business Logic DLL

    **Architecture:**
    ```
    C# Class Library (Logic)
           ↓
    VB.NET WinForms (UI)
    ```
    """)

    st.markdown("### C#.NET – Business Logic Class (DLL)")
    st.code("""
namespace SharedLogic
{
    public class CalculatorLogic
    {
        public int Add(int a, int b)
        {
            return a + b;
        }
    }
}
""", language="csharp")

    st.markdown("### VB.NET – Consuming C# DLL")
    st.code("""
Dim calc As New SharedLogic.CalculatorLogic()
Dim result As Integer = calc.Add(10, 20)
MessageBox.Show(result.ToString())
""", language="vbnet")

    st.info("""
    ✔️ Language-independent execution via CLR
    ✔️ Logic reused across multiple applications
    """)

    st.markdown("""
    ---
    ### Learning Summary

    - **Custom Controls** promote reuse and modular design
    - **Interoperability** enables cross-language collaboration
    - Both support **scalable and maintainable applications**

    🎯 Build once, reuse everywhere
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
