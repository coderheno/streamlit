import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Windows Applications & Event-Driven Programming",
    layout="wide"
)

st.title("🪟 Windows Applications & Event-Driven Programming")
st.caption("Practical-Based Learning (Quiz, Calculator, Paint, Notepad)")

# ---------- SIDEBAR (CREATE ONCE) ----------
if "menu" not in st.session_state:
    st.session_state.menu = "Introduction"

st.sidebar.header("📘 Topics")

st.session_state.menu = st.sidebar.radio(
    "Select Topic",
    (
        "Introduction",
        "Common Controls",
        "Timer & ProgressBar",
        "Menus & Dialog Boxes",
        "Lab-3: Calculator",
        "Lab-4: Drawing App"
    ),
    key="main_sidebar_radio"   # ✅ UNIQUE & SAFE
)

menu = st.session_state.menu

# ---------- CONTENT ----------
if menu == "Introduction":
    st.header("1️⃣ Event-Driven Programming")
    st.markdown("""
    **Event-Driven Programming** means:
    - Program waits for user action
    - Executes code only when an event occurs

    **Examples**
    - Calculator → Button Click
    - Stopwatch → Timer Tick
    - Paint → Mouse Move
    """)

elif menu == "Common Controls":
    st.header("2️⃣ Common Controls")
    st.subheader("Button – Calculator")
    st.code("""
private void btnAdd_Click(object sender, EventArgs e)
{
    int a = int.Parse(txtA.Text);
    int b = int.Parse(txtB.Text);
    lblResult.Text = (a + b).ToString();
}
""", language="csharp")

elif menu == "Timer & ProgressBar":
    st.header("3️⃣ Timer & ProgressBar")
    st.subheader("Stopwatch Timer")
    st.code("""
private void timer1_Tick(object sender, EventArgs e)
{
    seconds++;
    lblTime.Text = seconds.ToString();
}
""", language="csharp")

elif menu == "Menus & Dialog Boxes":
    st.header("4️⃣ Menus & Dialog Boxes")
    st.markdown("""
    **Notepad Example**
    - MenuStrip → File, Edit
    - OpenFileDialog
    - SaveFileDialog
    """)

elif menu == "Lab-3: Calculator":
    st.header("🧪 Lab-3: Calculator")

    st.subheader("Aim")
    st.write("To create a Windows Forms Calculator using VB.NET / C#")

    st.subheader("Steps")
    st.markdown("""
    1. Create Windows Forms Application
    2. Add TextBoxes for input
    3. Add Buttons for operations
    4. Write Click Events
    """)

    st.subheader("Sample Code (VB.NET)")
    st.code("""
Private Sub btnAdd_Click(sender As Object, e As EventArgs)
    Dim a As Integer = Val(TextBox1.Text)
    Dim b As Integer = Val(TextBox2.Text)
    Label1.Text = a + b
End Sub
""", language="vbnet")

elif menu == "Lab-4: Drawing App":
    st.header("🧪 Lab-4: Drawing App (Paint)")

    st.subheader("Aim")
    st.write("To create a simple Paint application using Mouse Events")

    st.subheader("Sample Code (C#)")
    st.code("""
private void Form1_MouseMove(object sender, MouseEventArgs e)
{
    if (e.Button == MouseButtons.Left)
    {
        Graphics g = this.CreateGraphics();
        g.FillEllipse(Brushes.Black, e.X, e.Y, 3, 3);
    }
}
""", language="csharp")
