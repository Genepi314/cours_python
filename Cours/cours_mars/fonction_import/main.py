import secondary
from secondary import location
# from secondary import  *
# ceci en haut est autre manière d'importer TOUT de secondary, mais il ne faudra plus préciser secondar.qqch, mettre le nom de la variable directement suffira

def weird():
    print(f"course: {secondary.course}")

# weird
# Je ne sais plus pourquoi ça ne marche pas de juste appeler weird...

# Ici, on réassigne une valeur à la variable course SANS la changer dans secondary
course = "Initiation à la programmation"

print(secondary.location)
print(secondary.course)

# Ici on imprimera seulement la variable course du fichier principal
print(course)
# Par contre ici, comme on a écrit from secondary import location, il va le chercher dans secondary sans devoir le préciser
print(location)

print(secondary.double(17))




