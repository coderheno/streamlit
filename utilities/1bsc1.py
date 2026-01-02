import streamlit as st

st.set_page_config(page_title="Windows Applications & Event-Driven Programming", layout="wide")

st.title("Windows Applications & Event-Driven Programming")
st.write("Practical-Based Learning (Simple & Error-Free)")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Select Topic",
    (
        "Introduction",
        "Common Controls",
        "Timer & ProgressBar",
        "Menus & Dialog Boxes",
        "Lab-3: Calculator",
        "Lab-4: Drawing App"
    )
)

# ---------------- INTRODUCTION ----------------
if menu == "Introduction":
    st.header("1. Windows Applications & Event-Driven Programming")
    st.write("Windows Applications are GUI-based programs that work based on user actions.")

    st.subheader("Event-Driven Programming")
    st.markdown("""
    - Program runs when an **event occurs**
    - Examples: Button Click, Timer Tick, Mouse Move

    **Real Applications:**
    - Calculator → Button Click
    - Stopwatch → Timer Tick
    - Paint → Mouse Move
    """)

# ---------------- CONTROLS ----------------
elif menu == "Common Controls":
    st.header("2. Common Controls")

    st.subheader("Button – Calculator")
    st.code("""
// C# Button Click
private void btnAdd_Click(object sender, EventArgs e)
{
    int a = int.Parse(txtA.Text);
    int b = int.Parse(txtB.Text);
    lblResult.Text = (a + b).ToString();
}
""", language="csharp")

    st.subheader("TextBox – Notepad")
    st.write("Used to type text (Multiline = true)")

    st.subheader("RadioButton – Quiz")
    st.code("""
If RadioButton1.Checked Then
    score = score + 1
End If
""", language="vbnet")

# ---------------- TIMER ----------------
elif menu == "Timer & ProgressBar":
    st.header("3. Timer & ProgressBar")

    st.subheader("Timer – Stopwatch")
    st.code("""
private void timer1_Tick(object sender, EventArgs e)
{
    seconds = seconds + 1;
    lblTime.Text = seconds.ToString();
}
""", language="csharp")

    st.subheader("ProgressBar – Quiz")
    st.code("""
progressBar1.Value = progressBar1.Value + 10;
""", language="csharp")

# ---------------- MENUS ----------------
elif menu == "Menus & Dialog Boxes":
    st.header("4. Menus & Dialog Boxes")

    st.subheader("MenuStrip – Notepad")
    st.write("File → New | Open | Save | Exit")

    st.subheader("Open File Dialog")
    st.code("""
OpenFileDialog dlg = new OpenFileDialog();
dlg.ShowDialog();
""", language="csharp")

# ---------------- LAB 3 ----------------
elif menu == "Lab-3: Calculator":
    st.header("Lab-3: Calculator")

    st.subheader("Aim")
    st.write("To create a simple calculator using Windows Forms")

    st.subheader("Steps")
    st.markdown("""
    1. Create Windows Forms Application
    2. Add two TextBoxes
    3. Add Add/Subtract buttons
    4. Write Button Click code
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
    st.write("Calculator adds numbers correctly")

# ---------------- LAB 4 ----------------
elif menu == "Lab-4: Drawing App":
    st.header("Lab-4: Drawing App (Paint)")

    st.subheader("Aim")
    st.write("To draw using mouse events")

    st.subheader("Steps")
    st.markdown("""
    1. Create Windows Form
    2. Use MouseMove event
    3. Draw using Graphics class
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
    st.write("User can draw freely on the form")
