class ExpenseSharing:
    def __init__(self, friends):
        self.friends = friends
        self.expenses = {friend: 0 for friend in friends}

    def add_expense(self, payer, amount, participants):
        split_amount = amount / len(participants)
        for participant in participants:
            if participant != payer:
                self.expenses[participant] += split_amount
                self.expenses[payer] -= split_amount

    def calculate_settlement(self):
        for friend, balance in self.expenses.items():
            if balance > 0:
                print(f"{friend} owes: Rs.{balance:.2f}")
            elif balance < 0:
                print(f"{friend} needs to be reimbursed: Rs.{-balance:.2f}")
            else:
                print(f"{friend} is settled up.")


if __name__ == "__main__":

    friends = input("Enter the names of friends, separated by commas: ").split(",")
    friends = [friend.strip() for friend in friends]

    expense_sharing = ExpenseSharing(friends)

    while True:
        payer = input("Enter the name of the person who paid (or 'done' to finish): ")
        if payer.lower() == "done":
            break

        amount = float(input("Enter the amount paid:"))

        participants = input("Enter the names of participants for this expense, separated by commas: ").split(",")
        participants = [participant.strip() for participant in participants]

        expense_sharing.add_expense(payer, amount, participants)

    print("\nFinal Settlement:")
    expense_sharing.calculate_settlement()
