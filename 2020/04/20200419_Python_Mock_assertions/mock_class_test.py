import unittest
from unittest.mock import Mock, call


# noinspection PyMethodMayBeStatic
class MockClassTest(unittest.TestCase):

    def test_assert_called(self):
        mock = Mock()
        mock.method()
        mock.method.assert_called()

    def test_assert_called_variant(self):
        mock = Mock()
        with self.assertRaises(AssertionError) as context:
            mock.method.assert_called()
        self.assertEqual("Expected 'method' to have been called.", context.exception.args[0])

    def test_assert_called_once_1(self):
        mock = Mock()
        mock.method()
        mock.method.assert_called_once()

    def test_assert_called_once_2(self):
        mock = Mock()
        mock.method()
        mock.method()
        with self.assertRaises(AssertionError) as context:
            mock.method.assert_called_once()
        self.assertEqual("Expected 'method' to have been called once. Called 2 times.\nCalls: [call(), call()].", context.exception.args[0])

    def test_assert_called_once_variant(self):
        mock = Mock()
        with self.assertRaises(AssertionError) as context:
            mock.method.assert_called_once()
        self.assertEqual("Expected 'method' to have been called once. Called 0 times.", context.exception.args[0])

    def test_assert_called_with(self):
        mock = Mock()
        mock.method(1, 2, 3, test='wow')
        mock.method.assert_called_with(1, 2, 3, test='wow')

    def test_assert_called_with_variant(self):
        mock = Mock()
        with self.assertRaises(AssertionError) as context:
            mock.method.assert_called_with(1, 2, 3, test='wow')
        self.assertEqual("expected call not found.\nExpected: method(1, 2, 3, test='wow')\nActual: not called.", context.exception.args[0])

    def test_assert_called_once_with_1(self):
        mock = Mock(return_value=None)
        mock('foo', bar='baz')
        mock.assert_called_once_with('foo', bar='baz')

    def test_assert_called_once_with_2(self):
        mock = Mock(return_value=None)
        mock('foo', bar='baz')
        mock('other', bar='values')
        with self.assertRaises(AssertionError) as context:
            mock.assert_called_once_with('other', bar='values')  # It is weird ... refer to "assert_any_call".
        self.assertEqual("Expected 'mock' to be called once. Called 2 times.\nCalls: [call('foo', bar='baz'), call('other', bar='values')].", context.exception.args[0])

    def test_assert_called_once_with_variant(self):
        mock = Mock(return_value=None)
        mock('foo', bar='baz')
        with self.assertRaises(AssertionError) as context:
            mock.assert_called_once_with('other', bar='values')
        self.assertEqual("expected call not found.\nExpected: mock('other', bar='values')\nActual: mock('foo', bar='baz')", context.exception.args[0])

    def test_assert_any_call(self):
        mock = Mock(return_value=None)
        mock('foo', bar='baz')
        mock('other', bar='values')
        mock.assert_any_call('other', bar='values')

    def test_assert_any_call_variant(self):
        mock = Mock(return_value=None)
        mock('foo', bar='baz')
        with self.assertRaises(AssertionError) as context:
            mock.assert_any_call('other', bar='values')
        self.assertEqual("mock('other', bar='values') call not found", context.exception.args[0])

    def test_assert_has_calls_1(self):
        mock = Mock(return_value=None)
        mock(1)
        mock(2)
        mock(3)
        mock(4)
        calls = [call(2), call(3)]
        mock.assert_has_calls(calls)

    def test_assert_has_calls_2(self):
        mock = Mock(return_value=None)
        mock(1)
        mock(2)
        mock(3)
        mock(4)
        calls = [call(4), call(2), call(3)]
        mock.assert_has_calls(calls, any_order=True)

    def test_assert_has_calls_variant(self):
        mock = Mock(return_value=None)
        mock(1)
        mock(2)
        mock(3)
        mock(4)
        calls = [call(5), call(2), call(3)]
        with self.assertRaises(AssertionError) as context:
            mock.assert_has_calls(calls, any_order=True)
        self.assertEqual("'mock' does not contain all of (call(5),) in its call list, found [call(1), call(4)] instead", context.exception.args[0])

    def test_assert_not_called_1(self):
        mock = Mock()
        mock.hello.assert_not_called()

    def test_assert_not_called_2(self):
        mock = Mock()
        mock.hello()
        with self.assertRaises(AssertionError) as context:
            mock.hello.assert_not_called()
        self.assertEqual("Expected 'hello' to not have been called. Called 1 times.\nCalls: [call()].", context.exception.args[0])


if __name__ == '__main__':
    unittest.main()
