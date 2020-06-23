import unittest


class DictTest(unittest.TestCase):

    def test_list(self):
        self.assertEqual([], list({}))  # 空 dict
        self.assertEqual(["one", "two", "three"], list({"one": 1, "two": 2, "three": 3}))

    def test_len(self):
        self.assertEqual(0, len({}))
        self.assertEqual(3, len({"one": 1, "two": 2, "three": 3}))

    def test_index(self):
        d1 = {"one": 1, "two": 2, "three": 3}
        d2 = {1: "one", 2: "two", 3: "three"}
        self.assertEqual(1, d1["one"])
        self.assertEqual("three", d2[3])

    # noinspection PyStatementEffect
    def test_non_existing_index(self):
        d = {"one": 1, "two": 2, "three": 3}
        with self.assertRaises(KeyError) as context:
            d["four"]
        self.assertEqual("four", context.exception.args[0])

    def test_missing_key(self):
        class DefaultDict(dict):
            def __missing__(self, key):
                return f'??{key}??'

        d = DefaultDict({"one": 1, "two": 2, "three": 3})
        self.assertEqual(1, d["one"])
        self.assertEqual("??four??", d["four"])

    # noinspection PyDictCreation
    def test_assign(self):
        d = {"one": 1, "two": 2, "three": 3}
        d["one"] = "一"
        self.assertEqual("一", d["one"])
        d["four"] = 4
        self.assertEqual(4, d["four"])

    def test_delete_key(self):
        d = {"one": 1, "two": 2, "three": 3}
        del d["one"]
        self.assertEqual({"two": 2, "three": 3}, d)

    def test_delete_non_existing_index(self):
        d = {"one": 1, "two": 2, "three": 3}
        with self.assertRaises(KeyError) as context:
            del d["four"]
        self.assertEqual("four", context.exception.args[0])

    def test_key_in_d(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertTrue("one" in d)
        self.assertFalse("four" in d)

    def test_key_not_in_d(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertFalse("one" not in d)
        self.assertTrue("four" not in d)

    def test_clear(self):
        d = {"one": 1, "two": 2, "three": 3}
        d.clear()
        self.assertEqual({}, d)

    def test_copy(self):
        d = {"one": 1, "two": 2, "three": 3}
        d_copy = d.copy()
        d_copy["one"] = "一"
        self.assertEqual("一", d_copy["one"])
        self.assertEqual(1, d["one"])

    def test_copy_2(self):
        d = {"one": [1], "two": [2], "three": [3]}
        d_copy = d.copy()
        d_copy["one"].append("一")
        self.assertEqual([1, "一"], d["one"])
        self.assertEqual([1, "一"], d_copy["one"])

    def test_get(self):
        d = {"one": 1, "two": 2, "three": 3}
        self.assertEqual(1, d.get("one"))
        self.assertEqual(4, d.get("four", 4))
        self.assertEqual(None, d.get("four"))

    def test_get_with_missing_key(self):
        class DefaultDict(dict):
            def __missing__(self, key):
                return f'??{key}??'

        d = DefaultDict({"one": 1, "two": 2, "three": 3})
        self.assertEqual(4, d.get("four", 4))
        self.assertEqual(None, d.get("four"))
