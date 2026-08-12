"""
1- Cree una función que imprima “Hola, [nombre]” dos veces:
Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, con los mismos argumentos
Ejemplo:
Salida:
"Hola, Jeanca"
"Hola, Jeanca"
"""

def repeat_twice(fun):
    def wrapper(arg):
        fun(arg)
        fun(arg)
    return wrapper

@repeat_twice
def print_name(name):
    print (f"Hola, {name}")

def main():
    print_name("Jeanca")

if __name__ == "__main__":
    main()
