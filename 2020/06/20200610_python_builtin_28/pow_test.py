import unittest


class PowTest(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(0.02631578947368421, pow(38, -1))
        self.assertEqual(23, pow(38, -1, 97))
        self.assertEqual(1, (23 * 38) % 97)

    def test_example_2(self):
        self.assertEqual(100, pow(10, 2))
        self.assertEqual(3, pow(10, 2, 97))
        self.assertEqual(0.01, pow(10, -2))
        self.assertEqual(65, pow(10, -2, 97))


if __name__ == '__main__':
    unittest.main()
