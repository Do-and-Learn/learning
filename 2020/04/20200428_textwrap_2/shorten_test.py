import textwrap
import unittest


class ShortenTest(unittest.TestCase):

    def test_shorten_1(self):
        self.assertEqual('Hello world!', textwrap.shorten('Hello  world!', width=12))

    def test_shorten_2(self):
        self.assertEqual('Hello [...]', textwrap.shorten('Hello  world!', width=11))

    def test_shorten_3(self):
        self.assertEqual('Hello...', textwrap.shorten("Hello world!", width=11, placeholder="..."))


if __name__ == '__main__':
    unittest.main()
