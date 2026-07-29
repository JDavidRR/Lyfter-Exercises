import os
import subprocess
import sys
import actions

class NotValidOptionError (Exception):
    def __init__(self,option):
        super().__init__(f"Error: The option \"{option}\" doesn't exist")

class OutOfRangeError(Exception):
    def __init__(self, quantity):
        super().__init__(f"Not in range: The quantity {quantity} is out of the allowed range.")


def clear_screen():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        sys.stdout.write("\033[H\033[2J\033[3J")
        sys.stdout.flush()


"""
1 - Ingresar estudiantes
2 - Mostrar estudiantes (Mostrar todos)
3 - Ver top 3 mejores promedio
4 - Ver promedios (es decir, el promedio de notas de cada uno)
5 - Eliminar estudiante
6 - Ver estudiantes reprobados (nombre, sección y las materias reprobadas con sus notas.)
7 - Exportar todos los datos
8 - Importar datos (Si no hay un archivo previamente exportado, debe informárselo al usuario.)
"""


def main_menu():
    clear_screen()
    print(f"""\n\nStudent Management System\n
    1 - Add students
    2 - Show students
    3 - View top 3 averages
    4 - View averages
    5 - Delete student
    6 - View failed students
    7 - Export all data
    8 - Import data""")


def validate_option():
    option = str(input("Type an option and hit ENTER: "))
    if not option.isdecimal():
        raise ValueError(f"Error: Only whole numbers are allowed")
    elif (int(option) > 8 or int(option) < 1):
        raise NotValidOptionError(option)
    else:
        return int(option)


def ask_students_quantity():
    quantity = 0
    try:
        number = input("How many students? (MAX: 10) ")
        quantity = int(number)
        if quantity < 0 or quantity > 10:
            raise OutOfRangeError(quantity)
    except OutOfRangeError as e:
        print(f"Error: [OutOfRangeError] {e}")
        quantity = ask_students_quantity()
    except ValueError as e:
        print(f"Error: [ValueError] Cannot convert the value \"{number}\" to integer {e}")
        quantity = ask_students_quantity()
    return quantity


def ask_name(option): #switch between name and lastname according to the bool received, if option = name, if not = lastname.
    name = ""
    try:
        clear_screen()
        if option:
            name = str(input("Enter the student's name: "))
            name = " ".join(name.split())
            if not actions.is_valid_name(name):
                raise ValueError(f"Invalid name \"{name}\". Please use letters and spaces only.")
        else:
            name = str(input("Enter the student's lastname: "))
            name = " ".join(name.split())
            if not actions.is_valid_name(name):
                raise ValueError(f"Invalid lastname \"{name}\". Please use letters and spaces only.")
    except ValueError as e:
        clear_screen()
        print(f"Error: [ValueError] {e}")
        input("Hit Enter to continue...")
        name = ask_name(option)
    return name

#def show_students(students_list)

#def tops_three_average (students_list)

#def show_all_average (students_list)

#def show_failed_students(students_list)

