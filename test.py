import unittest
from main import find


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find(5, '101101101'), 3)

    def test_2(self):
        self.assertEqual(find(5, '1111101'), 1)

    def test_3(self):
        self.assertEqual(find(5, '110011011'), 3)

    def test_4(self):
        self.assertEqual(find(7, '100111011110100100111110110011100101000111100101110010001100111011110100100111110110011100101000110010110000111100101110010001'), -1)


if __name__ == '__main__':
    unittest.main()
