import streamlit as st

st.set_page_config(page_title="From Mess to Smart Data", layout="wide")

st.title("📘 Normalization, File Organization & Indexing")
st.subheader("Interactive Teaching Module with MySQL Examples")

menu = st.sidebar.radio("Select Topic", [
    "Introduction",
    "Unnormalized to 1NF",
    "2NF",
    "3NF & BCNF",
    "4NF & 5NF",
    "Functional Dependency & Minimal Cover",
    "File Organization",
    "Indexing & B+ Tree",
    "Nulls & Dangling Tuples",
    "Mini Project Tasks",
    "Normalization Table Examples",
    "Anomalies"
])

# ---------------- INTRO ----------------
if menu == "Introduction":
    st.header("Why Normalization?")
    st.write("""
Normalization is **data hygiene**. Without it, databases suffer from:
- Insertion Anomalies - Insertion anomaly occurs when you cannot add new data into a database table without adding unnecessary or unrelated data.
- Update Anomalies - Update anomaly occurs when the same data appears in multiple rows, and updating it in one row but not in others causes data inconsistency.
- Deletion Anomalies - Deletion anomaly occurs when deleting one record unintentionally removes other important related data from the database.
""")

# ---------------- UNNORMALIZED TO 1NF ----------------
elif menu == "Unnormalized to 1NF":
    st.header("Unnormalized Table → 1NF")
    st.dataframe({
        "RegNo": [101, 102],
        "Name": ["Ravi", "Anu"],
        "Subjects": ["DBMS, OS", "DBMS"],
        "Faculty": ["Kumar, Rao", "Kumar"],
        "Phone": [9876, 9123]
    })

    st.subheader("Problems → Anomalies")
    st.write("Insertion, Update, and Deletion Anomalies occur.")

    st.subheader("1NF Rule → No Multi-Valued Attributes which also means all attributes must contain atomic (single) values; no multi-valued attributes are allowed.")
    st.code("""
CREATE TABLE Student_1NF (
    RegNo INT,
    Name VARCHAR(50),
    Subject VARCHAR(50),
    Faculty VARCHAR(50),
    Phone VARCHAR(15)
);
""")

# ---------------- 2NF ----------------
elif menu == "2NF":
    st.header("Second Normal Form (2NF)")
    st.write("Removes **partial dependency**, 2NF removes partial dependency by ensuring that every non-key attribute is fully dependent on the entire primary key, not just a part of it.")

    st.code("""
CREATE TABLE Student (
    RegNo INT PRIMARY KEY,
    Name VARCHAR(50),
    Phone VARCHAR(15)
);

CREATE TABLE SubjectFaculty (
    Subject VARCHAR(50) PRIMARY KEY,
    Faculty VARCHAR(50)
);

CREATE TABLE StudentSubject (
    RegNo INT,
    Subject VARCHAR(50),
    PRIMARY KEY (RegNo, Subject)
);
""")

# ---------------- 3NF & BCNF ----------------
elif menu == "3NF & BCNF":
    st.header("Third Normal Form (3NF)")
    st.write("""
3NF removes **transitive dependency**. A transitive dependency exists when:
A → B and B → C, meaning A indirectly determines C.

### Real-Time Meaning:
If RegNo determines Phone and Phone determines Network Provider, then RegNo indirectly determines Network.
This is not allowed in 3NF.
""")

    st.subheader("❌ Before 3NF (Transitive Dependency Example)")
    st.dataframe({
        "RegNo": [101, 102],
        "StudentName": ["Ravi", "Anu"],
        "Phone": [9876, 9123],
        "Network": ["Jio", "Airtel"]
    })

    st.subheader("✅ After 3NF (Correct Design)")
    st.code("""
CREATE TABLE Student (
    RegNo INT PRIMARY KEY,
    StudentName VARCHAR(50),
    Phone VARCHAR(15)
);

CREATE TABLE PhoneNetwork (
    Phone VARCHAR(15) PRIMARY KEY,
    Provider VARCHAR(50)
);
""")

    st.subheader("BCNF (Boyce-Codd Normal Form)")
    st.write("""
BCNF is a stronger version of 3NF where every determinant must be a candidate key.
Used in Banking, Finance & Transaction systems.
""")
    st.header("Third Normal Form (3NF)")
    st.write("3NF removes **transitive dependency**.")

    st.subheader("Example Before 3NF")
    st.dataframe({
        "RegNo": [101, 102],
        "Phone": [9876, 9123],
        "Network": ["Jio", "Airtel"]
    })

    st.subheader("Split Tables After 3NF")
    st.code("""
CREATE TABLE Student (
    RegNo INT PRIMARY KEY,
    Phone VARCHAR(15)
);

CREATE TABLE PhoneNetwork (
    Phone VARCHAR(15) PRIMARY KEY,
    Provider VARCHAR(50)
);
""")

    st.subheader("BCNF")
    st.write("Every determinant must be a candidate key. Stronger than 3NF.")

# ---------------- 4NF & 5NF ----------------
elif menu == "4NF & 5NF":
    st.header("Fourth Normal Form (4NF)")
    st.write("Removes multi-valued dependency (independent multiple values).")

    st.subheader("❌ Before 4NF")
    st.dataframe({
        "Student": ["Ravi", "Ravi"],
        "Hobby": ["Chess", "Cricket"],
        "Language": ["English", "Tamil"]
    })

    st.subheader("✅ After 4NF")
    st.code("""
CREATE TABLE StudentHobby (Student VARCHAR(50), Hobby VARCHAR(50));
CREATE TABLE StudentLanguage (Student VARCHAR(50), Language VARCHAR(50));
""")

    st.subheader("5NF (Fifth Normal Form)")
    st.write("Handles join dependency. Used in research & data warehouse systems.")
    st.header("Fourth Normal Form (4NF)")
    st.write("Removes **multi-valued dependency**.")

    st.dataframe({
        "Student": ["Ravi", "Ravi"],
        "Hobby": ["Chess", "Cricket"],
        "Language": ["English", "Tamil"]
    })

    st.subheader("Split into 4NF")
    st.code("""
CREATE TABLE StudentHobby (Student VARCHAR(50), Hobby VARCHAR(50));
CREATE TABLE StudentLanguage (Student VARCHAR(50), Language VARCHAR(50));
""")

    st.subheader("Fifth Normal Form (5NF)")
    st.write("Handles **join dependencies**. Used in high-end data warehousing.")

# ---------------- FUNCTIONAL DEPENDENCY ----------------
elif menu == "Functional Dependency & Minimal Cover":
    st.header("Functional Dependency (FD)")
    st.write("If attribute A uniquely determines B, it is written as A → B.")

    st.subheader("Examples")
    st.write("RegNo → StudentName")
    st.write("AccountNo → Balance")

    st.subheader("Minimal Cover")
    st.write("Minimal Cover is the smallest set of functional dependencies with no redundancy.")
    st.write("Example: A → BC, B → C, A → B  ⇒ Redundant rule: B → C")
    st.header("Functional Dependency (FD)")
    st.write("If A determines B → A → B.")

    st.subheader("Examples")
    st.write("RegNo → Name, Phone")
    st.write("Subject → Faculty")

    st.subheader("Minimal Cover")
    st.write("Smallest dependency set preserving full meaning.")
    st.write("Example: A → BC, B → C, A → B ⇒ redundant: B → C")

# ---------------- FILE ORGANIZATION ----------------
elif menu == "File Organization":
    st.header("File Organization")
    st.write("File organization explains how records are stored physically in memory.")

    st.markdown("""
- Heap File → Random Storage
- Sequential File → Ordered Storage
- Indexed File → Fast Search
- Hashed File → Direct Access
""")

    st.subheader("Physical Storage Structure")
    st.code("Database → Files → Blocks → Records → Fields")
    st.header("File Organization Methods")
    st.markdown("""
- **Heap File:** Random storage
- **Sequential File:** Stored in sorted order
- **Indexed File:** Uses index for fast search
- **Hashed File:** Uses hashing for direct access
""")

    st.subheader("Physical Storage Structure")
    st.code("Database → Files → Blocks → Records → Fields")

# ---------------- INDEXING & B+ TREE ----------------
elif menu == "Indexing & B+ Tree":
    st.header("Indexing")
    st.write("Indexing improves search speed by allowing direct access to rows.")

    st.subheader("Ordered Index")
    st.write("Values stored in sorted order for fast range queries.")

    st.subheader("B+ Tree Index")
    st.write("B+ Tree is a balanced index structure used in all major databases.")

    st.code("""
CREATE INDEX idx_regno ON Student(RegNo);
""")
    st.header("Indexing")
    st.write("Improves search speed.")

    st.subheader("Ordered Index")
    st.write("Values stored in sorted form.")

    st.subheader("B+ Tree Index")
    st.write("Balanced structure used in MySQL, Oracle.")

    st.code("""
CREATE INDEX idx_regno ON Student(RegNo);
""")

# ---------------- NULLS & DANGLING TUPLES ----------------
elif menu == "Nulls & Dangling Tuples":
    st.header("Nulls & Dangling Tuples")

    st.subheader("NULL")
    st.write("NULL represents missing or unknown value.")

    st.subheader("Dangling Tuple")
    st.write("Occurs when a child record exists without a parent record.")

    st.code("""
DELETE FROM Student WHERE RegNo = 101;
-- If Marks table still contains 101 → Dangling Tuple
""")
    st.header("Nulls & Dangling Tuples")

    st.subheader("NULL")
    st.write("Represents missing or unknown value.")

    st.subheader("Dangling Tuple Example")
    st.code("""
DELETE FROM Student WHERE RegNo = 101;
-- If Marks table still has 101 → Dangling Tuple
""")

# ---------------- MINI PROJECT ----------------
elif menu == "Mini Project Tasks":
    st.header("Mini Project Tasks")
    st.markdown("""
Choose Any One Domain:
- College Management System
- Hospital Management System
- E-Commerce System

Student Tasks:
1. Identify Functional Dependencies
2. Normalize tables from 1NF → 3NF
3. Create MySQL Tables
4. Insert at least 10 sample records
5. Create one index
6. Write 5 SELECT queries
""")
    st.header("Mini Project Tasks")
    st.markdown("""
### Choose Any Domain:
- College Management System
- Hospital Management System
- E-Commerce System

### Student Tasks:
1. Identify Functional Dependencies
2. Normalize tables up to 3NF
3. Create all tables in MySQL
4. Insert sample data
5. Create at least one index
6. Retrieve data using SELECT
""")

# ---------------- NORMALIZATION TABLE EXAMPLES ----------------
elif menu == "Normalization Table Examples":
    st.header("Normalization Table Examples")

    tab1, tab2, tab3 = st.tabs(["1NF", "2NF", "3NF"])

    with tab1:
        st.write("1NF removes multi-valued attributes.")
        st.dataframe({"RegNo": [101, 101], "Name": ["Ravi", "Ravi"], "Subject": ["DBMS", "OS"]})

    with tab2:
        st.write("2NF removes partial dependency.")
        st.dataframe({"RegNo": [101, 102], "Name": ["Ravi", "Anu"]})

    with tab3:
        st.write("3NF removes transitive dependency.")
        st.dataframe({"RegNo": [101, 102], "Phone": [9876, 9123]})
    st.header("Normalization Table Examples")

    tab1, tab2, tab3 = st.tabs(["1NF", "2NF", "3NF"])

    with tab1:
        st.write("1NF removes multi-valued attributes.")
        st.dataframe({"RegNo": [101, 101], "Name": ["Ravi", "Ravi"], "Subject": ["DBMS", "OS"]})

    with tab2:
        st.write("2NF removes partial dependency.")
        st.dataframe({"RegNo": [101, 102], "Name": ["Ravi", "Anu"]})

    with tab3:
        st.write("3NF removes transitive dependency.")
        st.dataframe({"RegNo": [101, 102], "Phone": [9876, 9123]})

# ---------------- ANOMALIES ----------------
elif menu == "Anomalies":
    st.header("Database Anomalies")

    tab1, tab2, tab3 = st.tabs(["Insertion Anomaly", "Update Anomaly", "Deletion Anomaly"])

    with tab1:
        st.subheader("Insertion Anomaly")
        st.write("Cannot insert new data without inserting unnecessary data.")
        st.dataframe({"RegNo": [101], "Name": ["Ravi"], "Subject": ["DBMS"]})

    with tab2:
        st.subheader("Update Anomaly")
        st.write("Updating data in one row but not others causes inconsistency.")
        st.dataframe({"RegNo": [101, 102], "Faculty": ["Kumar", "Kumar"], "Phone": [9999, 9876]})

    with tab3:
        st.subheader("Deletion Anomaly")
        st.write("Deleting a record removes important related data.")
        st.dataframe({"RegNo": [101], "Name": ["Ravi"], "Faculty": ["Kumar"]})
