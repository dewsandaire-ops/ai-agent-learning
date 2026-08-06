class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(self.owner)
        print("Balance:", self.balance)

account = BankAccount("John", 1000)

account.deposit(500)

account.show_balance()