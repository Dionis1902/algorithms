import unittest
from main import QueueWithPriority


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = QueueWithPriority()
        self.queue.push(3, 5)
        self.queue.push(7, 2)
        self.queue.push(433, 7)
        self.queue.push(323, 0)

    def test_get(self):
        self.assertEqual(self.queue.peek(), 433)

    def test_pull(self):
        self.assertEqual(self.queue.pop(), 433)
        self.assertEqual(len(self.queue), 3)

    def test_insert(self):
        self.queue.push(124, 44)
        self.assertEqual(self.queue.peek(), 124)


if __name__ == '__main__':
    unittest.main()
