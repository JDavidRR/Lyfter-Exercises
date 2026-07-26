"""
EXERCISE 4
Tabla de multiplicar personalizada
Pida al usuario un número del 1 al 10
Muestre su tabla de multiplicar del 1 al 12. Ejemplo:
Entrada:
"Ingrese un número: "
Salida:
7 x 1 = 7
7 x 2 = 14
...
7 x 12 = 84
"""

print(f" \n\nEXERCISE 4:\n")
number = int(input("Type a number from 1 to 10 and hit Enter: "))
counter = 1
while counter <= 12:
    print(f"{number} * {counter} = {counter*number}")
    counter += 1