# Project Report - Google Pay Expense Sharing

## 1. Introduction
The aim of this project is to create a simple expense-sharing system for friends. It helps calculate how much each person paid, how much each person should pay, and the final settlement.

## 2. Dataset
The sample dataset contains six expenses shared by Alice, Bob and Carol. It includes normal payments, one refund and one unpaid bill.

## 3. Data Processing
The CSV file is loaded using Pandas. The amount column is converted into numeric form and the payment status is checked.

## 4. Expense Calculation
For each paid bill, the amount is divided between the participants. Since the sample uses `1|1|1`, the expenses are divided equally.

The formula is:

**Fair Share = Total Expense / Number of Participants**

Then:

**Balance = Amount Paid - Fair Share**

## 5. Special Cases
- **Refund:** The refund is added back to the original payer and reduces the shared amount.
- **Unpaid payment:** It is kept pending and does not change the current settlement.

## 6. Data Science Tools
- **Pandas:** Reading, cleaning and grouping the data.
- **NumPy:** Numerical calculation support.
- **Matplotlib:** Creating simple spending charts.

## 7. Results
From the sample data:
- Alice has to receive Rs. 2100.
- Bob has to pay Rs. 900.
- Carol has to pay Rs. 1200.

Therefore:
- Bob pays Alice Rs. 900.
- Carol pays Alice Rs. 1200.

The unpaid Rs. 300 snacks expense remains pending.

## 8. Conclusion
The project demonstrates a simple real-world use of Python and data science for managing shared expenses. It is designed in a beginner-friendly way and can later be extended into a web or mobile application.
