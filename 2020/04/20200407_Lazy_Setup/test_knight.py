import unittest

from hand import Hand
from knife import Knife
from knight import Knight


class KnightTest(unittest.TestCase):
    knight = None

    def setUp(self) -> None:
        if KnightTest.knight is None:  # lazy setup
            KnightTest.knight = self.create_anonymous_knight()

    def test_attack_by_hand(self):
        # exercise
        pain = KnightTest.knight.attack_power()

        # verify
        self.assertEqual(pain, Hand().attack_power())

    def test_attack_by_knife(self):
        KnightTest.knight.arms = Knife()

        # exercise
        pain = self.knight.attack_power()

        # verify
        self.assertEqual(pain, Knife().attack_power())

    @classmethod
    def create_anonymous_knight(cls) -> Knight:
        return Knight(100)


if __name__ == '__main__':
    unittest.main()
