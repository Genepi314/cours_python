nombres = [1,1,2,2,3,3,4,4,5,5]
while nombres != []:
    print(nombres)
    dead_number = int(input("Choisissez un nombre: "))
    nombres.remove(dead_number)
    