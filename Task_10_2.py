from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate_fabric_consumption(self):
        pass


class Jacket(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calculate_fabric_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calculate_fabric_consumption(self):
        return self.h * 2 + 0.3


if __name__ == '__main__':
    j = Jacket(50)
    print(j.calculate_fabric_consumption)

    s = Suit(50)
    print(s.calculate_fabric_consumption)
