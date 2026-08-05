"""
Cree una clase Employee con los siguientes requisitos:
Atributos privados: _name, _salary
Use @property y @<atributo>.setter para:
Mostrar el nombre y el salario
Validar que el salario nunca sea negativo
Cree un método promote que aumente el salario un porcentaje definido
Ejemplo:
Entrada:

employee = Employee("Ana", 1000)
employee.promote(0.1)  # +10%

Salida:
print(employee.salary)  # 1100
"""

class Employee():
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        if salary < 0 :
            raise ValueError("Salary cannot be negative")
        self._salary = salary

    def promote(self,value):
        if value < 0:
            raise ValueError("Promotion percentage cannot be negative")
        self.salary += self.salary * value

    def ask_name():
        while True:
            try:
                name = input("Enter the employee's name: ").strip()
                if not name:
                    raise ValueError("Name cannot be empty")
                return name
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def ask_salary():
        while True:
            try:
                salary = float(input("Enter the initial salary: "))
                if salary < 0:
                    raise ValueError("Salary cannot be negative")
                return salary
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def ask_percentage():
        while True:
            try:
                percentage = float(input("Enter the promotion percentage (e.g., 0.1 for 10%): "))
                if percentage < 0:
                    raise ValueError("Promotion percentage cannot be negative")
                return percentage
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

def main():
    my_employee1 = Employee("Juan",2000)
    my_employee2 = Employee(Employee.ask_name(),Employee.ask_salary())
    my_employee1.promote(0.15)
    my_employee2.promote(Employee.ask_percentage())
    
    print (f"Nombre: {my_employee1.name}, Salario: {my_employee1.salary}")
    print (f"Nombre: {my_employee2.name}, Salario: {my_employee2.salary}")

if __name__ == "__main__":
    main()

