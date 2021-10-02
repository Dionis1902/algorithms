import unittest
from main import *


class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]),
                         [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)])

    def test_normalize(self):
        self.assertEqual(normalize_time([(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]),
                         [(0, 1), (3, 8), (9, 12)])


if __name__ == '__main__':
    unittest.main()
