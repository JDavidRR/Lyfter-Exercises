import json

"""
EXERCISE 1:
Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON de Pokémon
Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)
"""

def from_json_to_dict (file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        my_json_value = json.load(file)
    return my_json_value


def show_pokemons_name_type_level (file_path):
    my_pokemons = from_json_to_dict(file_path)
    for pokemon in my_pokemons:
        print(f"Name: {pokemon['name']}, Type: {pokemon['type']}, Level: {pokemon['level']}")

def main():
    show_pokemons_name_type_level("pokemons2.json")


if __name__ == "__main__":
    main()