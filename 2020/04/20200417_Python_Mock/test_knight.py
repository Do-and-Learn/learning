import unittest
from unittest.mock import PropertyMock, MagicMock


class KnightTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = MagicMock()

    def test_attack_by_hand(self):
        hp = PropertyMock(return_value=100)
        defense = PropertyMock(return_value=0)
        type(self.mock).hp = hp
        type(self.mock).defense = defense

        # exercise
        self.assertEqual(100, self.mock.hp)
        self.assertEqual(0, self.mock.defense)


if __name__ == '__main__':
    unittest.main()
