import contextlib
import io
import unittest


class Obj:

    def __str__(self):
        return 'xx'


class PrintTest(unittest.TestCase):

    def test_no_arg(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print()
        self.assertEqual('\n', out.getvalue())

    def test_sep(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print('a', 'b', 'c')
        self.assertEqual('a b c\n', out.getvalue())

        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print('a', 'b', 'c', sep=None)
        self.assertEqual('a b c\n', out.getvalue())

        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print('a', 'b', 'c', sep=', ')
        self.assertEqual('a, b, c\n', out.getvalue())

        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print('a', 'b', 'c', sep='')
        self.assertEqual('abc\n', out.getvalue())

    def test_end(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print('hello', end=None)
        self.assertEqual('hello\n', out.getvalue())

        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print('hello', end='')
        self.assertEqual('hello', out.getvalue())

        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print('hello', end='!!')
        self.assertEqual('hello!!', out.getvalue())

    def test_file(self):
        out = io.StringIO()
        print('hello world!', file=out)
        self.assertEqual('hello world!\n', out.getvalue())

        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print('hello', file=None)
        self.assertEqual('hello\n', out.getvalue())

    def test_obj(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print(Obj())
        self.assertEqual('xx\n', out.getvalue())

    # noinspection PyTypeChecker
    def test_exceptions(self):
        with self.assertRaises(TypeError) as context:
            print('', sep=Obj())
        self.assertEqual('sep must be None or a string, not Obj', context.exception.args[0])

        with self.assertRaises(TypeError) as context:
            print('', end=Obj())
        self.assertEqual('end must be None or a string, not Obj', context.exception.args[0])
