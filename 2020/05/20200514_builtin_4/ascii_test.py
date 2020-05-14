import unittest


class AsciiTest(unittest.TestCase):

    def test_ascii(self):
        self.assertEqual(ascii("Hello Teddy"), "'Hello Teddy'")
        self.assertEqual(ascii([1, 2, 3]), "[1, 2, 3]")
        self.assertEqual(ascii((3, 'Teddy', 9)), "(3, 'Teddy', 9)")

    def test_non_ascii(self):
        self.assertEqual(ascii("å"), "'\\xe5'")


if __name__ == '__main__':
    unittest.main()
