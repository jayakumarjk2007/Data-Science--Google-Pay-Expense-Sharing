# Google Pay Expense Sharing

## Project Idea
This project helps friends manage shared expenses and calculate who owes whom.
It uses a simple `ExpenseSharing` class built with Object-Oriented Programming (OOP) in Python.

## Files
- `GooglePay_Expense_Sharing.ipynb` — complete Jupyter Notebook
- `expense_sharing.py` — standalone Python version for deployment
- `easy_expenses.csv` — sample data
- `Project_Report.md` — detailed project report
- `README.md` — project explanation
- `requirements.txt` — libraries needed

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

## Dependencies & Libraries
- **Standalone Script (`expense_sharing.py`)**: 
  - **Zero external dependencies** — Built strictly using pure Python standard library (`dict`, `list`, standard I/O). Runs immediately without installing any packages.
- **Jupyter Notebook (`GooglePay_Expense_Sharing.ipynb`)**:
  - `pandas` — for reading dataset tables (`easy_expenses.csv`) and tabular summaries
  - `numpy` — for numerical operations
  - `matplotlib` — for generating data science charts and visual spending breakdowns

## How to Run

### 1. Standalone Python Script (Zero Setup)
No installation needed! Just run directly with Python:
```bash
python expense_sharing.py
```

### 2. Jupyter Notebook (Data Science & Visualizations)
If you want to view the data science analysis, charts, and visualizations:
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook GooglePay_Expense_Sharing.ipynb
   ```
3. Run the cells from top to bottom.
