import unittest
from unittest.mock import Mock, sentinel, DEFAULT, call, MagicMock


class MockTest(unittest.TestCase):

    def test_reset_mock(self):
        mock = Mock(return_value=None)
        mock('hello')
        self.assertTrue(mock.called)
        mock.reset_mock()
        self.assertFalse(mock.called)

    def test_mock_add_spec_1(self):
        mock = Mock(return_value=None)
        mock.mock_add_spec(['hi'])
        mock.hi()
        self.assertTrue(mock.hi.called)

    def test_mock_add_spec_2(self):
        mock = Mock(return_value=None)
        mock.mock_add_spec(['hi'], True)
        with self.assertRaises(AttributeError) as context:
            mock.hello()
        self.assertTrue("Mock object has no attribute 'hello'", context.exception.args[0])

    def test_mock_add_spec_3(self):
        mock = Mock(return_value=None)
        mock.mock_add_spec([], True)
        with self.assertRaises(AttributeError) as context:
            mock.hello()
        self.assertTrue("Mock object has no attribute 'hello'", context.exception.args[0])

    def test_mock_add_spec_4(self):
        mock = Mock(return_value=None)
        mock.hello()
        self.assertTrue(mock.hello.called)

    def test_attach_mock(self):
        mock = Mock(return_value=None)
        mock2 = Mock(return_value='hello')
        mock.attach_mock(mock2, 'hi')
        self.assertEqual('hello', mock.hi())

    def test_configure_mock_1(self):
        mock = Mock()
        attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
        mock.configure_mock(**attrs)
        self.assertEqual(3, mock.method())

    def test_configure_mock_2(self):
        mock = Mock()
        attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
        mock.configure_mock(**attrs)
        with self.assertRaises(KeyError) as _:
            mock.other()

    def test_configure_mock_3(self):
        attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
        mock = Mock(some_attribute='eggs', **attrs)
        mock.configure_mock(**attrs)
        self.assertEqual('eggs', mock.some_attribute)

    def test_configure_mock_4(self):
        attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
        mock = Mock(some_attribute='eggs', **attrs)
        mock.configure_mock(**attrs)
        self.assertEqual(3, mock.method())

    def test_configure_mock_5(self):
        attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
        mock = Mock(some_attribute='eggs', **attrs)
        mock.configure_mock(**attrs)
        with self.assertRaises(KeyError) as _:
            mock.other()

    def test_dir(self):
        attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
        mock = Mock(some_attribute='eggs', **attrs)
        members = dir(mock)
        self.assertIn('some_attribute', members)
        self.assertIn('method', members)
        self.assertIn('other', members)
        self.assertNotIn('hi', members)

    def test_called(self):
        mock = Mock(return_value=None)
        self.assertFalse(mock.called)
        mock()
        self.assertTrue(mock.called)

    def test_call_count(self):
        mock = Mock(return_value=None)
        self.assertEqual(0, mock.call_count)
        mock()
        mock()
        self.assertEqual(2, mock.call_count)

    def test_return_value_1(self):
        mock = Mock()
        mock.return_value = 'fish'
        self.assertEqual('fish', mock())

    def test_return_value_2(self):
        mock = Mock()
        mock.return_value.attribute = sentinel.Attribute
        self.assertIs(mock().attribute, sentinel.Attribute)

    def test_return_value_3(self):
        mock = Mock()
        mock.return_value.attribute = sentinel.Attribute
        mock.return_value()
        self.assertIsNone(mock.return_value.assert_called_with())

    def test_return_value_4(self):
        mock = Mock()
        mock.return_value.attribute = sentinel.Attribute
        with self.assertRaises(AssertionError) as context:
            mock.return_value.assert_called_with()
        self.assertEqual("expected call not found.\nExpected: mock()\nActual: not called.", context.exception.args[0])

    def test_return_value_5(self):
        mock = Mock(return_value=3)
        self.assertEqual(3, mock())
        self.assertEqual(3, mock.return_value)

    def test_side_effect_1(self):
        mock = Mock()
        mock.side_effect = Exception('Boom!')
        with self.assertRaises(Exception) as context:
            mock()
        self.assertEqual("Boom!", context.exception.args[0])

    def test_side_effect_2(self):
        mock = Mock()
        mock.side_effect = [3, 2, 1]
        self.assertListEqual([3, 2, 1], [mock(), mock(), mock()])

    def test_side_effect_3(self):
        mock = Mock(return_value=3)

        def side_effect(*args, **kwargs):
            return DEFAULT

        mock.side_effect = side_effect
        self.assertEqual(3, mock())

    def test_side_effect_4(self):
        mock = Mock(return_value=3)
        mock.side_effect = lambda *args, **kwargs: DEFAULT
        self.assertEqual(3, mock())

    def test_side_effect_5(self):
        mock = Mock(return_value=3)
        mock.side_effect = lambda: DEFAULT
        self.assertEqual(3, mock())

    def test_side_effect_6(self):
        mock = Mock(side_effect=lambda value: value + 1)
        self.assertEqual(4, mock(3))
        self.assertEqual(-7, mock(-8))

    def test_side_effect_7(self):
        mock = Mock(side_effect=KeyError('Boom!'), return_value=3)
        with self.assertRaises(KeyError) as context:
            mock()
        self.assertEqual("Boom!", context.exception.args[0])

    def test_side_effect_8(self):
        mock = Mock(side_effect=KeyError('Boom!'), return_value=3)
        mock.side_effect = None
        self.assertEqual(3, mock())

    def test_call_args_1(self):
        mock = Mock(return_value=None)
        self.assertIsNone(mock.call_args)

    def test_call_args_2(self):
        mock = Mock(return_value=None)
        mock()
        self.assertEqual(call(), mock.call_args)
        self.assertEqual(call, mock.call_args)

    def test_call_args_3(self):
        mock = Mock(return_value=None)
        mock()
        self.assertEqual((), mock.call_args)

    def test_call_args_4(self):
        mock = Mock(return_value=None)
        mock(3, 4)
        self.assertEqual(call(3, 4), mock.call_args)

    def test_call_args_5(self):
        mock = Mock(return_value=None)
        mock(3, 4)
        self.assertEqual(((3, 4),), mock.call_args)

    def test_call_args_6(self):
        mock = Mock(return_value=None)
        mock(3, 4, 5, key='fish', next='w00t!')
        self.assertEqual(((3, 4, 5), {'key': 'fish', 'next': 'w00t!'}), mock.call_args)

    def test_call_args_7(self):
        mock = Mock(return_value=None)
        mock(3, 4)
        self.assertEqual((3, 4), mock.call_args.args)
        self.assertEqual({}, mock.call_args.kwargs)

    def test_call_args_8(self):
        mock = Mock(return_value=None)
        mock(a='a', b='b')
        self.assertEqual((), mock.call_args.args)
        self.assertEqual({'a': 'a', 'b': 'b'}, mock.call_args.kwargs)

    def test_call_args_9(self):
        mock = Mock(return_value=None)
        mock(3, 4, 5, key='fish', next='w00t!')
        self.assertEqual(call(3, 4, 5, key='fish', next='w00t!'), mock.call_args)

    def test_call_args_list(self):
        mock = Mock(return_value=None)
        mock()
        mock(3, 4)
        mock(key='fish', next='w00t!')
        self.assertListEqual([call(), call(3, 4), call(key='fish', next='w00t!')], mock.call_args_list)

    def test_method_calls(self):
        mock = Mock()
        mock.method()
        mock.property.method.attribute()
        self.assertListEqual([call.method(), call.property.method.attribute()], mock.method_calls)

    def test_mock_calls_1(self):
        mock = Mock()
        result = mock(1, 2, 3)
        self.assertIsInstance(result, Mock)
        self.assertIsInstance(mock.first(a=3), Mock)
        self.assertIsInstance(mock.second(), Mock)
        self.assertIsInstance(result(1), Mock)
        self.assertListEqual([call(1, 2, 3), call.first(a=3), call.second(), call()(1)], mock.mock_calls)

    def test_mock_calls_2(self):
        mock = MagicMock()
        self.assertEqual(1, int(mock))
        self.assertListEqual([call.__int__()], mock.mock_calls)

    def test_mock_calls_variant(self):
        mock = Mock()
        with self.assertRaises(TypeError) as context:
            int(mock)
        self.assertEqual("int() argument must be a string, a bytes-like object or a number, not 'Mock'", context.exception.args[0])

    def test_mock_calls_3(self):
        mock = Mock()
        mock.top(a=3).bottom()
        self.assertListEqual([call.top(a=3), call.top().bottom()], mock.mock_calls)

    def test_class_1(self):
        mock = Mock(spec=3)
        self.assertIsInstance(mock, int)

    def test_class_2(self):
        mock = Mock(spec='hi')
        self.assertIsInstance(mock, str)

    def test_class_3(self):
        mock = Mock()
        mock.__class__ = dict
        self.assertIsInstance(mock, dict)


if __name__ == '__main__':
    unittest.main()
