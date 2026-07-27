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

