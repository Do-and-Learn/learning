import unittest


class Obj:
    pass


class ReprObj:

    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return self.val


class StrObj:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class ReprTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual("'123'", repr('123'))
        self.assertEqual('2', repr(1 + 1))
        self.assertEqual('(1+2j)', repr(complex(1, 2)))
        self.assertEqual('1.23', repr(1.23))
        self.assertEqual('None', repr(None))
        self.assertEqual('Hello', repr(ReprObj('Hello')))

    def test_string_enclosed_in_angle_brackets(self):
        self.assertRegexpMatches(repr(object()), r'<object object at 0x[0-9A-Z]+>')
        self.assertRegexpMatches(repr(Obj()), r'<repr_test.Obj object at 0x[0-9A-Z]+>')
        self.assertRegexpMatches(repr(StrObj('Hello')), r'<repr_test.StrObj object at 0x[0-9A-Z]+>')
