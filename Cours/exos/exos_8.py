password = "Pyth0n"
user_entry = input("Entrez le mot de passe: ")
entry_number = 1

while user_entry != password and entry_number < 3:
    print("Mauvais mot de passe.")
    user_entry = input("Entrez le mot de passe: ")
    entry_number += 1
if user_entry == password:
    print("C'est bien le mot de passe.")
else:
    print("Raté. Recommencez demain")

