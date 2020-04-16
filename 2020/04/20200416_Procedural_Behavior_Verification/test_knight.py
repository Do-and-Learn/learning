import unittest

from knight import Knight


class KnightTest(unittest.TestCase):

    def setUp(self) -> None:
        self.attacker = Knight(100)
        self.attackee = SpyKnight()

    def test_attack_by_hand(self):
        # exercise
        self.attacker.attack(self.attackee)

        # verify
        self.assertTrue(self.attackee.is_hp_called)
        self.assertTrue(self.attackee.is_defense_called)


class SpyKnight(Knight):

    def __init__(self):
        Knight.__init__(self, 100)
        self.is_defense_called = False
        self.is_hp_called = False

    @property
    def defense(self) -> int:
        self.is_defense_called = True
        return super().defense

    @property
    def hp(self) -> int:
        self.is_hp_called = True
        return super().hp


if __name__ == '__main__':
    unittest.main()
