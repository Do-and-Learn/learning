import unittest


class HexObj:
    _num: int

    def __init__(self, num: int):
        self._num = num

    def __index__(self):
        return self._num


class HexTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual('0xff', hex(255))
        self.assertEqual('-0xff', hex(-255))
        self.assertEqual('-0x2a', hex(-42))

    def test_hex_from_index_method(self):
        self.assertEqual('0xff', hex(HexObj(255)))
        self.assertEqual('-0xff', hex(HexObj(-255)))
        self.assertEqual('-0x2a', hex(HexObj(-42)))

    def test_hex_format(self):
        self.assertEqual('0xff', '%#x' % 255)
        self.assertEqual('0XFF', '%#X' % 255)
        self.assertEqual('ff', '%x' % 255)
        self.assertEqual('FF', '%X' % 255)

    def test_hex_format_2(self):
        self.assertEqual('0xff', format(255, '#x'))
        self.assertEqual('0XFF', format(255, '#X'))
        self.assertEqual('ff', format(255, 'x'))
        self.assertEqual('FF', format(255, 'X'))

    def test_hex_format_3(self):
        self.assertEqual('0xff', f'{255:#x}')
        self.assertEqual('0XFF', f'{255:#X}')
        self.assertEqual('ff', f'{255:x}')
        self.assertEqual('FF', f'{255:X}')

    def test_float_hex(self):
        self.assertEqual('0x1.999999999999ap-4', float(0.1).hex())
        self.assertEqual('0x1.199999999999ap+0', float(1.1).hex())

    # noinspection PyTypeChecker
    def test_hex_float(self):
        with self.assertRaises(TypeError) as context:
            hex(float(0.1))
        self.assertEqual('\'float\' object cannot be interpreted as an integer', context.exception.args[0])


if __name__ == '__main__':
    unittest.main()
