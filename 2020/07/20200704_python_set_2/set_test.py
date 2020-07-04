import unittest


class SetTest(unittest.TestCase):

    def test_not_in(self):
        self.assertTrue('Jake' not in {'Andy', 'Jack', 'Bob', 'Kent'})
        self.assertFalse('Jack' not in {'Andy', 'Jack', 'Bob', 'Kent'})

    def test_isdisjoint(self):
        self.assertFalse({1, 2, 3}.isdisjoint({1, 4, 5}))
        self.assertTrue({1, 2, 3}.isdisjoint({4, 5, 6}))
        self.assertTrue({1, 2, 3}.isdisjoint({}))

    def test_issubset(self):
        self.assertTrue(set().issubset({1, 2, 3}))
        self.assertFalse({1, 2, 3}.issubset(set()))
        self.assertTrue({1, 2, 3}.issubset({1, 2, 3, 4, 5}))
        self.assertTrue({1, 2, 3}.issubset({1, 2, 3}))
        self.assertFalse({1, 2, 3, 4, 5}.issubset({1, 2, 3}))

    def test_issuperset(self):
        self.assertTrue({1, 2, 3}.issuperset(set()))
        self.assertFalse(set().issuperset({1, 2, 3}))
        self.assertTrue({1, 2, 3, 4, 5}.issuperset({1, 2, 3}))
        self.assertTrue({1, 2, 3}.issuperset({1, 2, 3}))
        self.assertFalse({1, 2, 3}.issuperset({1, 2, 3, 4, 5}))

    def test_le(self):
        self.assertTrue(set() <= {1, 2, 3})
        self.assertFalse({1, 2, 3} <= set())
        self.assertTrue({1, 2, 3} <= {1, 2, 3})
        self.assertTrue({1, 2, 3} <= {1, 2, 3, 4, 5})
        self.assertFalse({1, 2, 3, 4, 5} <= {1, 2, 3})

    def test_lt(self):
        self.assertTrue(set() < {1, 2, 3})
        self.assertFalse({1, 2, 3} < set())
        self.assertFalse({1, 2, 3} < {1, 2, 3})
        self.assertTrue({1, 2, 3} < {1, 2, 3, 4, 5})
        self.assertFalse({1, 2, 3, 4, 5} < {1, 2, 3})

    def test_ge(self):
        self.assertFalse(set() >= {1, 2, 3})
        self.assertTrue({1, 2, 3} >= set())
        self.assertTrue({1, 2, 3} >= {1, 2, 3})
        self.assertFalse({1, 2, 3} >= {1, 2, 3, 4, 5})
        self.assertTrue({1, 2, 3, 4, 5} >= {1, 2, 3})

    def test_gt(self):
        self.assertFalse(set() > {1, 2, 3})
        self.assertTrue({1, 2, 3} > set())
        self.assertFalse({1, 2, 3} > {1, 2, 3})
        self.assertFalse({1, 2, 3} > {1, 2, 3, 4, 5})
        self.assertTrue({1, 2, 3, 4, 5} > {1, 2, 3})