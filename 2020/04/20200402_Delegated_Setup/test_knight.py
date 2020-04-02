import unittest

from hand import Hand
from knife import Knife
from knight import Knight


class KnightTest(unittest.TestCase):

    def test_attack_by_hand(self):
        # setup
        knight = self.create_knight()  # delegated setup

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Hand().attack_power())

    def test_attack_by_knife(self):
        # setup
        knight = self.create_knight_with_knife()  # delegated setup

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Knife().attack_power())

    def create_knight_with_knife(self):
        knight = self.create_knight()
        knight.arms = Knife()
        return knight

    @classmethod
    def create_knight(cls) -> Knight:
        return Knight(100)


if __name__ == '__main__':
    unittest.main()
