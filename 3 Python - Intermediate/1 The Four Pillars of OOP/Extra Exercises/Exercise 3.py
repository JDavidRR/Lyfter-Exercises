"""
Cree una clase base Vehicle con los atributos:
_brand
_year
Agregue un método get_info() que devuelva una descripción del vehículo.
Luego cree dos clases hijas:
Car
Motorcycle
Cada una debe agregar su propio atributo (por ejemplo, doors o type) y sobrescribir el método get_info() para incluir esta información adicional.

Ejemplo:
Entrada:
vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

Salida:
print(vehicle1.get_info())  # Toyota (2020) - 4 puertas
print(vehicle2.get_info())  # Yamaha (2022) - Tipo: Deportiva
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self.brand} ({self.year})"

    @property
    def brand(self):
        return self._brand

    @property
    def year(self):
        return self._year

class Car(Vehicle):
    def __init__(self, brand, year, car_model):
        super().__init__(brand, year)
        self.car_model = car_model

    def get_info(self):
        return super().get_info() + f" - {self.car_model}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, mot_type):
        super().__init__(brand, year)
        self.mot_type = mot_type

    def get_info(self):
        return super().get_info() + f" - {self.mot_type}"

def main():
    my_car = Car("Mazda",2002,"RX-7")
    my_moto = Motorcycle("Horwin",2026,"Café racer")
    print(my_car.get_info())
    print(my_moto.get_info())

if __name__ == "__main__":
    main()

