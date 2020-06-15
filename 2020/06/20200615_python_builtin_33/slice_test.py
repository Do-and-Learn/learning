import unittest


class SliceTest(unittest.TestCase):

    def test_slice(self):
        s = slice(4)
        self.assertEqual(slice(None, 4, None), s)
        self.assertEqual("This", "This is an apple"[s])

    def test_slice_2(self):
        s = slice(11, 16)
        self.assertEqual(slice(11, 16, None), s)
        self.assertEqual("apple", "This is an apple"[s])

    def test_slice_3(self):
        s = slice(11, 16, 2)
        self.assertEqual(slice(11, 16, 2), s)
        self.assertEqual("ape", "This is an apple"[s])

    def test_slice_4(self):
        s = slice(11, 99)
        self.assertEqual(slice(11, 99, None), s)
        self.assertEqual("apple", "This is an apple"[s])

    def test_slice_5(self):
        s = slice(11, -2)
        self.assertEqual(slice(11, -2, None), s)
        self.assertEqual("app", "This is an apple"[s])

    def test_slice_6(self):
        s = slice(-6)
        self.assertEqual(slice(None, -6, None), s)
        self.assertEqual("This is an", "This is an apple"[s])

    def test_slice_7(self):
        s = slice(0, 99, -1)
        self.assertEqual(slice(0, 99, -1), s)
        self.assertEqual("", "This is an apple"[s])

    def test_slice_8(self):
        s = slice(0, 99, -2)
        self.assertEqual(slice(0, 99, -2), s)
        self.assertEqual("", "This is an apple"[s])

    def test_exception(self):
        class Obj:
            pass

        s = slice(Obj())
        with self.assertRaises(TypeError) as context:
            self.assertEqual("", "This is an apple"[s])
        self.assertEqual("slice indices must be integers or None or have an __index__ method", context.exception.args[0])

        s = slice(Obj(), 10)
        with self.assertRaises(TypeError) as context:
            self.assertEqual("", "This is an apple"[s])
        self.assertEqual("slice indices must be integers or None or have an __index__ method", context.exception.args[0])

        s = slice(1, 10, Obj())
        with self.assertRaises(TypeError) as context:
            self.assertEqual("", "This is an apple"[s])
        self.assertEqual("slice indices must be integers or None or have an __index__ method", context.exception.args[0])
