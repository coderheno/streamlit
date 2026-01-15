import streamlit as st

st.set_page_config(
    page_title="File Handling, Security & Deployment",
    layout="wide"
)

st.title("📘 File Handling, Security & Deployment")
st.caption("Windows Forms | C# & VB.NET | Lab-Oriented Notes")

tabs = st.tabs([
    "📂 File Handling",
    "📝 Text & Binary Files",
    "🔁 Streams",
    "🔐 Security",
    "🚀 Deployment",
    "🧪 Lab Programs",
    "🎤 Viva Points"
])

# ---------------- TAB 1 ----------------
with tabs[0]:
    st.header("File Handling using System.IO")

    st.write("""
    File handling allows applications to create, read, write, update, 
    and delete files stored on disk.
    """)

    st.subheader("System.IO Namespace – Important Classes")
    st.table({
        "Class": [
            "File", "FileInfo", "Directory",
            "StreamReader", "StreamWriter",
            "BinaryReader", "BinaryWriter"
        ],
        "Purpose": [
            "Basic file operations",
            "Detailed file information",
            "Folder operations",
            "Read text files",
            "Write text files",
            "Read binary data",
            "Write binary data"
        ]
    })

    st.subheader("Create & Write File")
    st.code("""
File.WriteAllText("sample.txt", "Welcome to File Handling");
""", language="csharp")

    st.code("""
My.Computer.FileSystem.WriteAllText("sample.txt",
    "Welcome to File Handling", False)
""", language="vbnet")

# ---------------- TAB 2 ----------------
with tabs[1]:
    st.header("Reading & Writing Text and Binary Files")

    st.subheader("Reading a Text File")
    st.code("""
string content = File.ReadAllText("sample.txt");
""", language="csharp")

    st.code("""
Dim content As String =
    My.Computer.FileSystem.ReadAllText("sample.txt")
""", language="vbnet")

    st.subheader("Binary File – Write")
    st.code("""
BinaryWriter bw = new BinaryWriter(
    File.Open("data.bin", FileMode.Create));
bw.Write(100);
bw.Write("Secure Data");
bw.Close();
""", language="csharp")

    st.subheader("Binary File – Read")
    st.code("""
BinaryReader br = new BinaryReader(
    File.Open("data.bin", FileMode.Open));
int num = br.ReadInt32();
string text = br.ReadString();
br.Close();
""", language="csharp")

# ---------------- TAB 3 ----------------
with tabs[2]:
    st.header("Stream Readers, Writers & Buffered Streams")

    st.subheader("StreamReader Example")
    st.code("""
StreamReader sr = new StreamReader("data.txt");
string line = sr.ReadLine();
sr.Close();
""", language="csharp")

    st.subheader("StreamWriter Example")
    st.code("""
StreamWriter sw = new StreamWriter("data.txt");
sw.WriteLine("Hello World");
sw.Close();
""", language="csharp")

    st.subheader("BufferedStream Example")
    st.code("""
FileStream fs = new FileStream("data.bin", FileMode.Create);
BufferedStream bs = new BufferedStream(fs);
""", language="csharp")

# ---------------- TAB 4 ----------------
with tabs[3]:
    st.header("Secure Coding Practices in C#.NET")

    st.markdown("""
    **Why Secure Coding?**
    - Prevent unauthorized access
    - Protect sensitive data
    - Avoid crashes and vulnerabilities
    """)

    st.subheader("Best Practices")
    st.markdown("""
    ✔ Validate user input  
    ✔ Avoid hard-coded passwords  
    ✔ Use encryption  
    ✔ Proper exception handling  
    ✔ Follow least privilege principle  
    """)

    st.subheader("Try–Catch Example")
    st.code("""
try
{
    File.ReadAllText(path);
}
catch (Exception ex)
{
    MessageBox.Show("Error occurred");
}
""", language="csharp")

# ---------------- TAB 5 ----------------
with tabs[4]:
    st.header("Deploying Windows Forms Applications")

    st.subheader("What is Deployment?")
    st.write("""
    Deployment is the process of packaging and distributing
    an application so it can run on another system.
    """)

    st.subheader("Deployment Methods")
    st.markdown("""
    - Setup Project (MSI)
    - ClickOnce Deployment
    - Manual EXE distribution
    """)

    st.subheader("Deployment Steps")
    st.markdown("""
    1. Build the project  
    2. Create setup / installer  
    3. Include required DLLs  
    4. Test installation  
    5. Deploy to users  
    """)

# ---------------- TAB 6 ----------------
with tabs[5]:
    st.header("Lab Programs")

    st.subheader("🧪 Lab 7: Text Editor (Notepad++ like)")
    st.markdown("""
    **Objective:**  
    Create a Windows Forms Text Editor with file operations.

    **Features:**
    - New
    - Open
    - Save
    - Save As
    - Exit

    **Concepts Used:**
    - OpenFileDialog
    - SaveFileDialog
    - StreamReader
    - StreamWriter
    - MenuStrip
    """)

    st.divider()

    st.subheader("🧪 Lab 8: Secure File Encryption & Decryption Utility")
    st.markdown("""
    **Objective:**  
    Develop a utility to encrypt and decrypt files securely.

    **Features:**
    - File selection
    - Password-based encryption
    - Encrypt / Decrypt options
    - Error handling

    **Concepts Used:**
    - FileStream
    - Cryptography classes
    - Secure coding
    - Exception handling
    """)

# ---------------- TAB 7 ----------------
with tabs[6]:
    st.header("Viva & Exam Preparation")

    st.markdown("""
    **Important Viva Questions:**
    - Difference between text and binary files
    - StreamReader vs File.ReadAllText
    - Why encryption is required?
    - What is BufferedStream?
    - Steps for application deployment
    """)

    st.success("✔ Complete all lab evaluations before the ESE-II Lab Exam")

st.caption("Prepared for Lab Exams & Practical Learning | Streamlit-based ICT Tool")
