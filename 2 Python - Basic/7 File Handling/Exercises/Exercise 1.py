"""
Cree un programa que lea nombres de canciones de un archivo (línea por línea)
y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

Lea sobre el resto de métodos de la clase File de Python aquí
y cree una tabla donde explique qué hace cada uno.
No necesita usar código para esto, es solo crear una tabla en Notion o Word.

Siga el siguiente formato:

Método	    Descripción
read()	    Lee y retorna todo el contenido del archivo
readlines()	Lee todo el contenido del archivo y retorna una lista con cada línea.
write()	    Escribe contenidos en un archivo.
"""


def read_list():
    with open('MyList.txt','r',encoding="utf-8") as file:
        my_list = file.readlines()
        return my_list


def new_sorted_list(my_param_list,file_name):
    my_list = my_param_list
    my_list.sort()
    with open(file_name,"w",encoding="utf-8") as file:
        for line in my_list:
            file.write(line)


def main():
    music_list = read_list()
    new_sorted_list(music_list,"newSortedList.txt")


if __name__ == "__main__":
    main()


