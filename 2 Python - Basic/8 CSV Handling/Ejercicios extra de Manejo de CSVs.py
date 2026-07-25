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


"""
EXERCISE 2:
Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo CSV de videojuegos
Pida al usuario una clasificación ESRB (por ejemplo: "T")
Muestre todos los videojuegos que tengan esa clasificación
"""


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


"""
EXERCISE 3:
Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo .csv con videojuegos
Cuente cuántos videojuegos hay de cada género
Muestre el resultado de forma ordenada
Ejemplo:
Salida:

Géneros encontrados:
Acción: 5
Aventura: 3
Deportes: 4
...
"""


def count_genres(file_path):
    my_dict = {}
    reader = read_csv_file(file_path)
    for game in reader:
        if game['Género'] not in my_dict:
            my_dict[game['Género']] = 1
        else:
            my_dict[game['Género']] = my_dict[game['Género']] + 1
    print (dict(sorted(my_dict.items())))


"""
EXERCISE 4:
Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo .csv con videojuegos
Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
Ejemplo:
Salida:

Videojuegos desarrollados por Ubisoft:
- Assassin's Creed II (Clasificación: M, Género: Aventura)
- Rayman Legends (Clasificación: E, Género: Plataforma)
"""


def show_games_by_developer(file_path):
    dev = input("Type the developer's name to search games: ")
    my_dict = {}
    reader = read_csv_file(file_path)
    for game in reader:
        if dev in game['Desarrollador']:
            if dev not in my_dict:
                my_dict[dev] = [f"- {game['Nombre']} (Clasificación: {game['Clasificación']}, Género: {game['Género']})"]
            else:
                my_dict[dev].append(f"- {game['Nombre']} (Clasificación: {game['Clasificación']}, Género: {game['Género']})")
    if my_dict == {}:
        print(f"No se ha encontrado el desarrollador \"{dev}\"")
    else:
        print(f"Videojuegos desarrollados por {dev}:")
        for value in my_dict[dev]:
            print(value)


def main():
    #EXERCISE 1:
    show_csv_by_game("my_games_list2.csv")
    #EXERCISE 2:
    search_classification("my_games_list2.csv")
    #EXERCISE 3:
    count_genres("my_games_list2.csv")
    #EXERCISE 4:
    show_games_by_developer("my_games_list2.csv")


if __name__ == "__main__":
    main()


