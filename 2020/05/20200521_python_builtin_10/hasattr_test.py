import unittest


class X:
    pass


class HasattrTest(unittest.TestCase):

    def test_hasattr_1(self):
        x = X()
        self.assertFalse(hasattr(x, 'foobar'))

    def test_hasattr_2(self):
        x = X()
        x.foobar = 123
        self.assertTrue(hasattr(x, 'foobar'))

    def test_hasattr_3(self):
        x = X()
        x.foobar = 123
        delattr(x, 'foobar')
        self.assertFalse(hasattr(x, 'foobar'))


if __name__ == '__main__':
    unittest.main()
