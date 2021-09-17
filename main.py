class QueueWithPriority:
    def __init__(self):
        self.__queue = list()

    def insert_with_priority(self, value, priority: int = 0):
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
    queue = QueueWithPriority()
    queue.insert_with_priority(23, 4)
    queue.insert_with_priority(56, 0)
    queue.insert_with_priority(567, 2)
    queue.insert_with_priority(346, 5)
    queue.insert_with_priority(679, 2)
    queue.insert_with_priority(45746, 45)
    for element in queue:
        print(element)
