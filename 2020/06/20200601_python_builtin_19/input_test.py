import contextlib
import io
import sys
import unittest


# noinspection SpellCheckingInspection
class InputTest(unittest.TestCase):

    def test_input_text(self):
        sys.stdin = io.StringIO('Teddy')
        self.assertEqual('Teddy', input('What is your name?'))

    def test_promote(self):
        sys.stdin = io.StringIO('\n')
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            input('Hello')
        self.assertEqual('Hello', out.getvalue())


if __name__ == '__main__':
    unittest.main()
