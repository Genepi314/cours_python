# On choisit un nombre au hasard.
from random import randint
guess_number = randint(1,10)
# Pour vérifier le code : print(guess_number)

#  On définit qu'il y aura un nombre fini d'entrées.
entry = 1

#  On demande à l'utilisateur de choisir un nombre.
user_number = int(input("Donne un nombre entre 1 et 10: "))

while user_number != guess_number and entry < 3:
    if user_number > guess_number:
        print("Trop grand.")
    else:
        print("Trop petit.")
    user_number = int(input("Recommence: "))
    entry = entry + 1
    # on peut aussi écrire entry += 1, c'est pareil.

if user_number == guess_number:
    print("Félicitations!")
else:
    print("Vous avez atteint le nombre maximum d'entrées. Le bon nombre était " + str(guess_number))
