import unittest


class PowTest(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(0.02631578947368421, pow(38, -1))
        self.assertEqual(32, pow(2, 5))
        self.assertEqual(-32, pow(-2, 5))
        self.assertEqual(6.25, pow(-2.5, 2))

        self.assertEqual(23, pow(38, -1, 97))
        self.assertEqual(1, (23 * 38) % 97)

        self.assertEqual(44, pow(38, -2, 97))
        self.assertEqual(1, 44 * (38 ** 2) % 97)

        self.assertEqual(42, pow(38, -3, 97))
        self.assertEqual(1, 42 * (38 ** 3) % 97)

    def test_example_2(self):
        self.assertEqual(-2, pow(10, 2, -3))
        self.assertEqual(100, pow(10, 2))
        self.assertEqual(3, pow(10, 2, 97))
        self.assertEqual(3, 10 ** 2 % 97)

        self.assertEqual(0.01, pow(10, -2))
        self.assertEqual(65, pow(10, -2, 97))
        self.assertEqual(1, (65 * (10 ** 2) % 97))

    # noinspection PyTypeChecker
    def test_example_3(self):
        with self.assertRaises(TypeError) as context:
            pow(10, 2, 1.1)
        self.assertEqual('pow() 3rd argument not allowed unless all arguments are integers', context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            pow(10, 2.2, 1)
        self.assertEqual('pow() 3rd argument not allowed unless all arguments are integers', context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            pow(10.5, 2, 1)
        self.assertEqual('pow() 3rd argument not allowed unless all arguments are integers', context.exception.args[0])


if __name__ == '__main__':
    unittest.main()
