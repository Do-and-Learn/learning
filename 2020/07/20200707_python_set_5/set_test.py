import unittest


class SetTest(unittest.TestCase):

    def test_symmetric_difference_update(self):
        s = {1, 2, 3, 5, 8, 13, 21}
        s.symmetric_difference_update({2, 4, 6, 8, 10})
        self.assertEqual({1, 3, 4, 5, 6, 10, 13, 21}, s)

    def test_e_pow(self):
        s = {1, 2, 3, 5, 8, 13, 21}
        s ^= {2, 4, 6, 8, 10}
        self.assertEqual({1, 3, 4, 5, 6, 10, 13, 21}, s)

    def test_add(self):
        s = {2, 3, 4, 5}
        s.add(1)
        self.assertEqual({1, 2, 3, 4, 5}, s)

    def test_remove(self):
        s = {1, 2, 3, 4}
        s.remove(4)
        self.assertEqual({1, 2, 3}, s)

        with self.assertRaises(KeyError) as context:
            s.remove(9)
        self.assertEqual(9, context.exception.args[0])

    def test_discard(self):
        s = {1, 2, 3, 4}
        s.discard(4)
        self.assertEqual({1, 2, 3}, s)

        s.discard(4)  # will not throw an exception

    def test_pop(self):
        s = {1, 2, 3, 4}
        self.assertEqual(1, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual(3, s.pop())
        self.assertEqual(4, s.pop())

        with self.assertRaises(KeyError) as context:
            s.pop()
        self.assertEqual("pop from an empty set", context.exception.args[0])

    def test_clear(self):
        s = {1, 2, 3, 4}
        s.clear()
        self.assertEqual(set(), s)
