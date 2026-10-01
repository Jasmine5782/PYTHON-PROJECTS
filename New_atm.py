correct_pin = ("1234")
attempt = 0
current_balance = 100000

while True:
    entered_pin = input("Enter your PIN: ")
    if correct_pin == entered_pin:
        
        print("Login Successfully")

        print("====ATM MACHINE====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Change Pin")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your Balance is {current_balance} CFA")


        elif choice == "2":
            withdraw = int(input("Enter amount to withdraw: "))
            current_balance -= withdraw
            print(f"Your Balance is {current_balance} CFA")

        elif choice == "3":
            old_pin = input("Enter old pin: ")
            if old_pin == correct_pin:
                new_pin = input("Enter new pin: ")
                print("Pin changed successfully")
            else:
                print("Incorrect Pin")
        
        elif choice == "4":
            transfer_amount = int(input("Amount to transfer: "))
            current_balance -= transfer_amount
            print(f"Current Balance {current_balance} CFA")

        elif choice == "5":
            print(current_balance)
        
        elif choice == "6":
            print("Thank you for using our service")
        else:
            print("Invalid choice")
            


    else:
        print("Access Denied")
