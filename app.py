

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Personal Expense Tracker",
     page_icon="💰",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Expense Analyzer")

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if st.sidebar.button("Dashboard", use_container_width=True):
    st.session_state.page = "Dashboard"

if st.sidebar.button("Add Expense", use_container_width=True):
    st.session_state.page = "Add Expense"

if st.sidebar.button("Expenses", use_container_width=True):
    st.session_state.page = "Expenses"

if st.sidebar.button("Analytics", use_container_width=True):
    st.session_state.page = "Analytics"

if st.sidebar.button("Settings", use_container_width=True):
    st.session_state.page = "Settings"

page = st.session_state.page

# Load Dataset
df = pd.read_csv("data/expenses.csv")


# =========================
# DASHBOARD
# =========================

if page == "Dashboard":

    st.title("Personal Expense Analyzer")

    st.write(
        "Analyze and understand your personal spending habits."
    )

    total_expenses = df["Amount"].sum()
    average_expense = df["Amount"].mean()
    highest_expense = df["Amount"].max()
    lowest_expense = df["Amount"].min()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Expenses",
        f"₱{total_expenses:,.2f}"
    )

    col2.metric(
        "Average Expense",
        f"₱{average_expense:,.2f}"
    )

    col3.metric(
        "Highest Expense",
        f"₱{highest_expense:,.2f}"
    )

    col4.metric(
        "Lowest Expense",
        f"₱{lowest_expense:,.2f}"
    )

    st.subheader("Expense Records")

    col1, col2 = st.columns(2)

    with col1:

        selected_category = st.selectbox(
            "Filter by Category",
            ["All"] + sorted(
                df["Category"].unique().tolist()
            )
        )

    with col2:

        sort_order = st.selectbox(
            "Sort by Amount",
            [
                "Default",
                "Lowest to Highest",
                "Highest to Lowest"
            ]
        )

    filtered_df = df.copy()

    if selected_category != "All":

        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    if sort_order == "Lowest to Highest":

        filtered_df = filtered_df.sort_values(
            "Amount",
            ascending=True
        )

    elif sort_order == "Highest to Lowest":

        filtered_df = filtered_df.sort_values(
            "Amount",
            ascending=False
        )

    st.dataframe(
        filtered_df,
        use_container_width=True
    )



    st.subheader("Category Summary")

    category_summary = (
        df.groupby("Category")["Amount"]
        .agg(["sum", "count", "mean"])
        .reset_index()
    )

    category_summary.columns = [
        "Category",
        "Total Spending",
        "Number of Expenses",
        "Average Expense"
    ]

    st.dataframe(
        category_summary,
        use_container_width=True
    )


# =========================
# ANALYTICS
# =========================

elif page == "Analytics":

    st.title("Expense Analytics")

    st.write(
        "Visual analysis of your personal spending habits."
    )

    # Numerical Analysis

    st.subheader("Numerical Analysis")

    amounts = df["Amount"].to_numpy()

    mean_expense = np.mean(amounts)
    median_expense = np.median(amounts)
    std_expense = np.std(amounts)
    minimum_expense = np.min(amounts)
    maximum_expense = np.max(amounts)

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Mean",
        f"₱{mean_expense:,.2f}"
    )

    col2.metric(
        "Median",
        f"₱{median_expense:,.2f}"
    )

    col3.metric(
        "Standard Deviation",
        f"₱{std_expense:,.2f}"
    )

    col4.metric(
        "Minimum",
        f"₱{minimum_expense:,.2f}"
    )

    col5.metric(
        "Maximum",
        f"₱{maximum_expense:,.2f}"
    )

    # SciPy Statistical Analysis

    from scipy import stats

    st.subheader("Statistical Analysis")

    reference_amount = 200

    t_statistic, p_value = stats.ttest_1samp(
        amounts,
        reference_amount
    )

    st.write(
        f"Reference expense amount: ₱{reference_amount:,.2f}"
    )

    st.write(
        f"T-statistic: {t_statistic:.4f}"
    )

    st.write(
        f"P-value: {p_value:.4f}"
    )

    if p_value < 0.05:

        st.write(
            "The average expense is statistically different "
            "from the reference amount of ₱200."
        )

    else:

        st.write(
            "There is not enough statistical evidence to conclude "
            "that the average expense is different from ₱200."
        )



    # -------------------------
    # Bar Chart
    # -------------------------

    st.subheader("Spending by Category")

    category_expenses = (
        df.groupby("Category")["Amount"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=(17, 5)
    )

    bars = ax.bar(
        category_expenses.index,
        category_expenses.values,
        width=0.6
    )

    ax.bar_label(
        bars,
        fmt="₱%.0f",
        padding=3
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.4
    )

    ax.set_xlabel("Category")

    ax.set_ylabel(
        "Total Spending (₱)"
    )

    ax.set_title(
        "Total Spending by Category"
    )

    plt.xticks(
        rotation=45
    )

    st.pyplot(fig)

    highest_category = category_expenses.idxmax()
    highest_category_amount = category_expenses.max()

    st.write(
        f"Interpretation: {highest_category} has the highest total "
        f"spending at ₱{highest_category_amount:,.2f}."
    )


    # -------------------------
    # Line Chart and Histogram
    # -------------------------

    col1, col2 = st.columns(2)


    # Spending Over Time
    with col1:

        st.subheader("Spending Over Time")

        df["Date"] = pd.to_datetime(
            df["Date"]
        )

        daily_expenses = (
            df.groupby("Date")["Amount"]
            .sum()
        )

        fig, ax = plt.subplots(
            figsize=(6, 4)
        )

        ax.plot(
            daily_expenses.index,
            daily_expenses.values
        )

        ax.set_xlabel(
            "Date"
        )

        ax.set_ylabel(
            "Expense (₱)"
        )

        ax.set_title(
            "Daily Spending Over Time"
        )

        ax.grid(
            axis="y",
            linestyle="--",
            alpha=0.4
        )

        plt.xticks(
            rotation=45
        )

        st.pyplot(fig)

        most_common_range = pd.cut(
            df["Amount"],
            bins=8
        ).value_counts().idxmax()

        st.write(
            f"Interpretation: The most common expense range is "
            f"{most_common_range}."
        )


    # Expense Distribution
    with col2:

        st.subheader("Expense Distribution")

        fig, ax = plt.subplots(
            figsize=(6, 4)
        )

        ax.hist(
            df["Amount"],
            bins=8
        )

        ax.set_xlabel(
            "Expense Amount (₱)"
        )

        ax.set_ylabel(
            "Frequency"
        )

        ax.set_title(
            "Expense Amount Distribution"
        )

        ax.grid(
            axis="y",
            linestyle="--",
            alpha=0.4
        )

        st.pyplot(fig)

        highest_day = daily_expenses.idxmax()
        highest_day_amount = daily_expenses.max()

        st.write(
            f"Interpretation: The highest daily spending occurred on "
            f"{highest_day.strftime('%B %d, %Y')} with a total of "
            f"₱{highest_day_amount:,.2f}."
        )     


# =========================
# ADD EXPENSE
# =========================

elif page == "Add Expense":

    st.title("Add Expense")

    st.write(
        "Enter the details of your expense."
    )

    expense_date = st.date_input(
        "Date"
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Transportation",
            "School",
            "Bills",
            "Entertainment"
        ]
    )

    description = st.text_input(
        "Description"
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=10.0
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Cash",
            "Gcash"
        ]
    )

    if st.button("Add Expense"):

        if description == "":
            st.warning(
                "Please enter a description."
            )

        elif amount <= 0:
            st.warning(
                "Please enter an amount greater than 0."
            )

        else:

            new_expense = pd.DataFrame({
                "Date": [
                    expense_date
                ],
                "Category": [
                    category
                ],
                "Description": [
                    description
                ],
                "Amount": [
                    amount
                ],
                "Payment Method": [
                    payment_method
                ]
            })

            new_expense.to_csv(
                "data/expenses.csv",
                mode="a",
                header=False,
                index=False
            )

            st.success(
                "Expense added successfully."
            )

            st.rerun()


# =========================
# EXPENSES
# =========================

elif page == "Expenses":

    st.title("Expenses")

    st.write(
        "View and manage your expense records."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        category_filter = st.selectbox(
            "Category",
            ["All"] + sorted(
                df["Category"].unique().tolist()
            )
        )

    with col2:

        payment_filter = st.selectbox(
            "Payment Method",
            ["All"] + sorted(
                df["Payment Method"].unique().tolist()
            )
        )

    with col3:

        search = st.text_input(
            "Search Description"
        )

    filtered_expenses = df.copy()

    if category_filter != "All":

        filtered_expenses = filtered_expenses[
            filtered_expenses["Category"] == category_filter
        ]

    if payment_filter != "All":

        filtered_expenses = filtered_expenses[
            filtered_expenses["Payment Method"] == payment_filter
        ]

    if search:

        filtered_expenses = filtered_expenses[
            filtered_expenses["Description"]
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.write(
        f"Records found: {len(filtered_expenses)}"
    )

    st.dataframe(
        filtered_expenses,
        use_container_width=True
    )


# =========================
# SETTINGS
# =========================

elif page == "Settings":

    st.title("Settings")

    st.write(
        "Application settings will be added here."
    )