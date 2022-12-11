from time import sleep

from players import *
from cards import *

from random import shuffle
from const import BOT_NAMES


class Game:
    def __init__(self, user_name, bank):
        self.deck = Deck()
        self.player = Player(user_name, bank)
        self.dealer = Dealer(None, bank * 10)
        self.players = []
        self.min_bet, self.max_bet = 1, bank

    def _add_bots(self, bots_amount, bank):
        for _ in range(bots_amount):
            name = random.choice(BOT_NAMES)
            bot = Bot(name, random.randint(5, bank))
            print(f'{bot} with {bot.bank}$ bank is created')
            self.players.append(bot)

    def ask_bet(self):
        for player in self.players:
            print(f'{player} bets: {player.make_bet()}$')

    def print_cards_points(self):
        for player in self.players:
            print(f'{player} has {player.points} points')
            print('His cards: {}'.format(', '.join(map(str, player.cards))))

    def print_dealer_cards_points(self):
        print(f'{self.dealer} has {self.dealer.points} points')
        print('His cards: {}'.format(', '.join(map(str, self.dealer.cards))))

    def start_game(self, bots_amount):
        # Adding players to the game
        self._add_bots(bots_amount, self.player.bank)
        print('-' * 60)

        self.players.append(self.player)
        shuffle(self.players)

        # Players making bets
        self.ask_bet()
        print('-' * 60)

        # getting first 2 cards for each player
        sleep(3)
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

        # getting 1 card for dealer
        dealer_card = self.deck.get_card()
        self.dealer.take_card(dealer_card)

        # printing all cards and points for each player
        self.print_cards_points()
        print('-' * 60)

        # printing all cards and points for dealer
        self.print_dealer_cards_points()
        print('-' * 60)

