class Node:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent


class Tree:
    def __init__(self):
        self._root = None

    def insert(self, value):
        if not self._root:
            self._root = Node(value)
            return
        self._insert(value, self._root)

    def _insert(self, value, node):
        if value > node.value:
            if not node.right:
                node.right = Node(value, node.right)
                return
            return self._insert(value, node.right)
        else:
            if not node.left:
                node.left = Node(value, node.left)
                return
            return self._insert(value, node.left)

    def print(self):
        self._print(self._root)

    def _print(self, node):
        if node:
            print(node.value)
            self._print(node.right)
            self._print(node.left)
        return


tree = Tree()
tree.insert(4)
tree.insert(46)
tree.insert(7)
tree.insert(1)
tree.insert(9)
tree.print()
