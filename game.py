from cards import *
from players import *


class Game:
    def __init__(self, user_name, bank, players_amount):
        self.deck = Deck()
        self.player = Player(user_name, bank)
