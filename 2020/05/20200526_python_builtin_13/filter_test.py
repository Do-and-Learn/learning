import unittest


class FilterTest(unittest.TestCase):
    def test_none(self):
        self.assertCountEqual([], filter(None, []))
        self.assertCountEqual([], filter(None, [False]))
        self.assertCountEqual([True], filter(None, [True]))
        self.assertCountEqual([True], filter(None, [True, False]))
        self.assertCountEqual([True, True], filter(None, [True, False, True]))

    def test_filter_even(self):
        def is_even(x):
            return x % 2 == 0

        self.assertCountEqual([0, 2, 4, 6, 8, 10], filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertCountEqual([0, 2, 4, 6, 8, 10], filter(is_even, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_generator_expression(self):
        def is_even(x):
            return x % 2 == 0

        src = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertCountEqual((val for val in src if is_even(val)), filter(is_even, src))
