import random
from abc import abstractmethod, ABC
from const import get_int


class AbstractPlayer(ABC):
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.points = 0
        self.cards = []
        self.bet = None

    def take_card(self, card):
        self.cards.append(card)
        self._update_points(card)

    def _update_points(self, card):
        self.points += card.points

    @abstractmethod
    def make_bet(self):
        pass

    def end_round(self):
        self.points = 0
        self.cards = []
        self.bet = None


class Player(AbstractPlayer):
    def make_bet(self):
        while True:
            user_bet = get_int('Make your bet: ')
            if user_bet < self.bank:
                self.bank -= user_bet
                self.bet = user_bet
                break
            else:
                print('The bet can`t exceed the size of your bank')

    def __str__(self):
        return f'Player "{self.name}"'


class Bot(AbstractPlayer):
    def make_bet(self):
        bet = random.randint(1, self.bank)
        self.bank -= bet
        self.bet = bet

    def __str__(self):
        return f'Bot "{self.name}"'


class Dealer(AbstractPlayer):
    def make_bet(self):
        raise Exception('This type is dealer so it has no bets')

    def __str__(self):
        return 'Dealer'

