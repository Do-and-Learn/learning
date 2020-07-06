import unittest


class SetTest(unittest.TestCase):
    def test_update(self):
        s = {1, 2}
        s.update({3, 4})
        self.assertEqual({1, 2, 3, 4}, s)

        s = {1, 2}
        s.update({3, 4}, {5, 6}, {7, 8})
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, s)

    def test_e_or(self):
        s = {1, 2}
        s |= {3, 4}
        self.assertEqual({1, 2, 3, 4}, s)

        s = {1, 2}
        s |= {3, 4} | {5, 6} | {7, 8}
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, s)

    def test_intersection_update(self):
        s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s.intersection_update({2, 4, 6, 8})
        self.assertEqual({2, 4, 6, 8}, s)

        s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s.intersection_update({2, 4}, {4, 6}, {4, 8})
        self.assertEqual({4}, s)

    def test_e_and(self):
        s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s &= {2, 4, 6, 8}
        self.assertEqual({2, 4, 6, 8}, s)

        s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s &= {2, 4} & {4, 6} & {4, 8}
        self.assertEqual({4}, s)

    def test_difference_update(self):
        s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s.difference_update({2, 4, 6, 8})
        self.assertEqual({0, 1, 3, 5, 7, 9}, s)

        s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s.difference_update({2, 4}, {6, 8})
        self.assertEqual({0, 1, 3, 5, 7, 9}, s)

    def test_e_minus(self):
        s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s -= {2, 4, 6, 8}
        self.assertEqual({0, 1, 3, 5, 7, 9}, s)

        s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s -= {2, 4} | {6, 8}
        self.assertEqual({0, 1, 3, 5, 7, 9}, s)
