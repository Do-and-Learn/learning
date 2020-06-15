import unittest


class RoundObj:

    def __init__(self, val):
        self.val = val

    def __round__(self, n=None):
        if n:
            return self.val * n
        return self.val * 10


class Foo:
    pass


class RoundTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual(0, round(0.5))  # rounding is done toward the even choice
        self.assertEqual(1, round(0.6))
        self.assertEqual(0, round(-0.5))  # rounding is done toward the even choice
        self.assertEqual(1, round(1.4))
        self.assertEqual(2, round(1.5))
        self.assertEqual(2, round(2.5))  # rounding is done toward the even choice
        self.assertEqual(-2, round(-1.5))

    def test_example_2(self):
        self.assertEqual(2.67, round(2.675, 2))  # not a bug

    def test_example_3(self):
        self.assertEqual(1, round(0.51, None))
        self.assertEqual(1, round(0.51))
        self.assertEqual(0.51, round(0.51, 2))
        self.assertEqual(0.5, round(0.51, 1))
        self.assertEqual(0.6, round(0.55, 1))
        self.assertEqual(0.5, round(0.549, 1))

    def test_example_4(self):
        self.assertEqual(5, round(RoundObj(0.5)))
        self.assertEqual(1, round(RoundObj(0.5), 2))

    # noinspection PyTypeChecker
    def test_example_5(self):
        with self.assertRaises(TypeError) as context:
            round(Foo())
        self.assertEqual("type Foo doesn't define __round__ method", context.exception.args[0])
