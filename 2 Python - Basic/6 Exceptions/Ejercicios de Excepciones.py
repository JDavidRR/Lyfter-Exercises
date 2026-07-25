"""
Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir
qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual.
El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida,
o si ingresa un número invalido a la hora de hacer la operación.
"""
import os
import subprocess
import sys


class NotValidOptionError(Exception):
    def __init__(self, option):
        super().__init__(f"Error: La opción {option} no existe.")


def clear_screen():
    if os.name == 'nt':
        subprocess.run('cls', shell = True)
    else:
        sys.stdout.write("\033[H\033[2J\033[3J")
        sys.stdout.flush()


def menu(current_value = 0.0,current_operation = "",):
    clear_screen()
    print(" \n\nCALCULADORA\n\n")
    print(f"{current_operation}\n= {current_value}\n\n")
    print(
    "1. Suma\n" \
    "2. Resta\n" \
    "3. Multiplicación\n" \
    "4. División\n" \
    "5. Borrar resultado\n" \
    "6. Salir\n\n")


def current_operation(current_value,current_option):
    if current_option == 1:
        return f"{current_value} + "
    if current_option == 2:
        return f"{current_value} - "
    if current_option == 3:
        return f"{current_value} * "
    if current_option == 4:
        return f"{current_value} / "
    else:
        return ""


def addition(number_1,number_2):
    total = 0
    total = number_1 + number_2
    return total


def subtraction(number_1,number_2):
    total = 0
    total = number_1 - number_2
    return total


def multiplication(number_1,number_2):
    total = 0
    total = number_1 * number_2
    return total


def division(number_1,number_2):
    total = 0
    total = number_1 / number_2
    return total


def validate_option():
    option = str(input("Digite una opción y presione ENTER: "))
    if not option.isdecimal():
        raise ValueError(f"Error: Solo se permiten números enteros")
    elif (int(option) > 6 or int(option) < 1):
        raise NotValidOptionError(option)
    else:
        return int(option)


def ask_for_input():
    user_input = 0.0
    user_input = float(input("Digite el valor: "))
    return user_input

def execute_option(current_value,current_option,user_input):
    if current_option == 1:
        return addition (current_value,user_input)
    elif current_option == 2:
        return subtraction (current_value,user_input)
    elif current_option == 3:
        return multiplication (current_value,user_input)
    elif current_option == 4:
        if user_input == 0:
            raise ZeroDivisionError("Error: No se puede dividir entre cero.")
        return division (current_value,user_input)


def run_calc():
    option = 0
    current_value = 0.0
    user_input = 0.0
    operation_cache = ""
    while option != 6:
        operating = True
        while operating:
            menu(current_value,operation_cache)
            try:
                option = validate_option()
            except ValueError as ex:
                operation_cache = "Error"
                input(f"{ex}. Presione ENTER para continuar.")
                continue
            except NotValidOptionError as ex:
                operation_cache = "Error"
                input(f"{ex}. Presione ENTER para continuar.")
                continue
            operation_cache = current_operation(current_value,option)
            menu(current_value,operation_cache)
            if option == 6:
                operating = False
                continue
            elif option == 5:
                current_value = 0
                operation_cache = ""
                continue
            else:
                try:
                    user_input = ask_for_input()
                except ValueError as ex:
                    operation_cache = "Error"
                    input(f"{ex}. Presione ENTER para continuar.")
                    continue
                try:
                    current_value = execute_option(current_value,option,user_input)
                    operation_cache += str(user_input)
                except ZeroDivisionError as ex:
                    operation_cache = "Error"
                    input(f"{ex}. Presione ENTER para continuar.")
                    continue
                

run_calc()

"""
I did some research on my own and discovered there are even more kind of exception errors that were not mentioned.
For example the overflow error which were very common in coding languages such as C where the integers had a maximun of
32 or 64 bits of memory for each variable. But the only limit Python has for a variable is the system memory.
Thinking a little, I guess this can also be an issue if we do not limit users for using online calculators.
Lets say a malicious script is executed to run multiple task request for big numbers math operations.
Then the system may crash...

Also noticed the errors are not saved in system, they are only shown during execution time. If we want to record errors event,
then we must use a logging library for this or manage our own files.
"""

