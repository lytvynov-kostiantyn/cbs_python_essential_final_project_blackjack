import random
from abc import abstractmethod, ABC
from const import get_int, user_choice


class AbstractPlayer(ABC):
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.points = 0
        self.cards = []
        self.bet = None

    def take_card(self, card):
        self.cards.append(card)
        self._update_points()

    def _update_points(self):
        self.points = sum([card.points for card in self.cards])
        if self.points > 21:
            if 'A' in [card.rank for card in self.cards]:
                for card in self.cards:
                    if card.rank == 'A':
                        card.points = 1
                self._update_points()

    @abstractmethod
    def make_bet(self):
        pass

    def end_round(self):
        self.points = 0
        self.cards = []
        self.bet = None

    @abstractmethod
    def ask_cards(self):
        pass


class Player(AbstractPlayer):
    def make_bet(self):
        while True:
            user_bet = get_int('Make your bet: ')
            if user_bet <= self.bank:
                self.bank -= user_bet
                self.bet = user_bet
                break
            else:
                print('The bet can`t exceed the size of your bank')

    def ask_cards(self):
        if self.points >= 21:
            return False
        player_choice = user_choice('Do you need card?(y/n): ')
        boo = True if player_choice == 'y' else False
        return boo

    def __str__(self):
        return f'Player "{self.name}"'


class Bot(AbstractPlayer):
    def __init__(self, name, bank):
        super().__init__(name, bank)
        self.bot_level = random.randint(17, 20)

    def make_bet(self):
        bet = random.randint(1, self.bank)
        self.bank -= bet
        self.bet = bet

    def ask_cards(self):
        if self.points < self.bot_level:
            return True
        else:
            return False

    def __str__(self):
        return f'Bot "{self.name}"'


class Dealer(AbstractPlayer):
    def make_bet(self):
        raise Exception('This type is dealer so it has no bets')

    def ask_cards(self):
        if self.points < 17:
            return True
        else:
            return False

    def __str__(self):
        return 'Dealer'
