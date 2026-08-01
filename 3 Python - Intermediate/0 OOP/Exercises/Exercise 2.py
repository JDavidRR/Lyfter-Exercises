"""
2- Cree una clase de Bus con:
- Un atributo de max_passengers.
- Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección).
Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
- Un método para bajar pasajeros uno por uno (en cualquier orden).
"""
import random

class Person():
	def __init__(self, name):
		self.name = name

class Bus():
    max_passengers = 78
    passengers = []


    def __init__(self,max_passengers = 78):
        self.max_passengers = max_passengers


    def add_passenger(self, passenger : Person):
        if len(self.passengers) != self.max_passengers:
            self.passengers.append(passenger)
            print(f"{passenger.name} boarded the bus.")
        else:
            print(f"Sorry {passenger.name}, the bus has reached it's maximum capacity.")


    def leave_passenger(self):
        if len(self.passengers) == 0:
            print("The bus is empty")
        else:
            print(f"{self.passengers.pop(random.randint(0,(len(self.passengers)-1))).name} got off the bus")


def main():
    my_bus = Bus(4)
    pepe = Person("Pepe")
    juan = Person("Juan")
    camila = Person("Camila")
    ana = Person("Ana")
    paola = Person ("Paola")
    my_bus.add_passenger(pepe)
    my_bus.add_passenger(juan)
    my_bus.add_passenger(camila)
    my_bus.add_passenger(ana)
    my_bus.add_passenger(paola)
    my_bus.leave_passenger()
    my_bus.leave_passenger()
    my_bus.leave_passenger()
    my_bus.leave_passenger()
    my_bus.leave_passenger()


if __name__ == "__main__":
    main()

