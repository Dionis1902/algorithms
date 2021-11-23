import unittest
from main import *


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(prima(TEST_GRAPH).values()), 18)


if __name__ == '__main__':
    unittest.main()
