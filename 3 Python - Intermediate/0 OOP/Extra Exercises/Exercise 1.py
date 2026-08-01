"""
1- Cree una clase Rectangle que:
- Tenga atributos width y height
- Tenga un método get_area() que retorne el área
- Tenga un método get_perimeter() que retorne el perímetro
- Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

Ejemplo 1:
Entrada:

"Ingrese la altura: " 250
"Ingrese el ancho: " 300

Salida:
print(rectangle.get_area()) #75000
print(rectangle.get_perimeter()) #1100

Ejemplo 2:
Entrada:
"Ingrese la altura: " -250
"Ingrese el ancho: " 300

Salida:
"Existe un valor negativo, los valores deben ser positivos"
"""

class NotAllowedNumberError(Exception):
    def __init__(self, number):
        super().__init__(f"Not allowed number: The number {number} is negative or cero.")


class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0


    def set_attributes(self,width_p,height_p):
        self.width = width_p
        self.height = height_p


    def ask_attributes(self):
        try:
            height = str(input("Insert the height: "))
            width = str(input("Insert the width: "))
            if not height.isnumeric():
                raise ValueError(height)
            if not width.isnumeric():
                raise ValueError(width)
            if float(height) <= 0:
                raise NotAllowedNumberError(height)
            elif float(width) <= 0:
                raise NotAllowedNumberError(width)
            return float(width),float(height)
        except NotAllowedNumberError as ex:
            print(f"Error [NotAllowedNumberError]: {ex}\n")
            return self.ask_attributes()
        except ValueError as ex:
            print(f"\nError: [ValueError] Cannot convert the value. {ex}\n")
            return self.ask_attributes()


    def get_area(self):
        return self.width * self.height


    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)


def main():
    my_rectangle = Rectangle()
    my_rectangle.set_attributes(*my_rectangle.ask_attributes())
    print (f"The area of this rectangle is: {my_rectangle.get_area()}")
    print (f"The perimeter of this rectangle is: {my_rectangle.get_perimeter()}")


if __name__ == "__main__":
    main()