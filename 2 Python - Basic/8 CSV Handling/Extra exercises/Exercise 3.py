import csv

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

def read_csv_file(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def count_genres(file_path):
    my_dict = {}
    reader = read_csv_file(file_path)
    for game in reader:
        if game['Género'] not in my_dict:
            my_dict[game['Género']] = 1
        else:
            my_dict[game['Género']] = my_dict[game['Género']] + 1
    print (dict(sorted(my_dict.items())))

def main():
    count_genres("my_games_list.csv")


if __name__ == "__main__":
    main()

