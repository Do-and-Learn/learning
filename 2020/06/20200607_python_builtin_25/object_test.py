import unittest


class ObjectTest(unittest.TestCase):

    def test_object(self):
        obj = object()
        self.assertIsInstance(obj, object)

    # noinspection PyUnresolvedReferences,PyStatementEffect
    def test_exceptions(self):
        obj = object()

        with self.assertRaises(TypeError) as context:
            obj['name'] = 'Teddy'
        self.assertEqual("'object' object does not support item assignment", context.exception.args[0])

        with self.assertRaises(AttributeError) as context:
            obj.name = 'Teddy'
        self.assertEqual("'object' object has no attribute 'name'", context.exception.args[0])

        with self.assertRaises(AttributeError) as context:
            obj.foo
        self.assertEqual("'object' object has no attribute 'foo'", context.exception.args[0])

    # noinspection PyUnresolvedReferences,PyStatementEffect
    def test_subclass_object(self):
        class Obj(object):
            pass

        obj = Obj()
        with self.assertRaises(TypeError) as context:
            obj['name'] = 'Teddy'
        self.assertEqual("'Obj' object does not support item assignment", context.exception.args[0])

        obj.name = 'Teddy'
        self.assertEqual('Teddy', obj.name)

        with self.assertRaises(AttributeError) as context:
            obj.foo
        self.assertEqual("'Obj' object has no attribute 'foo'", context.exception.args[0])

        obj.foo = None
        self.assertIsNone(obj.foo)
