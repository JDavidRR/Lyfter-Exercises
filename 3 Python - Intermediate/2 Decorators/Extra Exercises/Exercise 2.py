"""
2- Cree un decorador @requires_login que:
Verifique si la variable global user_logged_in es True
Si no lo es, debe lanzar una excepción "Usuario no autenticado"
Si lo es, la función decorada se ejecuta normalmente
Ejemplo:

Entrada:
user_logged_in = False

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")
"""

user_logged_in = False


def requires_login(fun):
    def wrapper(user, *args):
        global user_logged_in
        if user_logged_in:
            return fun(user, *args)
        raise ValueError("User not authenticated. Please log in first.")
    return wrapper


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def try_login(self, email, password):
            if self.email == email and self.password == password:
                global user_logged_in
                user_logged_in = True
                print("Login successful")
                return True
            print("Wrong credentials")
            return False

    @requires_login
    def view_profile(self):
        print(f"Showing {self.name}'s profile...")


def main():
    my_new_user = User("Jose", "c@gmail.com", "123")
    my_new_user.try_login("c@gmail.com", "123")
    my_new_user.view_profile()

if __name__ == "__main__":
    main()

