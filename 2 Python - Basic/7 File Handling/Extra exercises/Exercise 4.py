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
    add_line_to_file("HelloHello.txt")


if __name__ == "__main__":
    main()
