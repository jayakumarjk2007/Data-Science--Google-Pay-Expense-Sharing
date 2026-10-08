# Google Pay Expense Sharing System

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen.svg)](https://docs.python.org/3/library/)
[![Paradigm](https://img.shields.io/badge/Design-Object--Oriented%20(OOP)-orange.svg)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An Object-Oriented expense management and debt settlement application designed to mimic group expense splitting tools like **Google Pay Bill Split** and **Splitwise**. Built using pure standard Python with **zero third-party dependencies**, this project calculates exact per-participant split obligations, tracks running net balances, and prints final reimbursement settlements.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Repository Structure](#repository-structure)
- [Mathematical Logic & Algorithm](#mathematical-logic--algorithm)
- [Step-by-Step Worked Example](#step-by-step-worked-example)
- [Dataset Specifications](#dataset-specifications)
- [Technologies Used](#technologies-used)
- [Setup & Installation](#setup--installation)
- [Usage Instructions](#usage-instructions)
- [Author & Acknowledgments](#author--acknowledgments)

---

## Project Overview

When friends travel or dine together, different members often pay for different shared expenses with varying sub-groups of beneficiaries. Manually tracking individual debts creates confusion and frequent arithmetic errors.

This project solves group expense reconciliation by providing:
1. An extensible `ExpenseSharing` class encapsulating participant registration, split updates, and final settlement generation.
2. An interactive Command-Line Interface (CLI) in `expense_sharing.py` that allows dynamic input of friends, payers, and amounts.
3. An exploratory Jupyter Notebook (`GooglePay_Expense_Sharing.ipynb`) detailing step-by-step balance calculations, intermediate states, and 4-person stress tests.
4. A structured CSV dataset (`easy_expenses.csv`) modeling real-world vacation expenses with dates, categories, split weights, and payment statuses.

---

## Key Features

- **Zero External Dependencies:** Runs immediately on any machine with Python 3 installed—no `pip install` required.
- **Dynamic Participant Subsets:** Each expense can be split among all members or any arbitrary subset of participants (e.g., fuel split between 2 people while lodging is split among 3).
- **Exact Balance Tracking:** Internal hash maps maintain net positive and negative balances with floating-point precision formatted to two decimal places (`₹0.00`).
- **Clear Settlement Direction:** Explicitly indicates whether each participant owes money or is owed reimbursement.

---

## Repository Structure

```text
Data-Science--Google-Pay-Expense-Sharing/
├── expense_sharing.py              # Standalone Python CLI application (zero external dependencies)
├── GooglePay_Expense_Sharing.ipynb # Jupyter notebook demonstrating step-by-step state verification
├── easy_expenses.csv               # Sample structured tabular dataset of vacation expenses
├── Project_Report.md               # In-depth architectural documentation and calculation proof
└── README.md                       # Comprehensive project documentation
```

---

## Mathematical Logic & Algorithm

### 1. Split Allocation
For each expense of value $A$ paid by payer $P$ with a participant list $S = \{p_1, p_2, \dots, p_k\}$:

$$\text{Per-Person Share} = \frac{A}{|S|}$$

### 2. Balance Updating Rule
The system tracks each friend's balance in a hash map `expenses`:
- For every non-paying participant $p_i \in S \setminus \{P\}$:
  $$\text{balance}[p_i] \leftarrow \text{balance}[p_i] + \frac{A}{|S|} \quad \text{(participant owes)}$$
- For the payer $P$:
  $$\text{balance}[P] \leftarrow \text{balance}[P] - \left(|S \setminus \{P\}| \times \frac{A}{|S|}\right) \quad \text{(payer is owed)}$$

### 3. Settlement Interpretation
At the end of all transactions:
- **$\text{Balance} > 0$:** The person has consumed more than they contributed $\rightarrow$ **Owes money**.
- **$\text{Balance} < 0$:** The person paid for others $\rightarrow$ **Needs to be reimbursed** $| \text{Balance} |$.
- **$\text{Balance} = 0$:** The person is **fully settled up**.

---

## Step-by-Step Worked Example

### Group Members: `["Alice", "Bob", "Carol"]`

| # | Expense Description | Payer | Amount | Participants | Split Per Person | Balance State After Expense |
|:---:|---|:---:|:---:|:---:|:---:|---|
| **1** | Hotel Accommodation | Alice | ₹900 | Alice, Bob, Carol | ₹300 each | Alice: **-₹600** (owed)<br>Bob: **+₹300** (owes)<br>Carol: **+₹300** (owes) |
| **2** | Lunch & Meals | Bob | ₹300 | Alice, Bob, Carol | ₹100 each | Alice: **-₹500** (owed)<br>Bob: **+₹100** (owes)<br>Carol: **+₹400** (owes) |
| **3** | Fuel / Cab Fare | Carol | ₹200 | Alice, Carol | ₹100 each | Alice: **-₹400** (owed)<br>Bob: **+₹100** (owes)<br>Carol: **+₹300** (owes) |

### Final Output:
```text
Final Settlement:
Alice needs to be reimbursed: Rs.400.00
Bob owes: Rs.100.00
Carol owes: Rs.300.00
```
$$\text{Reimbursement Check: } \text{Total Owed (Bob: ₹100 + Carol: ₹300)} = \text{Total Reimbursed (Alice: ₹400)} \quad \checkmark$$

---

## Dataset Specifications

`easy_expenses.csv` provides sample group transactions:

| Column | Type | Description |
|---|---|---|
| `id` | Integer | Transaction identifier |
| `date` | String | Transaction date (`DD-MM-YYYY`) |
| `description` | String | Expense description (`Hotel`, `Lunch`, `Taxi`) |
| `payer` | String | Member who made the payment |
| `amount` | Float | Transaction total amount |
| `category` | String | Classification (`Stay`, `Food`, `Travel`) |
| `participants` | String | Pipe-delimited list of beneficiaries |
| `split_weights` | String | Equal or weighted split ratios |
| `status` | String | Payment status (`paid`, `refund`, `unpaid`) |

---

## Technologies Used

- **Language:** Python 3.7+
- **Standard Library Modules:** `sys`, `typing`, `math`
- **Optional Notebook Environment:** Jupyter Notebook / JupyterLab (`pandas`, `matplotlib` optional for notebook visualization)

---

## Setup & Installation

### Prerequisites
- Python 3.x installed

### 1. Clone the Repository
```bash
git clone https://github.com/jayakumarjk2007/Data-Science--Google-Pay-Expense-Sharing.git
cd Data-Science--Google-Pay-Expense-Sharing
```

### 2. Zero-Dependency Run
No package installations or virtual environments are needed to execute the application!

---

## Usage Instructions

### Run the Interactive CLI Script
```bash
python expense_sharing.py
```
**Interactive Prompt Flow:**
```text
Enter the names of friends, separated by commas: Alice, Bob, Carol
Enter the name of the person who paid (or 'done' to finish): Alice
Enter the amount paid: 900
Enter the names of participants for this expense, separated by commas: Alice, Bob, Carol
Enter the name of the person who paid (or 'done' to finish): Bob
Enter the amount paid: 300
Enter the names of participants for this expense, separated by commas: Alice, Bob, Carol
Enter the name of the person who paid (or 'done' to finish): Carol
Enter the amount paid: 200
Enter the names of participants for this expense, separated by commas: Alice, Carol
Enter the name of the person who paid (or 'done' to finish): done

Final Settlement:
Alice needs to be reimbursed: Rs.400.00
Bob owes: Rs.100.00
Carol owes: Rs.300.00
```

### Run the Interactive Notebook
```bash
pip install jupyter
jupyter notebook GooglePay_Expense_Sharing.ipynb
```

---

## Author & Acknowledgments

- **Author:** Jayakumar P
- **GitHub:** [@jayakumarjk2007](https://github.com/jayakumarjk2007)
- **Concept:** Inspired by Google Pay Bill Split and Splitwise peer-to-peer settlement architecture.
