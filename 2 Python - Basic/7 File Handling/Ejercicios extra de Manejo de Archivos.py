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


"""
EXERCISE 2:
Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
(Considere que las palabras están separadas por espacios y/o saltos de línea)
Ejemplo:

Salida:

"Este archivo contiene " 123 "palabras"
"""


def count_file_words(file_name):
    my_string = ""
    with open(file_name, "r", encoding = "utf-8") as file:
        list_file = file.readlines()
        for line in list_file:
            my_string = my_string + line[:-1] + " "
    words = my_string.split()
    print(f"\"Este archivo contiene \" {len(words)} \"palabras\"")


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


"""
EXERCISE 4:
Cree un programa que:
Pida al usuario una línea de texto
Agregue esa línea al final de un archivo existente
Si el archivo no existe, lo crea automáticamente
Ejemplo:

Entrada:

"Este es un nuevo registro"

Salida:

"El texto se agrega al final del archivo sin borrar lo anterior"
"""


def add_line_to_file(file_name):
    newline = str(input("Please insert a new line and hit ENTER:\n\n"))


    with open(file_name,"a",encoding = "utf-8") as file:
        file.write("\n" + newline)


def main ():
    from_string_to_new_file(from_file_to_string("HolaMundo.txt"),"NuevoHolaMundo.txt") #EXERCISE 1
    count_file_words("HolaMundo.txt") #EXERCISE 2
    new_file_upper("HolaMundo.txt") #EXERCISE 3
    add_line_to_file("HelloHello.txt") #EXERCISE 4


if __name__ == "__main__":
    main()
