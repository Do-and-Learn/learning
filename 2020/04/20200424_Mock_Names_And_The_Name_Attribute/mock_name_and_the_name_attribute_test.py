import unittest
from unittest.mock import MagicMock


class MockNamesAndTheNameAttributeTest(unittest.TestCase):

    def test_name_1(self):
        mock = MagicMock()
        mock.configure_mock(name='my_name')
        self.assertEqual('my_name', mock.name)
        self.assertIsInstance(mock.name, str)

    def test_name_2(self):
        mock = MagicMock()
        mock.name = 'foo'
        self.assertEqual('foo', mock.name)
        self.assertIsInstance(mock.name, str)

    def test_name_3(self):
        mock = MagicMock()
        self.assertIsInstance(mock.name, MagicMock)
