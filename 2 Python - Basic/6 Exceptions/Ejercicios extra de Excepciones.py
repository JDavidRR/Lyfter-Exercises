"""
EXERCISE 1:

Cree un programa que:
Pida al usuario su nombre
Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
Ejemplo:

Entrada:
"Ingrese su nombre: " 5

Salida:
"El nombre no puede ser un número"

Luego pida su edad
Si no es un número válido, capture el ValueError y muestre un mensaje
Ejemplo:

Entrada:
"Ingrese su edad: " 5

Salida:
"Número no valido"

Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"
Ejemplo:

Entrada:
"Ingrese su nombre: " "Jean Carlo"
"Ingrese su edad: " 27

Salida:
Hola Jean Carlo, su edad es 27
"""

class NotValidAgeError (Exception):
    def __init__(self,age):
        super().__init__(f"Edad \'{age}\' fuera del rango aceptable")


def enter_name():
    name = str(input("Ingrese su nombre: "))
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")
    elif not name.replace(" ","").isalpha():
        raise ValueError("El nombre no puede contener símbolos o caracteres especiales")
    return name


def enter_age():
    age = str(input("Ingrese su edad: "))
    if not age.isdigit():
        raise ValueError ("Solo se pueden usar números")
    if 1 > int(age) or 100 < int(age) :
            raise NotValidAgeError (age)
    return age


def ask_name_and_age():
    name = ""
    age = 0
    try:
        name = enter_name()
        age = enter_age()
        print(f"Hola {name}, su edad es {age}")
    except ValueError as ex:
        print(f"ERROR: {ex}")
    except NotValidAgeError as ex:
        print(f"ERROR: {ex}")

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

"""
EXERCISE 3:
Cree una función sumar_valores(lista) que:
Reciba una lista de elementos (strings, enteros, flotantes mezclados)
Intente convertir cada elemento a tipo float
Si puede, sume el valor y muestre: "<valor> sumado correctamente"
Si no puede, muestre: "Elemento inválido: <valor>"
Al final, imprima la suma total
Ejemplo:

Entrada:
my_list = ['10', 'manzana', '5.5', '3', 'n/a']

Salida:
10.0 "sumado correctamente"
"Elemento inválido: manzana"
5.5 "sumado correctamente"
3.0 "sumado correctamente"
"Elemento inválido: n/a"
"Total de la suma:" 18.5
"""

def sumar_valores(lista):
    total = 0.0
    for element in lista:
        try:
            total += float(element)
            print (f"\"{element}\" sumado correctamente\"")
        except Exception:
            print(f"Elemento inválido: {element}")
    print(f"Total de la suma: {total}")


def main():
    #EXERCISE 1:
    ask_name_and_age()

    #EXERCISE 2:
    my_list = ['4', 'hola', '10', '5.2']
    convertir_a_entero(my_list)

    #EXERCISE 3:
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    sumar_valores(my_list)

if __name__ == "__main__":
    main()