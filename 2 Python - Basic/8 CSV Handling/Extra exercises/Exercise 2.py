import csv
"""
EXERCISE 2:
Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo CSV de videojuegos
Pida al usuario una clasificación ESRB (por ejemplo: "T")
Muestre todos los videojuegos que tengan esa clasificación
"""

def read_csv_file(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def search_classification(file_path):
    classification = input("Type a classification to search and hit enter: ")
    game_found = []
    reader = read_csv_file(file_path)
    for game in reader:
        if classification in game['Clasificación']:
            game_found.append(game['Nombre'])
    if len(game_found) == 0:
        print(f"There are no games classified as \"{classification}\"")
    else:
        print(f"The games classified as \"{classification}\" are:")
        for game in game_found:
            print(game)

def main():
    search_classification("my_games_list.csv")


if __name__ == "__main__":
    main()

