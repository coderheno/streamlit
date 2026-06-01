import streamlit as st

st.set_page_config(page_title="Windows Applications & Event Programming", layout="wide")

st.title("🪟 WINDOWS APPLICATIONS & EVENT-DRIVEN PROGRAMMING")
st.subheader("Interactive Learning Resource (VB.NET & C#)")
st.divider()

menu = st.sidebar.selectbox("Select Topic", [
    "Introduction",
    "Windows Forms in VB.NET & C#",
    "Event Handling",
    "Common Controls",
    "ListView",
    "TreeView",
    "ProgressBar",
    "Timer & Error Logs",
    "Custom Controls",
    "Menus, Toolbars & Dialogs",
    "VB.NET & C# Interoperability",
    "LAB 3: Calculator",
    "LAB 4: Drawing App"
])

# ------------------ INTRODUCTION ------------------
if menu == "Introduction":
    st.header("📘 Windows Applications & Event-Driven Programming")
    st.write("""
Windows Applications are GUI-based desktop programs developed using .NET technologies.
Event-driven programming means the program executes code based on user actions like:
- Button Click
- Mouse Move
- Timer Tick
- Keyboard Input
""")

# ------------------ WINDOWS FORMS ------------------
elif menu == "Windows Forms in VB.NET & C#":
    st.header("🧩 Windows Forms Development")
    st.write("""
Windows Forms is a .NET framework for building GUI applications using:
- VB.NET
- C#
It supports drag-and-drop UI design using Visual Studio.
""")

# ------------------ EVENT HANDLING ------------------
elif menu == "Event Handling":
    st.header("⚡ Event Handling")

    st.subheader("VB.NET Example")
    st.code("""
Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
    MessageBox.Show("Button Clicked")
End Sub
""", language="vbnet")

    st.subheader("C# Example")
    st.code("""
private void button1_Click(object sender, EventArgs e)
{
    MessageBox.Show("Button Clicked");
}
""", language="csharp")

# ------------------ COMMON CONTROLS ------------------
elif menu == "Common Controls":
    st.header("🧰 Common Controls")
    st.write("""
- Button – Executes actions
- TextBox – Input
- Label – Output
- CheckBox – Multiple selection
- RadioButton – Single selection
- PictureBox – Display images
""")

# ------------------ LISTVIEW ------------------
elif menu == "ListView":
    st.header("📋 ListView Control")

    st.subheader("VB.NET Code")
    st.code("""
ListView1.View = View.Details
ListView1.Columns.Add("ID", 80)
ListView1.Columns.Add("Name", 150)

Dim item As New ListViewItem("101")
item.SubItems.Add("Arjun")
ListView1.Items.Add(item)
""", language="vbnet")

    st.subheader("C# Code")
    st.code("""
listView1.View = View.Details;
listView1.Columns.Add("ID", 80);
listView1.Columns.Add("Name", 150);

ListViewItem i = new ListViewItem("101");
i.SubItems.Add("Arjun");
listView1.Items.Add(i);
""", language="csharp")

# ------------------ TREEVIEW ------------------
elif menu == "TreeView":
    st.header("🌳 TreeView Control")

    st.subheader("VB.NET Code")
    st.code("""
Dim root As New TreeNode("Courses")
root.Nodes.Add("BCA")
root.Nodes.Add("BSc CS")
TreeView1.Nodes.Add(root)
TreeView1.ExpandAll()
""", language="vbnet")

# ------------------ PROGRESSBAR ------------------
elif menu == "ProgressBar":
    st.header("📊 ProgressBar")

    st.code("""
ProgressBar1.Minimum = 0
ProgressBar1.Maximum = 100
ProgressBar1.Value = 50
""", language="vbnet")

# ------------------ TIMER & ERROR LOG ------------------
elif menu == "Timer & Error Logs":
    st.header("⏱ Timer & Error Logging")

    st.subheader("Timer")
    st.code("""
Private Sub Timer1_Tick(...) Handles Timer1.Tick
    Label1.Text = DateTime.Now.ToLongTimeString()
End Sub
""", language="vbnet")

    st.subheader("Error Log")
    st.code("""
Try
    Dim a = 5 / 0
Catch ex As Exception
    IO.File.AppendAllText("errorlog.txt", ex.Message)
End Try
""", language="vbnet")

# ------------------ CUSTOM CONTROLS ------------------
elif menu == "Custom Controls":
    st.header("🛠 Creating Custom Control")

    st.code("""
Public Class RoundButton
    Inherits Button

    Protected Overrides Sub OnPaint(e As PaintEventArgs)
        MyBase.OnPaint(e)
        Dim path As New Drawing2D.GraphicsPath()
        path.AddEllipse(0, 0, Width, Height)
        Me.Region = New Region(path)
    End Sub
End Class
""", language="vbnet")

# ------------------ MENUS & DIALOGS ------------------
elif menu == "Menus, Toolbars & Dialogs":
    st.header("📂 Menus, Toolbars & Dialogs")

    st.subheader("Menu Exit Example")
    st.code("""
Private Sub ExitToolStripMenuItem_Click(...) Handles ExitToolStripMenuItem.Click
    Me.Close()
End Sub
""", language="vbnet")

    st.subheader("OpenFileDialog")
    st.code("""
If OpenFileDialog1.ShowDialog() = DialogResult.OK Then
    TextBox1.Text = IO.File.ReadAllText(OpenFileDialog1.FileName)
End If
""", language="vbnet")

# ------------------ INTEROPERABILITY ------------------
elif menu == "VB.NET & C# Interoperability":
    st.header("🔄 VB.NET & C# Interoperability")

    st.subheader("C# Library")
    st.code("""
public class MathOps
{
    public int Add(int a, int b)
    {
        return a + b;
    }
}
""", language="csharp")

    st.subheader("VB.NET Usage")
    st.code("""
Dim m As New MathOps()
MsgBox(m.Add(3, 4))
""", language="vbnet")

# ------------------ LAB 3 ------------------
elif menu == "LAB 3: Calculator":
    st.header("🧮 LAB 3: Calculator")

    st.subheader("VB.NET Code")
    st.code("""
Dim num1 As Double
Dim num2 As Double
Dim op As String

Private Sub btnEquals_Click(...)
    num2 = Val(TextBox1.Text)
    Select Case op
        Case "+"
            TextBox1.Text = num1 + num2
        Case "-"
            TextBox1.Text = num1 - num2
    End Select
End Sub
""", language="vbnet")

    st.subheader("C# Code")
    st.code("""
double num1, num2;
string op;

private void btnEq_Click(object sender, EventArgs e)
{
    num2 = double.Parse(textBox1.Text);
    if(op == "+") textBox1.Text = (num1 + num2).ToString();
}
""", language="csharp")

# ------------------ LAB 4 ------------------
elif menu == "LAB 4: Drawing App":
    st.header("🎨 LAB 4: Paint Drawing App")

    st.subheader("VB.NET Drawing Code")
    st.code("""
Dim draw As Boolean = False
Dim lastPoint As Point

Private Sub PictureBox1_MouseDown(...)
    draw = True
    lastPoint = e.Location
End Sub

Private Sub PictureBox1_MouseMove(...)
    If draw Then
        Using g = Graphics.FromImage(PictureBox1.Image)
            g.DrawLine(Pens.Black, lastPoint, e.Location)
        End Using
        PictureBox1.Invalidate()
        lastPoint = e.Location
    End If
End Sub

Private Sub PictureBox1_MouseUp(...)
    draw = False
End Sub
""", language="vbnet")
