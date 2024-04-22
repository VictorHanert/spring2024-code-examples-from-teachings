class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def sort_accounts_by_customer_and_amount(self):
        self._accounts = sorted(self._accounts, key=lambda x: (x.owner.name, x.balance))

    @property
    def name(self):
        return self._name

    @property
    def accounts(self):
        return self._accounts


class Customer:
    def __init__(self, name, address, phone_number, age):
        self._name = name
        self._address = address
        self._phone_number = phone_number
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @property
    def phone_number(self):
        return self._phone_number
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age >= 18:
            self._age = age
        else:
            raise ValueError('You must be 18 years old')

class Account:
    def __init__(self, account_number, balance, owner):
        self._account_number = account_number
        self._balance = balance
        self._owner = owner

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds")

# ----- testing data -----
# Create bank
bank = Bank("Danske Bank")
bank2 = Bank("Nordea")
bank3 = Bank("Nykredit")

# Create customers
customer1 = Customer("John Doe", "Bygade 5", "+45 4040201", 20)
customer2 = Customer("Jane Smith", "Strandgade 17", "+45 65129503", 47)

# Create accounts
account1 = Account("123456", 170899, customer1)
account2 = Account("123457", 0, customer1)
account3 = Account("785012", 12505, customer2)
account4 = Account("121416", 9910, customer1)
account5 = Account("143257", 10010, customer1)
account6 = Account("435932", 12900, customer2)

# Add accounts to the bank
bank.add_account(account1)
bank.add_account(account2)
bank.add_account(account3)
bank.add_account(account4)
bank.add_account(account5)
bank.add_account(account6)

# Print bank's account details
for account in bank.accounts:
    print(f"Account Number: {account.account_number}, Balance: {account.balance}, Owner: {account.owner.name}")