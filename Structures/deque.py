class Node:
    def __init__(self, data):
        self.__data = data
        self.next = None

    @property
    def data(self):
        return self.__data


class Deque:
    def __init__(self):
        self.__front = None
        self.__size = 0

    def insert_front(self, data):
        temp = Node(data)
        self.__size += 1
        if not self.__size:
            self.__front = temp
        else:
            temp.next = self.__front
            self.__front = temp

    def insert_back(self, data):
        temp = Node(data)
        self.__size += 1
        if not self.__size:
            self.__front = temp
        else:
            current = self.__front
            while current.next:
                current = current.next
            current.next = temp

    def delete_front(self):
        if not self.__size:
            return
        temp = self.__front
        self.__front = self.__front.next
        self.__size -= 1
        del temp

    def delete_back(self):
        if not self.__size:
            return
        current = self.__front
        previous = None
        self.__size -= 1
        while current.next:
            previous = current
            current = current.next
        if previous:
            previous.next = None
        del current

    def size(self):
        return self.__size

    def get_front(self):
        if not self.__size:
            return
        return self.__front.data

    def get_back(self):
        if not self.__size:
            return
        current = self.__front
        while current.next:
            current = current.next
        return current.data

    def clear(self):
        current = self.__front
        while current.next:
            temp = current
            current = current.next
            del temp
        del current
        self.__size = 0


if __name__ == '__main__':
    deque = Deque()

    deque.insert_front(1)
    deque.insert_front(2)
    deque.insert_front(3)

    deque.insert_back(11)
    deque.insert_back(12)
    deque.insert_back(13)

    print(deque.get_front())
    print(deque.get_back())

    deque.delete_front()
    deque.delete_back()

    print(deque.get_front())
    print(deque.get_back())

    deque.clear()
