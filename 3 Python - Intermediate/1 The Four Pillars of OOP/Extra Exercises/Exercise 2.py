"""
Cree una clase abstracta User con los siguientes métodos abstractos:
get_role()
has_permission(permission)

Luego cree dos clases que hereden de ella:
AdminUser
RegularUser

Cada una debe implementar los métodos
Por ejemplo:

AdminUser siempre tiene permisos
RegularUser solo tiene permisos limitados ("read", por ejemplo)

Ejemplo:
Entrada:
user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

Salida:
print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  # False
"""
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self,name):
        self.name = name
        self.permissions = []

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(permission):
        pass


class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.permissions = ["Read","Write","Delete","Execute","Modify"]

    def get_role(self):
        return "Administrator"

    def has_permission(self,permission):
        if permission in self.permissions:
            return True
        return False


class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.permissions = ["Read","Execute"]

    def get_role(self):
        return "Regular User"

    def has_permission(self,permission):
        if permission in self.permissions:
            return True
        return False


def main():
    user1 = AdminUser("Carlos")
    user2 = RegularUser("Andrea")
    print(user1.name)
    print(user1.get_role())
    print(user1.has_permission("Delete"))
    print(user2.name)
    print(user2.get_role())
    print(user2.has_permission("Delete"))

if __name__ == "__main__":
    main()