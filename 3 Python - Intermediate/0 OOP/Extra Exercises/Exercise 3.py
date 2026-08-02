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


def add_product(list_param : list):
    name = ask_name()
    price = ask_price()
    quantity = ask_quantity()
    my_product = Product(name,price,quantity)
    list_param.append(my_product)


def is_valid_name(name):
    if name == "":
        return False
    for char in name:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


def ask_name():
    name = ""
    try:
        name = str(input("Enter the product's name: "))
        name = " ".join(name.split())
        if not is_valid_name(name):
            raise ValueError(f"Invalid name \"{name}\". Please use letters and spaces only.")
    except ValueError as ex:
        print(f"\nError: [ValueError] {ex}")
        input("Hit Enter to continue...")
        name = ask_name()
    return name


def ask_price():
    number = ""
    try:
        number = str(input("Type a price and hit enter: "))
        if not number.isnumeric():
            raise ValueError(f"Error: Only numbers are allowed")
        elif (float(number) < 1):
            raise NotValidNumberError(number)
        else:
            return float(number)
    except ValueError as ex:
        print(f"\nError: [ValueError] Cannot convert the value \"{number}\" to a number {ex}")
        input("Hit Enter to continue...")
        return ask_price()
    except NotValidNumberError as ex:
        print(f"\nError: [NotValidNumberError] {ex}")
        input("Hit Enter to continue...")
        return ask_price()


def ask_quantity():
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
        return ask_quantity()
    except NotValidQuantityError as ex:
        print(f"\nError: [NotValidQuantityError] {ex}")
        input("Hit Enter to continue...")
        return ask_quantity()


def show_products(my_products:list[Product]):
    for product in my_products:
        print(f"\nProduct: {product.name}, price: {product.price}, quantity: {product.inventory}")


def calculate_total_value_of_inventory(my_products:list[Product]):
    total = 0
    for product in my_products:
        total += product.price * product.inventory
    return total


def main():
    my_products=[]
    add_product(my_products)
    add_product(my_products)
    show_products(my_products)
    print(f"TOTAL: {calculate_total_value_of_inventory(my_products)}")


if __name__ == "__main__":
    main()

