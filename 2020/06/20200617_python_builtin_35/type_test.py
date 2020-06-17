import unittest


class TypeTest(unittest.TestCase):

    def test_type_to_primitive_types(self):
        self.assertEqual(int, type(1))
        self.assertEqual(float, type(1.23))
        self.assertEqual(str, type("Hello"))
        self.assertEqual(bool, type(False))
        self.assertEqual(tuple, type((1, 2)))
        self.assertEqual(complex, type(1 + 2j))
        self.assertEqual(range, type(range(10)))
        self.assertEqual(list, type([4, 5, 6]))

    def test_type_to_obj(self):
        class IntObj:
            pass

        int_obj = IntObj()
        self.assertEqual(type(int_obj), IntObj)

    # noinspection PyUnresolvedReferences
    def test_dynamic_type(self):
        obj = type('DynamicObj', (), dict(a=1, hi="Teddy"))
        self.assertEqual(obj.a, 1)
        self.assertEqual(obj.hi, "Teddy")
        self.assertEqual(type(obj), type)

        teddy = obj()
        claire = obj()
        claire.hi = "Claire"
        self.assertEqual(teddy.hi, "Teddy")
        self.assertEqual(claire.hi, "Claire")
        self.assertEqual(str(type(teddy)), "<class 'type_test.DynamicObj'>")

    # noinspection PyUnresolvedReferences
    def test_dynamic_type_inheritance(self):
        class Parent:
            @property
            def name(self):
                return "Parent"

        obj = type('DynamicObj', (Parent,), {})
        self.assertEqual("Parent", obj().name)
