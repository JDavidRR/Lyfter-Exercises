"""
EXERCISE 4:
Cree un programa que reciba una lista de números y calcule el promedio de los valores,
luego cree una nueva lista con solo los valores mayores al promedio
Ejemplo:
Entrada:
my_list = [10,20,30,40,50]
Salida:
"Promedio:" 30
Nueva lista:[40,50]
"""

print(" \n EXERCISE 4:\n\n")
my_list = [10,20,30,40,50]
new_list = []
counter = 0
average = 0
for element in my_list:
    average += element
    counter += 1
if counter > 0:
    average = average / counter
    for element in my_list:
        if element > average:
            new_list.append(element)
    print(f"Average: {average}")
    print(new_list)

