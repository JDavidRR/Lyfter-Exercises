import csv
"""
EXERCISE 2:
Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que
guarde el archivo separado por tabulaciones en vez de por comas.
Ejemplo de archivo final:

nombre	genero	desarrollador	clasificacion
Grand Theft Auto IV	Accion	Rockstar Games	M
The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
Tony Hawk's Pro Skater 2	Deportes	Activision	T
"""


class OutOfRangeError(Exception):
    def __init__(self, quantity):
        super().__init__(f"Not in range: The value {quantity} is out of the allowed range.")
    


def create_tab_sv_from_list(file_path,list_param):
    with open(file_path,"w",encoding="utf-8", newline="") as file:
        headers = list_param[0].keys()
        writer = csv.DictWriter(file,fieldnames=headers,delimiter="\t")
        writer.writeheader()
        writer.writerows(list_param)


def ask_game():
    name = input("Nuevo juego, por favor inserte:\nNombre: ")
    genre = input("Género: ")
    developer = input("Desarrollador: ")
    esrb = input("Clasificación ESRB: ")
    my_dictionary = {"Nombre" : name,
                    "Género" : genre,
                    "Desarrollador" : developer,
                    "Clasificación" : esrb}
    return my_dictionary


def ask_games():
    quantity = 0
    try:
        number = input("¿Cuántos juegos desea agregar? ")
        quantity = int(number)
        if quantity < 0:
            raise OutOfRangeError(quantity)
    except OutOfRangeError as e:
        print(f"Error: [OutOfRangeError] {e}")
        quantity = ask_games()
    except ValueError as e:
        print(f"Error: [ValueError]: Cannot convert the value \"{number}\" to integer {e}")
        quantity = ask_games()
    return quantity


def create_games_list():
    number_of_games = ask_games()
    my_games_list = []
    while number_of_games != 0:
        my_games_list.append(ask_game())
        number_of_games -= 1
    return my_games_list


def main():
    my_games_list = create_games_list()
    create_tab_sv_from_list("my_games_list_tab_sv.csv",my_games_list)


if __name__ == "__main__":
    main()

