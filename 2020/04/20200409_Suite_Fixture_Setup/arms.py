import abc


class Arms(abc.ABC):

    @abc.abstractmethod
    def attack_power(self) -> int:
        ...
