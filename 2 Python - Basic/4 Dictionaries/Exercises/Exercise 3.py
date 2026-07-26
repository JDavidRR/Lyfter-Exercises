"""
EXERCISE 3:
Cree un programa que use una lista para eliminar keys de un diccionario.
Ejemplos:
list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
→ {'name': 'John', 'email': 'john@ecorp.com'}
"""

print (" \nEXERCISE 3:\n\n")

list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
for index in range(0,len(list_of_keys)):
    employee.pop(list_of_keys[index])
print (employee)
