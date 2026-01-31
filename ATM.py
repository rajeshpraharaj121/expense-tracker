class bank_account:
    def __init__(self, account_holder, balance=0): # type: ignore
        self.account_holder = account_holder
        self.balance = balance
    
        self.pin_number = 1234
    

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance
# Example usage:
account = bank_account("rajesh", 1000) 


while True:
    pin = int(input("Enter your PIN to check balance: "))
    if pin == account.pin_number:
        print(f"Your balance is: {account.get_balance()}")
    
    else:
        print("Incorrect PIN. Try again.")
    print("\n1, Deposit\n2, Withdraw\n3, Check Balance\n4, Exit")
    choice = int(input("enter your choice: "))
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        pin = int(input("Enter your PIN to check balance: "))
        if pin == account.pin_number:
            print(f"Your balance is: {account.get_balance()}")
        else:
            print("Incorrect PIN. Try again.")
    elif choice == 4:
        print("Exiting...")
        break
    