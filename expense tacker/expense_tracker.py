
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

        try:
            with open("expenses.csv", "r") as file:
                for line in file:
                    amount, category, note = line.strip().split(",")
                    self.expenses.append({
                         "amount": float(amount),
                         "category": category,
                         "note": note
                           })
        except FileNotFoundError:
            pass

    def add_expense(self,  amount, category, note):
        expense = {
            "amount": amount,
            "category": category,
            "note": note
        }
        self.expenses.append(expense)

        with open("expenses.csv", "a") as file:
            file.write(f"{amount},{category},{note}\n")
            print("Expense added & saved successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nRecorded Expenses:")

        for exp in self.expenses:
            print(f"expenses: inr.{exp['amount']}, category: {exp['category']}, note: {exp['note']}")

    def total_expenses(self):
        total = 0
        for exp in self.expenses:
            total += exp['amount']
        print(f"Total Expenses: inr.{total}")

    def categorywise_expenses(self):
        category_total = {}
        for exp in self.expenses:
            category = exp['category']
            if category in category_total:
                category_total[category] += exp['amount']
            else:
                category_total[category] = exp['amount']

        print("\nCategory-wise Expenses:")
        for category, total in category_total.items():
            print(f"Category: {category}, Total: inr.{total}")



tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category-wise Expenses")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        try:
            amount = float(input("enter amount:"))
            category = input("enter category:")
            note = input("enter note:")
            tracker.add_expense(amount, category, note)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    elif choice == '2':
        tracker.view_expenses()
    elif choice == '3':
        tracker.total_expenses()
    elif choice == '4':
        tracker.categorywise_expenses()
    elif choice == '5':
        print("Exiting Expense Tracker. Goodbye!")
        break

