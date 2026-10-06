expenses = []
while True:

    print("==== EXPENSE TRACKER ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Choose an option: ")


    if choice == "1":
        print("Add Expenses Selected: ")
        name = input("Enter expense name: ")
        amount = int(input("Enter expenses amount: "))

        expense = {
                "name": name,
                "amount": amount
            }

        expenses.append(expense)

    elif choice == "2":
        print("View Expenses selected: ")

        for expense in expenses:
                print(f"Expense Name: {expense['name']}, Amount: {expense['amount']}")

    elif choice == "3": 
        print("Total Expenses selected")

        total = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: {total}")

    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid option selected")
    