from database import Bank

class BankingApp:
    def __init__(self):
        self.bank = Bank()

    def create_account(self, name):
        return self.bank.create_account(name)

    def delete_account(self, name):
        return self.bank.delete_account(name)

    def deposit(self, name, amount):
        account = self.bank.get_account(name)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, name, amount):
        account = self.bank.get_account(name)
        if account:
            return account.withdraw(amount)
        return False

    def get_balance(self, name):
        account = self.bank.get_account(name)
        if account:
            return account.get_balance()
        return None

    def get_all_accounts(self):
        return self.bank.get_all_accounts()
