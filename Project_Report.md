# Project Report - Google Pay Expense Sharing

## 1. Introduction
The aim of this project is to create a simple expense-sharing system for friends. It helps calculate how much each person paid, how much each person should pay, and the final settlement. The project is built using Object-Oriented Programming (OOP) in Python.

## 2. Dataset
The sample uses three friends — Alice, Bob and Carol — with three expenses:
- Alice paid Rs. 900 for accommodation (shared by all three)
- Bob paid Rs. 300 for meals (shared by all three)
- Carol paid Rs. 200 for fuel (shared by Alice and Carol)

## 3. OOP Design
The project uses the `ExpenseSharing` class with the following methods:
- **`__init__(self, friends)`** — Constructor that initialises the friends list and a balance dictionary.
- **`add_expense(self, payer, amount, participants)`** — Splits the expense equally among participants and updates balances.
- **`calculate_settlement(self)`** — Prints who owes money and who needs to be reimbursed.

## 4. Expense Calculation
For each expense, the amount is divided equally among participants.

**Formula:** `Split Amount = Total Amount / Number of Participants`

For each participant (who is not the payer):
- The participant's balance increases (they owe more)
- The payer's balance decreases (they are owed more)

**Final Balance:**
- Positive balance → person owes money
- Negative balance → person needs to be reimbursed

## 5. Step-by-Step Calculation

**Expense 1:** Alice paid Rs. 900 (split 3 ways = Rs. 300 each)
- Alice: +600, Bob: -300, Carol: -300

**Expense 2:** Bob paid Rs. 300 (split 3 ways = Rs. 100 each)
- Alice: +500, Bob: -100, Carol: -400

**Expense 3:** Carol paid Rs. 200 (split 2 ways = Rs. 100 each)
- Alice: +400, Bob: -100, Carol: -300

## 6. Results
From the sample data:
- Alice needs to be reimbursed Rs. 400
- Bob owes Rs. 100
- Carol owes Rs. 300

## 7. Features
- Supports any number of friends
- Handles uneven participation (not everyone shares every expense)
- Interactive input mode for custom expenses
- Two test scenarios (3 friends and 4 friends)

## 8. Tools & Dependencies
- **Python Standard Library (Core System)** — The entire expense sharing logic in `expense_sharing.py` requires **zero external libraries**. It is built strictly with Python built-ins (`dict`, `list`, standard I/O) for maximum portability and zero-setup deployment.
- **OOP (Object-Oriented Programming)** — Class-based architecture using constructor (`__init__`), encapsulation, and reusable methods (`add_expense`, `calculate_settlement`).
- **Optional Data Science Tools (Jupyter Notebook)** — The exploratory notebook (`GooglePay_Expense_Sharing.ipynb`) uses:
  - **Pandas** — for reading data tables and category summaries
  - **NumPy** — for numerical operations
  - **Matplotlib** — for spending charts and graphical visualization

## 9. Conclusion
The project demonstrates a real-world use of Python OOP for managing shared expenses. It can be extended with a database, web interface, or payment integration.
