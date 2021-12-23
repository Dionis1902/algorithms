class Node:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    @property
    def data(self):
        return self.__data

    @property
    def priority(self):
        return self.__priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority


class PriorityQueue:
    def __init__(self):
        self.__heap = []

    def insert(self, data, priority: int = 0):
        self.__heap.append(Node(data, priority))
        for i in range(self.size()//2, -1, -1):
            self.heapify(i)

    def pop(self):
        if not self.__heap:
            return None
        self.__heap[self.size() - 1], self.__heap[0] = self.__heap[0], self.__heap[self.size() - 1]
        root = self.__heap.pop()
        for i in range(self.size()//2, -1, -1):
            self.heapify(i)
        return root.data

    def peek(self):
        if not self.__heap:
            return None
        return self.__heap[0].data

    def size(self):
        return len(self.__heap)

    def heapify(self, i):
        biggest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.size() and self.__heap[biggest] < self.__heap[left]:
            biggest = left

        if right < self.size() and self.__heap[biggest] < self.__heap[right]:
            biggest = right

        if biggest != i:
            self.__heap[i], self.__heap[biggest] = self.__heap[biggest], self.__heap[i]
            self.heapify(biggest)


if __name__ == '__main__':
    priority_queue = PriorityQueue()

    priority_queue.insert('5th', 0)
    priority_queue.insert('2nd', 3)
    priority_queue.insert('3rd', 2)
    priority_queue.insert('1st', 4)
    priority_queue.insert('4th', 1)

    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())
