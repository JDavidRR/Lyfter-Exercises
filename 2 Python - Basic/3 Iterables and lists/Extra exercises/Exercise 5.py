"""
EXERCISE 5:
Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva
lista con solo aquellas palabras que tengan más de 4 letras
Ejemplo:
Entrada:
['sol','estrella','luz','planeta','roca']
Salida:
['estrella','planeta']
"""

print(" \n EXERCISE 5:\n\n")
my_list = []
for index in range(0,5):
    my_string_list = str(input("Type a line and hit Enter: "))
    if len(my_string_list) > 4:
        my_list.append(my_string_list)
print(my_list)    
