"""
EXERCISE 3:
Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
[4, 6, 2, 29] → 41
"""

def addition_list(list_of_numbers = [10,20,30,10,30]):
    total = 0
    for number in list_of_numbers:
        total += number
    return total

print (addition_list([30,40]))
