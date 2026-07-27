import math

"""
EXERCISE 7:
Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código.
No busque el código, eso no ayudaría.
Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista).
Así que lo mejor es agregar otra función para revisar si el numero es primo o no.
"""

list_of_numbers = [1, 4, 6, 7, 13, 9, 67]

def is_prime(int_param):
    if int_param <= 1:
        return False
    if int_param <= 3:
        return True
    if int_param % 2 == 0 or int_param % 3 == 0:
        return False
    limit = int(math.sqrt(int_param)) + 1
    for divisor in range(5, limit, 2):
        if int_param % divisor == 0:
            return False
    return True


def list_primes_on_list (list_param):
    output_list = []
    for number in list_param:
        if is_prime(number):
            output_list.append(number)
    if len(output_list) == 0:
        print("No odd numbers were listed")
    return output_list

print (list_primes_on_list(list_of_numbers))