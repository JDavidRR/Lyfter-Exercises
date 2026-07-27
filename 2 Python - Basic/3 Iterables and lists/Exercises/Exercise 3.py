"""
EXERCISE 3:
Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe
funcionar con listas de cualquier tamaño.
Ejemplos:
my_list = [4, 3, 6, 1, 7] → [7, 3, 6, 1, 4]
"""

print(" \n\nEXERCISE 3:\n")
my_list = [4, 3, 6, 1, 7]
auxiliar_1 = my_list[0]
auxiliar_2 = my_list[-1]
my_list[0] = auxiliar_2
my_list[-1] = auxiliar_1
print (my_list)
