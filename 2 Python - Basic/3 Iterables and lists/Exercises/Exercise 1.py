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

