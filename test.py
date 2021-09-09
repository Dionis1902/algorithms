from main import quick_sort
import unittest


class TestQuickSort(unittest.TestCase):
    def test_asc(self):
        self.assertEqual(quick_sort([1, 0, 4, 6, 6, 1]), [0, 1, 1, 4, 6, 6])

    def test_desc(self):
        self.assertEqual(quick_sort([1, 0, 4, 6, 6, 1], False), [6, 6, 4, 1, 1, 0])

    def test_asc_asc(self):
        self.assertEqual(quick_sort([0, 1, 1, 4, 6, 6]), [0, 1, 1, 4, 6, 6])

    def test_desc_asc(self):
        self.assertEqual(quick_sort([6, 6, 4, 1, 1, 0]), [0, 1, 1, 4, 6, 6])

    def test_asc_desc(self):
        self.assertEqual(quick_sort([0, 1, 1, 4, 6, 6], False), [6, 6, 4, 1, 1, 0])

    def test_desc_desc(self):
        self.assertEqual(quick_sort([6, 6, 4, 1, 1, 0], False), [6, 6, 4, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
