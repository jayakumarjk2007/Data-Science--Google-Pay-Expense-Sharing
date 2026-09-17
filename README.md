# Google Pay Expense Sharing

## Project Idea
This project helps friends manage shared expenses and calculate who owes whom.
It uses a simple `ExpenseSharing` class built with Object-Oriented Programming (OOP) in Python.

## Files
- `expense_sharing.py` — standalone Python version for deployment (pure Python, zero dependencies)
- `GooglePay_Expense_Sharing.ipynb` — complete Jupyter Notebook for data analysis & visualization
- `easy_expenses.csv` — sample data
- `Project_Report.md` — detailed project report
- `README.md` — project explanation

## How It Works
1. Create a list of friends
2. Add expenses — who paid, how much, and who shared it
3. The program calculates each person's balance
4. Final settlement shows who owes and who gets reimbursed

## Sample Data (3 Friends)
| Expense | Payer | Amount | Shared By |
|---------|-------|--------|-----------|
| Accommodation | Alice | Rs. 900 | Alice, Bob, Carol |
| Meals | Bob | Rs. 300 | Alice, Bob, Carol |
| Fuel | Carol | Rs. 200 | Alice, Carol |

## Expected Output
```
Final Settlement:
Alice needs to be reimbursed: Rs.400.00
Bob owes: Rs.100.00
Carol owes: Rs.300.00
```

## Formula
**Balance = Amount Paid for Others − Own Share Owed to Others**

- Positive balance → person needs to be reimbursed
- Negative balance → person owes money

## Dependencies
- **No external libraries required!**
- The project script (`expense_sharing.py`) is written in **100% pure standard Python** (using built-in data structures like dictionaries and lists).
- It runs out-of-the-box on any system with Python 3.x installed without running `pip install`.
- *(Optional)*: If you want to run the Jupyter Notebook (`GooglePay_Expense_Sharing.ipynb`) to view charts and data frames, `pandas` and `matplotlib` can be used.

## How to Run

### Run the Project (Zero Setup)
Simply run the script with Python:
```bash
python expense_sharing.py
```

### (Optional) Run the Jupyter Notebook
If you want to view the interactive notebook with graphs:
```bash
pip install pandas matplotlib jupyter
jupyter notebook GooglePay_Expense_Sharing.ipynb
```
