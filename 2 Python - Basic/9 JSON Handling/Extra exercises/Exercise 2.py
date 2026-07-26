import json

"""
EXERCISE 2:
Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON de Pokémon
Pida al usuario un tipo de Pokémon
Muestre todos los Pokémon que sean de ese tipo
Ejemplo:

Entrada:
"Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc): " 
"Fuego"

Salida:
"Los pokemos que existen de ese tipo son: "
Charmander
Growlithe
Victini
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


def show_pokemon_type (file_path):
    type_to_search = input("Please enter a pokemon type to search(Water, Electric, Fire, etc): ")
    type_to_search = type_to_search.lower()
    type_to_search = type_to_search.capitalize()
    my_pokemons = from_json_to_dict(file_path)
    results = search_type(type_to_search,my_pokemons)
    if len(results) == 0:
        print(f"There are no pokemons type \"{type_to_search}\"")
    else:
        print("The pokemons of this type are:")
        for pokemon in results:
            print (pokemon['name'])


def main():
    show_pokemon_type("pokemons2.json")


if __name__ == "__main__":
    main()