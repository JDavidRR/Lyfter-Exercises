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


def main ():
    count_file_words("HolaMundo.txt")


if __name__ == "__main__":
    main()
