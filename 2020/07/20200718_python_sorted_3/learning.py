import random
import unittest


class SetTest(unittest.TestCase):

    def test_ascending(self):
        lst = list(range(10))
        random.shuffle(lst)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], sorted(lst))

    def test_descending(self):
        lst = list(range(10))
        random.shuffle(lst)
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], sorted(lst, reverse=True))
