import data
import menu

def execute_option(students_list,current_option):
    if current_option == 1:
        insert_students (students_list)
    elif current_option == 2:
        show_students (students_list)
    elif current_option == 3:
        tops_three_everage (students_list)
    elif current_option == 4:
        show_all_everage (students_list)
    elif current_option == 5:
        delete_studen (students_list)
    elif current_option == 6:
        show_failed_students(students_list)
    elif current_option == 7:
        export_database_csv(students_list)
    else:
        import_database_csv(students_list)


def is_valid_name(name):
    if name == "":
        return False
    for char in name:
        if not (char.isalpha() or char.isspace()):
            return False
    return True

#def is_valid_section(section)

#def student_exists(student)

def insert_students(students_list):
    quantity = menu.ask_students_quantity()
    new_students = []
    name = ""
    lastname = ""
    section = ""
    spanish_grade = 0
    english_grade = 0
    social_studies_grade = 0
    science_grade = 0
    for i in range(1, quantity + 1):
        name = menu.ask_name(True)
        lastname = menu.ask_name(False)
        

#def delete_student (students_list)