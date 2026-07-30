import os
import subprocess
import sys
import actions


class NotValidOptionError (Exception):
    def __init__(self,option):
        super().__init__(f"Error: The option \"{option}\" doesn't exist")


class OutOfRangeError(Exception):
    def __init__(self, quantity):
        super().__init__(f"Not in range: The number {quantity} is out of the allowed range.")


class NotValidSectionError (Exception):
    def __init__(self,section):
        super().__init__(f"Error: The section \"{section}\" doesn't exist")


def clear_screen():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        sys.stdout.write("\033[H\033[2J\033[3J")
        sys.stdout.flush()


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
    8 - Import data
    9 - Exit\n""")


def validate_option():
    option = ""
    try:
        option = str(input("Type an option and hit ENTER: "))
        if not option.isdecimal():
            raise ValueError(f"Error: Only whole numbers are allowed")
        elif (int(option) > 9 or int(option) < 1):
            raise NotValidOptionError(option)
        else:
            return int(option)
    except ValueError as ex:
        print(f"\nError: [ValueError] Cannot convert the value \"{option}\" to integer {ex}")
        input("Hit Enter to continue...")
        return 0
    except NotValidOptionError as ex:
        print(f"\nError: [NotValidOptionError] {ex}")
        input("Hit Enter to continue...")
        return 0


def ask_students_quantity():
    quantity = 0
    try:
        number = input("How many students? (MAX: 10) ")
        quantity = int(number)
        if quantity < 0 or quantity > 10:
            raise OutOfRangeError(quantity)
    except OutOfRangeError as ex:
        print(f"\nError: [OutOfRangeError] {ex}")
        quantity = ask_students_quantity()
    except ValueError as ex:
        print(f"\nError: [ValueError] Cannot convert the value \"{number}\" to integer {ex}")
        quantity = ask_students_quantity()
    return quantity


def ask_name(option): #switch between name and lastname according to the bool received, if option == True: name, if option == False: lastname.
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
    except ValueError as ex:
        clear_screen()
        print(f"\nError: [ValueError] {ex}")
        input("Hit Enter to continue...")
        name = ask_name(option)
    return name


def ask_section():
    while True:
        try:
            clear_screen()
            print("Please enter the student's section in the format <grade><group> for example: 7A or 11B")
            print("Rules:")
            print("- Grade must be between 7 and 11")
            print("- Group must be a single letter (A-Z)")
            section = input("Type the section: ")
            section = section.replace(" ", "").upper()
            if not actions.is_valid_section(section):
                raise NotValidSectionError(section)
            return section
        except NotValidSectionError as ex:
            print(f"\nError: [NotValidSectionError] {ex}")
            input("Please try again...\n")


def ask_students(students_list):
    quantity = ask_students_quantity()
    counter = 0
    while counter < quantity:
        new_student, exists = actions.create_student(students_list)
        if not exists:
            students_list.append(new_student)
            input(f"\nThe student {new_student['Name']} was added in section {new_student['Section']}...")
            counter += 1
        else:
            input(f"\nThe student {new_student['Name']} already exists in section {new_student['Section']}, please try again...")


def show_student(student:dict):
    print(f"\nName: {student['Name']}\nSection: {student['Section']}\nSpanish Grade: {student['Spanish']}\tEnglish Grade: {student['English']}\tSocial Studies Grade: {student['Social Studies']}\tScience Grade: {student['Science']}")


def show_students(students_list:list):
    if not students_list:
        print("There are not students")
    for student in students_list:
        show_student(student)
    input("\nHit enter to continue...")


def ask_average_grade(subject):
    average = ""
    while True:
        try:
            clear_screen()
            print(f"Please input the {subject} average grade, it must be between 0 and 100")
            average = input("Average: ")
            average_float = float(average)
            if average_float < 0.0 or average_float > 100.0:
                raise OutOfRangeError(average_float)
            return average_float
        except ValueError as ex:
            print(f"\nError: [ValueError] Cannot convert the value \"{average}\" to float. {ex}")
        except OutOfRangeError as ex:
            print(f"\nError: [OutOfRangeError] {ex}")
            input("Please try again...\n")


def tops_three_average (students_list: list[dict[str]]):
    students_temporal_list:list[(dict,float)] = actions.calculate_averages(students_list)[:3]
    print("Top students:\n")
    for student_tuple in students_temporal_list:
        show_student(student_tuple[0])
        print(f"Total Average grade: {student_tuple[1]}")
    input("\nPress Enter to continue")


def show_all_average (students_list: list[dict[str]]):
    students_temporal_list:list[(dict,float)] = actions.calculate_averages(students_list)
    for student_tuple in students_temporal_list:
            show_student(student_tuple[0])
            print(f"Total Average grade: {student_tuple[1]}")
    input("\nPress Enter to continue")


def show_failed_students(students_list: list[dict[str]]):
    students_temporal_list = actions.list_failed_students(students_list)
    print("List of students that reproved at least one subject\n")
    show_students(students_temporal_list)

