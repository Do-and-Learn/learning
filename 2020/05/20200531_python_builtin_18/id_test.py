import unittest


class Obj:
    val: int

    def __init__(self, val: int):
        self.val = val

    def __eq__(self, other):
        return other.val == self.val


class IdTest(unittest.TestCase):

    def test_id(self):
        obj1 = object()
        obj2 = object()
        self.assertNotEqual(obj1, obj2)
        self.assertNotEqual(id(obj1), id(obj2))

    def test_id_2(self):
        obj1 = Obj(1)
        obj2 = Obj(1)
        self.assertEqual(obj1, obj2)
        self.assertNotEqual(id(obj1), id(obj2))
