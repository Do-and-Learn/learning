import unittest


class X:
    foobar: int


class Y:
    pass


# noinspection PyStatementEffect,PyUnresolvedReferences
class SetattrTest(unittest.TestCase):

    def test_setattr_1(self):
        obj = object()
        with self.assertRaises(AttributeError) as context:
            obj.foobar
        self.assertEqual("'object' object has no attribute 'foobar'", context.exception.args[0])

    def test_setattr_2(self):
        obj = object()
        with self.assertRaises(AttributeError) as context:
            setattr(obj, 'foobar', 123)
        self.assertEqual("'object' object has no attribute 'foobar'", context.exception.args[0])

    def test_setattr_3(self):
        x = X()
        with self.assertRaises(AttributeError) as context:
            x.foobar
        self.assertEqual("'X' object has no attribute 'foobar'", context.exception.args[0])

    def test_setattr_4(self):
        x1 = X()
        x2 = X()
        x1.foobar = 1
        x2.foobar = 2
        self.assertEqual(1, x1.foobar)
        self.assertEqual(2, x2.foobar)

    def test_setattr_5(self):
        x = X()
        y = Y()
        setattr(x, 'foobar', 123)
        setattr(y, 'foobar', 456)
        self.assertEqual(123, x.foobar)
        self.assertEqual(456, y.foobar)


if __name__ == '__main__':
    unittest.main()
