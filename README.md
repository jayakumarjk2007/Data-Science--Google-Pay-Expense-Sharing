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

## Libraries
- pandas
- numpy
- matplotlib

## How to Run

### Jupyter Notebook
1. Install Python
2. Run `pip install pandas numpy matplotlib jupyter`
3. Open `GooglePay_Expense_Sharing.ipynb`
4. Run the cells from top to bottom

### Python File
```
python expense_sharing.py
```
