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
