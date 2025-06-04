number = input("Nombre: ")
number = int(number)

previous_number = None

sum_numbers = number

while number != previous_number:
    previous_number = number
    number = input("Nombre: ")
    number = int(number)

    sum_numbers += number

print(f"La somme des nombres est de {sum_numbers}")