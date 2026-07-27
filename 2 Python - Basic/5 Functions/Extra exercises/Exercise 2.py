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

