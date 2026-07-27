"""
EXERCISE 2:
Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando
una para sus keys, y la otra para sus values.
Ejemplos:
list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
→ {'first_name': 'Alek', 'last_name': 'Castillo', 'role': 'Software Engineer'}
"""

print (" \nEXERCISE 2:\n\n")

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
dictionary_of_lists = {}
for index in range(0,len(list_a)):
    dictionary_of_lists [list_a[index]] = list_b[index]
print(dictionary_of_lists)

