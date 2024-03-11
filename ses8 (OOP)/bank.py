class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        
class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Account:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")


## ----- testing data -----
# Create bank
bank = Bank("Danske Bank")
bank2 = Bank("Nordea")
bank3 = Bank("Nykredit")

# Create customers
customer1 = Customer("John Doe", "Bygade 5", "+45 4040201")
customer2 = Customer("Jane Smith", "Strandgade 17", "+45 65129503")

# Create accounts
account1 = Account("123456", 170899, customer1)
account2 = Account("123457", 6650, customer1)
account3 = Account("789012", 12505, customer2)


# Add accounts to the bank
bank.add_account(account1)
bank.add_account(account2)

# Print bank's account details
for account in bank.accounts:
    print(f"Account Number: {account.account_number}, Balance: {account.balance}, Owner: {account.owner.name}")
