import unittest


class IntObj:

    def __index__(self):
        return 987

    def __trunc__(self):
        return 654.321


class TruncObj:

    def __trunc__(self):
        return 654.321


class IntTest(unittest.TestCase):

    def test_normal_cases(self):
        self.assertEqual(0, int())
        self.assertEqual(123, int(123))
        self.assertEqual(456, int('456'))
        self.assertEqual(-456, int('-456'))

    def test_base(self):
        self.assertEqual(0, int('0', 0))

        self.assertEqual(3, int('11', 2))
        self.assertEqual(3, int(0b11))
        self.assertEqual(3, int(0B11))

        self.assertEqual(8, int('10', 8))
        self.assertEqual(8, int('010', 8))
        self.assertEqual(8, int(b'10', 8))
        self.assertEqual(8, int(0o10))
        self.assertEqual(8, int(0O10))

        self.assertEqual(15, int('F', 16))
        self.assertEqual(15, int(0xF))
        self.assertEqual(15, int(0XF))

        self.assertEqual(16, int('G', 17))
        self.assertEqual(17, int(b'10', 17))

    def test_float_cases(self):
        self.assertEqual(123, int(123.456))
        self.assertEqual(0, int(.456))

    def test_complex_cases(self):
        with self.assertRaises(TypeError) as context:
            # noinspection PyTypeChecker
            int(complex(852, 369))
        self.assertEqual("can't convert complex to int", context.exception.args[0])

    def test_exceptional_cases(self):
        with self.subTest('case 1'):
            with self.assertRaises(ValueError) as context:
                int('123.456')
            self.assertEqual("invalid literal for int() with base 10: '123.456'", context.exception.args[0])

        with self.subTest('case 2'):
            with self.assertRaises(ValueError) as context:
                int('abc')
            self.assertEqual("invalid literal for int() with base 10: 'abc'", context.exception.args[0])

        with self.subTest('case 3'):
            with self.assertRaises(ValueError) as context:
                int('010', 0)
            self.assertEqual("invalid literal for int() with base 0: '010'", context.exception.args[0])

        with self.subTest('case 4'):
            with self.assertRaises(ValueError) as context:
                int('2', 2)
            self.assertEqual("invalid literal for int() with base 2: '2'", context.exception.args[0])

    def test_obj(self):
        self.assertEqual(987, int(IntObj()))
        # noinspection PyTypeChecker
        self.assertEqual(654, int(TruncObj()))  # truncates towards zero


if __name__ == '__main__':
    unittest.main()
