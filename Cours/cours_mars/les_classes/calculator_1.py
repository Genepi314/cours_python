class Calculator:

    def __init__(self):
        self.result = 0

# Ici on fait une def "compteur" plutôt qu'une calculette
    def add(self):
        self.result += 1

calc = Calculator()
print(type(calc))
print(calc.result)


calc.add()
calc.add()
print(calc.result)
# result est gardé ! Il est dans la classe.

# Ici python va aimablement nous donner toutes ses infos sur calc, càd où il se trouve dans la mémoire de l'ordi
# pratique pour savoir si un objet est différent d'un autre de la même classe
print(calc)
calc2 = Calculator()
print(calc2)

# Il faut revoir ce que ceci veut dire !!!
# En gros, ceci transforme un résultat en string... à revoir
#    def __str__(self):
#       return f"Calculator with result: {self.result}"
