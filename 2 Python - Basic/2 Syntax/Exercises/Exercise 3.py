import random

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