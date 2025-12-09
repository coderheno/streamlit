import streamlit as st

st.set_page_config(page_title="Software Design & Implementation", layout="wide")

st.title("📘 Software Design & Implementation")
st.subheader("Interactive Learning Module with Examples & Best Practices")

menu = st.sidebar.radio("Select Topic", [
    "Introduction",
    "UML for Object-Oriented Design",
    "Design Patterns",
    "Test Driven Development (TDD)",
    "Code Reviews & Inspections",
    "Implementation Issues",
    "Coding Standards & Best Practices",
    "Writing Clean Code",
    "Refactoring Techniques",
    "Self-Learning: Code Review Tools"
])

# ---------------- INTRO ----------------
if menu == "Introduction":
    st.header("Why Software Design Matters")
    st.write("""
Good software design helps developers build:
- Reliable systems
- Scalable applications
- Easy-to-maintain code

Poor design leads to:
- More bugs
- Difficult maintenance
- Frequent system failures

**Design happens BEFORE coding.**
""")

# ---------------- UML ----------------
elif menu == "UML for Object-Oriented Design":
    st.header("UML – Object-Oriented Design with Diagrams")

    st.subheader("1. Class Diagram")
    st.write("Shows classes, attributes, methods and relationships.")

    st.code("""
+------------------+
|   Student        |
+------------------+
| regNo            |
| name             |
+------------------+
| enroll()         |
| viewMarks()      |
+------------------+
""")

    st.subheader("2. Use Case Diagram")
    st.write("Shows what actions users can perform.")
    st.write("Example: Student can Login, Enroll Course, View Results")

    st.subheader("3. Sequence Diagram")
    st.write("Shows interaction between objects step by step.")
    st.write("User → Login Page → Database → Dashboard")

    st.subheader("4. Activity Diagram")
    st.write("Represents workflow of a process.")
    st.write("Login → Validate → Success → Dashboard")

# ---------------- DESIGN PATTERNS ----------------
elif menu == "Design Patterns":
    st.header("Design Patterns")

    st.subheader("1. Singleton Pattern")
    st.write("Ensures only one instance of a class exists.")
    st.write("Real use: Database connection, Logger")

    st.code("""
public class Logger {
    private static Logger instance;
    private Logger() {}
    public static Logger Instance {
        get {
            if(instance == null)
                instance = new Logger();
            return instance;
        }
    }
}
""")

    st.subheader("2. Factory Pattern")
    st.write("Creates objects without exposing creation logic.")
    st.write("Real use: Payment gateway (UPI, Card, Wallet)")

    st.subheader("3. Observer Pattern")
    st.write("One-to-many dependency. Used in notifications.")
    st.write("Example: WhatsApp message alerts, Stock price updates")

# ---------------- TDD ----------------
elif menu == "Test Driven Development (TDD)":
    st.header("Test Driven Development (TDD)")
    st.write("Write tests first, then write code.")

    st.subheader("TDD Cycle")
    st.write("Red → Green → Refactor")

    st.code("""
[Test]
public void Add_Test() {
    Assert.AreEqual(5, Add(2,3));
}
""")

# ---------------- CODE REVIEWS ----------------
elif menu == "Code Reviews & Inspections":
    st.header("Code Reviews & Inspections")

    st.write("Developers review each other's code before merging.")

    st.subheader("What to Check")
    st.markdown("""
- Code correctness
- Naming conventions
- Logic errors
- Security issues
- Performance
""")

# ---------------- IMPLEMENTATION ISSUES ----------------
elif menu == "Implementation Issues":
    st.header("Common Implementation Issues")

    st.markdown("""
- Hardcoded values
- Poor variable naming
- No exception handling
- Code duplication
- Performance problems
""")

    st.subheader("Solution")
    st.write("Use constants, modular functions, and error handling.")

# ---------------- CODING STANDARDS ----------------
elif menu == "Coding Standards & Best Practices":
    st.header("Coding Standards & Best Practices")

    st.markdown("""
- Class names → PascalCase
- Variable names → camelCase
- Constants → UPPER_CASE
- One function = One task
""")

# ---------------- CLEAN CODE ----------------
elif menu == "Writing Clean Code":
    st.header("Writing Clean Code")

    st.subheader("Bad Code")
    st.code("x = 10; if(x==10){print('ok')} ")

    st.subheader("Clean Code")
    st.code("""
const int MAX_RETRY = 10;
if(retryCount == MAX_RETRY) {
    Console.WriteLine("Retry limit reached");
}
""")

# ---------------- REFACTORING ----------------
elif menu == "Refactoring Techniques":
    st.header("Refactoring Techniques")

    st.write("Improving code structure without changing behavior.")

    st.subheader("Before Refactoring")
    st.code("""
if(a>0){
 if(b>0){
  if(c>0){
   // logic
  }
 }
}
""")

    st.subheader("After Refactoring")
    st.code("""
if(isValid(a,b,c)){
 // logic
}
""")

# ---------------- CODE REVIEW TOOLS ----------------
elif menu == "Self-Learning: Code Review Tools":
    st.header("Self-Learning: Code Review Tools")

    st.markdown("""
- GitHub
- GitLab
- Bitbucket
- SonarQube
- Review Board
""")

st.sidebar.success("Use this app for learning Software Engineering in an interactive way.")
