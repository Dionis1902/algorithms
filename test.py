import unittest
from main import boyer_moore


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(boyer_moore("world", "hello world!"), 6)

    def test_not_find(self):
        self.assertEqual(boyer_moore("world", "test hello!"), -1)


if __name__ == '__main__':
    unittest.main()
