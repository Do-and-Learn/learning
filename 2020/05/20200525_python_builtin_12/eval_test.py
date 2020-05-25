import unittest


def hi():
    return 'Hello'


# noinspection PyUnusedLocal
class EvalTest(unittest.TestCase):

    def test_local_1(self):
        x = 1
        self.assertEqual(2, eval('x+1'))

    def test_local_2(self):
        x = 1
        self.assertEqual(3, eval('x+1', {'x': 2}))

    def test_local_3(self):
        x = 1
        self.assertEqual(3, eval('x+1', {}, {'x': 2}))

    def test_globs(self):
        self.assertEqual(2, eval('x+1', {'x': 1}))

    def test_locals_override_global_1(self):
        self.assertEqual(3, eval('x+1', {'x': 1}, {'x': 2}))

    def test_locals_override_global_2(self):
        self.assertEqual('local var', eval('var', {'var': 'global var'}, {'var': 'local var'}))

    def test_var_not_define(self):
        with self.assertRaises(NameError) as context:
            eval('x')
        self.assertEqual("name 'x' is not defined", context.exception.args[0])

    def test_syntax_error(self):
        with self.assertRaises(SyntaxError) as context:
            eval('1+*2')
        self.assertEqual("invalid syntax", context.exception.args[0])

    def test_function(self):
        self.assertEqual('Hello', eval('hi()'))

    def test_return_value(self):
        with self.assertRaises(SyntaxError) as context:
            eval('x=x+1')
        self.assertEqual("invalid syntax", context.exception.args[0])


if __name__ == '__main__':
    unittest.main()
