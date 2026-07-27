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

