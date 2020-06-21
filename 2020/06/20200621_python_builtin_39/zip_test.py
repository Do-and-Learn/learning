import unittest
from itertools import zip_longest


class ZipTest(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual([('Teddy', 'M'), ('Claire', 'F'), ('Bob', 'M')], list(zip(['Teddy', 'Claire', 'Bob'], ['M', 'F', 'M'])))
        self.assertEqual([('Teddy', 'M', 30), ('Claire', 'F', 18), ('Bob', 'M', 40)], list(zip(['Teddy', 'Claire', 'Bob'], ['M', 'F', 'M'], [30, 18, 40])))

    def test_shortest_list(self):
        self.assertEqual([(1, True), (2, False), (3, True), (4, False)], list(zip([1, 2, 3, 4, 5, 6, 7], [True, False, True, False])))

    def test_longest_list(self):
        self.assertEqual([(1, True), (2, False), (3, True), (4, False), (5, None), (6, None), (7, None)], list(zip_longest([1, 2, 3, 4, 5, 6, 7], [True, False, True, False])))

    # noinspection PyTypeChecker
    def test_exception(self):
        with self.assertRaises(TypeError) as context:
            iter(object())
        self.assertEqual("'object' object is not iterable", context.exception.args[0])

    def test_unzip(self):
        self.assertEqual([('Teddy', 'Claire', 'Bob'), ('M', 'F', 'M')], list(zip(*[('Teddy', 'M'), ('Claire', 'F'), ('Bob', 'M')])))
        self.assertEqual([('Teddy', 'Claire', 'Bob'), ('M', 'F', 'M')], list(zip(('Teddy', 'M'), ('Claire', 'F'), ('Bob', 'M'))))
