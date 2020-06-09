import unittest


class OrdTest(unittest.TestCase):
    """
    ord = ordinal
    """

    def test_ord(self):
        self.assertEqual(97, ord('a'))
        self.assertEqual(8364, ord('€'))

    # noinspection PyTypeChecker
    def test_exception(self):
        with self.assertRaises(TypeError) as context:
            ord(123)
        self.assertEqual('ord() expected string of length 1, but int found', context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            ord(None)
        self.assertEqual('ord() expected string of length 1, but NoneType found', context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            ord('abc')
        self.assertEqual('ord() expected a character, but string of length 3 found', context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            ord('')
        self.assertEqual('ord() expected a character, but string of length 0 found', context.exception.args[0])
