import unittest
from unittest.mock import MagicMock, call, DEFAULT


class CallingTest(unittest.TestCase):

    def test_mock_calls_1(self):
        mock = MagicMock(side_effect=IndexError)
        with self.assertRaises(IndexError) as _:
            mock(1, 2, 3)
        self.assertListEqual([call(1, 2, 3)], mock.mock_calls)

        mock.side_effect = KeyError('Bang!')
        with self.assertRaises(KeyError) as context:
            mock('two', 'three', 'four')
        self.assertEqual('Bang!', context.exception.args[0])

        self.assertListEqual([call(1, 2, 3), call('two', 'three', 'four')], mock.mock_calls)

    def test_mock_calls_2(self):
        mock = MagicMock(side_effect=lambda value: value + 1)
        self.assertEqual(2, mock(1))
        self.assertEqual(3, mock(2))
        self.assertListEqual([call(1), call(2)], mock.mock_calls)

    def test_mock_calls_3(self):
        mock = MagicMock()
        mock.side_effect = lambda: mock.return_value
        mock.return_value = 3
        self.assertEqual(3, mock())

    def test_mock_calls_4(self):
        mock = MagicMock()
        mock.side_effect = lambda: DEFAULT
        mock.return_value = 3
        self.assertEqual(3, mock())

    def test_mock_calls_5(self):
        mock = MagicMock(return_value=6)
        mock.side_effect = lambda: 3
        self.assertEqual(3, mock())

        mock.side_effect = None
        self.assertEqual(6, mock())

    def test_mock_calls_6(self):
        mock = MagicMock(side_effect=[1, 2, 3])
        self.assertEqual(1, mock())
        self.assertEqual(2, mock())
        self.assertEqual(3, mock())
        with self.assertRaises(StopIteration) as _:
            mock()

    def test_mock_calls_7(self):
        iterable = (33, ValueError, 66)
        mock = MagicMock(side_effect=iterable)
        self.assertEqual(33, mock())
        with self.assertRaises(ValueError) as _:
            mock()
        self.assertEqual(66, mock())


if __name__ == '__main__':
    unittest.main()
