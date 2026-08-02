"""2- Cree una clase base Animal y dos clases hijas Dog y Cat:
Animal debe tener nombre y método speak() que retorne "Hace un sonido"
Dog debe sobrescribir speak() para decir "Guau"
Cat debe sobrescribir speak() para decir "Miau"
Ejemplo:
Entrada:
dog = Dog("Firulais")

Salida:
print(dog.speak())  # Guau"""

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Makes a sound.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


    def speak(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")


def main():
    my_dog = Dog("Firu")
    my_cat = Cat("Michi")
    my_dog.speak()
    my_cat.speak()


if __name__ == "__main__":
    main()

