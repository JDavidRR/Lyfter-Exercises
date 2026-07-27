
"""
EXERCISE 1:
Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
Ejemplo:
Entrada:
"programacion"
"Ingrese el carácter que desea buscar:" "o"
Salida:
"Se a encontrado 2 veces el carácter"
"""

text = str(input(" \n\nType your text and hit ENTER at the end.\n"))
char = ""
while len(char) != 1:
    char = str(input("Type a character to search in the text and press ENTER: "))


def count_character(text,char):
    counter = 0
    for index in range (0,len(text)):
        if text[index] == char:
            counter += 1
    return counter

chat_times = count_character(text,char)
print(f"The character \"{char}\" is shown in the text {chat_times} times.\n\n")
