import unittest
from main import *


class Test(unittest.TestCase):
    def test_a_g(self):
        self.assertEqual(breadth_first_search(test_graph, 'a', 'e'), True)

    def test_a_z(self):
        self.assertEqual(breadth_first_search(test_graph, 'a', 'z'), False)


if __name__ == '__main__':
    unittest.main()
