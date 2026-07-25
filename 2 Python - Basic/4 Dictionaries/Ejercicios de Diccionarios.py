"""
EXERCISE 1:
Cree un diccionario que guarde la siguiente información sobre un hotel:
nombre
numero_de_estrellas
habitaciones
El value del key de habitaciones debe ser una lista, y cada habitación debe tener la
siguiente información:
numero
piso
precio_por_noche
"""

print (" \nEXERCISE 1:\n\n")
hotel = {
    'name':'Saturn Hotel',
    'stars': 4,
    'rooms': [
        {
            'number':1,
            'floor':1,
            'price_per_night':120.00
        },
        {
            'number':2,
            'floor':1,
            'price_per_night':120.00
        },
        {
            'number':3,
            'floor':1,
            'price_per_night':150.00
        }
    ]
}
for key, value in hotel.items():
    if key == 'rooms':
        print (f' \n{key}: ')
        for rooms in value:
            print("")
            for key2, value2 in rooms.items():
                print(f'{key2}: {value2}')
    else:
        print(f'{key}: {value}')

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