
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

"""
EXERCISE 2:
Cree una función que reciba una lista de palabras y un número n,
y retorne una nueva lista con solo las palabras que tengan más de n letras
Ejemplo:
Entrada:
["cielo","sol","maravilloso","día"]
"Ingrese el numero de letras minimas en la palabra: " 4
Salida:
["cielo","maravilloso"]
"""
list_of_words = ["cielo","sol","maravilloso","día"]

def cut_list(list_of_words = ["empty list", "but not really"], char_num = 10):
    output_list = []
    for word in list_of_words:
        if len(word) > char_num:
            output_list.append(word)
    return output_list

print(str(cut_list(list_of_words,4)) + "\n\n")

"""
EXERCISE 3:
Cree una función que reciba un string y retorne cuántas vocales contiene
Ejemplo:
Entrada:
"Hola mundo"
Salida:
4
"""

text = str(input(" \n\nType your text and hit ENTER at the end.\n"))

def count_vowels(text = ""):
    text = text.lower()
    counter = 0
    for index in range (0,len(text)):
        if text[index] == 'a' or text[index] == 'e' or text[index] == 'i' or text[index] == 'o' or text[index] == 'u':
            counter += 1
    return counter

print(count_vowels(text))