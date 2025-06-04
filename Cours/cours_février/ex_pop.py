nombres = [1,1,2,2,3,3,4,4,5,5]
print(nombres)
while nombres != []: 
# On aurait aussi pu écrire while nombres:
    removed = nombres.pop(0)
    print(removed)
    print(nombres)