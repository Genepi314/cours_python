a = "11"
print(int(a) + 1)
# Ici après, on aura un message d'erreur pour ces 2 lignes:
# b = "ten"
# print(int(b))
# car "ten" n'est pas considéré comme un chiffre qu'il peut lire en base 10 (!)
# Par contre, on peut dire à l'ordi de changer de base
b = "ff"
print(int(b,16))
