import unittest

from hand import Hand
from knife import Knife
from knight import Knight


class KnightTest(unittest.TestCase):

    def test_attack_by_hand(self):
        # in-line setup
        knight = Knight(100)

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Hand().attack_power())

    def test_attack_by_knife(self):
        # in-line setup
        knight = Knight(100)
        knight.arms = Knife()

        # exercise
        pain = knight.attack_power()

        # verify
        self.assertEqual(pain, Knife().attack_power())


if __name__ == '__main__':
    unittest.main()
