"""
EXERCISE 6:
Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
"""

def sort_str(str_param = "Here-We-Go"):
    the_list_of_words = []
    auxiliar_word = ""
    for index in range (0,len(str_param)):
        if str_param[index] == "-":
            the_list_of_words.append(auxiliar_word)
            auxiliar_word = ""
        else:
            auxiliar_word += str_param[index]
    the_list_of_words.append(auxiliar_word)
    auxiliar_word = ""
    the_list_of_words.sort()
    for word in the_list_of_words:
        auxiliar_word += word + "-"
    auxiliar_word = auxiliar_word[:-1]
    return auxiliar_word

print(sort_str("python-variable-funcion-computadora-monitor"))
