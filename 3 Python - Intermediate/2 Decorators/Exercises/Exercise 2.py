"""
2- Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.
"""

def decorator_are_param_num(func):
    def wrapper(*params):
        try:
            for item in params:
                if not isinstance(item, (int, float)):
                    raise ValueError(f"Error, the value \"{item}\" is not numeric")
            return func(*params)
        except ValueError as e:
            print(e)
    return wrapper

@decorator_are_param_num
def addition(num1 , num2):
    return num1 + num2

def main():
    print(addition("10","20"))

if __name__ == "__main__":
    main()
