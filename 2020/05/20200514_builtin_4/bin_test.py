import unittest


class BinTest(unittest.TestCase):

    def test_bin_1(self):
        self.assertEqual(bin(0), '0b0')
        self.assertEqual(bin(3), '0b11')
        self.assertEqual(bin(-10), '-0b1010')

    def test_bin_2(self):
        self.assertEqual(format(3, '#b'), '0b11')
        self.assertEqual(format(14, '#b'), '0b1110')
        self.assertEqual(format(14, 'b'), '1110')

    def test_bin_3(self):
        self.assertEqual(f'{3:#b}', '0b11')
        self.assertEqual(f'{14:#b}', '0b1110')
        self.assertEqual(f'{14:b}', '1110')


if __name__ == '__main__':
    unittest.main()
