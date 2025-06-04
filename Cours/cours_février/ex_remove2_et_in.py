numbers = [1,1,2,2,3,3,4,4,5,5]
print(numbers)
n = int(input("Entrez un nombre: "))
while n in numbers:
    numbers.remove(n)
# Il manque un bout pour finir cet exemple