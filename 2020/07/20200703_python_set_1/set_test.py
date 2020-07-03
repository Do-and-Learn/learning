import unittest


class SetTest(unittest.TestCase):

    # noinspection SpellCheckingInspection,PySetFunctionToLiteral
    def test_constructor(self):
        self.assertEqual(set(['jack', 'sjoerd']), {'jack', 'sjoerd'})
        self.assertEqual({1, 2, 3}, {1, 1, 2, 2, 2, 3})
        self.assertEqual({1, 2, 3}, set([1, 1, 2, 2, 2, 3]))

    def test_len(self):
        self.assertEqual(0, len(set()))
        self.assertEqual(1, len({'apple'}))
        self.assertEqual(2, len({'apple', 'banana'}))

    def test_in(self):
        self.assertTrue('Jack' in {'Andy', 'Jack', 'Bob', 'Kent'})
        self.assertFalse('Jake' in {'Andy', 'Jack', 'Bob', 'Kent'})
