correct_pin = '1234ty'
attempt = 0

logged_in = False
current_balance = 100000
while attempt < 3:
   
    pin = input("Enter your PIN: ")
   
    if pin == correct_pin:
        print("Valid Pin")
        logged_in = True
        break
    else:
        print("Invalid Pin")
        attempt += 1

if logged_in:
    print("Login Successful")

   
    while True:
        print("==== ATM MENU ====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Current Balance: {current_balance} CFA")

        elif choice == "2":
            deposit = int(input("Enter deposit amount: "))
            
            if deposit <= 0:
                print("Invalid Amount")
            else:
                current_balance += deposit
                print(f"New Balance: {current_balance} CFA")

        elif choice == "3":
            withdrawal = int(input("Enter withdrawal amount: "))

            if withdrawal <= 0:
                print("Invalid Amount")
            elif withdrawal > current_balance:
                print("Insufficient Balance")
            else:
                current_balance -= withdrawal
                print(f"New Balance: {current_balance} CFA")

        elif choice == "4":
            entered_pin = input(f"Enter your current pin: ")

            if correct_pin == entered_pin:
                new_pin = input("Enter your new pin: ")

                if len(new_pin) == 4:
                    correct_pin = new_pin   
                    print("PIN change succesfully")
                else:
                    print("Invalid pin")    

            else:
                print("Incorrect pin")
                

        elif choice == "5":
            print("Thank you for Using the ATM")
            break
        else:
            print("Invalid choice")
else:
    print("Access Denied")