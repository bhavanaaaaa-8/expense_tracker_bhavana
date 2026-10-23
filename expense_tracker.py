
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

FILE_NAME = Path("expenses.json")


def load_expenses():
    if not FILE_NAME.exists():
        return []

    try:
        with FILE_NAME.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Could not read the expense file.")
        return []


def save_expenses(expenses):
    with FILE_NAME.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


def get_amount():
    while True:
        try:
            amount = float(input("Enter amount (₹): "))
            if amount > 0:
                return round(amount, 2)
            print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def add_expense(expenses):
    date = get_date()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    amount = get_amount()

    expense = {
        "date": date,
        "category": category.title(),
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- All Expenses ---")
    print(f"{'Date':<12} {'Category':<15} "
          f"{'Description':<25} {'Amount (₹)':>12}")
    print("-" * 68)

    for expense in sorted(expenses, key=lambda item: item["date"]):
        print(
            f"{expense['date']:<12} "
            f"{expense['category']:<15} "
            f"{expense['description'][:24]:<25} "
            f"{expense['amount']:>12.2f}"
        )


def spending_summary(expenses):
    if not expenses:
        print("No expenses available for summary.")
        return

    total = sum(item["amount"] for item in expenses)
    categories = defaultdict(float)

    for expense in expenses:
        categories[expense["category"]] += expense["amount"]

    print("\n--- Spending Summary ---")
    print(f"Total expenses: ₹{total:.2f}")
    print(f"Number of expenses: {len(expenses)}")

    print("\nSpending by category:")
    for category, amount in sorted(categories.items()):
        percentage = amount / total * 100
        print(f"{category}: ₹{amount:.2f} ({percentage:.1f}%)")


def daily_summary(expenses):
    date = get_date()
    daily_expenses = [
        item for item in expenses if item["date"] == date
    ]

    if not daily_expenses:
        print("No expenses found for this date.")
        return

    total = sum(item["amount"] for item in daily_expenses)

    print(f"\nExpenses on {date}:")
    for expense in daily_expenses:
        print(
            f"{expense['category']} - {expense['description']}: "
            f"₹{expense['amount']:.2f}"
        )

    print(f"Daily total: ₹{total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Overall Spending Summary")
        print("4. Daily Spending Summary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            spending_summary(expenses)
        elif choice == "4":
            daily_summary(expenses)
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
