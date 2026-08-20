"""
EXERCISE 2:
Cree una clase LinkedList con los métodos:

insert_front(data): Inserta al inicio
Ejemplo:

Entrada:
ll.insert_front(10)
ll.insert_front(20)

Salida:
20 -> 10

insert_back(data): Inserta al final
Ejemplo:

Entrada:
ll.insert_back(30)

Salida:
20 -> 10 -> 30

delete(data): Elimina el primer nodo con el valor dado
Ejemplo:

Entrada:
ll.delete(10)

Salida:
20 -> 30

print_all(): Imprime todos los valores
Ejemplo:

Salida:
ll.print_all() #20 -> 30
"""

class Node:
    data: str
    node: "Node"

    def __init__(self,data,node = None):
        self.data = data
        self.node = node


class LinkedList:
    def __init__(self, node = None):
        self.head = node

    def insert_front(self, data):
        new_node = Node(data)
        if self.head:
            new_node.node = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.node != None:
                temp = temp.node
            temp.node = new_node

    def delete(self, data):
        temp = self.head
        prev = self.head
        if temp:
            while temp:
                if temp.data == data:
                    if temp == self.head:
                        self.head = temp.node
                        print("Deleted: ",data)
                        return data
                    elif temp.node == None:
                        prev.node = None
                        print("Deleted: ",data)
                        return data
                    else:
                        prev.node = temp.node
                        print("Deleted: ",data)
                        return data
                prev = temp
                temp = temp.node
            print(f"The value {data} wasn't found")
        else:
            print("Cannot delete a value from an empty LinkedList")

    def print_all(self):
        temp = self.head
        result = ""
        if temp:
            while temp:
                if temp == self.head:
                    result = (temp.data)
                else:
                    result += f" -> {temp.data}"
                temp = temp.node
            print(result)
        else:
            print("Empty LinkedList")


def main():
    my_linked_list = LinkedList()
    my_linked_list.insert_front("X")
    my_linked_list.insert_front("A")
    my_linked_list.insert_back("Y")
    my_linked_list.insert_back("B")
    my_linked_list.delete("A")
    my_linked_list.print_all()


if __name__ == "__main__":
    main()