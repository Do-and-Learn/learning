import typing
import unittest


class Obj:
    pass


class HashObj:
    name: typing.Optional[str]

    def __init__(self):
        self.name = None

    def __hash__(self):
        return hash(self.name)


class HashTest(unittest.TestCase):

    def test_hash_different_objects1(self):
        obj1 = object()
        obj2 = object()
        self.assertEqual(hash(object()), hash(object()))
        self.assertNotEqual(hash(obj1), hash(obj2))

    def test_hash_different_objects2(self):
        obj1 = Obj()
        obj2 = Obj()
        self.assertEqual(hash(Obj()), hash(Obj()))
        self.assertNotEqual(hash(obj1), hash(obj2))

    def test_hash_same_objects1(self):
        obj = object()
        self.assertEqual(hash(obj), hash(obj))

    def test_hash_same_objects2(self):
        obj = Obj()
        self.assertEqual(hash(obj), hash(obj))

    def test_hash_strings(self):
        str_1 = 'name'
        str_2 = 'name'
        self.assertEqual(hash(str_1), hash(str_2))

    def test_class_with_hash(self):
        obj1 = HashObj()
        obj2 = HashObj()
        self.assertEqual(hash(obj1), hash(obj2))

        obj1.name = 'Teddy'
        obj2.name = 'Ted'
        self.assertNotEqual(hash(obj1), hash(obj2))

        obj2.name = 'Teddy'
        self.assertEqual(hash(obj1), hash(obj2))


if __name__ == '__main__':
    unittest.main()
