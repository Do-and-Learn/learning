import unittest


class DivmodTest(unittest.TestCase):

    def test_divmod_1(self):
        self.assertEqual(divmod(1, 1), (1, 0))
        self.assertEqual(divmod(1, 2), (0, 1))
        self.assertEqual(divmod(2, 1), (2, 0))
        self.assertEqual(divmod(4, 3), (1, 1))

    def test_divmod_2(self):
        with self.assertRaises(ZeroDivisionError) as context:
            divmod(1, 0)
        self.assertEqual(context.exception.args[0], 'integer division or modulo by zero')

    def test_divmod_3(self):
        self.assert_divmod(divmod(1.1, 1), (1.0, 0.1))
        self.assert_divmod(divmod(2.4, 0.1), (23.0, 0.1))  # (24, 0)?
        self.assert_divmod(divmod(2.4, 0.2), (11.0, 0.2))  # (12, 0)?
        self.assert_divmod(divmod(2.4, 0.3), (8.0, 0.0))
        self.assert_divmod(divmod(2.4, 0.6), (4.0, 0.0))
        self.assert_divmod(divmod(2.4, 0.8), (2.0, 0.8))  # (3, 0)?
        self.assert_divmod(divmod(2.4, 1.2), (2.0, 0.0))
        self.assert_divmod(divmod(3.4, 1.7), (2.0, 0.0))

    def assert_divmod(self, first, second):
        self.assertAlmostEqual(first[0], second[0])
        self.assertAlmostEqual(first[1], second[1])


if __name__ == '__main__':
    unittest.main()
