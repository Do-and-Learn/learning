import unittest


class TupleTest(unittest.TestCase):

    def test_creation(self):
        self.assertEqual((), tuple())

        t = 1,
        self.assertEqual((1,), t)

        t = 1, 2, 3
        self.assertEqual((1, 2, 3), t)

        self.assertEqual(('a', 'b', 'c'), tuple('abc'))
        self.assertEqual((1, 2, 3), tuple([1, 2, 3]))

    # noinspection PyTypeChecker
    def test_exception(self):
        with self.assertRaises(TypeError) as context:
            tuple(None)
        self.assertEqual("'NoneType' object is not iterable", context.exception.args[0])
