import unittest
from main import QueueWithPriority


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = QueueWithPriority()
        self.queue.insert_with_priority(3, 5)
        self.queue.insert_with_priority(7, 2)
        self.queue.insert_with_priority(433, 7)
        self.queue.insert_with_priority(323, 0)

    def test_get(self):
        self.assertEqual(self.queue.get_highest_priority_element(), 433)

    def test_pull(self):
        self.assertEqual(self.queue.pull_highest_priority_element(), 433)
        self.assertEqual(len(self.queue), 3)

    def test_insert(self):
        self.queue.insert_with_priority(124, 44)
        self.assertEqual(self.queue.get_highest_priority_element(), 124)


if __name__ == '__main__':
    unittest.main()
