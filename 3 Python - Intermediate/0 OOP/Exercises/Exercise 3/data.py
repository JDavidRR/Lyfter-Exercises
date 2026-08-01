import csv


class Student:
    def __init__(self, name_p, section_p, spanish_p, english_p, social_std_p, science_p):
        self.name = name_p
        self.section = section_p
        self.spanish = spanish_p
        self.english = english_p
        self.social_std = social_std_p
        self.science = science_p


    def to_dict(self):
        return {
            "Name": self.name,
            "Section": self.section,
            "Spanish": self.spanish,
            "English": self.english,
            "Social Studies": self.social_std,
            "Science": self.science
        }


def import_database_csv(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            my_students = []
            for row in reader:
                student = Student(row["Name"],row["Section"],float(row["Spanish"]),float(row["English"]),float(row["Social Studies"]),float(row["Science"]))
                my_students.append(student)
            input(f"Data imported successfully from path \"{file_path}\". Hit enter to continue...")
            return my_students
    except FileNotFoundError as ex:
        print(f"Error: [FileNotFoundError] The file or database in path \"{file_path}\" doesn't exist\n{ex}\n")
        headers = ["Name", "Section", "Spanish", "English", "Social Studies", "Science"]
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
        input("A new empty database file was created, hit enter to continue...")
        return []


def export_database_csv(file_path, students_list):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        headers = ["Name", "Section", "Spanish", "English", "Social Studies", "Science"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows([student.to_dict() for student in students_list])
    input(f"Data exported successfully, path \"{file_path}\". Hit enter to continue...")
