import unittest


class DictTest(unittest.TestCase):

    def test_iter(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertEqual(["one", "two", "three"], [k for k in iter(d)])

    def test_fromkeys(self):
        self.assertEqual({"one": None, "two": None, "three": None}, dict.fromkeys(["one", "two", "three"]))
        self.assertEqual({"one": "?", "two": "?", "three": "?"}, dict.fromkeys(["one", "two", "three"], "?"))

    def test_items(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertEqual([("one", 1), ("two", 2), ("three", 3)], list(d.items()))

    def test_keys(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertEqual(["one", "two", "three"], list(d.keys()))

    def test_pop(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertEqual(1, d.pop("one"))
        self.assertEqual("一", d.pop("one", "一"))
        self.assertEqual(2, d.pop("two", "二"))
        self.assertEqual("二", d.pop("two", "二"))

        with self.assertRaises(KeyError) as context:
            d.pop("two")
        self.assertEqual("two", context.exception.args[0])

    def test_popitem(self):
        d = {"one": 1, "two": 2, "three": 3}
        items = []
        while len(d) > 0:
            items.append(d.popitem())
        self.assertEqual([("three", 3), ("two", 2), ("one", 1)], items)

        with self.assertRaises(KeyError) as context:
            d.popitem()
        self.assertEqual("popitem(): dictionary is empty", context.exception.args[0])

        d = {"three": 3, "one": 1, "two": 2}
        items = []
        while len(d) > 0:
            items.append(d.popitem())
        self.assertEqual([("two", 2), ("one", 1), ("three", 3)], items)

    def test_reversed(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertEqual(["one", "two", "three"], list(d))
        self.assertEqual(["three", "two", "one"], list(reversed(d)))

    def test_setdefault(self):
        d = {"one": 1, "two": 2, "three": 3}

        self.assertEqual(4, d.setdefault("four", 4))
        self.assertEqual({"one": 1, "two": 2, "three": 3, "four": 4}, d)

        self.assertEqual(1, d.setdefault("one", "一"))
        self.assertEqual({"one": 1, "two": 2, "three": 3, "four": 4}, d)

        self.assertEqual(None, d.setdefault("five"))
        self.assertEqual({"one": 1, "two": 2, "three": 3, "four": 4, "five": None}, d)

    def test_update(self):
        d = {"one": 1, "two": 2, "three": 3}
        d.update({"one": "一", "four": "四"})
        self.assertEqual({"one": "一", "two": 2, "three": 3, "four": "四"}, d)

        d.update(two="二", three="三")
        self.assertEqual({"one": "一", "two": "二", "three": "三", "four": "四"}, d)

    def test_values(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertEqual([1, 2, 3], list(d.values()))
