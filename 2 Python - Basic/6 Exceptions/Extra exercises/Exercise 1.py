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


def main():
    ask_name_and_age()

if __name__ == "__main__":
    main()

