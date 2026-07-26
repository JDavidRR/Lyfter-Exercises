"""
EXERCISE 3:
Cree un programa que:
Lea un archivo línea por línea
Convierta cada línea a mayúsculas
Escriba el contenido en un nuevo archivo
Ejemplo:

Entrada:

# archivo original:
hola mundo
esto es python

Salida:

# archivo nuevo:
HOLA MUNDO
ESTO ES PYTHON
"""


def new_file_upper(file_name):
    my_list = []
    with open(file_name, "r", encoding = "utf-8") as file:
        list_file = file.readlines()
        for line in list_file:
            my_list.append(line.upper())
    
    with open(f"UPPER - {file_name}", "w", encoding = "utf-8") as file:
        file.writelines(my_list)


def main ():
    new_file_upper("HolaMundo.txt")


if __name__ == "__main__":
    main()
