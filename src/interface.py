import tkinter as tk
from tkinter import messagebox
from banking import BankingApp

class BankApp:
    def __init__(self, root):
        self.app = BankingApp()
        self.root = root
        self.root.title("Application Bancaire")

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Nom du compte:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        self.create_button = tk.Button(self.root, text="Créer un compte", command=self.create_account)
        self.create_button.grid(row=0, column=2)

        self.delete_button = tk.Button(self.root, text="Supprimer un compte", command=self.delete_account)
        self.delete_button.grid(row=0, column=3)

        self.balance_label = tk.Label(self.root, text="Montant:")
        self.balance_label.grid(row=1, column=0)

        self.balance_entry = tk.Entry(self.root)
        self.balance_entry.grid(row=1, column=1)

        self.deposit_button = tk.Button(self.root, text="Déposer", command=self.deposit)
        self.deposit_button.grid(row=1, column=2)

        self.withdraw_button = tk.Button(self.root, text="Retirer", command=self.withdraw)
        self.withdraw_button.grid(row=1, column=3)

        self.account_info_button = tk.Button(self.root, text="Consulter le solde", command=self.get_balance)
        self.account_info_button.grid(row=2, column=0, columnspan=2)

        self.all_accounts_button = tk.Button(self.root, text="Consulter tous les comptes", command=self.get_all_accounts)
        self.all_accounts_button.grid(row=2, column=2, columnspan=2)

    def create_account(self):
        name = self.name_entry.get()
        if self.app.create_account(name):
            messagebox.showinfo("Succès", f"Compte {name} créé avec succès.")
        else:
            messagebox.showwarning("Erreur", "Le compte existe déjà.")

    def delete_account(self):
        name = self.name_entry.get()
        if self.app.delete_account(name):
            messagebox.showinfo("Succès", f"Compte {name} supprimé avec succès.")
        else:
            messagebox.showwarning("Erreur", "Compte non trouvé.")

    def deposit(self):
        name = self.name_entry.get()
        try:
            amount = float(self.balance_entry.get())
        except ValueError:
            messagebox.showwarning("Erreur", "Montant invalide.")
            return

        if self.app.deposit(name, amount):
            messagebox.showinfo("Succès", f"{amount} a été déposé sur le compte {name}.")
        else:
            messagebox.showwarning("Erreur", "Dépôt échoué.")

    def withdraw(self):
        name = self.name_entry.get()
        try:
            amount = float(self.balance_entry.get())
        except ValueError:
            messagebox.showwarning("Erreur", "Montant invalide.")
            return

        if self.app.withdraw(name, amount):
            messagebox.showinfo("Succès", f"{amount} a été retiré du compte {name}.")
        else:
            messagebox.showwarning("Erreur", "Retrait échoué.")

    def get_balance(self):
        name = self.name_entry.get()
        balance = self.app.get_balance(name)
        if balance is not None:
            messagebox.showinfo("Solde", f"Solde du compte {name} : {balance}")
        else:
            messagebox.showwarning("Erreur", "Compte non trouvé.")

    def get_all_accounts(self):
        accounts = self.app.get_all_accounts()
        all_accounts_str = "\n".join([f"Compte {account.name} : {account.get_balance()}" for account in accounts])
        messagebox.showinfo("Tous les Comptes", all_accounts_str)

def run_interface():
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()

