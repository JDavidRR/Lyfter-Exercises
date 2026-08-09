"""
3- Cree una clase de User que:
- Tenga un atributo de date_of_birth.
- Tenga un property de age.
Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.
"""

class UnderAgeError(Exception):
    def __init__(self, user):
        super().__init__(f"Error: {user.name} is \"{user.age}\". This activity requires 18+ years.")

class Drink:
    def __init__(self, name, drink_type):
        self.name = name
        self.type = drink_type

def decorator_is_user_adult(func):
    def wrapper(user_param, drink_param):
        try:
            if drink_param.type == "Alcoholic":
                if user_param.age >= 18:
                    return func(user_param, drink_param)
                else:
                    raise UnderAgeError(user_param)
            else:
                return func(user_param, drink_param)
        except UnderAgeError as ex:
            print(f"{ex} {drink_param.name} is an alcoholic drink")
    return wrapper

class User():
    def __init__(self, name, date_of_birth, age):
        self.name = name
        self.date_of_birth = date_of_birth
        self.age = age

    @decorator_is_user_adult
    def drink(self, drink : Drink):
        print(f"{self.name} is drinking '{drink.name}' ({drink.type}).")

def main():
    drink1 = Drink("Beer", "Alcoholic")
    drink2 = Drink("Whiskey", "Alcoholic")
    drink3 = Drink("Wine", "Alcoholic")
    drink4 = Drink("Orange Juice", "Non-Alcoholic")

    user1 = User("Alice", "01/01/2005", 21)
    user2 = User("Bob", "10/05/2010", 14)
    user3 = User("Charlie", "03/03/2018", 8)
    user4 = User("Diana", "07/07/2000", 26)

    drinks = [drink1, drink2, drink3, drink4]
    users = [user1, user2, user3, user4]

    for user in users:
        for drink in drinks:
            user.drink(drink)


if __name__ == "__main__":
    main()
