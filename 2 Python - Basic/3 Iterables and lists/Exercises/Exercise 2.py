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

