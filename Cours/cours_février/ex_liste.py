# On va choisir un No. d'index au hasard.
from random import randint

# (On annonce une constante (la liste) en l'écrivant en MAJUSCULES.)
LISTE_EXHAUSTIVE = ["Rohru", "Zelda", "Link", "Saria", "Le gars du moulin", "Ganon"]
random_index =  randint(0, len(LISTE_EXHAUSTIVE) - 1)
print(LISTE_EXHAUSTIVE)
print(random_index)
# On affiche le mot désigné par le No. d'index pris au hasard.
print(LISTE_EXHAUSTIVE[random_index])

# On aurait aussi pu automatiser le comptage et la randomisation en faisant random_index =  randint(0, LISTE_EXHAUSTIVE - 1)