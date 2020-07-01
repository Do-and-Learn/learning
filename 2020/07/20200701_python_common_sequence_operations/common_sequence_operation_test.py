import unittest


class CommonSequenceOperationTest(unittest.TestCase):

    def test_in(self):
        self.assertTrue(2 in [1, 2, 3])
        self.assertFalse(4 in [1, 2, 3])
        self.assertTrue("Teddy" in "Hello Teddy!")
        self.assertFalse("Teddy" in "Hello Claire!")

    def test_not_in(self):
        self.assertFalse(2 not in [1, 2, 3])
        self.assertTrue(4 not in [1, 2, 3])
        self.assertFalse("Teddy" not in "Hello Teddy!")
        self.assertTrue("Teddy" not in "Hello Claire!")

    def test_concatenation(self):
        self.assertEqual([1, 2, 3, 4], [1, 2] + [3, 4])
        self.assertEqual("Hello Teddy!", "Hello " + "Teddy" + "!")

    # noinspection PyUnresolvedReferences
    def test_concatenation_exception(self):
        with self.assertRaises(TypeError) as context:
            range(1, 2) + range(2, 3)
        self.assertEqual("unsupported operand type(s) for +: 'range' and 'range'", context.exception.args[0])

    def test_repetition(self):
        self.assertEqual(['?', '?', '?', '?', '?'], ['?'] * 5)
        self.assertEqual("hahaha", "ha" * 3)

    def test_ith(self):
        lst = [11, 12, 13, 14, 15]
        self.assertEqual(13, lst[2])
        self.assertEqual(14, lst[-2])

    def test_slice(self):
        lst = [11, 12, 13, 14, 15]
        self.assertEqual([12], lst[1:2])
        self.assertEqual([12, 13], lst[1:3])
        self.assertEqual([12, 13, 14], lst[1:-1])
        self.assertEqual([12, 13, 14, 15], lst[1:])
        self.assertEqual([11, 12, 13], lst[:3])

    def test_slice_with_step(self):
        lst = list(range(0, 100))  # [0, 1, 2, ..., 99]
        self.assertEqual([0, 2, 4, 6, 8], lst[0:10:2])
        self.assertEqual([1, 3, 5, 7, 9], lst[1:10:2])

    def test_len(self):
        lst = list(range(0, 50))  # [0, 1, 2, ..., 49]
        self.assertEqual(0, len([]))
        self.assertEqual(50, len(lst))

    def test_min(self):
        import random
        lst = list(range(0, 10))  # [0, 1, 2, ..., 9]
        random.shuffle(lst)
        self.assertEqual(0, min(lst))

    def test_max(self):
        import random
        lst = list(range(0, 10))  # [0, 1, 2, ..., 9]
        random.shuffle(lst)
        self.assertEqual(9, max(lst))

    def test_min_max_exception(self):
        with self.assertRaises(ValueError) as context:
            self.assertEqual(None, min([]))
        self.assertEqual("min() arg is an empty sequence", context.exception.args[0])

        with self.assertRaises(ValueError) as context:
            self.assertEqual(None, max([]))
        self.assertEqual("max() arg is an empty sequence", context.exception.args[0])

    def test_index(self):
        alpha = [chr(ord('a') + i) for i in range(26)]  # ['a', 'b', 'c', ..., 'z']
        self.assertEqual(0, alpha.index('a'))
        self.assertEqual(10, alpha.index('k'))
        self.assertEqual(25, alpha.index('z'))

    def test_index_i_j(self):
        #      0  1  2  3  4  5  6  7
        lst = [0, 1, 2, 3, 4, 2, 3, 4]
        self.assertEqual(2, lst.index(2))
        self.assertEqual(2, lst.index(2, 2))
        self.assertEqual(5, lst.index(2, 3))
        self.assertEqual(5, lst.index(2, 3, 6))
        with self.assertRaises(ValueError) as context:
            lst.index(2, 3, 5)
        self.assertEqual("2 is not in list", context.exception.args[0])

    def test_index_exception(self):
        alpha = [chr(ord('a') + i) for i in range(26)]  # ['a', 'b', 'c', ..., 'z']

        with self.assertRaises(ValueError) as context:
            alpha.index('Z')
        self.assertEqual("'Z' is not in list", context.exception.args[0])

    # noinspection PyTypeChecker
    def test_count(self):
        lst = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
        self.assertEqual(2, lst.count(1))
        self.assertEqual(3, lst.count(2))
        self.assertEqual(1, lst.count(5))
        self.assertEqual(0, lst.count('x'))
