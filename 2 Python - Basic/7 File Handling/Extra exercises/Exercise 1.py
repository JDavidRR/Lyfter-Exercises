"""
EXERCISE 1:
Cree un programa que lea un archivo con texto línea por línea, 
quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo
Ejemplo:

Entrada:

Hola
mundo
esto
es
Python

Salida:

"Hola mundo esto es Python"
"""


def from_file_to_string(file_name):
    my_string = ""
    with open(file_name, "r", encoding = "utf-8") as file:
        list_file = file.readlines()
        for line in list_file:
            my_string = my_string + line[:-1] + " "
    return my_string


def from_string_to_new_file(my_string,new_file_name):
    with open(new_file_name, "w", encoding = "utf-8") as file:
        file.write(my_string)


def main ():
    from_string_to_new_file(from_file_to_string("HolaMundo.txt"),"NuevoHolaMundo.txt")


if __name__ == "__main__":
    main()
