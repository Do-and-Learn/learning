import unittest
from textwrap import dedent


class DedentTest(unittest.TestCase):

    def test_dedent_1(self):
        s = '''\
            hello
              world
            '''
        self.assertEqual('hello\n  world\n', dedent(s))

    def test_dedent_2(self):
        s = '''\
              hello
            world
            '''
        self.assertEqual('  hello\nworld\n', dedent(s))


if __name__ == '__main__':
    unittest.main()
