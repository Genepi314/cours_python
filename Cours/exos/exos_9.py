from random import randint
random_1 = randint(1,6)
random_2 = randint(1,6)
random_3 = randint(1,6)


while not (random_1 == random_2 and random_2 == random_3):
    random_1 = randint(1,6)
    random_2 = randint(1,6)
    random_3 = randint(1,6)
    print(f"{random_1, random_2, random_3}")
else:
    print("Youhou")

# while a != b or b != c est l'équivalent de la condition:
# while not(a == b and b ==c)

