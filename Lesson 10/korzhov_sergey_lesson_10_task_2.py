from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def calculate(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def calculate(self):
        return 2 * self.h + 0.3


coat = Coat(10)
costume = Costume(20)

print(f'Расход ткани = {coat.calculate + costume.calculate}')
