import json


"""
Investigue cómo leer y escribir archivos JSON en Python aquí.
Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON.
Debe leer el archivo para importar los Pokémones existentes.
Luego debe pedir la información del Pokémon a agregar.
Finalmente debe guardar el nuevo Pokémon en el archivo.
"""


def from_json_to_dict (file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        my_json_value = json.load(file)
    return my_json_value


def from_dict_to_json (file_path,my_value):
    with open(file_path,"w",encoding="utf-8") as file:
        json.dump(my_value,file,indent=4)


def ask_value_for_key (key):
    value = input(f"Please type a value for {key}: ")
    return value


def add_new_instance_to_dict (template_format):
    new_dict = {}
    for key,value in template_format.items():
        if isinstance(value,dict):
            print(f"Enter the {key}")
            new_dict[key] = add_new_instance_to_dict(value)
        elif isinstance(value,list):
            print(f"Enter the {key}")
            new_list = []
            counter = 1
            for element in value:
                new_list.append(ask_value_for_key(f"{key} No {counter}: "))
                counter += 1
            new_dict[key] = new_list
        else:
            new_dict[key] = ask_value_for_key(key)
    return new_dict


def main():
    my_json_value = from_json_to_dict("pokemons.json")
    template_format = my_json_value[0]
    my_json_value.append(add_new_instance_to_dict(template_format))
    from_dict_to_json("pokemons.json",my_json_value)


if __name__ == "__main__":
    main ()

