def test(a, b):

    return 5, 6
# Ceci est un topple, pas une liste. On peut mettre les valeurs entre parenthèses (contrairement à entre crochets pour une liste).
# Ca veut dire que ce sont des données qui ont du sens uniquement par paires, comme des coordonnées.
# Ce commentaire sert à comprendre l'exemple :
# for key, value in inventory.items():
# print (key + " : "


#  --main--

d, m = test(5, 3)
print(d)
print(m)

#  ça marche aussi avec plus de valeurs.

x, y, z = [1, 2, 3]
print(x)