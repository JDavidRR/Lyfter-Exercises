"""
1- Cree una estructura de objetos que asemeje un Stack.
- Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
- Debe incluir un método para hacer print de toda la estructura.
- No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
"""


class Node:
    data: str
    node: "Node"

    def __init__(self,data,node = None):
        self.data = data
        self.node = node


class Stack:
    top: "Node"

    def __init__(self,node = None):
        self.top = node

    def pop(self):
        if self.top:
            temporal = self.top
            self.top = self.top.node
            return temporal
        else:
            raise IndexError("Cannot pop a value from an empty Stack")

    def push(self,node):
        if self.top:
            node.node = self.top
            self.top = node
        else:
            self.top = node

    def print_stack(self):
        node = self.top
        while node:
            print(node.data)
            node = node.node


def main():
    my_stack = Stack()
    my_first_node = Node("1st node")
    my_second_node = Node("2nd node")
    my_third_node = Node("3rd node")
    my_stack.push(my_first_node)
    my_stack.push(my_second_node)
    my_stack.push(my_third_node)
    print("pop method return: ",my_stack.pop().data)
    my_stack.print_stack()

if __name__ == "__main__":
    main()