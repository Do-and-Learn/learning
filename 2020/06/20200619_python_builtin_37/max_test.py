import random
import unittest


class MaxTest(unittest.TestCase):

    def test_example_1(self):
        lst = [i + 1 for i in range(10)]
        random.shuffle(lst)
        self.assertEqual(10, max(lst))
        self.assertEqual(10, max(lst, key=None))
        self.assertEqual(10, max(*lst))
        self.assertEqual(10, max(*lst, key=None))

    def test_example_2(self):
        lst = []
        for i in range(10):
            lst.append({"level1": i + 1, "level2": -(i + 1)})
        random.shuffle(lst)
        self.assertEqual({'level1': 10, 'level2': -10}, max(lst, key=lambda key: key["level1"]))
        self.assertEqual({'level1': 10, 'level2': -10}, max(*lst, key=lambda key: key["level1"]))
        self.assertEqual({'level1': 1, 'level2': -1}, max(lst, key=lambda key: key["level2"]))
        self.assertEqual({'level1': 1, 'level2': -1}, max(*lst, key=lambda key: key["level2"]))

    def test_example_3(self):
        lst = []
        for i in range(10):
            for j in range(10):
                lst.append({"level1": i + 1, "level2": -(j + 1)})
        random.shuffle(lst)
        self.assertEqual({'level1': 10, 'level2': -1}, max(lst, key=lambda key: (key["level1"], key["level2"])))
        self.assertEqual({'level1': 10, 'level2': -1}, max(*lst, key=lambda key: (key["level1"], key["level2"])))

    def test_example_4(self):
        self.assertEqual(99, max([], default=99))

    def test_example_5(self):
        with self.assertRaises(ValueError) as context:
            max([])
        self.assertEqual("max() arg is an empty sequence", context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            max({"value": 5}, {"value": 7}, {"value": 1}, {"value": 2}, {"value": -3})
        self.assertEqual("'>' not supported between instances of 'dict' and 'dict'", context.exception.args[0])
