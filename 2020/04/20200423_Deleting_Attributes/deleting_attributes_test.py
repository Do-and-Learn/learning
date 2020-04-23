import unittest
from unittest.mock import MagicMock


class DeletingAttributesTest(unittest.TestCase):

    def test_deleting_attributes_1(self):
        mock = MagicMock()
        self.assertTrue(hasattr(mock, 'm'))
        del mock.m
        self.assertFalse(hasattr(mock, 'm'))

    def test_deleting_attributes_2(self):
        mock = MagicMock()
        mock.m.return_value = 3
        del mock.m
        with self.assertRaises(AttributeError) as _:
            mock.m()

    def test_deleting_attributes_3(self):
        mock = MagicMock()
        mock.m.return_value = 3
        self.assertEqual(3, mock.m())
