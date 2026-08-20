"""
3- Cree una estructura de objetos que asemeje un Binary Tree.
- Debe incluir un método para hacer print de toda la estructura.
- No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

    def print_tree(self):
        self._print_in_order(self.root,0)

    def _print_in_order(self, node, level):
        if node is not None:
            self._print_in_order(node.left, level+1)
            print( "Level: ",level, "\t" * (level+1), node.data)
            self._print_in_order(node.right, level+1)


def main():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    print("Binary Tree:")
    tree.print_tree()


if __name__ == "__main__":
    main()

# After doing some research, I realized how this works.
# The complexity of recursive functions is key here.
# It's hard to imagine a static approach for building such data structures.