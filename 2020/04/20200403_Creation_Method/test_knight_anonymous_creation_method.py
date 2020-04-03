import unittest

from hand import Hand
from knife import Knife
from knight import Knight


class KnightTest(unittest.TestCase):

    def test_attack_by_hand(self):
        # setup
        knight = self.create_anonymous_knight()  # anonymous creation method

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Hand().attack_power())

    def test_attack_by_knife(self):
        # setup
        knight = self.create_anonymous_knight()  # anonymous creation method
        knight.arms = Knife()

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Knife().attack_power())

    @classmethod
    def create_anonymous_knight(cls) -> Knight:
        return Knight(100)


if __name__ == '__main__':
    unittest.main()
