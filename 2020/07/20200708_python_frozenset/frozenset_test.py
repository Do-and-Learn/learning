import unittest


class FrozensetTest(unittest.TestCase):

    def test_constructor(self):
        self.assertEqual({'jack', 'sjoerd'}, frozenset(['jack', 'sjoerd']))
        self.assertEqual({1, 2, 3}, frozenset([1, 1, 2, 2, 2, 3]))
