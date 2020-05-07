import re
import unittest


class ExampleTest(unittest.TestCase):

    def test_example_1(self):
        match = re.match(r"\W(.)\1\W", " ff ")  # row string annotation
        self.assertIsNotNone(match)

    def test_example_1_variant(self):
        match = re.match("\W(.)\1\W", " ff ")
        self.assertIsNone(match)

    def test_example_2(self):
        match = re.match("\W(.)\\1\W", " ff ")
        self.assertIsNotNone(match)

    def test_example_2_variant(self):
        match = re.match(r"\W(.)\\1\W", " ff ")  # row string annotation
        self.assertIsNone(match)

    def test_example_3(self):
        match = re.match(r"\\", r"\\")
        self.assertIsNotNone(match)

    def test_example_3_variant_1(self):
        match = re.match(r"\\", "\\")
        self.assertIsNotNone(match)

    def test_example_3_variant_2(self):
        with self.assertRaises(re.error) as context:
            re.match("\\", "\\")
        self.assertEqual('bad escape (end of pattern) at position 0', context.exception.args[0])

    def test_example_4(self):
        match = re.match("\\\\", r"\\")
        self.assertIsNotNone(match)

    def test_example_4_variant_1(self):
        match = re.match("\\\\", "\\")
        self.assertIsNotNone(match)

    def test_example_4_variant_2(self):
        match = re.match(r"\\\\", "\\")
        self.assertIsNone(match)

    def test_example_4_variant_3(self):
        match = re.match(r"\\\\", "\\\\")
        self.assertIsNotNone(match)

    def test_example_4_variant_4(self):
        match = re.match("\\\\", "\\\\")
        self.assertIsNotNone(match)


if __name__ == '__main__':
    unittest.main()
