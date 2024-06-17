class Account:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account({self.name}, {self.balance})"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name in self.accounts:
            return False
        self.accounts[name] = Account(name)
        return True

    def delete_account(self, name):
        if name in self.accounts:
            del self.accounts[name]
            return True
        return False

    def get_account(self, name):
        return self.accounts.get(name)

    def get_all_accounts(self):
        return self.accounts.values()