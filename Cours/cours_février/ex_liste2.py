NOMBRES = [1, 2, 3, 5, 7, 11, 13, 17]
user_index = int(input("Choisissez un nombre entre 1 et " + str((len(NOMBRES) - 1)) + ": "))
if user_index < 1 or user_index >= len(NOMBRES):
    print("Nope, ce nombre doit être compris entre 1 et " + str((len(NOMBRES) - 1)) + ".")
    user_index = int(input("Maintenant, soyez attentif. Choisissez un nombre entre 1 et " + str((len(NOMBRES) - 1)) + ": ")) 
print(NOMBRES)
print(NOMBRES[:user_index])
print(NOMBRES[user_index:(len(NOMBRES)-1)]) 

# user_index = int(input(f"Choisissez un nombre entre 1 et {len(NOMBRES) - 1) : }"))