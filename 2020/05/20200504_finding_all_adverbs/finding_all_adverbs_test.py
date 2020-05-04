import re
import unittest


class FindingAllAdverbsTest(unittest.TestCase):

    def test_finding_all_adverbs(self):
        text = "He was carefully disguised but captured quickly by police."
        verbs = re.findall(r"\w+ly", text)
        self.assertEqual(['carefully', 'quickly'], verbs)


if __name__ == '__main__':
    unittest.main()
