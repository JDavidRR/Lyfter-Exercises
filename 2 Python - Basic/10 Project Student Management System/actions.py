import data
import menu

def execute():
    menu.clear_screen()
    file_path = "students.csv"
    students = data.import_database_csv(file_path)
    option = 0
    while option != 9:
            menu.clear_screen()
            menu.main_menu()
            option = menu.validate_option()
            menu.clear_screen()
            if option == 1:
                menu.ask_students (students)
            elif option == 2:
                menu.show_students (students)
            elif option == 3:
                menu.tops_three_average (students)
            elif option == 4:
                menu.show_all_average (students)
            elif option == 5:
                delete_student (students)
            elif option == 6:
                menu.show_failed_students(students)
            elif option == 7:
                data.export_database_csv(file_path,students)
            elif option == 8:
                students = data.import_database_csv(file_path)
            else:
                menu.clear_screen()
                print("Thank you!")


def is_valid_name(name):
    if name == "":
        return False
    for char in name:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


def is_valid_section(section):
        my_section = section.replace(" ", "").upper()
        grade_part = my_section[:-1]
        group_part = my_section[-1]
        if not grade_part.isdigit():
            return False
        grade = int(grade_part)
        if grade < 7 or grade > 11:
            return False
        if not group_part.isalpha() or len(group_part) != 1:
            return False
        return True


def student_exists(students_list: list[dict], student_name: str,student_section: str):
    for student in students_list:
        if student['Name'] == student_name and student['Section'] == student_section:
            return True, student
    return False, {}


def create_student(students_list):
    name = ""
    lastname = ""
    section = ""
    spanish_grade = 0
    english_grade = 0
    social_studies_grade = 0
    science_grade = 0
    name = menu.ask_name(True)
    lastname = menu.ask_name(False)
    section = menu.ask_section()
    name += " " + lastname
    exist, student = student_exists(students_list,name,section)
    if not exist:
        spanish_grade = menu.ask_average_grade('Spanish')
        english_grade = menu.ask_average_grade('English')
        social_studies_grade = menu.ask_average_grade('Social Studies')
        science_grade = menu.ask_average_grade('Science')
        new_student = {'Name' : name,
        'Section' : section,
        'Spanish' : spanish_grade,
        'English' : english_grade,
        'Social Studies' : social_studies_grade,
        'Science' : science_grade}
        return new_student, False
    else:
        return student, True


def delete_student (students_list: list[dict[str]]):
    name = menu.ask_name(True)
    lastname = menu.ask_name(False)
    name += " " + lastname
    section = menu.ask_section()
    exist, student = student_exists(students_list,name,section)
    if not exist:
        print(f"There are no results for search name: {name} and section: {section}")
    else:
        students_list.remove(student)
        print(f"The student \"{student['Name']}\" from section \"{student['Section']}\" was removed successfully")
    input("Hit Enter to continue...")


def calculate_averages(students_list: list[dict[str]]):
    list_averages =[]
    for student in students_list:
        average = (float(student['Spanish']) + float(student['English']) + float(student['Social Studies']) + float(student['Science'])) / 4
        my_tuple = (student,average)
        list_averages.append(my_tuple)
    return sorted(list_averages, key = lambda x:x[1],reverse = True)


def list_failed_students(students_list: list[dict[str]]):
    students_temporal_list = []
    for student in students_list:
        if int(student['Section'][:-1]) < 10:
            if float(student['Spanish']) < 65 or float(student['English']) < 65 or float(student['Social Studies']) < 65 or float(student['Science']) < 65:
                students_temporal_list.append(student)
        else:
            if float(student['Spanish']) < 70 or float(student['English']) < 70 or float(student['Social Studies']) < 70 or float(student['Science']) < 70:
                students_temporal_list.append(student)
    return students_temporal_list