"""
EXERCISE 3:

Lista doblemente enlazada
Requisitos:
Cada nodo debe tener referencia al siguiente y al anterior
Métodos:
append(data): Agrega al final
Ejemplo:

Entrada:
dll.append("A")
dll.append("B")
dll.append("C")

Salida (print_forward):
A -> B -> C

Salida (print_bacward)
C -> B -> A

prepend(data): Agrega al inicio
Ejemplo:

Entrada:
dll.prepend("X")

Salida(print_forward):
X -> A -> B -> C

Salida(print_backward):
C -> B -> A -> X


delete(data): Elimina el primer nodo con ese valor
Ejemplo:

Entrada:
dll.delete("B")

Salida(print_forward):
X -> A -> C

Salida(print_backward):
C -> A -> X

print_forward() y print_backward(): Imprime en ambas direcciones
Ejemplo:

Salida:
print_forward()  #→ X -> A -> C
print_backward() #← C -> A -> X
"""

class Node:
    data: str
    prev_node: "Node"
    next_node: "Node"

    def __init__(self,data,prev_node = None, next_node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class DoubleLinkedList:
    head: "Node"
    tail: "Node"

    def __init__(self,node = None):
        self.head = node
        self.tail = node

    def append(self, data):
        new_node = Node(data)
        if self.tail:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def print_forward(self):
        print("print_forward method:")
        if self.head:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next_node
        else:
            print("No data in the list")

    def print_backward(self):
        print("print_backward method:")
        if self.tail:
            current_node = self.tail
            while current_node:
                print(current_node.data)
                current_node = current_node.prev_node
        else:
            print("No data in the list")

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next_node
                    if self.head:
                        self.head.prev_node = None

                elif current == self.tail:
                    self.tail = current.prev_node
                    self.tail.next_node = None

                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node

                print("Deleted: ",data)
                return data
            current = current.next_node
        print(f"The value {data} wasn't found")


def main():
    my_double_linked_list = DoubleLinkedList()
    my_double_linked_list.prepend("A")
    my_double_linked_list.append("B")
    my_double_linked_list.prepend("C")
    my_double_linked_list.append("D")
    my_double_linked_list.print_forward()
    my_double_linked_list.delete("A")
    my_double_linked_list.print_forward()
    my_double_linked_list.delete("B")
    my_double_linked_list.print_backward()

if __name__ == "__main__":
    main()
