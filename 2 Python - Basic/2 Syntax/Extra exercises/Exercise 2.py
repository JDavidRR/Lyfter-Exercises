"""
EXERCISE 2
Cree un programa que pida 3 números al usuario. Si uno de esos números es 30, o si los 3
sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.
Ejemplos:
23, 30, 768 → Correcto (hay un 30)
10, 15, 5 → Correcto (10 + 15 + 5 = 30)
35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)
"""

print(f" \n\nEXERCISE 2:\n")
number_1 = int(input("Please enter the 1st number: "))
number_2 = int(input("Please enter the 2nd number: "))
number_3 = int(input("Please enter the 3rd number: "))
if (number_1 == 30 or number_2 == 30 or number_3 == 30 or number_1 + number_2 + number_3 == 30):
    print("Correct!")
else:
    print("Incorrect.")

