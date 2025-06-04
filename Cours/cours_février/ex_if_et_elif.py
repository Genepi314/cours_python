n = int(input("Choose a number between 1 and 10: "))

if n > 10:
    print("score acceptable")
elif n > 7:
    print("score correct")
elif n > 4:
    print("score acceptable")
else:
    print("score insuffisant")
# Ici, on verra que si on entre le chiffre 5 par exemple, il va passer par la première condition (F), puis la 2de (F), puis à la 3ème, la condition étant True, on rentre dans ce elif. 
# On s'arrête à cette 3ème condition sans réaliser le else.  
# On n'a pas besoin de revérifier les conditions précédentes, car python lit les conditions dans l'ordre. On n'arrivera pas à la 3ème condition sans respecter les 2 premières.