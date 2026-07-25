""""
EXERCISE 1:
Cree un programa que cuente cuántas veces aparece un número específico en una lista.
Pida al usuario una lista de números y otro número a buscar
Ejemplo:
Entrada:
my_list = [4,2,7,2,8,2,1]
numero_a_buscar = 2
Salida:
"El número 2 aparece 3 veces"
"""

print(" \n EXERCISE 1:\n\n")
list_len = int(input ("How many numbers you want to enter in the list? "))
my_list = []
while list_len > 0:
    my_list.append(int(input("Enter a number: ")))
    list_len -= 1
number_to_search = int(input("List complete. Enter a number to search: "))
counter = 0
for element in my_list:
    if element == number_to_search:
        counter +=1
print (f"The number {number_to_search} was found {counter} times")

"""
EXERCISE 2:
Cree un programa que verifique si todos los elementos de una lista son positivos
Restricciones:
No use funciones como all()
Ejemplo:
Entrada:
my_list = [3,6,0,-2,4]
Salida:
"Hay al menos un número negativo o cero"
"""
print(" \n EXERCISE 2:\n\n")
my_list = [3,6,0,-2,4]
for element in my_list:
    if element < 1:
        print (f"There is at least one negative number or a cero in the list")
        break

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
