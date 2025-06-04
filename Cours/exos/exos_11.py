from random import randint


n1 = randint(0, 100)
n2 = randint(0, 100)

answer = input(f"{n1} + {n2} = ")
answer = int(answer)

errors = 0

while answer != n1 + n2:
    errors = errors + 1
    answer = input(f"{n1} + {n2} = ")
    answer = int(answer)

print(f"Bravo, tu as trouvé la bonne réponses.\nTu as commis {errors} erreur(s).")