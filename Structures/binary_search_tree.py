class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        if type(other) != Node:
            return self.data < other
        return self.data < other.data

    def __gt__(self, other):
        if type(other) != Node:
            return self.data > other
        return self.data > other.data


class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, data):
        temp = Node(data)
        if not self.__root:
            self.__root = temp
        else:
            self.__insert(self.__root, temp)

    def delete(self, data):
        if self.__root:
            self.__delete(self.__root, data)

    def show_tree(self):
        print(', '.join(str(element) for element in self.__show_tree(self.__root)))

    def find(self, data):
        return self.__find(self.__root, data) is not None

    def __insert(self, root, node):
        if node > root:
            if not root.right:
                root.right = node
            else:
                self.__insert(root.right, node)
        else:
            if not root.left:
                root.left = node
            else:
                self.__insert(root.left, node)

    @staticmethod
    def __min_value_node(root):
        current = root
        while current.left:
            current = current.left
        return current

    def __delete(self, root, data):
        if not root:
            return root

        if root > data:
            root.left = self.__delete(root.left, data)
        elif root < data:
            root.right = self.__delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.__min_value_node(root.right)
            root.data = temp.data
            root.right = self.__delete(root.right, temp.data)
        return root

    def __show_tree(self, root):
        if not root:
            return
        yield root.data
        yield from self.__show_tree(root.right)
        yield from self.__show_tree(root.left)

    def __find(self, root, data):
        if not root:
            return
        if root > data:
            return self.__find(root.left, data)
        elif root < data:
            return self.__find(root.right, data)
        return root


if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(34)
    binary_search_tree.insert(342)
    binary_search_tree.insert(3)
    binary_search_tree.insert(1)
    binary_search_tree.insert(454)
    binary_search_tree.insert(5)

    binary_search_tree.show_tree()
    binary_search_tree.delete(3)
    binary_search_tree.show_tree()

    print(binary_search_tree.find(5))