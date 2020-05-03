import random
import re
import unittest


def repl(m):
    inner_word = list(m.group(2))
    random.seed(0)
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)


class TextMungingTest(unittest.TestCase):

    def test_example(self):
        text = "Professor Abdolmalek, please report your absences promptly."
        sub = re.sub(r"(\w)(\w+)(\w)", repl, text)
        self.assertEqual('Psforseor Amdaoblelk, palese roeprt your acesbens ptmorlpy.', sub)


if __name__ == '__main__':
    unittest.main()
