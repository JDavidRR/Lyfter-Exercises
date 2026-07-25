
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

"""
EXERCISE 3
Convertidor de unidades de temperatura
Pida al usuario ingresar una temperatura en Celsius
Conviértala a Fahrenheit y Kelvin
Muestre los tres valores. Ejemplo:
Entrada:
"Ingrese temperatura en Celsius: "
Salida:
Fahrenheit: 77.0
Kelvin: 298.15
"""

print(f" \n\nEXERCISE 3:\n")
temperature_celsius = float(input("Enter a Celsius temperature: "))
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
temperature_kelvin = temperature_celsius + 273.15
print("Celsius = " + str(temperature_celsius))
print("Fahrenheit = " + str(temperature_fahrenheit))
print("Kelvin = " + str(temperature_kelvin))

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