class QueueWithPriority:
    def __init__(self):
        self.__queue = list()

    def insert_with_priority(self, value, priority: int = 0):
        if not self:
            self.__queue.insert(0, QueueWithPriority.__Element(value, priority))
            return
        for i, element in enumerate(self.__queue):
            if priority >= element.priority:
                self.__queue.insert(i, QueueWithPriority.__Element(value, priority))
                return
        self.__queue.append(QueueWithPriority.__Element(value, priority))

    def pull_highest_priority_element(self):
        if self:
            return self.__queue.pop(0).value
        return None

    def get_highest_priority_element(self):
        if self:
            return self.__queue[0].value
        return None

    def __iter__(self):
        return (element for element in self.__queue)

    def __len__(self):
        return len(self.__queue)

    def __str__(self):
        return 'Count of elements {count}'.format(count=len(self))

    class __Element:
        def __init__(self, value, priority: int):
            self.value = value
            self.__priority = priority

        @property
        def priority(self):
            return self.__priority

        def __str__(self):
            return 'Value : {value}, Priority : {priority}'.format(value=self.value, priority=self.__priority)


if __name__ == '__main__':
    q = QueueWithPriority()
    q.insert_with_priority([24], 4)
    q.insert_with_priority(56, 0)
    q.insert_with_priority([3524], 2)
    q.insert_with_priority([3456], 5)
    q.insert_with_priority([67967], 2)
    q.insert_with_priority([67967], 45)
    print(q.get_highest_priority_element())
