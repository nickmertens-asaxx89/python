class BankAccount:
    def __init__(self, account_id, owner):
        self.account_id = account_id
        self.owner = owner
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")
        return "Deposit successful"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        self.transactions.append(f"Withdraw: -{amount}")
        return "Withdraw successful"

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.transactions
    
class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_id):
        if account_id in self.accounts:
            return None
        acc = BankAccount(account_id, self.name)
        self.accounts[account_id] = acc
        return acc

    def get_account(self, account_id):
        return self.accounts.get(account_id)
    
class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name):
        if name in self.customers:
            return False
        self.customers[name] = Customer(name)
        return True

    def get_customer(self, name):
        return self.customers.get(name)

    def transfer(self, acc1, acc2, amount):
        if amount <= 0:
            return "Invalid amount"
        if acc1.balance < amount:
            return "Insufficient funds"

        acc1.withdraw(amount)
        acc2.deposit(amount)
        return "Transfer successful"
    
def main():
    bank = Bank()

    while True:
        print("\n🏦 MINI BANK SYSTEM")
        print("1. Add customer")
        print("2. Create account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Check balance")
        print("7. Transaction history")
        print("8. Exit")

        choice = input("Choose an option: ")

        # 1. Add customer
        if choice == "1":
            name = input("Customer name: ")
            if bank.add_customer(name):
                print("Customer added")
            else:
                print("Customer already exists")

        # 2. Create account
        elif choice == "2":
            name = input("Customer name: ")
            customer = bank.get_customer(name)
            if not customer:
                print("Customer not found")
                continue

            acc_id = input("Account ID: ")
            acc = customer.create_account(acc_id)
            if acc:
                print("Account created")
            else:
                print("Account already exists")

        # 3. Deposit
        elif choice == "3":
            name = input("Customer name: ")
            acc_id = input("Account ID: ")
            amount = float(input("Amount: "))

            customer = bank.get_customer(name)
            if customer:
                acc = customer.get_account(acc_id)
                if acc:
                    print(acc.deposit(amount))
                else:
                    print("Account not found")

        # 4. Withdraw
        elif choice == "4":
            name = input("Customer name: ")
            acc_id = input("Account ID: ")
            amount = float(input("Amount: "))

            customer = bank.get_customer(name)
            if customer:
                acc = customer.get_account(acc_id)
                if acc:
                    print(acc.withdraw(amount))
                else:
                    print("Account not found")

        # 5. Transfer
        elif choice == "5":
            n1 = input("From customer: ")
            a1 = input("From account: ")
            n2 = input("To customer: ")
            a2 = input("To account: ")
            amount = float(input("Amount: "))

            c1 = bank.get_customer(n1)
            c2 = bank.get_customer(n2)

            if c1 and c2:
                acc1 = c1.get_account(a1)
                acc2 = c2.get_account(a2)

                if acc1 and acc2:
                    print(bank.transfer(acc1, acc2, amount))
                else:
                    print("Account not found")

        # 6. Balance
        elif choice == "6":
            name = input("Customer name: ")
            acc_id = input("Account ID: ")

            customer = bank.get_customer(name)
            if customer:
                acc = customer.get_account(acc_id)
                if acc:
                    print("Balance:", acc.get_balance())

        # 7. History
        elif choice == "7":
            name = input("Customer name: ")
            acc_id = input("Account ID: ")

            customer = bank.get_customer(name)
            if customer:
                acc = customer.get_account(acc_id)
                if acc:
                    print("\n".join(acc.get_history()))

        # 8. Exit
        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
