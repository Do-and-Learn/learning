import re
import unittest


class CheckingForAPairTest(unittest.TestCase):

    def test_valid_poker(self):
        valid = re.compile(r"^[a2-9tjqk]{5}$")
        self.assertIsNotNone(valid.match("akt5q"))
        self.assertIsNotNone(valid.match("727ak"))

    def test_invalid_poker(self):
        valid = re.compile(r"^[a2-9tjqk]{5}$")
        self.assertIsNone(valid.match("akt5e"))
        self.assertIsNone(valid.match("akt"))

    def test_pair(self):
        pair = re.compile(r".*(.).*\1")  # \1: back references
        match = pair.match("717ak")
        self.assertIsNotNone(match)
        self.assertEqual('717', match.group())
        self.assertEqual(('7',), match.groups())
        self.assertEqual('7', match.group(1))

    def test_no_pair(self):
        pair = re.compile(r".*(.).*\1")  # \1: back references
        match = pair.match("718ak")
        self.assertIsNone(match)

        with self.assertRaises(AttributeError) as context:
            match.group(1)
        self.assertEqual("'NoneType' object has no attribute 'group'", context.exception.args[0])

    def test_pair_2(self):
        pair = re.compile(r".*(.).*\1")  # \1: back references
        match = pair.match("354aa")
        self.assertIsNotNone(match)
        self.assertEqual('354aa', match.group())
        self.assertEqual(('a',), match.groups())
        self.assertEqual('a', match.group(1))


if __name__ == '__main__':
    unittest.main()
