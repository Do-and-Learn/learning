import unittest


class SumTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual(15, sum([1, 2, 3, 4, 5]))
        self.assertEqual(16, sum([1, 2, 3, 4, 5], start=1))
        self.assertEqual(17, sum([1, 2, 3, 4, 5], start=2))
        self.assertEqual(18, sum([1, 2, 3, 4, 5], start=3))
        self.assertEqual(0, sum([]))
        self.assertEqual(99, sum([], start=99))

    def test_example_2(self):
        self.assertEqual(6.6, sum([1.1, 2.2, 3.3]))

    # noinspection PyTypeChecker
    def test_example_3(self):
        class Obj:
            pass

        with self.assertRaises(TypeError) as context:
            sum(Obj())
        self.assertEqual("'Obj' object is not iterable", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            sum([1, 2, 3, 4, 5], start=Obj())
        self.assertEqual("unsupported operand type(s) for +: 'Obj' and 'int'", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            sum([1, 2, 3, 4, 5], start="88")
        self.assertEqual("sum() can't sum strings [use ''.join(seq) instead]", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            sum(["1", "2"], start="88")
        self.assertEqual("sum() can't sum strings [use ''.join(seq) instead]", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            sum(["1", "2"])
        self.assertEqual("unsupported operand type(s) for +: 'int' and 'str'", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            sum([[1, 2], [3, 4, 5]])
        self.assertEqual("unsupported operand type(s) for +: 'int' and 'list'", context.exception.args[0])
