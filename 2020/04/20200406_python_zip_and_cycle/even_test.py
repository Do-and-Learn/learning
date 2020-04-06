import unittest
from itertools import cycle


class MyTestCase(unittest.TestCase):

    def test_something(self):
        ret = [(value, isEven) for value, isEven in zip(range(5), cycle([True, False]))]
        self.assertCountEqual([
            (0, True),
            (1, False),
            (2, True),
            (3, False),
            (4, True)
        ], ret)


if __name__ == '__main__':
    unittest.main()
