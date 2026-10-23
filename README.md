# Expense Tracker

## Description
A Python command-line application that records expenses and generates spending summaries.

## Features
- Record date, category, description, and amount.
- Validate dates and numerical amounts.
- View all recorded expenses.
- Calculate total spending.
- Generate category-wise spending summaries with percentages.
- View expenses and totals for a particular date.
- Store expenses in a JSON file for future use.

## Requirements
- Python 3.8 or later
- No external libraries required.

## How to Run
1. Save the program as `expense_tracker.py`.
2. Open a terminal in the project folder.
3. Run:

   `python expense_tracker.py`

4. Select an option from the menu.

## Data Storage
Expenses are stored in `expenses.json`, which is created automatically when the first expense is saved.

## Concepts Used
- Functions
- Lists and dictionaries
- Loops and conditional statements
- Exception handling
- JSON file handling
- Date validation
- `defaultdict` for category-wise totals

## Example Summary
Total expenses: ₹1,500.00

- Food: ₹500.00 (33.3%)
- Travel: ₹700.00 (46.7%)
- Education: ₹300.00 (20.0%)

## Future Improvements
- Monthly spending reports
- Budget limits and alerts
- Edit and delete expenses
- Export reports to CSV
