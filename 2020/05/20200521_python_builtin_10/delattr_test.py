import unittest


class X:
    pass


class DelattrTest(unittest.TestCase):

    def test_delattr_1(self):
        x = X()
        with self.assertRaises(AttributeError) as context:
            delattr(x, 'foobar')
        self.assertEqual('foobar', context.exception.args[0])

    def test_delattr_2(self):
        x = X()
        x.foobar = 123
        delattr(x, 'foobar')
        self.assertFalse(hasattr(x, 'foobar'))


if __name__ == '__main__':
    unittest.main()
