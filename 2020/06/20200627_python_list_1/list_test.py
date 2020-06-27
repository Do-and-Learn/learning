import unittest


class ListTest(unittest.TestCase):

    def test_constructor(self):
        self.assertEqual([], list())  # empty list
        self.assertEqual(['a', 'b', 'c'], list('abc'))
        self.assertEqual(['a', 'b', 'c'], list(('a', 'b', 'c')))
        self.assertEqual([0, 2, 4, 6, 8], [x * 2 for x in range(5)])
