class Node:
    def __init__(self, data):
        self.__data = data
        self.next = None

    @property
    def data(self):
        return self.__data


class Stack:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def push(self, data):
        temp = Node(data)
        if self.is_empty():
            self.__root = temp
        else:
            temp.next = self.__root
            self.__root = temp

        self.__size += 1

    def pop(self):
        if self.is_empty():
            return
        self.__size -= 1

        return_data = self.__root.data
        self.__root = self.__root.next
        return return_data

    def peek(self):
        if self.is_empty():
            return
        return self.__root.data

    def size(self):
        return self.__size


if __name__ == '__main__':
    stack = Stack()

    stack.push(3)
    stack.push(2)
    stack.push(1)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())