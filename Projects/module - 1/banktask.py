account = {
    "name": "",
    "type": "",
    "number": "",
    "balance": 0
}

def open_account():
    account["name"] = input("Enter Account Holder Name: ")
    account["type"] = input("Enter Account Type (Savings/Current): ")
    account["number"] = input("Enter Account Number: ")
    account["balance"] = 2000
    print("\nAccount Created Successfully with ₹2000 Minimum Balance.\n")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount >= 2000:
        account["balance"] += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{account['balance']}")
    else:
        print("Minimum deposit should be ₹2000.")

def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{account['balance']}")
    else:
        print("Insufficient balance.")

def statement():
    print("\n------ Account Statement ------")
    print(f"Account Holder: {account['name']}")
    print(f"Account Type: {account['type']}")
    print(f"Account Number: {account['number']}")
    print(f"Main Balance: ₹{account['balance']}")
    print("------------------------------\n")

while True:
    print("1. Open Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        open_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        statement()
    elif choice == 5:
        print("Thank you for using Banking System!")
        break
    else:
        print("Invalid choice, try again.")
