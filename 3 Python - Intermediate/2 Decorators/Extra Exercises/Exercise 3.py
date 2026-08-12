"""
Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
A esta función se le debe combinar dos decoradores:
@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
@validate_numbers: revisa que todos los argumentos sean numéricos
Ejemplo:
Entrada:
multiply(3, 4)

Salida:
"func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Resultado: 12"
"Resultado 12"
"""
from datetime import datetime

class NotValidNumberError (Exception):
    def __init__(self,number):
        super().__init__(f"Error: \"{number}\". Not valid number")


def validate_numbers(func):
    def wrapper(*args):
        try:
            for value in args:
                number = float(value)
            return func(*args)
        except ValueError as ex:
            raise NotValidNumberError(ex)
    return wrapper


def log_call(func):
    def wrapper(*args):
        result = func(*args)
        current_time = datetime.now()
        print(f"func: {func.__name__} - args: ", *args, f" - [{current_time}] - Resultado: {result}")
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(value1,value2):
    return value1*value2


def main():
    multiply(35,2)
    multiply("a",2)


if __name__ == "__main__":
    main()