"""
1- Cree un decorador que haga print de los parámetros y retorno de la función que decore.
"""

def decorator_param_printer(func):
    def wrapper(*args):
        for item in args:
            print(f"Printing parameter: {item}")
        return func(*args)
    return wrapper

@decorator_param_printer
def addition(num1 , num2):
    return num1 + num2

def main():
    print(addition(10,20))

if __name__ == "__main__":
    main()

