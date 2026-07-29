import data
import actions
import menu

def main():
    file_name = "students.csv"
    students = data.import_database_csv(file_name)
    actions.execute(students,file_name)

if __name__ == "__main__":
    main()