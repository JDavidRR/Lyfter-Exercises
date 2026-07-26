import json
"""
EXERCISE 4:

Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON
Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
Calcule y muestre el promedio de nivel para cada tipo:
Ejemplo:

Salida:
Tipo: Agua → Promedio de nivel: 42.6
Tipo: Fuego → Promedio de nivel: 37.2
Tipo: Planta → Promedio de nivel: 30.4
"""


def from_json_to_dict (file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        my_json_value = json.load(file)
    return my_json_value


def search_type(type_to_search,my_pokemons):    
    results = []
    for pokemon in my_pokemons:
        if type_to_search in pokemon['type']:
            results.append(pokemon)
    return results


def average_level_by_type(file_path):
    my_pokemons = from_json_to_dict(file_path)
    my_pokemon_types = {}
    for pokemon in my_pokemons:
        if pokemon['type'] not in my_pokemon_types:
            my_pokemon_types[pokemon['type']] = search_type(pokemon['type'],my_pokemons)
    my_pokemon_types = dict(sorted(my_pokemon_types.items()))
    
    for pokemon_type, pokemons in my_pokemon_types.items():
        average = 0
        for pokemon in pokemons:
            average += pokemon['level']
        average = average / len(pokemons)
        print(f"Type: {pokemon_type}, → Promedio de nivel: {average}")


def main():
    average_level_by_type("pokemons2.json")


if __name__ == "__main__":
    main()