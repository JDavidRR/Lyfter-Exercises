"""
2- Cree una estructura de objetos que asemeje un Double Ended Queue.
- Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
- Debe incluir un método para hacer print de toda la estructura.
- No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
"""

class Node:
    data: str
    left_node: "Node"
    right_node: "Node"

    def __init__(self,data,left_node = None, right_node = None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


class DoubleEndedQueue:
    top_left: "Node"
    top_right: "Node"

    def __init__(self,node = None):
        self.top_left = node
        self.top_right = node

    def pop_left(self):
        if self.top_left:
            if self.top_left == self.top_right:
                temp = self.top_left
                self.top_left = None
                self.top_right = None
                return temp
            else:
                temp = self.top_left
                self.top_left = self.top_left.right_node
                self.top_left.left_node = None
                return temp
        else:
            raise IndexError("Cannot pop a value from an empty queue")

    def pop_right(self):
            if self.top_right:
                if self.top_left == self.top_right:
                    temp = self.top_right
                    self.top_left = None
                    self.top_right = None
                    return temp
                else:
                    temp = self.top_right
                    self.top_right = self.top_right.left_node
                    self.top_right.right_node = None
                    return temp
            else:
                raise IndexError("Cannot pop a value from an empty queue")

    def push_left(self, new_node : Node):
        if self.top_left:
            new_node.right_node = self.top_left
            self.top_left.left_node = new_node
            self.top_left = new_node
        else:
            self.top_left = new_node
            self.top_right = new_node

    def push_right(self, new_node : Node):
        if self.top_right:
            new_node.left_node = self.top_right
            self.top_right.right_node = new_node
            self.top_right = new_node
        else:
            self.top_left = new_node
            self.top_right = new_node

    def print_structure(self):
        if self.top_left:
            current_node = self.top_left
            while current_node:
                print(current_node.data)
                current_node = current_node.right_node
        else:
            print("No data in the queue")


def main():
    my_double_ended_queue = DoubleEndedQueue()
    my_first_node = Node("1st node")
    my_second_node = Node("2nd node")
    my_third_node = Node("3rd node")
    my_fourth_node = Node("4th node")
    my_double_ended_queue.push_left(my_first_node)
    my_double_ended_queue.push_right(my_second_node)
    my_double_ended_queue.push_left(my_third_node)
    my_double_ended_queue.push_right(my_fourth_node)
    my_double_ended_queue.print_structure()
    print("pop_left method return: ",my_double_ended_queue.pop_left().data)
    print("pop_right method return: ",my_double_ended_queue.pop_right().data)
    my_double_ended_queue.print_structure()

if __name__ == "__main__":
    main()
