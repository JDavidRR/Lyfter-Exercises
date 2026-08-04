"""3- Cree una clase Product con:
Nombre, precio y cantidad
Cree una clase Inventory que:
Guarde productos en una lista
Tenga métodos para:
Agregar un producto
Mostrar todos los productos
Calcular el valor total del inventario

Ejemplo:
Entrada:
product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

Salida:
print(product.calculate_total_value_of_inventory) #34000"""

class NotValidQuantityError (Exception):
    def __init__(self,option):
        super().__init__(f"Error: The option \"{option}\" doesn't exist")

class NotValidNumberError (Exception):
    def __init__(self,number):
        super().__init__(f"Error: \"{number}\" is not a valid number")

class Product():
    def __init__(self,name,price,inventory):
        self.name = name
        self.price = price
        self.inventory = inventory

class Inventory():
    def __init__(self):
        self.my_products = []

    def add_product(self):
        name = self.ask_name()
        price = self.ask_price()
        quantity = self.ask_quantity()
        my_product = Product(name,price,quantity)
        self.my_products.append(my_product)

    def is_valid_name(self,name):
        if name == "":
            return False
        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False
        return True

    def ask_name(self):
        name = ""
        try:
            name = str(input("Enter the product's name: "))
            name = " ".join(name.split())
            if not self.is_valid_name(name):
                raise ValueError(f"Invalid name \"{name}\". Please use letters and spaces only.")
        except ValueError as ex:
            print(f"\nError: [ValueError] {ex}")
            input("Hit Enter to continue...")
            name = self.ask_name()
        return name

    def ask_price(self):
        number = ""
        try:
            number = float(input("Type a price and hit enter: "))
            if number < 1:
                raise NotValidNumberError(number)
            else:
                return number
        except ValueError as ex:
            print(f"\nError: [ValueError] Cannot convert the value \"{number}\" to a number {ex}")
            input("Hit Enter to continue...")
            return self.ask_price()
        except NotValidNumberError as ex:
            print(f"\nError: [NotValidNumberError] {ex}")
            input("Hit Enter to continue...")
            return self.ask_price()

    def ask_quantity(self):
        option = ""
        try:
            option = str(input("Type a quantity and hit enter: "))
            if not option.isdecimal():
                raise ValueError(f"Error: Only whole numbers are allowed")
            elif (int(option) < 1):
                raise NotValidQuantityError(option)
            else:
                return int(option)
        except ValueError as ex:
            print(f"\nError: [ValueError] Cannot convert the value \"{option}\" to integer {ex}")
            input("Hit Enter to continue...")
            return self.ask_quantity()
        except NotValidQuantityError as ex:
            print(f"\nError: [NotValidQuantityError] {ex}")
            input("Hit Enter to continue...")
            return self.ask_quantity()

    def show_products(self):
        for product in self.my_products:
            print(f"\nProduct: {product.name}, price: {product.price}, quantity: {product.inventory}")

    def calculate_total_value_of_inventory(self):
        total = 0
        for product in self.my_products:
            total += product.price * product.inventory
        return total


def main():
    my_inventory = Inventory()
    my_inventory.add_product()
    my_inventory.add_product()
    my_inventory.show_products()
    print(f"TOTAL: {my_inventory.calculate_total_value_of_inventory()}")


if __name__ == "__main__":
    main()

