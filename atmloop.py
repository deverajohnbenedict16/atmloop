balance = 0 
loop = True

print("--- Welcome to De Vera's ATM ---")

while loop:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")

    if choice == '1':
        print(f"Current Balance: ${balance:.2f}")

    elif choice == '2':
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid amount.")

    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

    elif choice == '4':
        print("Thank you for using our service. Goodbye!")
        loop = False 

    else:
        print("Invalid selection. Please try again.")