"""
Cree una estructura que represente una cola básica (Queue) con objetos enlazados
Restricción:
no usar list, dict, tuple, collections
Métodos requeridos:
enqueue(data): agrega un nodo al final
Ejemplo:

Entrada:
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

Salida:
A -> B -> C

dequeue(): elimina y retorna el nodo del inicio
Ejemplo:

Entrada:
q.dequeue()

Salida:
"A"

print_all(): imprime todos los elementos de la cola en orden
Ejemplo:

Entrada:
q.print_all()

Salida:
B -> C
"""

class Node:
    data: str
    node: "Node"

    def __init__(self,data,node = None):
        self.data = data
        self.node = node


class Queue:
    def __init__(self, node : Node = None):
        self.head = node

    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.node != None:
                temp = temp.node
            temp.node = new_node

    def dequeue(self):
        if self.head:
            temporal = self.head
            self.head = self.head.node
            print(temporal.data)
            return temporal.data
        else:
            raise IndexError("Cannot dequeue a value from an empty Queue")

    def print_all(self):
        result = ""
        temp = self.head
        while temp != None:
            if temp == self.head:
                result = (temp.data)
            else:
                result += f" -> {temp.data}"
            temp = temp.node
        print(result)


def main():
    my_queue = Queue()
    my_queue.enqueue("Z")
    my_queue.enqueue("Y")
    my_queue.enqueue("X")
    my_queue.enqueue("A")
    my_queue.enqueue("B")
    my_queue.enqueue("C")
    print("print method:")
    my_queue.print_all()
    print("dequeue:")
    my_queue.dequeue()
    print("dequeue:")
    my_queue.dequeue()
    print("print method:")
    my_queue.print_all()


if __name__ == "__main__":
    main()