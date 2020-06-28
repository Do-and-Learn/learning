import contextlib
import unittest


class ListTest(unittest.TestCase):
    def test_normal_case(self):
        lst = [5, 2, 3, 1, 4]
        lst.sort()
        self.assertEqual([1, 2, 3, 4, 5], lst)

    def test_reverse(self):
        lst = [5, 2, 3, 1, 4]
        lst.sort(reverse=True)
        self.assertEqual([5, 4, 3, 2, 1], lst)

    def test_sort_obj(self):
        class Obj:
            def __init__(self, val):
                self.val = val

            def __lt__(self, other):
                return self.val < other.val

            def __eq__(self, other):
                return self.val == other.val

            def __repr__(self):
                return str(self.val)

        lst = [Obj(5), Obj(2), Obj(3), Obj(1), Obj(4)]
        lst.sort()
        self.assertEqual([Obj(1), Obj(2), Obj(3), Obj(4), Obj(5)], lst)

    def test_exception(self):
        class Obj:
            def __init__(self, val):
                self.val = val

            def __eq__(self, other):
                return self.val == other.val

            def __repr__(self):
                return str(self.val)

        lst = [Obj(5), Obj(2), Obj(3), Obj(1), Obj(4)]
        with self.assertRaises(TypeError) as context:
            lst.sort()
        self.assertEqual("'<' not supported between instances of 'Obj' and 'Obj'", context.exception.args[0])

    def test_key(self):
        class Obj:
            def __init__(self, val):
                self.val = val

            def __eq__(self, other):
                return self.val == other.val

            def __repr__(self):
                return str(self.val)

        lst = [Obj(5), Obj(2), Obj(3), Obj(1), Obj(4)]
        lst.sort(key=lambda obj: obj.val)
        self.assertEqual([Obj(1), Obj(2), Obj(3), Obj(4), Obj(5)], lst)

    def test_exception_partial_sort(self):
        class Obj:
            def __init__(self, val):
                self.val = val

            def __lt__(self, other):
                return self.val < other.val

            def __eq__(self, other):
                return self.val == other.val

            def __repr__(self):
                return str(self.val)

        lst = [Obj(5), Obj(2), Obj(3), 6, Obj(1), Obj(4)]
        with contextlib.suppress(TypeError):
            lst.sort()
        self.assertNotEqual([Obj(5), Obj(2), Obj(3), 6, Obj(1), Obj(4)], lst)
