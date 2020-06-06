import unittest


class MapTest(unittest.TestCase):

    def test_map(self):
        def double(num):
            return num * 2

        self.assertEqual([2, 4, 6, 8, 10], list(map(double, [1, 2, 3, 4, 5])))

    def test_more_arg_1(self):
        def mul(num, times):
            return num * times

        self.assertEqual([3, 6, 9, 12, 15], list(map(mul, [1, 2, 3, 4, 5], [3] * 5)))
        self.assertEqual([1, 4, 9, 16, 25], list(map(mul, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])))

    def test_more_arg_len_different(self):
        def mul(num, times):
            return num * times

        self.assertEqual([2, 8], list(map(mul, [1, 2, 3, 4, 5], [2, 4])))

        def mul(num, times):
            return num * times

        self.assertEqual([2, 8], list(map(mul, [2, 4], [1, 2, 3, 4, 5])))

    # noinspection PyTypeChecker
    def test_exceptions(self):
        def double(num):
            return num * 2

        class Foo:
            pass

        with self.assertRaises(TypeError) as context:
            list(map(Foo(), [1, 2, 3, 4, 5]))
        self.assertEqual("'Foo' object is not callable", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            list(map(None, [1, 2, 3, 4, 5]))
        self.assertEqual("'NoneType' object is not callable", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            list(map(double, None))
        self.assertEqual("'NoneType' object is not iterable", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            list(map(double, Foo()))
        self.assertEqual("'Foo' object is not iterable", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            list(map(double, Foo))
        self.assertEqual("'type' object is not iterable", context.exception.args[0])
