from itertools import product
from random import shuffle

SUITS = ['Heart', 'Diamond', 'Club', 'Spade']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, rank, suit, points):
        self.rank = rank
        self.suit = suit
        self.points = points

    def __str__(self):
        return f'Card: {self.rank}/{self.suit} (points: {self.points})'

    def __repr__(self):
        return f'{self.rank}/{self.suit}/{self.points}'


class Deck:
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    @staticmethod
    def _generate_deck():
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            card = Card(suit=suit, rank=rank, points=points)
            cards.append(card)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
