# Google Pay-Inspired Expense Sharing System

## About the project

This is a beginner Python data-science project for splitting trip expenses between three friends: **Alice, Bob, and Carol**. It is inspired by Google Pay expense sharing, but it is only a learning project and is not connected to the real Google Pay application.

The program reads a CSV file, calculates a fair share for each friend, shows who should pay whom, saves result CSV files, and creates two charts.

## Project files

| File | Purpose |
| --- | --- |
| `expense_sharing.ipynb` | Main Jupyter Notebook with clear Markdown titles and code cells. |
| `sample_expenses.csv` | Input data for Alice, Bob, and Carol. |
| `README.md` | Project explanation and discussion notes. |
| `requirements.txt` | Required Python libraries. |

## How to run

Install the libraries once:

```powershell
python -m pip install -r requirements.txt
```

Start Jupyter Notebook in the project folder:

```powershell
jupyter notebook
```

Open `expense_sharing.ipynb`, then choose **Run All Cells**. The notebook creates a `generated` folder containing result CSV files and two charts.

## Dataset explanation

Each CSV row is one expense.

| Column | Meaning |
| --- | --- |
| `payer` | Friend who paid the bill. |
| `amount` | Bill amount in rupees. |
| `participants` | Friends who shared the bill, separated by `|`. |
| `split_weights` | How the bill is divided. Blank means equal split. `1|2|1` means 25%, 50%, and 25%. |
| `status` | `paid`, `refund`, or `unpaid`. |

The sample data has normal payments, uneven splits, one hotel refund, and one unpaid bill.

## How the calculation works

For a normal paid bill:

```text
balance = money paid by friend - fair share of expenses
```

For example, if Alice pays Rs. 9,000 for a hotel shared equally by all three friends:

- Alice pays Rs. 9,000.
- Alice, Bob, and Carol each have a fair share of Rs. 3,000.
- Alice receives Rs. 6,000 credit for that bill.

A positive balance means the friend should receive money. A negative balance means the friend should pay money.

## Special cases used in this project

- **Uneven split:** `1|2|1` gives Bob two shares because he used more or agreed to contribute more.
- **Refund:** a refund is treated as a negative expense, so it reduces the total fairly for all participants.
- **Unpaid bill:** the program shows it as a warning and does not add it to the settlement because no one has paid it yet.
- **Rounding:** a small one-paise difference can happen after division, so the code adjusts it to keep the final balances equal to zero.

## Libraries used

- **Pandas** reads the CSV file and saves result tables.
- **NumPy** calculates the average expense.
- **Matplotlib** creates bar charts.

## Sample result

For the provided data, the net group expense is **Rs. 15,400.00**. The Rs. 450 unpaid snack is not included in settlement.

| Friend | Result |
| --- | ---: |
| Alice | Receives Rs. 5,166.66 |
| Bob | Pays Rs. 2,633.33 |
| Carol | Pays Rs. 2,533.33 |

Final payments:

- Bob pays Alice Rs. 2,633.33.
- Carol pays Alice Rs. 2,533.33.

## What to explain in a technical discussion

1. I used three fixed friends, Alice, Bob, and Carol, to keep the beginner project simple.
2. I used a Python dictionary to store each friend's balance.
3. I used loops to read every bill and calculate the share of each participant.
4. I used Pandas `groupby()` to make the spending-by-category chart.
5. The settlement plan matches people who owe money with the person who should receive money.
6. A limitation is that the project uses sample CSV data only; a future version could add user input, a database, or online payment links.
