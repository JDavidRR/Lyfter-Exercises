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

