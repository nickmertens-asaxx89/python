class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        self._balance += amount
        return f"Deposited {amount}. New balance: {self._balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return f"Withdrew {amount}. New balance: {self._balance}"

    def check_balance(self):
        return f"Balance: {self._balance}"
    
account = BankAccount("Sarah", 1000)

print(account.deposit(50))
print(account.withdraw(30))
print(account.check_balance())
