import unittest

from arms import Arms
from gun import Gun
from hand import Hand
from knife import Knife
from knight import Knight


class KnightTest(unittest.TestCase):

    def test_attack_by_hand(self):
        # setup
        knight = self.create_knight()  # parameterized creation method

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Hand().attack_power())

    def test_attack_by_knife(self):
        # setup
        knight = self.create_knight(Knife())  # parameterized creation method

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Knife().attack_power())

    def test_attack_by_gun(self):
        # setup
        knight = self.create_knight(Gun())  # parameterized creation method

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Gun().attack_power())

    @classmethod
    def create_knight(cls, arms: Arms = None) -> Knight:
        knight = Knight(100)
        if arms:
            knight.arms = arms
        return knight


if __name__ == '__main__':
    unittest.main()
