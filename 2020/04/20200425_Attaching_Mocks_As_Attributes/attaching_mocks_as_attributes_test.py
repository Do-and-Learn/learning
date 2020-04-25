import unittest
from unittest.mock import MagicMock, call, patch


class AttachingMocksAsAttributesTest(unittest.TestCase):

    def test_attaching_mocks_as_attributes_1(self):
        parent = MagicMock()
        child1 = MagicMock(return_value=None)
        child2 = MagicMock(return_value=None)
        parent.child1 = child1
        parent.child2 = child2
        self.assertIsNone(child1(1))
        self.assertIsNone(child2(2))
        self.assertListEqual([call.child1(1), call.child2(2)], parent.mock_calls)

    def test_attaching_mocks_as_attributes_2(self):
        parent = MagicMock()
        child1 = MagicMock(return_value=None)
        child2 = MagicMock(return_value=None)
        parent.child1 = child1
        parent.child2 = child2
        self.assertIsNone(parent.child1(1))
        self.assertIsNone(parent.child2(2))
        self.assertListEqual([call.child1(1), call.child2(2)], parent.mock_calls)

    def test_attaching_mocks_as_attributes_3(self):
        parent = MagicMock()
        child1 = MagicMock(return_value='hi')
        child2 = MagicMock(return_value='hello')
        parent.child1 = child1
        parent.child2 = child2
        self.assertEqual('hi', parent.child1(1))
        self.assertEqual('hello', parent.child2(2))
        self.assertListEqual([call.child1(1), call.child2(2)], parent.mock_calls)

    def test_attaching_mocks_as_attributes_4(self):
        mock = MagicMock()
        not_a_child = MagicMock(name='not-a-child')  # if the mock has a name, this allows you to prevent the “parenting”
        mock.attribute = not_a_child
        self.assertIsInstance(mock.attribute(), MagicMock)
        self.assertListEqual([], mock.mock_calls)

    def test_attaching_mocks_as_attributes_5(self):
        parent = MagicMock()
        with patch('attaching_mocks_as_attributes_test.thing1', return_value=None) as child1:
            with patch('attaching_mocks_as_attributes_test.thing2', return_value=None) as child2:
                parent.attach_mock(child1, 'child1')
                parent.attach_mock(child2, 'child2')
                self.assertIsNone(child1('one'))
                self.assertIsNone(child2('two'))
        self.assertListEqual([call.child1('one'), call.child2('two')], parent.mock_calls)

    def test_attaching_mocks_as_attributes_6(self):
        parent = MagicMock()
        with patch('attaching_mocks_as_attributes_test.thing1', return_value=None) as child1:
            with patch('attaching_mocks_as_attributes_test.thing2', return_value=None) as child2:
                self.assertIsNone(child1('one'))
                self.assertIsNone(child2('two'))
        self.assertListEqual([], parent.mock_calls)

    def test_attaching_mocks_as_attributes_7(self):
        parent = MagicMock()
        parent.child1('one')
        parent.child2('two')
        self.assertListEqual([call.child1('one'), call.child2('two')], parent.mock_calls)


thing1 = object()
thing2 = object()

if __name__ == '__main__':
    unittest.main()
