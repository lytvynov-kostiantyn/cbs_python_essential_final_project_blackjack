from abc import abstractmethod, ABC
from cards import *


class AbstractPlayer(ABC):
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.points = 0
        self.cards = []

    def take_card(self, card):
        self.cards.append(card)
        self._update_points(card)

    def _update_points(self, card):
        self.points += card.points


class Player(AbstractPlayer):
    pass


class Bot(AbstractPlayer):
    pass

    def __str__(self):
        return f'Bot "{self.name}" with {self.bank} bank is created'
