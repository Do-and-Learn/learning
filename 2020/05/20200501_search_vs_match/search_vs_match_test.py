import re
import unittest


class SearchVsMatchTest(unittest.TestCase):

    def test_1(self):
        with self.subTest("match"):
            match = re.match("c", "abcdef")
            self.assertIsNone(match)

        with self.subTest("search"):
            search = re.search("c", "abcdef")
            self.assertIsNotNone(search)
            self.assertEqual((2, 3), search.span())

    def test_2(self):
        search = re.search("^c", "abcdef")
        self.assertIsNone(search)

    def test_3(self):
        search = re.search("^a", "abcdef")
        self.assertIsNotNone(search)
        self.assertEqual((0, 1), search.span())

    def test_4(self):
        with self.subTest("match"):
            match = re.match('X', 'A\nB\nX', re.MULTILINE)
            self.assertIsNone(match)

        with self.subTest("search"):
            search = re.search('^X', 'A\nB\nX', re.MULTILINE)
            self.assertIsNotNone(search)
            self.assertEqual((4, 5), search.span())

    def test_5(self):
        match = re.match("abc", "abcdef")
        self.assertIsNotNone(match)

        match = re.match("^abc$", "abcdef")
        self.assertIsNone(match)


if __name__ == '__main__':
    unittest.main()
