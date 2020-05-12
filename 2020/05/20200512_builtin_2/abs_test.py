import unittest


class DString:

    def __init__(self, s):
        self.s = s

    def __abs__(self):
        return len(self.s)


class ABSTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1, abs(1))
        self.assertEqual(1.0, abs(1.0))
        self.assertEqual(1, abs(1.0))
        self.assertEqual(9.99, abs(9.99))
        self.assertEqual(1, abs(-1))
        self.assertEqual(1.0, abs(-1.0))
        self.assertEqual(9.99, abs(-9.99))

    def test_complex_number(self):
        self.assertEqual(pow(1 * 1 + 2 * 2, 0.5), abs(complex(1, 2)))
        self.assertEqual(pow(2 * 2 + 2 * 2, 0.5), abs(complex(2, 2)))
        self.assertEqual(pow(2 * 2 + 5 * 5, 0.5), abs(complex(2, -5)))

    def test_abs_method(self):
        self.assertEqual(1, abs(DString('A')))
        self.assertEqual(5, abs(DString('Hello')))


if __name__ == '__main__':
    unittest.main()
