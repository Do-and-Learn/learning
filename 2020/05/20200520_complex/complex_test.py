import unittest


class Complex:

    def __index__(self):
        return 3

    def __float__(self):
        return 2.2

    def __complex__(self):
        return 1 + 1j


class Float:

    def __index__(self):
        return 3

    def __float__(self):
        return 2.2


class Index:

    def __index__(self):
        return 3


class ComplexTest(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(0j, complex())
        self.assertEqual(1, complex(1))
        self.assertEqual(-1, complex(-1))
        self.assertEqual(1 + 2j, complex(1, 2))
        self.assertEqual(1 - 2j, complex(1, -2))
        self.assertEqual(1.5 - 2.6j, complex(1.5, -2.6))
        self.assertEqual(2j, complex(imag=2))
        self.assertEqual(-2j, complex(imag=-2))

    def test_example_2(self):
        self.assertEqual(1 + 0j, complex('1'))
        self.assertEqual(0 + 2j, complex('2j'))
        self.assertEqual(1 + 2j, complex('1+2j'))

    def test_example_3(self):
        self.assertEqual(1 + 2j, complex('1') + complex(imag=2))

    def test_example_4(self):
        self.assertEqual(1 + 1j, complex(Complex()))
        self.assertEqual(2.2, complex(Float()))
        self.assertEqual(3, complex(Index()))


if __name__ == '__main__':
    unittest.main()
