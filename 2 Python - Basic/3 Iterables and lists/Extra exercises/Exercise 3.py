"""
EXERCISE 3:
Cree un programa que muestre el valor más pequeño de una lista sin usar min().
Use una variable para comparar uno a uno
Ejemplo:
Entrada:
my_list = [9,4,7,1,5]
Salida:
"El menor valor es 1"
"""

print(" \n EXERCISE 3:\n\n")
my_list = [9,4,7,1,0]
lowest_number = my_list[0]
for element in my_list:
    if lowest_number > element:
        lowest_number = element
print(f"The lowest number in the list is {lowest_number}")

