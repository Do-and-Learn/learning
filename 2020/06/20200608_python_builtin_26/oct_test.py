import unittest


class Index:

    def __init__(self, index):
        self.index = index

    def __index__(self):
        return self.index


class OctTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual('0o10', oct(8))
        self.assertEqual('0o10', oct(Index(8)))
        self.assertEqual('-0o70', oct(-56))
        self.assertEqual('-0o70', oct(Index(-56)))

    def test_format(self):
        self.assertEqual('0o12', '%#o' % 10)
        self.assertEqual('0o12', '%#o' % Index(10))
        self.assertEqual('0o12', format(10, '#o'))
        self.assertEqual('0o12', f'{10:#o}')
        self.assertEqual('12', '%o' % 10)
        self.assertEqual('12', '%o' % Index(10))
        self.assertEqual('12', format(10, 'o'))
        self.assertEqual('12', f'{10:o}')
