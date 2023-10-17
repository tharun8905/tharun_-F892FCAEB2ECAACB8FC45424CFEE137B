class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Holder: {self._account_holder_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Account Balance: ${self._account_balance}")

# Example usage of the BankAccount class
if _name_ == "_main_":
    account = BankAccount("123456", "John Doe", 1000.0)
    
    account.display_balance()  # Display initial balance
    
    account.deposit(500)       # Deposit $500
    account.withdraw(200)     # Withdraw $200
    
    account.display_balance()  # Display updated balance