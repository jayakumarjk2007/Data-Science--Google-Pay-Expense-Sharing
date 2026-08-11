import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


class ExpenseSharing:
    def __init__(self, friends):
        self.friends = friends
        self.balances = {friend: 0 for friend in friends}
        self.expenses = []

    def add_expense(self, payer, amount, participants, description, category):
        if payer not in self.friends:
            raise ValueError("Payer name is not in the friends list.")
        if not participants:
            raise ValueError("At least one participant is needed.")
        if any(person not in self.friends for person in participants):
            raise ValueError("One of the participants is not in the friends list.")

        amount = float(amount)
        split_amount = amount / len(participants)

        # I save every expense here so I can make a table and graphs later.
        self.expenses.append(
            {
                "Description": description,
                "Payer": payer,
                "Amount": amount,
                "Category": category,
                "Participants": ", ".join(participants),
            }
        )

        # The payer paid the full bill.
        self.balances[payer] += amount

        # Then each person pays their own share.
        for person in participants:
            self.balances[person] -= split_amount

    def load_expenses_from_csv(self, filename):
        data = pd.read_csv(filename)

        for _, row in data.iterrows():
            participants = row["participants"].split("|")
            self.add_expense(
                row["payer"],
                row["amount"],
                participants,
                row["description"],
                row["category"],
            )

        return data

    def show_balances(self):
        print("\nBalances:")
        for friend, balance in self.balances.items():
            balance = round(balance, 2)
            if balance > 0:
                print(f"{friend} should receive Rs. {balance:.2f}")
            elif balance < 0:
                print(f"{friend} owes Rs. {-balance:.2f}")
            else:
                print(f"{friend} is settled up")

    def calculate_settlement(self):
        creditors = []
        debtors = []

        for friend, balance in self.balances.items():
            balance = round(balance, 2)
            if balance > 0:
                creditors.append([friend, balance])
            elif balance < 0:
                debtors.append([friend, -balance])

        payments = []
        debtor_index = 0
        creditor_index = 0

        while debtor_index < len(debtors) and creditor_index < len(creditors):
            debtor, amount_owed = debtors[debtor_index]
            creditor, amount_to_receive = creditors[creditor_index]
            payment = round(min(amount_owed, amount_to_receive), 2)
            payments.append((debtor, creditor, payment))

            debtors[debtor_index][1] = round(amount_owed - payment, 2)
            creditors[creditor_index][1] = round(amount_to_receive - payment, 2)

            if debtors[debtor_index][1] == 0:
                debtor_index += 1
            if creditors[creditor_index][1] == 0:
                creditor_index += 1

        return payments

    def save_analysis(self, output_folder):
        data = pd.DataFrame(self.expenses)
        data.to_csv(f"{output_folder}/expense_data_used.csv", index=False)

        # These two lines give the main data analysis for the project.
        category_totals = data.groupby("Category")["Amount"].sum()
        payer_totals = data.groupby("Payer")["Amount"].sum()

        category_totals.to_csv(f"{output_folder}/spending_by_category.csv")
        payer_totals.to_csv(f"{output_folder}/spending_by_payer.csv")

        # I used NumPy to find the average expense.
        average_expense = round(np.mean(data["Amount"]), 2)
        summary = pd.DataFrame(
            {
                "Metric": ["Number of expenses", "Total group expense", "Average expense"],
                "Value (Rs.)": [len(data), round(data["Amount"].sum(), 2), average_expense],
            }
        )
        summary.to_csv(f"{output_folder}/project_summary.csv", index=False)

        balance_data = pd.DataFrame(
            {
                "Friend": list(self.balances.keys()),
                "Balance": [round(value, 2) for value in self.balances.values()],
            }
        )
        balance_data.to_csv(f"{output_folder}/user_balances.csv", index=False)

        plt.figure(figsize=(7, 4))
        category_totals.plot(kind="bar", color="skyblue")
        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount (Rs.)")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(f"{output_folder}/spending_by_category.png")
        plt.close()

        plt.figure(figsize=(7, 4))
        payer_totals.plot(kind="bar", color="lightgreen")
        plt.title("Amount Paid by Each Friend")
        plt.xlabel("Friend")
        plt.ylabel("Amount (Rs.)")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(f"{output_folder}/spending_by_payer.png")
        plt.close()

        return data, category_totals, payer_totals, balance_data, summary
