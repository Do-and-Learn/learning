import unittest


class DictTest(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual({}, dict())
        self.assertEqual({}, dict([]))
        self.assertEqual({}, dict({}))

    def test_creation(self):
        d1 = {"one": 1, "two": 2, "three": 3}
        d2 = dict(one=1, two=2, three=3)
        d3 = dict({"one": 1, "two": 2, "three": 3})
        d4 = dict({"one": 1, "three": 3}, two=2)
        d5 = dict([("one", 1), ("two", 2), ("three", 3)])
        d6 = dict([("one", 1), ("two", 2)], three=3)
        self.assertTrue(d1 == d2 == d3 == d4 == d5 == d6)

    # noinspection PyDictDuplicateKeys
    def test_duplicated_key(self):
        d = dict({"one": 2}, one=1)
        self.assertEqual(1, d["one"])

        d = dict([("two", 1)], two=2)
        self.assertEqual(2, d["two"])
