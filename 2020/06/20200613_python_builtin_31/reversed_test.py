import typing
import unittest
from collections import Reversible, Sequence
from typing import Iterator, Iterable


class ReversibleObj(Reversible, Iterable):

    def __init__(self, val: typing.List[int]):
        self.val = val

    def __iter__(self) -> Iterator[int]:
        return self.val

    def __reversed__(self) -> Iterator[int]:
        return [-v for v in self.val]


class SequenceObj(Sequence):

    def __init__(self, val: typing.List[int]):
        self.val = val

    def __getitem__(self, i: int) -> int:
        return self.val[i]

    def __len__(self) -> int:
        return len(self.val)


class Foo:
    pass


class ReversedTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual([1, 2, 3, 4, 5], list(reversed([5, 4, 3, 2, 1])))
        self.assertEqual(['o', 'l', 'l', 'e', 'h'], list(reversed('hello')))

    def test_obj(self):
        self.assertEqual([-1, -2, -3], reversed(ReversibleObj([1, 2, 3])))
        self.assertEqual([1, 2, 3, 4, 5], list(reversed(SequenceObj([5, 4, 3, 2, 1]))))

    # noinspection PyTypeChecker
    def test_exception(self):
        with self.assertRaises(TypeError) as context:
            reversed(Foo())
        self.assertEqual("'Foo' object is not reversible", context.exception.args[0])
