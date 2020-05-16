import unittest


class ChrTest(unittest.TestCase):

    def test_chr(self):
        self.assertEqual(chr(97), 'a')
        self.assertEqual(chr(8364), '€')

    def test_invalid_chr(self):
        chr(0x10FFFF)
        with self.assertRaises(ValueError) as context:
            chr(0x110000)
        self.assertEqual(context.exception.args[0], 'chr() arg not in range(0x110000)')


if __name__ == '__main__':
    unittest.main()
