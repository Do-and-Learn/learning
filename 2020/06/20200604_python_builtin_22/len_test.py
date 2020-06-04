import unittest


class LenObj:

    def __len__(self):
        return 3276


class FooObj:
    pass


class LenTest(unittest.TestCase):

    def test_zero_len(self):
        self.assertEqual(0, len([]))
        self.assertEqual(0, len(''))
        self.assertEqual(0, len(b''))
        self.assertEqual(0, len(()))
        self.assertEqual(0, len(range(0)))
        self.assertEqual(0, len({}))
        self.assertEqual(0, len(set()))

    def test_len(self):
        self.assertEqual(5, len([1, 2, 3, 4, 5]))
        self.assertEqual(6, len('happy!'))
        self.assertEqual(3, len(b'xyz'))
        self.assertEqual(2, len(('hello', 123)))
        self.assertEqual(80, len(range(80)))
        self.assertEqual(3, len({'name': 'Teddy', 'sex': 'Boy', 'born': 1988}))
        self.assertEqual(3, len({'Apple', 'Banana', 'Egg'}))

    def test_obj(self):
        self.assertEqual(3276, len(LenObj()))

    # noinspection PyTypeChecker
    def test_exception(self):
        with self.assertRaises(TypeError) as context:
            len(None)
        self.assertEqual("object of type 'NoneType' has no len()", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            len(FooObj())
        self.assertEqual("object of type 'FooObj' has no len()", context.exception.args[0])
