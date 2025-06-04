number = input("Nombre: ")
number = int(number)

greater = number
lower = number

while number != 0:
    number = input("Nombre: ")
    number = int(number)

    if number > greater:
        greater = number
    elif number < lower:
        lower = number

print(f"Plus grand: {greater}")
print(f"Plus petit: {lower}")