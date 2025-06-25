import streamlit as st

st.set_page_config(page_title="Conditional & Looping Demos", layout="wide")

# — Demo Functions —

def employee_promotion():
    st.header("🧑‍💼 Employee Promotion Eligibility Checker")
    name = st.text_input("Employee Name", key="emp_name")
    exp = st.number_input("Years of Experience", min_value=0.0, step=0.1, key="emp_exp")
    rating = st.slider("Performance Rating (1-5)", 1, 5, key="emp_rating")
    if st.button("Check Promotion Eligibility", key="btn_emp"):
        if exp >= 5 and rating >= 4:
            st.success(f"{name} is eligible for promotion! 🎉")
        else:
            st.warning(f"{name} is not eligible for promotion.")


def student_promotion():
    st.header("🎓 Student Promotion Checker")
    name = st.text_input("Student Name", key="stu_name")
    subjects = ["Maths", "Science", "English", "Computer"]
    marks = {}
    for subj in subjects:
        marks[subj] = st.number_input(f"Marks in {subj}", 0, 100, step=1, key=subj)
    if st.button("Check Student Promotion", key="btn_stu"):
        if all(m >= 35 for m in marks.values()):
            st.success(f"{name} is promoted to the next year! 🎉")
        else:
            failed = [s for s, m in marks.items() if m < 35]
            st.error(f"{name} failed in: {', '.join(failed)}. Not promoted.")


def electricity_bill():
    st.header("💡 Electricity Bill Calculator")
    units = st.number_input("Total Units Consumed", min_value=0, step=1, key="units")
    if st.button("Calculate Bill", key="btn_bill"):
        if units <= 100:
            bill = units * 5
        elif units <= 200:
            bill = 100*5 + (units-100)*7
        else:
            bill = 100*5 + 100*7 + (units-200)*10
        st.info(f"Total Electricity Bill: ₹{bill}")


def bus_fare():
    st.header("🚌 Bus Fare Discount System")
    age = st.number_input("Passenger Age", 1, 120, key="bus_age")
    base_fare = 50
    if st.button("Calculate Fare", key="btn_bus"):
        if age < 12:
            fare = base_fare * 0.5
        elif age > 60:
            fare = base_fare * 0.7
        else:
            fare = base_fare
        st.success(f"Ticket Fare: ₹{fare}")


def atm_simulator():
    st.header("🏧 ATM Cash Withdrawal Simulator")
    balance = 10000
    withdraw = st.number_input("Amount to Withdraw", min_value=0, step=100, key="atm_withdraw")
    if st.button("Withdraw Cash", key="btn_atm"):
        if withdraw <= balance:
            balance -= withdraw
            st.success(f"₹{withdraw} withdrawn. Remaining Balance: ₹{balance}")
        else:
            st.error("Insufficient balance!")


def stock_alert():
    st.header("📦 Inventory Stock Alert")
    item = st.text_input("Item Name", key="item_name")
    stock = st.number_input("Current Stock", 0, key="stock")
    threshold = st.number_input("Reorder Threshold", 0, key="threshold")
    if st.button("Check Stock", key="btn_stock"):
        if stock <= threshold:
            st.warning(f"Stock for {item} is low ({stock}). Please reorder!")
        else:
            st.success(f"Stock for {item} is sufficient ({stock}).")


def loan_eligibility():
    st.header("🏦 Loan Eligibility Checker")
    salary = st.number_input("Monthly Salary (₹)", 0, step=1000, key="salary")
    credit = st.slider("Credit Score (300-850)", 300, 850, key="credit_score")
    if st.button("Check Eligibility", key="btn_loan"):
        if salary >= 30000 and credit >= 650:
            st.success("Eligible for loan! 😊")
        else:
            st.error("Not eligible for loan.")


def grade_calculator():
    st.header("📊 Grade Distribution Calculator")
    count = st.number_input("Number of Students", 1, step=1, key="num_students")
    marks = []
    for i in range(int(count)):
        m = st.number_input(f"Marks for student {i+1}", 0, 100, key=f"grade_{i}")
        marks.append(m)
    if st.button("Calculate Grades", key="btn_grade"):
        grades = {'A': 0, 'B':0, 'C':0, 'D':0, 'F':0}
        for m in marks:
            if m >= 85: grades['A'] += 1
            elif m >= 70: grades['B'] += 1
            elif m >= 50: grades['C'] += 1
            elif m >= 35: grades['D'] += 1
            else: grades['F'] += 1
        st.write(grades)


def temp_converter():
    st.header("🌡️ Temperature Converter")
    mode = st.radio("Convert:", ['Celsius to Fahrenheit', 'Fahrenheit to Celsius'], key="temp_mode")
    value = st.number_input("Enter Temperature", key="temp_value")
    if st.button("Convert", key="btn_temp"):
        if mode == 'Celsius to Fahrenheit':
            res = (value * 9/5) + 32
        else:
            res = (value - 32) * 5/9
        st.success(f"Converted Temperature: {res:.2f}")


def discount_calc():
    st.header("🏷️ Discount Calculator")
    amount = st.number_input("Original Amount (₹)", 0.0, key="orig_amt")
    disc = st.slider("Discount %", 0, 100, key="disc_pct")
    if st.button("Calculate Final Price", key="btn_disc"):
        final = amount * (1 - disc/100)
        st.info(f"Final Price after {disc}% discount: ₹{final:.2f}")


def attendance_tracker():
    st.header("✅ Attendance Tracker")
    total = st.number_input("Total Classes", 1, key="total_cls")
    attended = st.number_input("Classes Attended", 0, key="attended_cls")
    if st.button("Calculate Attendance", key="btn_attn"):
        pct = (attended/total)*100
        if pct >= 75:
            st.success(f"Attendance: {pct:.2f}% - Eligible 🎉")
        else:
            st.error(f"Attendance: {pct:.2f}% - Not Eligible")


def library_fine():
    st.header("📚 Library Fine Calculator")
    days = st.number_input("Days Overdue", 0, key="overdue")
    if st.button("Calculate Fine", key="btn_fine"):
        fine = days * 2  # ₹2 per day
        st.info(f"Total Fine: ₹{fine}")


def parking_fee():
    st.header("🚗 Parking Fee Calculator")
    hours = st.number_input("Hours Parked", 0.0, step=0.5, key="park_hrs")
    if st.button("Calculate Fee", key="btn_park"):
        fee = hours * 20  # ₹20 per hour
        st.info(f"Parking Fee: ₹{fee}")


def bmi_calculator():
    st.header("⚖️ BMI Calculator")
    weight = st.number_input("Weight (kg)", 0.0, key="weight")
    height = st.number_input("Height (m)", 0.0, key="height")
    if st.button("Compute BMI", key="btn_bmi"):
        bmi = weight / (height**2) if height > 0 else 0
        if bmi > 25:
            status = 'Overweight'
        elif bmi >= 18.5:
            status = 'Normal'
        else:
            status = 'Underweight'
        st.success(f"BMI: {bmi:.2f} - {status}")


def main():
    st.sidebar.title("📋 Select Demo")
    demos = [
        "Employee Promotion", "Student Promotion", "Electricity Bill",
        "Bus Fare Discount", "ATM Simulator", "Inventory Stock Alert",
        "Loan Eligibility", "Grade Calculator", "Temperature Converter",
        "Discount Calculator", "Attendance Tracker", "Library Fine Calculator",
        "Parking Fee Calculator", "BMI Calculator"
    ]
    choice = st.sidebar.selectbox("Choose a task:", demos)

    mapping = {
        "Employee Promotion": employee_promotion,
        "Student Promotion": student_promotion,
        "Electricity Bill": electricity_bill,
        "Bus Fare Discount": bus_fare,
        "ATM Simulator": atm_simulator,
        "Inventory Stock Alert": stock_alert,
        "Loan Eligibility": loan_eligibility,
        "Grade Calculator": grade_calculator,
        "Temperature Converter": temp_converter,
        "Discount Calculator": discount_calc,
        "Attendance Tracker": attendance_tracker,
        "Library Fine Calculator": library_fine,
        "Parking Fee Calculator": parking_fee,
        "BMI Calculator": bmi_calculator
    }
    mapping[choice]()

if __name__ == "__main__":
    main()
