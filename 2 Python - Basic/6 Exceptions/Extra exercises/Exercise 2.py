"""
EXERCISE 2:

Cree una función convertir_a_entero(lista) que:
Reciba una lista de strings
Intente convertir cada elemento a entero usando int()
Use try-except para atrapar los errores ValueError
Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
Ejemplo:

Entrada:
my_list = ['4', 'hola', '10', '5.2']

Salida:
"Resultado:"
"4" "convertido a" 4
"No se pudo convertir el elemento: hola"
"10" "convertido a" 10
"No se pudo convertir el elemento: 5.2"
"""

def convertir_a_entero(list_param = []):
    list = list_param
    number = 0
    for element in list:
        try:
            number = int(element)
            print (f"\"{element}\" \"convertido a\" {number}")
        except Exception:
            print(f"No se pudo convertir el elemento {element}")


def main():
    my_list = ['4', 'hola', '10', '5.2']
    convertir_a_entero(my_list)

if __name__ == "__main__":
    main()

