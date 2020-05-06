import re
import unittest


class ExampleTest(unittest.TestCase):

    def test_something(self):
        text = "He was carefully disguised but captured quickly by police."
        result = []
        for m in re.finditer(r"\w+ly", text):
            result.append((m.start(), m.end(), m.group(0)))

        self.assertCountEqual([(7, 16, 'carefully'), (40, 47, 'quickly')], result)


if __name__ == '__main__':
    unittest.main()
