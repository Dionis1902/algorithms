class Node:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value


class Tree:

    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node:
            return True
        return False

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    def min_elem(self):
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def max_elem(self):
        node = self.root
        while node.right:
            node = node.right
        return node.value

    def _insert(self, node, value):
        if value >= node.value:
            if not node.right:
                node.right = Node(value, node)
                return
            else:
                return self._insert(node.right, value)
        else:
            if not node.left:
                node.left = Node(value, node)
                return
            else:
                return self._insert(node.left, value)

    def _search(self, node_to_check, value):
        if (not node_to_check) or node_to_check.value == value:
            return node_to_check

        if value > node_to_check.value:
            return self._search(node_to_check.right, value)
        else:
            return self._search(node_to_check.left, value)

    def print_elems(self):
        if not self.root:
            print("No elements in tree")
            return
        print(self.root.value, end=", ")
        self._print_node_child(self.root.left)
        self._print_node_child(self.root.right)
        print(chr(8) * 2)

    def _print_node_child(self, current_node):
        if current_node:
            print(current_node.value, end=", ")
            self._print_node_child(current_node.left)
        else:
            return

        if current_node.left:
            self._print_node_child(current_node.left)
        if current_node.right:
            self._print_node_child(current_node.right)

    def pretty_print(self):
        if not self.root:
            print("No elements in tree")
            return
        lines, *_ = self._pretty_print(self.root)
        for line in lines:
            print(line)

    def _pretty_print(self, node):
        if node.right is None and node.left is None:
            line = str(node.value)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None:
            lines, width, height, middle = self._pretty_print(node.left)
            str_value = str(node.value)
            value_len = len(str_value)
            first_line = (middle + 1) * ' ' + (width - middle - 1) * '_' + str_value
            second_line = middle * ' ' + '/' + (width - middle - 1 + value_len) * ' '
            shifted_lines = [line + value_len * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, width + value_len, height + 2, width + value_len // 2

        if node.left is None:
            lines, width, height, middle = self._pretty_print(node.right)
            str_value = str(node.value)
            value_len = len(str_value)
            first_line = str_value + middle * '_' + (width - middle) * ' '
            second_line = (value_len + middle) * ' ' + '\\' + (width - middle - 1) * ' '
            shifted_lines = [value_len * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, width + value_len, height + 2, value_len // 2

        left, l_width, l_height, l_middle = self._pretty_print(node.left)
        right, r_width, r_height, r_middle = self._pretty_print(node.right)
        str_value = str(node.value)
        value_len = len(str_value)
        first_line = (l_middle + 1) * ' ' + (l_width - l_middle - 1) * '_' + str_value + r_middle * '_' + (r_width - r_middle) * ' '
        second_line = l_middle * ' ' + '/' + (l_width - l_middle - 1 + value_len + r_middle) * ' ' + '\\' + (r_width - r_middle - 1) * ' '
        if l_height < r_height:
            left += [l_width * ' '] * (r_height - l_height)
        elif r_height < l_height:
            right += [r_width * ' '] * (l_height - r_height)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + value_len * ' ' + b for a, b in zipped_lines]
        return lines, l_width + r_width + value_len, max(l_height, r_height) + 2, l_width + value_len // 2


test = Tree()
test.insert(6)
test.insert(10)
test.insert(11)
test.insert(9)
test.insert(4)
test.insert(2)
test.insert(5)
test.insert(4)
test.insert(-1)
test.insert(8)
test.pretty_print()
