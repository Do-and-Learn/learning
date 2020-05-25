import contextlib
import io
import unittest


def hi():
    return 'Hello'


# noinspection PyUnusedLocal
class ExecTest(unittest.TestCase):

    def test_return_value(self):
        x = 1
        self.assertEqual(None, exec('x+1'))

    def test_local_var_not_changed(self):
        x = 1
        g = {}
        self.assertEqual(None, exec('x=2', g))
        self.assertEqual(2, g['x'])
        self.assertEqual(1, x)

    def test_local_var_changed(self):
        x = 1
        g = {}
        loc = locals()
        self.assertEqual(None, exec('x=x+2', g, loc))
        self.assertNotIn('x', g)
        self.assertEqual(3, loc['x'])
        self.assertEqual(1, x)

    def test_glob_and_local_var(self):
        g = {'x': 1}
        loc = {'x': 2}
        self.assertEqual(None, exec('x=x+2', g, loc))
        self.assertEqual(1, g['x'])
        self.assertEqual(4, loc['x'])

    def test_call_function_no_return(self):
        self.assertEqual(None, exec('print(hi())'))

    def test_call_function(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            exec('print(hi())')
        self.assertEqual('Hello\n', f.getvalue())
