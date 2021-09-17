class Element:
    def __init__(self, value, priority: int):
        self.value = value
        self.__priority = priority

    @property
    def priority(self):
        return self.__priority

    def __str__(self):
        return 'Value : {value}, Priority : {priority}'.format(value=self.value, priority=self.__priority)


class QueueWithPriority:
    def __init__(self):
        self._heap = []

    def push(self, value, priority):
        self._heap.append(Element(value, priority))
        self._bottom_up(len(self) - 1)

    def pop(self):
        if self._heap:
            self._heap[len(self) - 1], self._heap[0] = self._heap[0], self._heap[len(self) - 1]
            root = self._heap.pop()
            self._top_down(0)
            return root.value
        return None

    def __len__(self):
        return len(self._heap)

    def peek(self):
        if self._heap:
            return self._heap[0].value
        return None

    def _bottom_up(self, index):
        root_index = (index - 1) // 2
        if root_index < 0:
            return

        if self._heap[index].priority > self._heap[root_index].priority:
            self._heap[index], self._heap[root_index] = self._heap[root_index], self._heap[index]
            self._bottom_up(root_index)

    def _top_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index
        if right_child_index >= len(self._heap):
            return

        if self._heap[largest].priority < self._heap[left_child_index].priority:
            largest = left_child_index
        if self._heap[largest].priority < self._heap[right_child_index].priority:
            largest = right_child_index

        if largest is not index:
            self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
            self._top_down(largest)


if __name__ == '__main__':
    queue = QueueWithPriority()
    queue.push(23, 4)
    queue.push(56, 0)
    queue.push(567, 2)
    queue.push(346, 5)
    queue.push(679, 2)
    queue.push(45746, 45)
    print(queue.pop())
    print(queue.pop())
