import unittest

# Truth value testing: https://docs.python.org/3/library/stdtypes.html#truth
from decimal import Decimal
from fractions import Fraction


class BoolTest(unittest.TestCase):

    def test_bool_1(self):
        for false_value in [None, False, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), complex(0, 0), '', (), [], {}, set(), range(0)]:
            with self.subTest(str(false_value)):
                self.assertFalse(bool(false_value))
                self.assertFalse(false_value)

    def test_bool_2(self):
        for true_value in [True, 1, 0.1, 1j, Decimal(1), Fraction(1, 1), complex(0, 1), ' ', (0, 0), [0], {0}, range(1)]:
            with self.subTest(str(true_value)):
                self.assertTrue(bool(true_value))
                self.assertTrue(true_value)


if __name__ == '__main__':
    unittest.main()
