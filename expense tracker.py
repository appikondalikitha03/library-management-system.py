import random

# Expense categories
categories = ["Food", "Travel", "Shopping", "Entertainment", "Bills"]

expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))

        # Randomly choose a category
        category = random.choice(categories)

        expenses.append({"amount": amount, "category": category})

        print(f"Expense added under category: {category}")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ₹{expense['amount']} - {expense['category']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Expense: ₹{total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")