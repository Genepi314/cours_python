from random import randint

code = []
letters = ["a","b","c","d","e","f"]

for i in range(4): # par convention, quand on n'utilise pas la variable i, on l'écrit "_"
    index = randint(0, len(letters) - 1)
    code.append(letters[index])
print(code)

tentative = input("Devine le code en écrivant 4 lettres choisies entre a et f: ")
if len(tentative) != 4:
    input("Entrez bien 4 lettres: ")
else:
    list(tentative)
    print(list(tentative))
