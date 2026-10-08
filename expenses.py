expenses = []
while True:
    try:
        expense = input("Enter an amount (Or done to finish): ")
        if expense == "done":
            break
        expenses.append(float(expense))
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")
print(f"Number of expenses: {len(expenses)}")
print(f"Total expenses: {sum(expenses):.2f}")
for expense in expenses:
    print(f"Expense: {expense:.2f}")
