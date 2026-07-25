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

"""
EXERCISE 3:

Cree un programa que abra un archivo .json con la información de Pokémon (en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON de Pokémon
Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)
Ejemplo:
Salida:

Nombre: Pikachu
Ataque: 55
Defensa: 40
Velocidad: 90

Nombre: Bulbasaur
Ataque: 49
Defensa: 49
Velocidad: 45
...
"""


def show_pokemon_stats (file_path):
    my_pokemons = from_json_to_dict(file_path)
    for pokemon in my_pokemons:
        print(f"Name: {pokemon['name']}")
        print(f"HP: {pokemon['stats']['hp']}")
        print(f"Attack: {pokemon['stats']['attack']}")
        print(f"Defense: {pokemon['stats']['defense']}")
        print(f"Sp attack: {pokemon['stats']['sp_attack']}")
        print(f"Sp defense: {pokemon['stats']['sp_defense']}")
        print(f"Speed: {pokemon['stats']['speed']}\n")


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
    print ("EXERCISE 1:\n")
    show_pokemons_name_type_level("pokemons2.json")
    print ("\nEXERCISE 2:\n")
    show_pokemon_type("pokemons2.json")
    print ("\nEXERCISE 3:\n")
    show_pokemon_stats("pokemons2.json")
    print ("\nEXERCISE 4:\n")
    average_level_by_type("pokemons2.json")


if __name__ == "__main__":
    main()