import abc
import unittest


class Parent:
    pass


class Uncle:
    pass


class Child(Parent):
    pass


class VirtualChild(Parent, abc.ABC):
    pass


class GrandSon(Child):
    pass


class OddMan:
    pass


class IsSubclassTest(unittest.TestCase):

    def test_is_subclass(self):
        self.assertTrue(issubclass(Parent, Parent))  # self
        self.assertTrue(issubclass(Child, Parent))  # direct
        self.assertTrue(issubclass(VirtualChild, Parent))  # virtual
        self.assertTrue(issubclass(GrandSon, Parent))  # indirect

    def test_tuple(self):
        self.assertTrue(issubclass(Parent, (Parent, Uncle)))
        self.assertTrue(issubclass(Child, (Parent, Uncle)))
        self.assertTrue(issubclass(Child, (OddMan, ((Parent, OddMan), Uncle))))  # tuples
        self.assertFalse(issubclass(Child, (OddMan, Uncle)))

    def test_reverse(self):
        self.assertFalse(issubclass(Parent, Child))

    def test_non_subclass(self):
        self.assertFalse(issubclass(OddMan, Parent))

    def test_is_not_class(self):
        with self.assertRaises(TypeError) as context:
            # noinspection PyTypeChecker
            issubclass(Child(), Parent)
        self.assertEqual('issubclass() arg 1 must be a class', context.exception.args[0])
