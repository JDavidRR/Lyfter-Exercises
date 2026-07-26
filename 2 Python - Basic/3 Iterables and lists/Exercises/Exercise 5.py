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
