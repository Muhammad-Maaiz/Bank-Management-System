# BANK MANAGEMENT SYSTEM:

print("*** WELCOME TO THE ABC BANK ***".center(120))
password = int(input("Enter your four-digit password: "))    
balance = int(input("Enter your Balance: "))

while True:
    print("\n*** Menu ***")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print(f"Your current Balance is: {balance}")

    elif choice == 2:
        deposit_amount = int(input("Enter the deposit amount: "))
        balance += deposit_amount
        print(f"Deposit successful. Your current Balance is: {balance}")

    elif choice == 3:
        withdraw_amount = int(input("Enter the withdrawal amount: "))
        if withdraw_amount <= balance:
          balance -= withdraw_amount
          print(f"Withdrawal successful. Your current Balance is: {balance}")
        else:
          print("Insufficient balance.")

    elif choice == 4:
        print("Thank you for using ABC Bank.")
        break

    else:
        print("Invalid choice. Please select a valid choice.")