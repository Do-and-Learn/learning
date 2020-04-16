from __future__ import annotations

from arms import Arms
from hand import Hand


class Knight:

    def __init__(self, max_hp: int) -> None:
        self.__max_hp = max_hp
        self.__hp = max_hp
        self.__arms = Hand()

    @property
    def max_hp(self) -> int:
        return self.__max_hp

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def arms(self):
        return self.__arms

    @arms.setter
    def arms(self, value: Arms):
        self.__arms = value

    @property
    def defense(self) -> int:
        return 0

    def attack(self, obj: Knight):
        obj.__hp = obj.hp - max(self.__arms.attack_power() - obj.defense, 0)
