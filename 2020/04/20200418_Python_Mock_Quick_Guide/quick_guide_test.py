import unittest
from unittest.mock import MagicMock, Mock, patch, create_autospec

import module
from production_class import ProductionClass


@patch('module.ClassName2')
@patch('module.ClassName1')
def test(mock_class_1, mock_class_2):
    module.ClassName1()
    module.ClassName2()
    assert mock_class_1 is module.ClassName1
    assert mock_class_2 is module.ClassName2
    assert mock_class_1.called
    assert mock_class_2.called


def function(a, b, c):
    pass


class QuickGuideTest(unittest.TestCase):

    def test_example_1(self):
        expected_return_value = 3
        thing = ProductionClass()
        thing.method = MagicMock(return_value=expected_return_value)
        ret = thing.method(3, 4, 5, key='value')
        self.assertEqual(expected_return_value, ret)

    def test_example_1_variant(self):
        expected_return_value = 3
        thing = ProductionClass()
        thing.method = MagicMock(return_value=expected_return_value)
        ret = thing.method()  # Parameter is not necessary, because we don't specify it.
        self.assertEqual(expected_return_value, ret)

    def test_example_2(self):
        mock = Mock(side_effect=KeyError('foo'))
        with self.assertRaises(KeyError) as context:
            mock()
        self.assertEqual('foo', context.exception.args[0])

    def test_example_2_variant_1(self):
        expected_return_value = 3
        mock = Mock(side_effect=KeyError('foo'))
        mock.method = MagicMock(return_value=expected_return_value)
        ret = mock.method()
        self.assertIsInstance(ret, int)
        self.assertEqual(expected_return_value, ret)

    def test_example_2_variant_2(self):
        expected_return_value = 3
        mock = Mock(side_effect=KeyError('foo'))
        mock.method = MagicMock(return_value=expected_return_value)
        ret = mock.method2()  # Call a method without mocking it. This will not throw an exception, even if we init a mock with side_effect parameter.
        self.assertIsInstance(ret, Mock)

    def test_example_3(self):
        values = {'a': 1, 'b': 2, 'c': 3}
        mock = Mock()
        mock.side_effect = lambda key: values[key]
        self.assertEqual(values['a'], mock('a'))
        self.assertEqual(values['b'], mock('b'))
        self.assertEqual(values['c'], mock('c'))

    # noinspection PyMethodMayBeStatic
    def test_example_4(self):
        test()

    @patch('module.ClassName2')
    @patch('module.ClassName1')
    def test_example_4_variant_1(self, mock_class_1, mock_class_2):
        module.ClassName1()
        module.ClassName2()
        self.assertIs(mock_class_1, module.ClassName1)
        self.assertIs(mock_class_2, module.ClassName2)
        self.assertTrue(mock_class_1.called)
        self.assertTrue(mock_class_2.called)

    @patch('module.ClassName1')
    def test_example_4_variant_2(self, mock_class):
        module.ClassName1()
        self.assertTrue(mock_class.called)

    @patch('module.ClassName1')
    def test_example_4_variant_3(self, mock_class):
        self.assertFalse(mock_class.called)

    # noinspection PyMethodMayBeStatic
    def test_example_5(self):
        with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
            thing = ProductionClass()
            thing.method(1, 2, 3)
        mock_method.assert_called_once_with(1, 2, 3)

    # noinspection PyMethodMayBeStatic
    def test_example_5_variant_1(self):
        with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
            ProductionClass()
        mock_method.assert_not_called()

    # noinspection PyMethodMayBeStatic
    def test_example_5_variant_2(self):
        with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
            thing = ProductionClass()
            thing.method(1, 2, 3)
        with self.assertRaises(AssertionError) as context:
            mock_method.assert_not_called()
        self.assertEqual("Expected 'method' to not have been called. Called 1 times.\nCalls: [call(1, 2, 3)].", context.exception.args[0])

    # noinspection PyMethodMayBeStatic
    def test_example_5_variant_3(self):
        with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
            thing = ProductionClass()
            thing.method(1, 2, 3)
            thing.method(1, 2, 3)
        with self.assertRaises(AssertionError) as context:
            mock_method.assert_called_once_with(1, 2, 3)
        self.assertEqual("Expected 'method' to be called once. Called 2 times.\nCalls: [call(1, 2, 3), call(1, 2, 3)].", context.exception.args[0])

    # noinspection SpellCheckingInspection
    def test_example_6(self):
        foo = {'key': 'value'}
        original = foo.copy()
        with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
            self.assertNotEqual(foo, original)
            self.assertEqual(foo, {'newkey': 'newvalue'})
        self.assertEqual(foo, original)
        self.assertEqual(foo, {'key': 'value'})

    # noinspection SpellCheckingInspection
    def test_example_6_variant(self):
        foo = {'key': 'value'}
        original = foo.copy()
        with patch.dict(foo, {'newkey': 'newvalue'}, clear=False):
            self.assertNotEqual(foo, original)
            self.assertEqual(foo, {'key': 'value', 'newkey': 'newvalue'})
        self.assertEqual(foo, original)
        self.assertEqual(foo, {'key': 'value'})

    # noinspection SpellCheckingInspection
    def test_example_7(self):
        mock = MagicMock()
        mock.__str__.return_value = 'foobarbaz'
        self.assertEqual('foobarbaz', str(mock))
        mock.__str__.assert_called_with()

    # noinspection SpellCheckingInspection,PyMethodMayBeStatic
    def test_example_7_variant(self):
        mock = MagicMock()
        mock.__str__.return_value = 'foobarbaz'
        mock.__str__.assert_not_called()

    # noinspection SpellCheckingInspection
    def test_example_8(self):
        mock = Mock()
        mock.__str__ = Mock(return_value='wheeeeee')
        self.assertEqual('wheeeeee', str(mock))

    def test_example_9(self):
        mock_function = create_autospec(function, return_value='fishy')
        ret = mock_function(1, 2, 3)
        self.assertEqual('fishy', ret)
        mock_function.assert_called_once_with(1, 2, 3)

    def test_example_9_2(self):
        mock_function = create_autospec(function, return_value='fishy')
        with self.assertRaises(TypeError) as context:
            mock_function('wrong arguments')
        self.assertEqual("missing a required argument: 'b'", context.exception.args[0])


if __name__ == '__main__':
    unittest.main()
