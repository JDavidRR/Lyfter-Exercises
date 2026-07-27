"""
EXERCISE 4 - Cree un programa que le pida tres números al usuario y muestre el mayor.
"""

NUMBER_1 = int(input("Insert the first number: "))
NUMBER_2 = int(input("Insert the second number: "))
NUMBER_3 = int(input("Insert the third number: "))
if NUMBER_1 < NUMBER_2:
    NUMBER_1 = NUMBER_2
if NUMBER_1 < NUMBER_3:
    NUMBER_1 = NUMBER_3
print ("The highest number is " + str(NUMBER_1)+"\n")
