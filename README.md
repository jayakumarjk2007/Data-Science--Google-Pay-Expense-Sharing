# GooglePay Expense Sharing

## About my project

This is a small Python data-science project I made for shared trip expenses. I used three friends—Alice, Bob and Carol—as an example. Each person paid for different things during the trip, and the program works out who should pay whom at the end.

I chose this topic because splitting expenses is a common real-life problem. The idea is similar to the expense-sharing feature in Google Pay, but this is only a simple learning project.

## What is in this folder?

- `GooglePay_Expense_Sharing.ipynb` is the main notebook. This is the file to show during submission.
- `data/sample_expenses.csv` is the small input dataset.
- `expense_sharing.py` and `run_project.py` are the same project in normal Python files.
- `generated/` has the result CSV files, the settlement text file, and charts after running the project.

## Libraries I used

- **Pandas**: to create an expense table and group the data.
- **NumPy**: to find the average expense.
- **Matplotlib**: to create simple bar charts.

Install them with:

```powershell
pip install -r requirements.txt
```

## How it works

For every bill, the person who pays gets the full amount added to their balance. Then every person sharing that bill has their equal share subtracted.

```text
balance = amount paid - person's share of expenses
```

If the balance is positive, the person should get money back. If it is negative, they need to pay. The final part of the code matches people who owe money with the person who should receive it.

For example, Alice pays Rs. 9,000 for accommodation. Since all three friends stay there, each share is Rs. 3,000. Alice paid Rs. 9,000 but her own share is only Rs. 3,000, so she should get Rs. 6,000 back from that bill.

## Data processing and analysis

I first read the CSV file and put the expenses into a Pandas DataFrame. I used `groupby()` to find spending by category and spending by payer. I used NumPy to calculate the average expense. Finally, I made two simple bar charts.

The project shows:

- Spending by category
- Amount paid by each friend
- Average expense
- Final balance for each friend
- Final settlement payments

## Result from the sample data

The total trip cost is Rs. 15,000. Since three people shared the trip, the fair share for each person is Rs. 5,000.

| Friend | Paid | Final result |
| --- | ---: | --- |
| Alice | Rs. 10,800 | Receives Rs. 5,800 |
| Bob | Rs. 2,400 | Pays Rs. 2,600 |
| Carol | Rs. 1,800 | Pays Rs. 3,200 |

So the final settlement is:

- Bob pays Alice Rs. 2,600.
- Carol pays Alice Rs. 3,200.

The charts show that accommodation is the highest expense and Alice paid the most during the trip.

## Things I can improve later

- Let users enter expenses instead of using only the sample CSV.
- Add dates and more categories.
- Allow different split percentages instead of only equal splitting.
- Add a refund as a negative expense.
- Build a simple web page for the project.

## Run the project

Open `GooglePay_Expense_Sharing.ipynb` in Jupyter Notebook and run the cells from top to bottom.

Or run this command in the project folder:

```powershell
python run_project.py
```
