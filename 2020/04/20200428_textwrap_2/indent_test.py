import unittest
from textwrap import indent


class IndentTest(unittest.TestCase):

    def test_indent_1(self):
        s = 'hello\n\n \nworld'
        self.assertEqual('  hello\n\n \n  world', indent(s, '  '))

    def test_indent_2(self):
        s = 'hello\n\n \nworld'
        self.assertEqual('+ hello\n+ \n+  \n+ world', indent(s, '+ ', lambda line: True))

    def test_indent_3(self):
        s = 'hello\n\n \n   world'
        self.assertEqual('  hello\n\n \n     world', indent(s, '  '))


if __name__ == '__main__':
    unittest.main()
