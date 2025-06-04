scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

player_name = input("Hello ! Choisis un pseudo : ")
player_score = int(input("Quel est ton score ? "))

scores[player_name] = player_score
# print(scores)

# Ici il y a un souci... revoir les parenthèses etc
# print("Elocin03: " + str(scores["Elocin03"]))
# print(f"{player_name}: {scores[player_name]}")

for name, score in scores.items():
    print(name + ": " + str(score))