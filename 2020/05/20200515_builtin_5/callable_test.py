import unittest


class Foo:

    def foo(self):
        pass


class CallableFoo:

    def __call__(self, *args, **kwargs):
        pass


def foo():
    pass


class CallableTest(unittest.TestCase):

    def test_callable(self):
        self.assertTrue(callable(foo))
        self.assertTrue(callable(lambda: None))
        self.assertTrue(callable(Foo))
        self.assertTrue(callable(Foo.foo))
        self.assertTrue(callable(Foo().foo))
        self.assertTrue(callable(CallableFoo()))

    def test_not_callable(self):
        self.assertFalse(callable(foo()))
        self.assertFalse(callable(Foo()))
        self.assertFalse(callable(Foo.foo(None)))
        self.assertFalse(callable(Foo().foo()))
        self.assertFalse(callable(1))
        self.assertFalse(callable('Hello'))


if __name__ == '__main__':
    unittest.main()
