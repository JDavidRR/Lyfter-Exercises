
"""
Ejercicios extra de Sintaxis
Python Básico

Pasa los Ejercicios de Pseudocódigo previamente creados a código:

EXERCISE 1.1
Cree un programa que le pida un precio de producto al usuario, calcule su descuento y
muestre el precio final tomando en cuenta que:
Si el precio es menor a 100, el descuento es del 2%.
Si el precio es mayor o igual a 100, el descuento es del 10%.
Ejemplos:
120 → 108
40 → 39.2
"""

print(f" \n\nEXERCISE 1.1:\n")
price = float(input ("Please enter the product price: $"))
discount = 0.0
if (price < 100):
    discount = price * 0.02
else:
    discount = price * 0.1
print("Discount applied: $" + str(discount))
print("Total price after discount: $" + str(price - discount))

"""
EXERCISE 1.2
Cree un programa que le pida un tiempo en segundos al usuario y calcule si es menor o
mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a
10 minutos. Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.
Ejemplos:
1040 → Mayor
140 → 460
600 → Igual
599 → 1
"""

print(f" \n\nEXERCISE 1.2:\n")
seconds = int(input("Please enter the seconds: "))
ten_mins = 60 * 10
if (seconds < ten_mins):
    print(f"{(ten_mins-seconds)} seconds remaining")
elif (seconds == ten_mins):
    print ("Equal")
else:
    print ("Greater")

"""
EXERCISE 1.3
Cree un programa que le pida un numero al usuario, y realice una suma de cada numero
del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
5 → 15 (1 + 2 + 3 + 4 + 5)
3 → 6 (1 + 2 + 3)
12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)
"""

print(f" \n\nEXERCISE 1.3:\n")
number = int(input("Please enter a number: "))
addition = 0
while number > 0:
    addition += number
    number -= 1
print("The addition from 1 upto the inserted number is: " + str(addition))

