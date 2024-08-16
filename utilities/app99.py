import streamlit as st
import pandas as pd

def main():
    st.title("Personal Finance Management Demo")

    # Tab layout for the app
    tabs = st.tabs(["Overview", "Income & Expenses", "Savings & Investments", "Simple Problems", "Group Task"])

    # Overview Tab
    with tabs[0]:
        st.header("Overview")
        st.write("""
        Welcome to the Personal Finance Management demo app! This simple tool will help you understand the basics of managing your personal finances.
        You can track your income, expenses, savings, and investments, and solve simple finance management problems.
        """)

    # Income & Expenses Tab
    with tabs[1]:
        st.header("Income & Expenses")

        # Input fields for income and expenses
        income = st.number_input("Enter your total monthly income", min_value=0, step=100)
        expenses = st.number_input("Enter your total monthly expenses", min_value=0, step=100)
        
        # Calculate remaining balance
        remaining_balance = income - expenses
        if remaining_balance > 0:
            st.success(f"Great! You have a surplus of ₹{remaining_balance} this month.")
        elif remaining_balance < 0:
            st.warning(f"Be careful! You have a deficit of ₹{-remaining_balance} this month.")
        else:
            st.info("You're breaking even this month.")

    # Savings & Investments Tab
    with tabs[2]:
        st.header("Savings & Investments")

        # Input fields for savings and investments
        savings = st.number_input("Enter your total monthly savings", min_value=0, step=100)
        investments = st.number_input("Enter your total monthly investments", min_value=0, step=100)

        # Calculate the total amount allocated to savings and investments
        total_savings_investments = savings + investments
        st.info(f"You're saving and investing a total of ₹{total_savings_investments} each month.")

        # Simple savings rate calculation
        if income > 0:
            savings_rate = (total_savings_investments / income) * 100
            st.write(f"Your savings rate is {savings_rate:.2f}% of your total income.")
        else:
            st.write("Please enter your income to calculate the savings rate.")

    # Simple Problems Tab
    with tabs[3]:
        st.header("Simple Personal Finance Problems")

        st.subheader("Problem 1: Budgeting")
        st.write("""
        You have a monthly income of ₹50,000. Your expenses are as follows:
        - Rent: ₹15,000
        - Groceries: ₹8,000
        - Utilities: ₹5,000
        - Miscellaneous: ₹7,000
        
        How much can you save or invest each month?
        """)
        st.text_input("Your answer", key="budgeting_answer")

        st.subheader("Problem 2: Emergency Fund")
        st.write("""
        You want to build an emergency fund that covers 6 months of your expenses. If your monthly expenses are ₹25,000, how much do you need to save in total for the emergency fund?
        """)
        st.text_input("Your answer", key="emergency_fund_answer")

        st.subheader("Problem 3: Investment Returns")
        st.write("""
        You invest ₹1,00,000 in a fixed deposit that offers an annual interest rate of 5%. How much will your investment be worth after one year?
        """)
        st.text_input("Your answer", key="investment_returns_answer")

    # Group Task Tab
    with tabs[4]:
        st.header("Group Task: Personal Finance Plan")
        
        st.write("In this group task, each group needs to create a basic personal finance plan. The plan should include:")
        st.write("""
        - A monthly budget showing income, expenses, savings, and investments.
        - An emergency fund calculation.
        - A simple investment strategy for the next year.
        - A brief explanation of how you would adjust the plan if your income increased or decreased by 10%.
        """)

        # Input for group name
        group_name = st.text_input("Enter your group name", key="group_name")

        # Scoring section
        st.subheader("Scoring")
        budgeting_score = st.slider("Budgeting (out of 10)", 0, 10, key="budgeting_score")
        savings_score = st.slider("Savings and Investments (out of 10)", 0, 10, key="savings_score")
        emergency_fund_score = st.slider("Emergency Fund Calculation (out of 10)", 0, 10, key="emergency_fund_score")
        investment_strategy_score = st.slider("Investment Strategy (out of 10)", 0, 10, key="investment_strategy_score")
        adjustment_plan_score = st.slider("Adjustment Plan (out of 10)", 0, 10, key="adjustment_plan_score")

        # Calculate total score
        total_score = budgeting_score + savings_score + emergency_fund_score + investment_strategy_score + adjustment_plan_score

        # Display the total score
        st.write(f"**Total Score for {group_name}:** {total_score} out of 50")
        
        # Option to save the score
        save_option = st.checkbox("Save the score to CSV file", key="save_option")
        if save_option:
            df = pd.DataFrame({
                "Group Name": [group_name],
                "Budgeting Score": [budgeting_score],
                "Savings Score": [savings_score],
                "Emergency Fund Score": [emergency_fund_score],
                "Investment Strategy Score": [investment_strategy_score],
                "Adjustment Plan Score": [adjustment_plan_score],
                "Total Score": [total_score]
            })
            csv = df.to_csv(index=False)
            st.download_button(label="Download CSV", data=csv, file_name=f"{group_name}_score.csv", mime='text/csv')

if __name__ == "__main__":
    main()
