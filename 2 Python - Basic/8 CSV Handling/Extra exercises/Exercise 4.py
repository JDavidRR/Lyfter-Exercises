import csv
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


def read_csv_file(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


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
    show_games_by_developer("my_games_list.csv")


if __name__ == "__main__":
    main()
