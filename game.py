import random

from cards import *
from players import *


class Game:
    def __init__(self, user_name, bank):
        self.deck = Deck()
        self.player = Player(user_name, bank)
        self.players = []
        self.max_bet, self.min_bet = bank, 1

    def _add_bots(self, bots_amount, bank):
        for _ in range(bots_amount):
            name = random.choice(['Jon', 'Tom', 'Bob', 'Anna', 'May'])
            bot = Bot(name, random.randint(5, bank))
            print(bot)
            self.players.append(bot)
        print('-' * 60)

    def start_game(self, bots_amount):
        # Adding players to the game
        self._add_bots(bots_amount, self.player.bank)
        self.players.append(self.player)

        # getting first 2 cards for each player
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                self.player.take_card(card)







