import unittest


class EnumerateTest(unittest.TestCase):

    def test_enumerate_1(self):
        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        self.assertCountEqual(enumerate(seasons), [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')])

    def test_enumerate_2(self):
        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        self.assertCountEqual(enumerate(seasons, start=1), [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')])


if __name__ == '__main__':
    unittest.main()
