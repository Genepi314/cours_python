word_list = ["I", "really", "love", "Python"]
word_types = ["pronoun", "adverb", "verbe", "noun"]
for word in word_list:
    print(word)

# Ici, "exo" n'est pas considéré comme un nombre (genre 4), mais comme UNE LISTE (!!!)
# Cela fonctionne donc comme dans "for i in range(10)" par exemple. "for i in 10" ne fonctionnerait pas !
#  i ne doit pas forcément s'appeler i. Il s'agit simplement nom de la variable dans laquelle on va itérer.

for i in range(len(word_list)):
    print(word_list[i], word_types[i])