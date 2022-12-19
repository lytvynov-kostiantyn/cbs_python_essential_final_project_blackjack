import random
from abc import abstractmethod, ABC


class AbstractPlayer(ABC):
    def __init__(self):
        self.points = 0
        self.cards = []
        self.bet = None

    def take_card(self, card):
        self.cards.append(card)
        self._update_points()

    def _update_points(self):
        self.points = sum([card.points for card in self.cards])

    @abstractmethod
    def make_bet(self):
        pass

    @abstractmethod
    def ask_cards(self):
        pass

    @staticmethod
    def _get_int(phrase='Input: '):
        while True:
            try:
                num = int(input(f'{phrase}'))
            except ValueError:
                print('Invalid input')
            else:
                return num if num >= 0 else print('Invalid input')

    @staticmethod
    def _user_choice(phrase='Input: '):
        while True:
            user_input = input(f'{phrase}').lower()
            if user_input in ['y', 'n']:
                return user_input
            else:
                print('Invalid input')


class Player(AbstractPlayer):
    def __init__(self, name, bank):
        super().__init__()
        self.name = name
        self.bank = bank

    def make_bet(self):
        while True:
            user_bet = self._get_int('Make your bet: ')
            if user_bet <= self.bank:
                self.bank -= user_bet
                self.bet = user_bet
                break
            else:
                print('The bet can`t exceed the size of your bank')

    def ask_cards(self):
        if self.points >= 21:
            return False
        player_choice = self._user_choice('Do you need card?(y/n): ')
        boo = True if player_choice == 'y' else False
        return boo

    def __str__(self):
        return f'Player "{self.name}"'


class Bot(AbstractPlayer):
    def __init__(self, name, bank):
        super().__init__()
        self.name = name
        self.bank = bank
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
