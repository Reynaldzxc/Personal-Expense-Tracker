# Personal-Expense-Tracker
Python-based personal expense analysis and visualization system

# Personal Expense Analyzer

## Project Overview

The Personal Expense Analyzer is a Python-based data analysis and visualization system developed using Streamlit. The system allows users to record, view, filter, and analyze personal expenses.

The project uses Pandas for data processing, NumPy for numerical calculations, Matplotlib for data visualization, and SciPy for statistical analysis.

## Problem Statement

Managing personal expenses manually can make it difficult to understand spending patterns and identify where money is being spent.

This project provides a simple system that organizes expense records and presents numerical and visual analysis to help users understand their spending habits.

## Purpose

The purpose of this project is to develop a Python-based system that can process personal expense data, perform numerical and statistical analysis, and present the results through interactive visualizations.

## Objectives

1. To create a system for recording and managing personal expense data.
2. To process and organize expense records using Pandas.
3. To perform numerical calculations using NumPy.
4. To visualize spending patterns using Matplotlib.
5. To perform statistical analysis using SciPy.
6. To provide useful interpretations of the analyzed expense data.

## Dataset Description

The dataset contains personal expense records used for analysis and visualization.

### Number of Records

The initial dataset contains 30 expense records.

Additional records can be added through the application's Add Expense feature.

### Dataset Columns

| Column | Description | Data Type |
|---|---|---|
| Date | Date when the expense occurred | Date |
| Category | Category of the expense | String |
| Description | Description of the expense | String |
| Amount | Amount spent | Numeric |
| Payment_Method | Method used to pay the expense | String |

### Expense Categories

The dataset contains categories such as:

- Food
- Transportation
- School
- Bills
- Entertainment

### Payment Methods

The dataset contains payment methods such as:

- Cash
- Gcash

## Python Libraries

The project uses the following Python libraries:

### Streamlit

Used to create the interactive web-based user interface.

### Pandas

Used for reading, filtering, sorting, grouping, and manipulating the expense dataset.

### NumPy

Used for numerical calculations including:

- Mean
- Median
- Standard deviation
- Minimum
- Maximum

### Matplotlib

Used to create the required data visualizations:

- Spending by Category
- Spending Over Time
- Expense Distribution

### SciPy

Used to perform statistical analysis using a one-sample t-test.

## System Features

### Dashboard

The Dashboard displays:

- Total expenses
- Average expense
- Highest expense
- Lowest expense
- Expense records
- Category filtering
- Amount sorting
- Category summary

### Add Expense

Users can add a new expense by entering:

- Date
- Category
- Description
- Amount
- Payment method

The new expense is saved to the CSV dataset.

### Expenses

Users can:

- View expense records
- Filter by category
- Filter by payment method
- Search expense descriptions
- View the number of matching records

### Analytics

The Analytics page provides numerical, statistical, and visual analysis of the dataset.

### Settings

The Settings page displays information about the dataset, categories, and payment methods.

## Data Processing

Pandas is used for several data-processing operations, including:

1. Reading the CSV dataset.
2. Filtering expense records.
3. Sorting expenses by amount.
4. Grouping expenses by category.
5. Calculating category summaries.
6. Searching expense descriptions.

## Numerical Analysis

NumPy is used to calculate:

- Mean expense
- Median expense
- Standard deviation
- Minimum expense
- Maximum expense

These calculations provide numerical information about the distribution of expense amounts.

## Data Visualization

The system uses Matplotlib to create three visualizations.

### 1. Spending by Category

A bar chart shows the total amount spent in each expense category.

### 2. Spending Over Time

A line chart shows daily spending throughout the dataset period.

### 3. Expense Distribution

A histogram shows how frequently different expense amounts occur.

Each visualization includes an automatic interpretation based on the dataset.

## Statistical Analysis

SciPy is used to perform a one-sample t-test.

The test compares the expense amounts against a reference amount of ₱200.

The system displays:

- T-statistic
- P-value
- Statistical interpretation

## Results and Analysis

The system provides several ways to understand personal spending behavior.

The Dashboard provides an overview of total and average expenses. The category summary allows spending to be compared across different expense categories.

The Analytics page provides numerical measurements using NumPy, visual patterns using Matplotlib, and statistical analysis using SciPy.

The chart interpretations are generated from the actual expense dataset used by the application.

## Conclusion

The Personal Expense Analyzer demonstrates how Python can be used for data processing, numerical analysis, statistical analysis, and visualization.

By combining Streamlit, Pandas, NumPy, Matplotlib, and SciPy, the system provides an interactive way to record and analyze personal expenses.

## How to Run the Project

### 1. Activate the virtual environment

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1