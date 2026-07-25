"""
Para estos ejercicios debe utilizar solo lo visto en clase. No es valido utilizar funciones como zip o reversed.

EXERCISE 1:
Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
Ejemplos:
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util'] ->
Hay casos
en los
que la
iteracion por
indice es
muy util
"""

print(" \n\nEXERCISE 1:\n")
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]
for index in range(0,len(first_list)):
    print (f"{first_list[index]} {second_list[index]}")

"""
EXERCISE 2:
Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
Pista: investigue de que otras maneras se puede usar el range.
Ejemplos:
my_string = 'Pizza con piña' →
a
ñ
i
p

n
o
c

a
z
z
i
p
"""

print(" \n\nEXERCISE 2:\n")
my_string = "Pizza con piña"
for index in range(len(my_string),0,-1):
    print(f"{my_string[index-1]}")

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

"""
EXERCISE 4:
Cree un programa que elimine todos los números impares de una lista.
Ejemplos:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]
"""

print(" \n\nEXERCISE 4:\n")
index = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while index != len(my_list):
    if my_list[index] % 2 != 0:
        my_list.pop(index)
        continue
    else:
        index += 1

print(my_list)

"""
EXERCISE 5:
Cree un programa que le pida al usuario 10 números, y al final le muestre todos los
números que ingresó, seguido del numero ingresado más alto.
Ejemplos:
86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.
"""

print(" \n\nEXERCISE 5:\n")
my_list = []
highest = 0
counter = 0
while len(my_list) < 10:
    my_list.append(int(input("Enter a number: ")))
    if my_list[counter] > highest:
        highest = my_list[counter]
    counter += 1

print (f"{my_list} -> The highest number inserted in the list is: {highest}")