import unittest
from collections import Iterable


class IterNextTest(unittest.TestCase):

    def test_example(self):
        result = []
        lst = [1, 2, 3, 4, 5, 6, 7]
        for e in iter(lst):
            result.append(e)
        self.assertEqual(lst, result)

    def test_sentinel(self):
        class IterInts:

            def __init__(self, _lst):
                self.lst = _lst
                self.it = iter(_lst)

            def __call__(self):
                return next(self.it)

        result = []
        for e in iter(IterInts([1, 2, 3, 4, 5, 6, 7]), 4):
            result.append(e)
        self.assertEqual([1, 2, 3], result)

        result = []
        for e in iter(IterInts([1, 2, 3, 4, 5, 6, 7]), 1):
            result.append(e)
        self.assertEqual([], result)

    def test_iter(self):
        class IterInts(Iterable):

            def __init__(self, _lst):
                self.lst = _lst

            def __iter__(self):
                return iter(self.lst)

        result = []
        for e in iter(IterInts([1, 2, 3, 4, 5, 6, 7])):
            result.append(e)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], result)

    def test_next(self):

        class DoubleIntsIter(Iterable):

            def __init__(self, n):
                self.n = n

            def __iter__(self):
                self.current = 0
                return self

            def __next__(self):
                if self.current < self.n:
                    self.current += 1
                    return self.current * 2
                else:
                    raise StopIteration

        result = []
        for e in iter(DoubleIntsIter(5)):
            result.append(e)
        self.assertEqual([2, 4, 6, 8, 10], result)

        it1 = iter(DoubleIntsIter(5))
        it2 = iter(DoubleIntsIter(5))
        self.assertEqual(2, next(it1))
        self.assertEqual(2, next(it2))
        self.assertEqual(4, next(it1))
        self.assertEqual(6, next(it1))
        self.assertEqual(8, next(it1))
        self.assertEqual(4, next(it2))
        self.assertEqual(10, next(it1))
        with self.assertRaises(StopIteration):
            next(it1)
        self.assertEqual(99, next(it1, 99))
        self.assertEqual(6, next(it2))

    def test_getitem(self):

        class DoubleIntsIter:

            def __init__(self, n):
                self.n = n

            def __getitem__(self, key):
                if key < self.n:
                    return (key + 1) * 2
                else:
                    raise StopIteration

        result = []
        for e in iter(DoubleIntsIter(5)):
            result.append(e)
        self.assertEqual([2, 4, 6, 8, 10], result)

        it1 = iter(DoubleIntsIter(5))
        it2 = iter(DoubleIntsIter(5))
        self.assertEqual(2, next(it1))
        self.assertEqual(2, next(it2))
        self.assertEqual(4, next(it1))
        self.assertEqual(6, next(it1))
        self.assertEqual(8, next(it1))
        self.assertEqual(4, next(it2))
        self.assertEqual(10, next(it1))
        with self.assertRaises(StopIteration):
            next(it1)
        self.assertEqual(6, next(it2))

    def test_read_fixed_block(self):
        from functools import partial
        result = []
        with open('data.txt', 'r') as f:
            for block in iter(partial(f.read, 2), ''):
                result.append(block)
        self.assertEqual(['12', '34', '56', '78', '90', '\n0', '12', '34', '56', '78', '9'], result)

    # noinspection PyTypeChecker
    def test_exception(self):
        with self.assertRaises(TypeError) as context:
            iter(object())
        self.assertEqual("'object' object is not iterable", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            iter([1, 2, 3], 1)
        self.assertEqual("iter(v, w): v must be callable", context.exception.args[0])
