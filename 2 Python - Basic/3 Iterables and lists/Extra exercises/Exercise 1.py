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

