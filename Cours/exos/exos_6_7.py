note = int(input("Quelle note as-tu eue pour cet exercice? "))

while note > 10 or note < 0:
    print("Eh là, le nombre doit être compris entre un et dix... ")
    note = int(input("Recommence "))
else:
    if note == 10:
        print("Bravo!")
    elif note >= 8:
        print("Pas mal.")
    elif note >=5:
        print("Mouais, bof.")
    else:
        print("Pas terrible.")
