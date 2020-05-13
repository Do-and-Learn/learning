import unittest


class AnyTest(unittest.TestCase):

    def test_any_1(self):
        self.assertFalse(any([]))

    def test_any_2(self):
        self.assertFalse(any([False] * 10))

    def test_any_3(self):
        self.assertTrue(any([False, False, False, False, True]))
        self.assertTrue(any([False, False, False, True, False]))
        self.assertTrue(any([False, False, True, False, False]))
        self.assertTrue(any([False, True, False, False, False]))
        self.assertTrue(any([True, False, False, False, False]))


if __name__ == '__main__':
    unittest.main()
