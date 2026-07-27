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
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    sumar_valores(my_list)

if __name__ == "__main__":
    main()

