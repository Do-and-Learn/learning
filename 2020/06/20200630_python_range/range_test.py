import unittest


class RangeTest(unittest.TestCase):

    def test_constructor(self):
        self.assertEqual([0, 1, 2, 3, 4], list(range(5)))
        self.assertEqual([], list(range(0)))
        self.assertEqual([], list(range(-5)))

    def test_constructor_start(self):
        self.assertEqual([5, 6, 7, 8, 9], list(range(5, 10)))
        self.assertEqual([-5, -4, -3, -2, -1], list(range(-5, 0)))
        self.assertEqual([], list(range(-5, -8)))

    def test_constructor_start_step(self):
        self.assertEqual([5, 7, 9], list(range(5, 10, 2)))
        self.assertEqual([5, 7, 9], list(range(5, 11, 2)))
        self.assertEqual([5], list(range(5, 6, 2)))
        self.assertEqual([-5, -7, -9], list(range(-5, -10, -2)))
        self.assertEqual([0, -1, -2, -3, -4], list(range(0, -5, -1)))

    def test_exception(self):
        with self.assertRaises(ValueError) as context:
            range(0, 10, 0)
        self.assertEqual("range() arg 3 must not be zero", context.exception.args[0])
