import random

"""
EXERCISE 1 - Experimente haciendo sumas entre distintos tipos de datos
y apunte los resultados.
"""


# 1.1 string + string
print ("\nstring + string")
print ("testing"+"text")
TEXT_1 = "texting"
TEXT_2 = "text"
print (TEXT_1+TEXT_2)
print (TEXT_1+"text")
print (f'{TEXT_1}{TEXT_2}')
print (f'{TEXT_1}text')
TEXT_3=TEXT_1+TEXT_2
print (TEXT_3)
TEXT_3 = f'{TEXT_1}{TEXT_2}'
print (TEXT_3)
TEXT_4 = "texting"+" "+"text"
print (TEXT_4)

# 1.2 string + int
print ("\nstring + int")
# I tried:
# print ("Viva la " + 12)
# TypeError: can only concatenate str (not "int") to str
# To correct this issue we must convert the variable type as follows:
print ("Viva la " + str(12))
TEXT_5 = "Viva la " + str(12)
print(TEXT_5)

# 1.3 int + string
print ("\nint + string")
# this is the same as previous point 1.2, but in a different order
print (str(21) + " pilots")

# 1.4 list + list
print ("\nlist + list")
MY_LIST_1 = ['You','spin','my head']
MY_LIST_2 = ['right','round']
MY_LIST_3 = ['when','you','go','down']
MY_LIST_4 = ['down']
print (MY_LIST_1 + MY_LIST_2)
MY_LIST_5 = MY_LIST_1 + ['right','round']
print (MY_LIST_5)
print (MY_LIST_5 + MY_LIST_2 + MY_LIST_3 + MY_LIST_3 + MY_LIST_4)
# No errors found

# 1.5 string + list
print ("\nstring + list")
# I tired:
# STR_LIST = "This is an string " + ['This is a list']
# TypeError: can only concatenate str (not "list") to str
# To resolve this issue, you have 2 options:
# Option 1: use str() to get a string of the listed elements
STR_LIST = "This is an string " + str(['This is a list'])
print (STR_LIST)
STR_LIST = TEXT_1 + str(MY_LIST_5)
print (STR_LIST)
# Option 2: Iterate the list to get each element and save them in a string
STR_LIST = TEXT_1 + ' '
for ELEMENT in MY_LIST_5:
    STR_LIST += str.lower(ELEMENT) + " " # I added str() because 
    # if the element in list is not a string, it may return a type error
    # the .lower is an string built-in function. I used it just for nice looking
print(STR_LIST)

# 1.6 float + int
print ("\nfloat + int")
MY_FLOAT_INT = 0.45 + 3
print (MY_FLOAT_INT)
#it worked
MY_FLOAT_INT = 0.00 + 0
print (MY_FLOAT_INT)
#the float type persist even if no float numbers ".00" are left

# 1.7 bool + bool
print ("\nbool + bool")
MY_BOOL = True
print (MY_BOOL)
MY_BOOL += True
print (MY_BOOL)
MY_BOOL = MY_BOOL + True
print(MY_BOOL)
MY_BOOL = True + True + True + True
# Interesting, true is equal to 1.
print(MY_BOOL)
MY_BOOL = bool(MY_BOOL)
print(MY_BOOL)
if bool(MY_BOOL + True) == True:
    print("Equal")
else:
    print("Not equal")
MY_BOOL += False
print (MY_BOOL) # No changes
MY_BOOL = True + False
print (MY_BOOL) # No changes
MY_BOOL = False
print (MY_BOOL) # False returned
MY_BOOL = False + False
print (MY_BOOL) # It printed a 0, meaning at the time an operator is used
# then the false (0) or true (1) is interpreted as an integer
# since the result is an integer, the variable type is changed to int

"""
EXERCISE 2 - Cree un programa que le pida al usuario su nombre, apellido, y edad,
y muestre si es un bebé, niño, pre-adolescente, adolescente, adulto joven,
adulto, o adulto mayor.
"""


NAME = input("\nType your name: ")
LAST_NAME = input("Type your last name: ")
NAME = "Hello " + NAME + " " + LAST_NAME + ". "
AGE = int(input("How old are you? "))
if 0 <= AGE <= 2:
    NAME += "You are a baby"
elif 3 <= AGE <= 9:
    NAME += "You are a child"
elif 10 <= AGE <= 12:
    NAME += "You are a pre-adolescent"
elif 13 <= AGE <= 18:
    NAME += "You are an adolescent"
elif 19 <= AGE <= 25:
    NAME += "You are a young adult"
elif 26 <= AGE <= 59:
    NAME += "You are an adult"
elif AGE >= 60:
    NAME += "You are an older adult"
else:
    NAME += "Are you dead?"
print (NAME + "\n")

"""
EXERCISE 3 - Cree un programa con un numero secreto del 1 al 10.
El programa no debe cerrarse hasta que el usuario adivine el numero.
Debe investigar cómo generar un número aleatorio distinto cada vez que
se ejecute.
"""

RANDOM_NUMBER = random.randint(1, 10) #random function, including a library
CONTINUE = True
while CONTINUE:
    if int(input("Guess the secret number from 1 to 10: ")) == RANDOM_NUMBER:
        print ("Correct!")
        CONTINUE = False
    else:
        print("Try again.\n")

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

"""
EXERCISE 5 - Dada n cantidad de notas de un estudiante, calcular:
Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.
"""

NOTE_COUNTER = 1
PASSED_COUNT = 0
FAILED_COUNT = 0
PASSED_AVERAGE = 0
FAILED_AVERAGE = 0
TOTAL_AVERAGE = 0

TOTAL_NOTES = int(input("Enter the total number of grades: "))

while NOTE_COUNTER <= TOTAL_NOTES:
    CURRENT_NOTE = int(input("Enter grade number " + str(NOTE_COUNTER) + ": "))
    if CURRENT_NOTE < 70:
        FAILED_COUNT = FAILED_COUNT + 1
        FAILED_AVERAGE = FAILED_AVERAGE + CURRENT_NOTE
    else:
        PASSED_COUNT = PASSED_COUNT + 1
        PASSED_AVERAGE = PASSED_AVERAGE + CURRENT_NOTE
    TOTAL_AVERAGE = TOTAL_AVERAGE + (CURRENT_NOTE / TOTAL_NOTES)
    NOTE_COUNTER = NOTE_COUNTER + 1

if FAILED_COUNT > 0:
    FAILED_AVERAGE = FAILED_AVERAGE / FAILED_COUNT
else:
    FAILED_AVERAGE = 0

if PASSED_COUNT > 0:
    PASSED_AVERAGE = PASSED_AVERAGE / PASSED_COUNT
else:
    PASSED_AVERAGE = 0

print("The student has this number of passed grades: " + str(PASSED_COUNT))
print("This is the average of passed grades: " + str(PASSED_AVERAGE))
print("The student has this number of failed grades: " + str(FAILED_COUNT))
print("This is the average of failed grades: " + str(FAILED_AVERAGE))
print("This is the total average of grades: " + str(TOTAL_AVERAGE))