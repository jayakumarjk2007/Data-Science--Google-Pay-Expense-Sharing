from expense_sharing import ExpenseSharing

DATA_FILE = "data/sample_expenses.csv"
OUTPUT_FOLDER = "generated"


def main():
    friends = ["Alice", "Bob", "Carol"]
    expense_sharing = ExpenseSharing(friends)

    # Read the CSV, calculate balances, then create charts and result files.
    expense_sharing.load_expenses_from_csv(DATA_FILE)
    expense_sharing.show_balances()

    payments = expense_sharing.calculate_settlement()
    print("\nFinal Settlement:")
    for debtor, creditor, amount in payments:
        print(f"{debtor} pays {creditor}: Rs. {amount:.2f}")

    _, _, _, _, summary = expense_sharing.save_analysis(OUTPUT_FOLDER)
    print("\nProject summary:")
    print(summary.to_string(index=False))

    # Save the final payments in a simple text file too.
    with open("generated/final_settlement.txt", "w", encoding="utf-8") as file:
        file.write("Final Settlement\n")
        for debtor, creditor, amount in payments:
            file.write(f"{debtor} pays {creditor}: Rs. {amount:.2f}\n")

    print("\nCharts and CSV result files were saved in the generated folder.")


if __name__ == "__main__":
    main()
