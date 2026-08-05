"""2- Cree una clase abstracta de Shape que:
Tenga los métodos abstractos de calculate_perimeter y calculate_area.
Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro."""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return pi * (self.radius ** 2)


    def calculate_perimeter(self):
        return 2 * pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side


    def calculate_perimeter(self):
        return 4 * self.side


    def calculate_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
            self.length = length
            self.width = width


    def calculate_perimeter(self):
        return ( 2 * self.length) + ( 2 * self.width)


    def calculate_area(self):
        return self.width * self.length


def main():
    my_circle = Circle(10)
    print(f"Circle radius: {my_circle.radius}")
    print(f"Area: {my_circle.calculate_area()}")
    print(f"Perimeter: {my_circle.calculate_perimeter()}\n")
    my_square = Square(5)
    print(f"Square side: {my_square.side}")
    print(f"Area: {my_square.calculate_area()}")
    print(f"Perimeter: {my_square.calculate_perimeter()}\n")
    my_rectangle = Rectangle(15,5)
    print(f"Rectangle length: {my_rectangle.length}")
    print(f"Rectangle width: {my_rectangle.width}")
    print(f"Area: {my_rectangle.calculate_area()}")
    print(f"Perimeter: {my_rectangle.calculate_perimeter()}\n")


if __name__ == "__main__":
    main()