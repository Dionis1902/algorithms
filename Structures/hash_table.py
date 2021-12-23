class Node:
    def __init__(self, data, key):
        self.__data = data
        self.__key = key
        self.next = None

    @property
    def data(self):
        return self.__data

    @property
    def key(self):
        return self.__key


class HashTable:
    def __init__(self):
        self.__capacity = 256
        self.__buckets = [None] * self.__capacity

    def __hash(self, key):
        return hash(key) % self.__capacity

    def __insert(self, key, data):
        i = self.__hash(key)

        node = self.__buckets[i]

        if node is None:
            self.__buckets[i] = Node(data, key)
        else:

            prev = node
            while node is not None:
                prev = node
                node = node.next
            prev.next = Node(data, key)

    def __find(self, key):
        i = self.__hash(key)

        node = self.__buckets[i]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.data

    def __remove(self, key):
        i = self.__hash(key)
        node = self.__buckets[i]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            result = node.data
            if prev is None:
                self.__buckets[i] = None
            else:
                prev.next = prev.next.next
            return result

    def __setitem__(self, key, data):
        self.__insert(key, data)

    def __getitem__(self, key):
        return self.__find(key)

    def __delitem__(self, key):
        self.__remove(key)


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table['foo'] = 'bar'
    hash_table['hello'] = 'world'

    print(hash_table['foo'])
    print(hash_table['hello'])

    del hash_table['foo']

    print(hash_table['foo'])
    print(hash_table['hello'])
