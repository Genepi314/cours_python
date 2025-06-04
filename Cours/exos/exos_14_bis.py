word = None
count_words = 0

while word != "end":
    word = input("Mot: ")
    count_words += 1
    if word[0] == "t":
        print(f"{word}!!!")

print(f"Nombre de mots: {count_words}")