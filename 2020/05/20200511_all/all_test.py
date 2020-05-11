import unittest


class AllTest(unittest.TestCase):

    def test_all_1(self):
        self.assertTrue(all([]))

    def test_all_2(self):
        self.assertTrue(all([True] * 10))

    def test_all_3(self):
        self.assertFalse(all([True, True, True, True, False]))
        self.assertFalse(all([True, True, True, False, True]))
        self.assertFalse(all([True, True, False, True, True]))
        self.assertFalse(all([True, False, True, True, True]))
        self.assertFalse(all([False, True, True, True, True]))
        self.assertFalse(all([False, True, False, True, False]))


if __name__ == '__main__':
    unittest.main()
