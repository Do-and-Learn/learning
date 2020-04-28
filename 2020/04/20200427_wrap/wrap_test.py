import textwrap
import unittest


class WrapTest(unittest.TestCase):

    def test_wrap(self):
        self.assertListEqual(['12', '34', '56', '78'], textwrap.wrap('12345678', width=2))

    def test_wrap2(self):
        self.assertListEqual(['12345', '678'], textwrap.wrap('12345678', width=5))


if __name__ == '__main__':
    unittest.main()
