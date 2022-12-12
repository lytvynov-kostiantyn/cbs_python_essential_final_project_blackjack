from time import sleep

from players import *
from cards import *

from random import shuffle
from const import BOT_NAMES, user_choice


class Game:
    def __init__(self, user_name, bank):
        self.deck = Deck()
        self.player = Player(user_name, bank)
        self.dealer = Dealer(None, bank * 5)
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
            player.make_bet()
            print(f'{player} bets: {player.bet}$')

    @staticmethod
    def print_cards_points(player):
        print(f'{player} has {player.points} points')
        print('His cards: {}'.format(', '.join(map(str, player.cards))))

    # getting first cards for each player
    def get_card(self, player):
        card = self.deck.get_card()
        player.take_card(card)

    def checking_points(self):
        if len(self.dealer.cards) == 1:
            for player in self.players:
                if player.points == 21:
                    print(f'{player} has blackjack!')
                    if self.dealer.points < 10:
                        player.bank += player.bet * 2.5
                        print(f'{player} get 1.5 x bet to his bank!')
                        player.end_round()
                    else:
                        if isinstance(player, Bot):
                            player_choice = random.choice(['y', 'n'])
                        else:
                            print('You can take your prize(1xbet) now or wait dealer second card and win 1.5xbet')
                            player_choice = user_choice('Want to continue("y"/"n"): ')
                        match player_choice:
                            case 'y':
                                print(f'{player} decide to wait dealers second card!')
                            case 'n':
                                player.bank += player.bet * 2
                                print(f'{player} gets 1xbet to his bank!')
                                player.end_round()
        else:
            pass

    def add_cards(self, player):
        while player.ask_cards():
            sleep(2)
            self.get_card(player)
            self.print_cards_points(player)
            print('-' * 60)

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
                self.get_card(player)

        # getting 1 card for dealer
        self.get_card(self.dealer)

        # printing all cards and points for each player
        for player in self.players:
            self.print_cards_points(player)
        print('-' * 60)

        # printing all cards and points for dealer
        self.print_cards_points(self.dealer)
        print('-' * 60)

        # checking players points
        self.checking_points()

        for player in self.players:
            if player.bet != 0 or player.points != 21:
                self.add_cards(player)

        # printing all cards and points for each player
        for player in self.players:
            self.print_cards_points(player)
        print('-' * 60)

