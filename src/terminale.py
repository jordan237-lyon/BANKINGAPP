from banking import BankingApp

def run_terminale():
    app = BankingApp()
    
    while True:
        print("\n--- Menu Principal ---")
        print("1. Créer un compte")
        print("2. Supprimer un compte")
        print("3. Déposer de l'argent")
        print("4. Retirer de l'argent")
        print("5. Consulter le solde")
        print("6. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            name = input("Entrez le nom du compte : ")
            if app.create_account(name):
                print(f"Compte {name} créé avec succès.")
            else:
                print("Le compte existe déjà.")
        
        elif choice == "2":
            name = input("Entrez le nom du compte : ")
            if app.delete_account(name):
                print(f"Compte {name} supprimé avec succès.")
            else:
                print("Compte non trouvé.")
        
        elif choice == "3":
            name = input("Entrez le nom du compte : ")
            amount = float(input("Entrez le montant à déposer : "))
            if app.deposit(name, amount):
                print(f"{amount} a été déposé sur le compte {name}.")
            else:
                print("Dépôt échoué.")
        
        elif choice == "4":
            name = input("Entrez le nom du compte : ")
            amount = float(input("Entrez le montant à retirer : "))
            if app.withdraw(name, amount):
                print(f"{amount} a été retiré du compte {name}.")
            else:
                print("Retrait échoué.")
        
        elif choice == "5":
            name = input("Entrez le nom du compte : ")
            balance = app.get_balance(name)
            if balance is not None:
                print(f"Solde du compte {name} : {balance}")
            else:
                print("Compte non trouvé.")
        
        elif choice == "6":
            print("Merci d'avoir utilisé l'application bancaire.")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")
