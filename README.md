# Google Pay Expense Sharing - Easy Full Project

## Project idea
This project divides common expenses between Alice, Bob and Carol and finds the final settlement.

## Files
- `GooglePay_Expense_Sharing.ipynb` - complete Jupyter Notebook
- `expense_sharing.py` - simple Python version
- `easy_expenses.csv` - easy sample data
- `README.md` - project explanation
- `requirements.txt` - libraries needed

## Data
The data has only six simple expenses:

1. Hotel - Alice - Rs. 3000 - paid
2. Lunch - Bob - Rs. 900 - paid
3. Taxi - Carol - Rs. 600 - paid
4. Dinner - Alice - Rs. 1200 - paid
5. Hotel Refund - Alice - Rs. 300 - refund
6. Snacks - unpaid - Rs. 300

All paid expenses are shared equally (`1|1|1`).

## Main formula
Balance = Amount Paid - Fair Share

A positive balance means the person should receive money.
A negative balance means the person should pay money.

## Expected settlement from the sample data
- Bob pays Alice Rs. 900
- Carol pays Alice Rs. 1200

The Rs. 300 snacks bill is still pending and is not included in the settlement.

## Libraries
- pandas
- numpy
- matplotlib

## How to run
### Jupyter Notebook
1. Install Python.
2. Run `pip install pandas numpy matplotlib jupyter`
3. Open Jupyter Notebook.
4. Open `GooglePay_Expense_Sharing.ipynb`.
5. Run the cells from top to bottom.

### Python file
Run:
`python expense_sharing.py`
