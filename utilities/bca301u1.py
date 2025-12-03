import streamlit as st

st.set_page_config(page_title="Unit 1 - .NET & OOP", layout="wide")

st.title("Unit 1: .NET and Object-Oriented Programming")


menu = st.sidebar.radio("Navigate", [
    "Introduction to .NET",
    ".NET 6/7 Overview",
    "CLR, MSIL, Assemblies & Metadata",
    "Garbage Collection",
    "C# vs VB.NET",
    "Advanced OOPS",
    "Delegates, Events, Lambda",
    "Multithreading & Async Programming",
    "Exercises & Activities"
])

# -----------------------------------------------------------
# SECTION 1 — INTRODUCTION TO .NET
# -----------------------------------------------------------
if menu == "Introduction to .NET":
    st.header("Introduction to .NET Framework")
    st.write("""
    .NET is a software development platform created by Microsoft.  
    It supports multiple programming languages such as C#, VB.NET, and F# and is used to build:
    - Desktop applications  
    - Web applications  
    - Mobile applications  
    - Cloud and IoT applications  
    - AI/ML workloads  
    """)

    st.subheader(".NET Versions Evolution")
    st.markdown("""
    - **.NET Framework** – Windows-only, traditional  
    - **.NET Core** – Cross-platform & open-source  
    - **.NET 5/6/7/8** – Unified modern .NET  
    """)

    st.code("""
.NET Framework → Windows only  
.NET Core → Cross-platform  
.NET 6/7 → Unified platform  
    """)

# -----------------------------------------------------------
# SECTION 2 — .NET 6/7
# -----------------------------------------------------------
elif menu == ".NET 6/7 Overview":
    st.header(".NET 6/7 Overview")

    st.write("""
    **.NET 6 and .NET 7** are part of the new unified .NET platform which combines the best of
    .NET Framework, .NET Core, and Xamarin.

    ### Key Features:
    - Cross-platform
    - Improved performance
    - Minimal APIs
    - Cloud-native development
    - Hot Reload
    - Improved runtime and JIT
    """)

    st.subheader("Why .NET 6/7?")
    st.write("""
    - Faster than previous .NET versions  
    - Better memory optimization  
    - Reduced boilerplate code  
    - Support for Web, Mobile, Desktop, IoT, and Cloud  
    """)

# -----------------------------------------------------------
# SECTION 3 — CLR, MSIL, Assemblies, Metadata
# -----------------------------------------------------------
elif menu == "CLR, MSIL, Assemblies & Metadata":
    st.header("CLR, MSIL, Assemblies & Metadata")

    st.subheader("✔️ Common Language Runtime (CLR)")
    st.write("""
    CLR is the heart of .NET. It manages:
    - Memory Management  
    - Exception Handling  
    - Debugging  
    - Security  
    - Code Execution  
    """)

    st.subheader("✔️ MSIL (Microsoft Intermediate Language)")
    st.write("""
    After compilation, C#/VB.NET code is converted into **MSIL**, which is then converted by JIT compiler into native code.
    """)

    st.subheader("✔️ Assemblies")
    st.write("""
    Assemblies are the building blocks of .NET applications.
    - `.exe` or `.dll`  
    - Contains MSIL, Metadata, and Manifest  
    """)

    st.subheader("✔️ Metadata")
    st.write("""
    Metadata describes all types:
    - Classes  
    - Methods  
    - Properties  
    - Attributes  
    """)

# -----------------------------------------------------------
# SECTION 4 — Garbage Collection
# -----------------------------------------------------------
elif menu == "Garbage Collection":
    st.header("Garbage Collection in .NET")

    st.write("""
    Garbage Collector (GC) manages memory automatically:
    
    ### Responsibilities:
    - Freeing unused objects  
    - Preventing memory leaks  
    - Compacting memory  

    ### Generations:
    - **Generation 0** – Short-lived objects  
    - **Generation 1** – Medium-lived objects  
    - **Generation 2** – Long-lived objects  
    """)

# -----------------------------------------------------------
# SECTION 5 — C# vs VB.NET
# -----------------------------------------------------------
elif menu == "C# vs VB.NET":
    st.header("C# vs VB.NET – Key Differences")

    st.write("""
| Feature | C# | VB.NET |
|--------|-----|--------|
| Syntax | C-style braces {} | English-like |
| Case Sensitivity | Yes | No |
| Events | Manual wiring | Automatic |
| Popularity | Very High | Moderate |
    """)

    st.subheader("C# Example")
    st.code("""
int x = 10;
Console.WriteLine(x);
    """, language="csharp")

    st.subheader("VB.NET Example")
    st.code("""
Dim x As Integer = 10
Console.WriteLine(x)
    """, language="vbnet")

# -----------------------------------------------------------
# SECTION 6 — ADVANCED OOPS
# -----------------------------------------------------------
elif menu == "Advanced OOPS":
    st.header("Advanced Object-Oriented Concepts in C# & VB.NET")

    st.subheader("✔️ Encapsulation")
    st.write("Hiding internal details using properties.")

    st.code("""
class Student {
    private int age;
    public int Age {
        get { return age; }
        set { age = value; }
    }
}
    """, language="csharp")

    st.code("""
Class Student
    Private age As Integer
    Public Property Age() As Integer
End Class
    """, language="vbnet")

    st.subheader("✔️ Inheritance")
    st.code("""
class A {}
class B : A {}
    """, language="csharp")

    st.code("""
Class A
End Class

Class B
    Inherits A
End Class
    """, language="vbnet")

    st.subheader("✔️ Polymorphism")
    st.code("""
public virtual void Show(){}
public override void Show(){}
    """, language="csharp")

    st.code("""
Public Overridable Sub Show()
End Sub

Public Overrides Sub Show()
End Sub
    """, language="vbnet")

# -----------------------------------------------------------
# SECTION 7 — Delegates, Events, Lambda
# -----------------------------------------------------------
elif menu == "Delegates, Events, Lambda":
    st.header("Delegates, Events, Lambda Expressions")

    st.subheader("✔️ Delegates")
    st.write("A delegate is a type-safe function pointer.")

    st.code("""
public delegate void MyDelegate(string msg);
    """, language="csharp")

    st.code("""
Public Delegate Sub MyDelegate(msg As String)
    """, language="vbnet")

    st.subheader("✔️ Events")
    st.code("""
public event MyDelegate ProcessCompleted;
    """, language="csharp")

    st.code("""
Public Event ProcessCompleted As MyDelegate
    """, language="vbnet")

    st.subheader("✔️ Lambda Expressions")
    st.code("""
var add = (a, b) => a + b;
    """, language="csharp")

    st.code("""
Dim add = Function(a, b) a + b
    """, language="vbnet")

# -----------------------------------------------------------
# SECTION 8 — Multithreading & Async Programming
# -----------------------------------------------------------
elif menu == "Multithreading & Async Programming":
    st.header("Working with Threads and Asynchronous Programming")

    st.subheader("✔️ Multithreading Example")
    st.code("""
Thread t = new Thread(() => Console.WriteLine("Thread!"));
t.Start();
    """, language="csharp")

    st.code("""
Dim t As New Thread(Sub() Console.WriteLine("Thread!"))
t.Start()
    """, language="vbnet")

    st.subheader("✔️ Async–await Example")
    st.code("""
async Task Download()
{
    await Task.Delay(1000);
}
    """, language="csharp")

    st.code("""
Async Function Download() As Task
    Await Task.Delay(1000)
End Function
    """, language="vbnet")

# -----------------------------------------------------------
# SECTION 9 — Exercises & Activities
# -----------------------------------------------------------
elif menu == "Exercises & Activities":

    st.header("Exercises & Activities")

    st.subheader("📝 PART A — Short Exercises")
    st.write("""
1. Explain MSIL with an example.  
2. Write Encapsulation example in C# and VB.NET.  
3. What is the role of CLR?  
4. Write a delegate program.  
5. Explain memory generations in Garbage Collection.  
    """)

    st.subheader("💻 PART B — Coding Tasks")
    st.write("""
### Task 1  
Write a class `Employee` with properties and display data.

### Task 2  
Implement inheritance: Shape → Circle → Rectangle.

### Task 3  
Create a multithreading program to print numbers 1–10.

### Task 4  
Create an event `OnProcessCompleted` and trigger it.
    """)

    st.subheader("🎮 PART C — Classroom Activities")
    st.write("""
### Activity 1 – MSIL Demo  
Teacher shows ILDASM output for student code.

### Activity 2 – OOPS Race Game  
Teams explain and act Encapsulation, Inheritance, Polymorphism.

### Activity 3 – Delegate Chain  
Students simulate event propagation.

### Activity 4 – Thread Simulation  
Volunteers act as parallel threads.

### Activity 5 – Async Simulation  
Students hold cards: Await, Task, Async.
    """)

    st.subheader("📘 Mini Project Ideas")
    st.write("""
- Student Information System using OOPS  
- Async-based File Downloader  
- Threaded number generator  
- Event-driven notification system  
    """)

