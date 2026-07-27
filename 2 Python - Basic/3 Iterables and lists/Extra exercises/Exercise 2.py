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

