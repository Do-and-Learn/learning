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


class IsinstanceTest(unittest.TestCase):

    def test_isinstance(self):
        self.assertTrue(isinstance(Parent(), Parent))  # self
        self.assertTrue(isinstance(Child(), Parent))  # direct
        self.assertTrue(isinstance(VirtualChild(), Parent))  # virtual
        self.assertTrue(isinstance(GrandSon(), Parent))  # indirect

    def test_tuple(self):
        self.assertTrue(isinstance(Parent(), (Parent, Uncle)))
        self.assertTrue(isinstance(Child(), (Parent, Uncle)))
        self.assertTrue(isinstance(Child(), (OddMan, ((Parent, OddMan), Uncle))))  # tuples
        self.assertFalse(isinstance(Child(), (OddMan, Uncle)))

    def test_isinstance_reverse(self):
        self.assertFalse(isinstance(Parent(), Child))

    def test_non_instance(self):
        self.assertFalse(isinstance(OddMan(), Parent))

    def test_non_tuple_and_type(self):
        with self.assertRaises(TypeError) as context:
            # noinspection PyTypeChecker
            isinstance(Parent(), None)
        self.assertEqual('isinstance() arg 2 must be a type or tuple of types', context.exception.args[0])
