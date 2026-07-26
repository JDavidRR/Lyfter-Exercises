import json
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


def from_json_to_dict (file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        my_json_value = json.load(file)
    return my_json_value


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

def main():
    show_pokemon_stats("pokemons2.json")


if __name__ == "__main__":
    main()