import data
import menu

def execute(students,file_path):
    option = 0
    while option != 9:
            menu.clear_screen()
            menu.main_menu()
            option = menu.validate_option()
            menu.clear_screen()
            if option == 1:
                menu.insert_students (students)
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
                data.import_database_csv(file_path)
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


def student_exists(students_list:list[dict], student_name: str,student_section: str):
    for student in students_list:
        if student['Name'] == student_name and student['Section'] == student_section:
            return True
    return False


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
    if not student_exists(students_list,name,section):
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
        new_student = {
            "Name": name,
            "Section": section,
            "Spanish": 0.0,
            "English": 0.0,
            "Social Studies": 0.0,
            "Science": 0.0
        }
        return new_student, True


#def delete_student (students_list)