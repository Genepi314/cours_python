liste = []
new_word = input("Entrez un mot: ")

while new_word != "stop":
    liste.append(new_word)
    new_word = input("Un autre: ")

print(liste)