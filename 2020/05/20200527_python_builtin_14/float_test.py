import math
import random
import unittest
from math import inf


class FloatClass:

    def __float__(self):
        return 1.234

    def __index__(self):
        return 6789


class IntegerClass:

    def __index__(self):
        return 6789


class Foo:
    pass


class FloatTest(unittest.TestCase):

    def test_normal_cases(self):
        self.assertEqual(1, float('1'))
        self.assertEqual(1.2345, float('1.2345'))
        self.assertEqual(0.001, float('1e-003'))
        self.assertEqual(1000000, float('+1E6'))
        self.assertEqual(0, float())

    def test_special_normal_case(self):
        self.assertEqual(1.2345, float('   1.2345  '))
        self.assertEqual(-12345, float('   -12345\n'))
        self.assertEqual(-12345, float(-12345))

    def test_sign(self):
        self.assertEqual(.3, float('.3'))
        self.assertEqual(.3, float('+.3'))
        self.assertEqual(-.3, float('-.3'))
        self.assertEqual(1.23, float('+1.23'))

    def test_inf(self):
        self.assertEqual(inf, float('Infinity'))
        self.assertEqual(inf, float('infinity'))
        self.assertEqual(-inf, float('-Infinity'))
        self.assertEqual(-inf, float('-infinity'))
        self.assertEqual(inf, float('inf'))
        self.assertEqual(inf, float('INF'))
        self.assertEqual(-inf, float('-INF'))
        self.assertEqual(inf, float(random.choice('123456789') + ''.join(random.choices('1234567890', k=1000))))

    def test_nan(self):
        self.assertTrue(math.isnan(float('nan')))
        self.assertFalse(math.isnan(float('123')))

    def test_abnormal_cases(self):
        abnormal_cases = ['', 'hello', '1.2.3', '123 hi']
        for case in abnormal_cases:
            with self.subTest(case):
                with self.assertRaises(ValueError) as context:
                    float(case)
                self.assertEqual(f'could not convert string to float: \'{case}\'', context.exception.args[0])

    def test_overflow(self):
        with self.assertRaises(OverflowError) as context:
            float(math.factorial(171))
        self.assertEqual('int too large to convert to float', context.exception.args[0])

    def test_classes(self):
        self.assertEqual(1.234, float(FloatClass()))
        self.assertEqual(6789, float(IntegerClass()))

    # noinspection PyTypeChecker
    def test_no_float_or_index_method_class(self):
        with self.assertRaises(TypeError) as context:
            float(Foo())
        self.assertEqual('float() argument must be a string or a number, not \'Foo\'', context.exception.args[0])
