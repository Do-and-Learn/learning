import unittest


class X:
    pass


class GetattrTest(unittest.TestCase):

    def test_getattr_1(self):
        x = X()
        with self.assertRaises(AttributeError) as context:
            getattr(x, 'foobar')
        self.assertEqual("'X' object has no attribute 'foobar'", context.exception.args[0])

    def test_getattr_2(self):
        x = X()
        x.foobar = 123
        self.assertEqual(123, getattr(x, 'foobar'))


if __name__ == '__main__':
    unittest.main()
