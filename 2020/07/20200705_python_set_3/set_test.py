import unittest


class SetTest(unittest.TestCase):

    def test_union(self):
        self.assertEqual({1, 2, 3, 4, 5, 6}, {1, 2, 3}.union({4, 5, 6}))
        self.assertEqual({1, 2, 3, 4, 5}, {1, 2, 3}.union({3, 4, 5}))
        self.assertEqual({1, 2, 3, 4, 5, 6}, {1, 2}.union({3, 4}, {5, 6}))

    def test_or(self):
        self.assertEqual({1, 2, 3, 4, 5, 6}, {1, 2, 3} | {4, 5, 6})
        self.assertEqual({1, 2, 3, 4, 5}, {1, 2, 3} | {3, 4, 5})
        self.assertEqual({1, 2, 3, 4, 5, 6}, {1, 2} | {3, 4} | {5, 6})

    def test_intersection(self):
        self.assertEqual({2, 3}, {1, 2, 3}.intersection({2, 3, 4}))
        self.assertEqual({3}, {1, 2, 3}.intersection({2, 3, 4}, {3, 4, 5}))

    def test_and(self):
        self.assertEqual({2, 3}, {1, 2, 3} & {2, 3, 4})
        self.assertEqual({3}, {1, 2, 3} & {2, 3, 4} & {3, 4, 5})

    def test_difference(self):
        self.assertEqual({1, 5, 6}, {1, 2, 3, 4, 5, 6}.difference({2, 3, 4}))
        self.assertEqual({1, 6}, {1, 2, 3, 4, 5, 6}.difference({2, 3}, {4, 5}))

    def test_minus(self):
        self.assertEqual({1, 5, 6}, {1, 2, 3, 4, 5, 6} - {2, 3, 4})
        self.assertEqual({1, 6}, {1, 2, 3, 4, 5, 6} - {2, 3} - {4, 5})

    def test_symmetric_difference(self):
        self.assertEqual({1, 2, 6, 7}, {1, 2, 3, 4, 5}.symmetric_difference({3, 4, 5, 6, 7}))

    def test_pow(self):
        self.assertEqual({1, 2, 6, 7}, {1, 2, 3, 4, 5} ^ {3, 4, 5, 6, 7})

    def test_copy(self):
        original = {1, 2, 3}
        copy = original.copy()
        self.assertEqual({1, 2, 3}, copy)

        copy.add(4)
        self.assertEqual({1, 2, 3}, original)
        self.assertEqual({1, 2, 3, 4}, copy)
