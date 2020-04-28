import unittest
from textwrap import wrap, fill


class FillTest(unittest.TestCase):

    def test_fill_1(self):
        self.assertEqual('123\n456', '\n'.join(wrap('123456', 3)))

    def test_fill_2(self):
        self.assertEqual('123\n456', fill('123456', 3))


if __name__ == '__main__':
    unittest.main()
