from time import sleep

from players import *
from cards import *

from random import shuffle
from const import BOT_NAMES, user_choice
from math import ceil


class Game:
    def __init__(self, user_name, bank):
        self.deck = Deck()
        self.player = Player(user_name, bank)
        self.dealer = Dealer(None, None)
        self.players = []
        self.min_bet, self.max_bet = 1, bank

    def _add_bots(self, bots_amount, bank):
        for i in range(bots_amount):
            bot = Bot(BOT_NAMES[i], random.randint(5, bank))
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

    def first_round_check(self, players_in_game):
        boo = players_in_game
        for player in players_in_game:
            if player.points == 21:
                print(f'{player} has blackjack!')
                if self.dealer.points < 10:
                    player.bank += player.bet * 2.5
                    print(f'{player} get 1.5xbet to his bank!')
                    print('-' * 90)
                    boo.remove(player)
                else:
                    if isinstance(player, Bot):
                        player_choice = random.choice(['y', 'n'])
                    else:
                        print('You can take your prize(1xbet) now or wait dealer second card and win 1.5xbet')
                        player_choice = user_choice('Want to continue?(y/n): ')
                    match player_choice:
                        case 'y':
                            print(f'{player} decide to wait dealers second card!')
                            print('-' * 90)
                        case 'n':
                            player.bank += player.bet * 2
                            print(f'{player} gets 1xbet to his bank!')
                            print('-' * 90)
                            boo.remove(player)
        return boo

    @staticmethod
    def second_round_check(players_in_game):
        boo = players_in_game
        for player in players_in_game:
            if player.points > 21:
                print(f'{player} lose his bet!')
                boo.remove(player)
        return boo

    def add_cards(self, player):
        while player.ask_cards():
            sleep(2)
            self.get_card(player)
            self.print_cards_points(player)

    def get_result(self, players_in_game):
        if self.dealer.points > 21:
            for player in players_in_game:
                player.bank += player.bet * 2.5
                print(f'{player} win and get 1.5xbet to his bank!')
        else:
            for player in players_in_game:
                if player.points > self.dealer.points:
                    player.bank += player.bet * 2.5
                    print(f'{player} win and get 1.5xbet to his bank!')
                elif player.points < self.dealer.points:
                    print(f'{player} lose his bet!')
                else:
                    player.bank += player.bet
                    print(f'{player} get his bet back!')

    @staticmethod
    def restart(player):
        player.points = 0
        player.cards = []
        player.bet = None

    def start_game(self, bots_amount):
        # Adding players to the game
        self._add_bots(bots_amount, self.player.bank)
        print('-' * 90)

        self.players.append(self.player)
        shuffle(self.players)

        while True:
            # list with players that still in game
            players_in_game = [i for i in self.players]

            # Players making bets
            self.ask_bet()
            print('-' * 90)

            # getting first 2 cards for each player
            sleep(3)
            for player in players_in_game:
                for _ in range(2):
                    self.get_card(player)

            # getting 1 card for dealer
            self.get_card(self.dealer)

            # printing all cards and points for each player
            print('First leg:'.center(90, ' '))
            for player in players_in_game:
                self.print_cards_points(player)
            print('-' * 90)

            # printing all cards and points for dealer
            self.print_cards_points(self.dealer)
            print('-' * 90)

            # checking players points
            players_in_game = self.first_round_check(players_in_game)

            print('Players takes the cards:'.center(90, ' '))

            # adding cards to players
            for player in players_in_game:
                self.add_cards(player)
            print('-' * 90)

            # checking players points
            players_in_game = self.second_round_check(players_in_game)

            print('-' * 90)
            print('Dealer takes the cards:'.center(90, ' '))

            # adding cards to dealer
            self.add_cards(self.dealer)
            print('-' * 90)

            # printing all cards and points for each player
            print('Second leg:'.center(90, ' '))
            for player in players_in_game:
                self.print_cards_points(player)
            print('-' * 90)

            # printing all cards and points for dealer
            self.print_cards_points(self.dealer)
            print('-' * 90)

            # Getting results of the game
            self.get_result(players_in_game)
            print('-' * 90)

            # Rounding and printing players bank
            print('Players bank after the game:'.center(90, ' '))
            for player in self.players:
                player.bank = ceil(player.bank)
                print(f'{player} has {player.bank}$')
            print('-' * 90)

            if self.player.bank == 0:
                print('Sorry but you lose all your money:(')
                exit(0)
            else:
                choice = user_choice('Want to play again?(y/n): ')
                if choice == 'n':
                    print('We hope you like to play with us:)')
                    break
                else:
                    # Deleting players with empty bank
                    self.players = [i for i in self.players if i.bank != 0]

                    # Clear story of last game
                    for player in self.players:
                        self.restart(player)
                    self.restart(self.dealer)
