import random
import unittest
from typing import Iterable


class ClassWithDirMethod:

    def __dir__(self) -> Iterable[str]:
        return ['a', 'b', 'c']


class ClassWithAttr:
    hi = 'hello'


class ClassWithGetAttr:

    def __getattr__(self, item):
        if item == 'hi':
            return 'hello'
        raise Exception(f'Unknown {item}')


class DirTest(unittest.TestCase):

    def setUp(self) -> None:
        self.maxDiff = None

    # noinspection PyUnusedLocal
    def test_dir_no_arguments(self):
        i: int = 123
        s: str = 'Hello'
        j: int
        self.assertCountEqual(['i', 's', 'self'], dir())  # no j

    def test_dir_class_with_dir_method(self):
        obj = ClassWithDirMethod()
        self.assertEqual(['a', 'b', 'c'], dir(obj))
        self.assertNotEqual(['a', 'b', 'c'], dir(ClassWithDirMethod))
        self.assertNotIn('a', dir(ClassWithDirMethod))

    def test_dir_attr(self):
        obj = ClassWithAttr()
        self.assertIn('hi', dir(obj))
        self.assertIn('hi', dir(ClassWithAttr))
        self.assertNotIn('hello', dir(obj))

    def test_dir_getattr(self):
        obj = ClassWithGetAttr()
        self.assertEqual('hello', obj.hi)
        self.assertNotIn('hi', dir(obj))

    def test_dir_module(self):
        self.assertIn('random', dir(random))
        self.assertIn('randint', dir(random))
        self.assertIn('shuffle', dir(random))


if __name__ == '__main__':
    unittest.main()
