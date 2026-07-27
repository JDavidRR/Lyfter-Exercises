"""
EXERCISE 4:
Cree un programa que elimine todos los números impares de una lista.
Ejemplos:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]
"""

print(" \n\nEXERCISE 4:\n")
index = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while index != len(my_list):
    if my_list[index] % 2 != 0:
        my_list.pop(index)
        continue
    else:
        index += 1

print(my_list)
