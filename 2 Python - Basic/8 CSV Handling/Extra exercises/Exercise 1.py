import csv

"""
EXERCISE 1:
Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
Lea cada línea usando csv.reader()
Muestre el contenido en pantalla de forma legible, línea por línea
Ejemplo:
Salida:

Nombre: Grand Theft Auto IV
Género: Accion
Desarrollador: Rockstar Games
Clasificación: M
"""


def read_csv_file(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def show_csv_by_game(file_path):
    reader = read_csv_file(file_path)
    for game in reader:
        print(f"Nombre: {game['Nombre']}\nGénero: {game['Género']},\nDesarrollador: {game['Desarrollador']}\nClasificación: {game['Clasificación']}\n")


def main():
    #EXERCISE 1:
    show_csv_by_game("my_games_list.csv")


if __name__ == "__main__":
    main()

