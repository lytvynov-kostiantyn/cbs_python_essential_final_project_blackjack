from time import sleep

from players import *
from cards import *

from random import shuffle
from const import BOT_NAMES, MAX_PLAYERS
from math import ceil


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = None
        self.dealer = Dealer()
        self.players = []
        self.min_bet, self.max_bet = 1, None

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
        # Change ace value
        if card.rank == 'A':
            if isinstance(player, Player):
                # If user have 10 points this change make no sens
                if player.points != 10:
                    print('You get Ace and you can choice Ase points value: 11 or 1.')
                    player_choice = self._user_choice('Count Ase as 11 points?(y/n): ')
                    card.points = 11 if player_choice == 'y' else 1

            # If bot or dealer already have 11 points or more, ace value will be 1 point
            else:
                if player.points > 10:
                    card.points = 1
        player.take_card(card)

    @staticmethod
    def blackjack(player):
        player.bank += player.bet * 2.5
        print(f'{player} win and get 1.5xbet to his bank!')

    @staticmethod
    def player_win(player):
        player.bank += player.bet * 2
        print(f'{player} win and get 1xbet to his bank!')

    @staticmethod
    def player_lose(player):
        print(f'{player} lose his bet!')

    @staticmethod
    def draw(player):
        player.bank += player.bet
        print(f'{player} get his bet back!')

    def first_round_check(self, players_in_game):
        boo = [i for i in players_in_game]
        for player in players_in_game:
            if player.points == 21:
                print(f'{player} has blackjack!')
                if self.dealer.points < 10:
                    self.blackjack(player)
                    print('-' * 90)
                    boo.remove(player)
                else:
                    if isinstance(player, Bot):
                        player_choice = random.choice(['y', 'n'])
                    else:
                        print('You can take your prize 1xbet now or wait dealer second card and win 1.5xbet')
                        player_choice = self._user_choice('Want to continue?(y/n): ')
                    match player_choice:
                        case 'y':
                            print(f'{player} decide to wait dealers second card!')
                            print('-' * 90)
                        case 'n':
                            self.player_win(player)
                            print('-' * 90)
                            boo.remove(player)
        return boo

    def second_round_check(self, players_in_game):
        boo = [i for i in players_in_game]
        for player in players_in_game:
            if player.points > 21:
                self.player_lose(player)
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
                sleep(2)
                # If player have blackjack
                if player.points == 21 and len(player.cards) == 2:
                    self.blackjack(player)

                # If player have <= 21
                else:
                    self.player_win(player)

        # If dealer have blackjack
        elif self.dealer.points == 21 and len(self.dealer.cards) == 2:
            for player in players_in_game:
                sleep(2)
                # And player have blackjack
                if player.points == 21 and len(player.cards) == 2:
                    self.draw(player)

                # And player have <= 21
                else:
                    self.player_lose(player)

        # If dealer have <= 21
        else:
            for player in players_in_game:
                sleep(2)
                # If player have blackjack
                if player.points == 21 and len(player.cards) == 2:
                    self.blackjack(player)

                # If player have more than dealer
                elif player.points > self.dealer.points:
                    self.player_win(player)

                # If dealer have more than player
                elif player.points < self.dealer.points:
                    self.player_lose(player)

                # If draw
                else:
                    self.draw(player)

    @staticmethod
    def restart(player):
        player.points = 0
        player.cards = []
        player.bet = None

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

    def start_game(self):
        print('Welcome to cbs blackjack!'.center(90, '-'))

        # Getting name from user
        user_name = input('Your name: ')
        if not user_name:
            user_name = 'User'

        # Get size of user bank
        bank = self._get_int('Your bank: ')
        if bank < 5:
            print("Sorry, but you can't play with less than 5$")
            exit(0)

        # Create user and update size of max bet
        self.player = Player(user_name, bank)
        self.max_bet = bank

        # Get bots amount from user
        while True:
            bots_amount = self._get_int(f'The number of players (max: {MAX_PLAYERS - 1}): ')
            if bots_amount <= MAX_PLAYERS - 1:
                break
            else:
                print('Invalid input')
        print('-' * 90)

        # Adding players to the game
        self._add_bots(bots_amount, self.player.bank)
        print('-' * 90)

        # Adding user to the game and shuffle the list
        self.players.append(self.player)
        shuffle(self.players)

        while True:
            # list with players that still in game
            players_in_game = [i for i in self.players]

            # Players making bets
            print('Players bets:'.center(90, ' '))
            self.ask_bet()
            print('-' * 90)

            # getting first 2 cards for each player
            for player in players_in_game:
                for _ in range(2):
                    self.get_card(player)

            # getting 1 card for dealer
            self.get_card(self.dealer)

            # printing all cards and points for each player
            print('First hand:'.center(90, ' '))
            for player in players_in_game:
                sleep(2)
                self.print_cards_points(player)
            print('-' * 90)

            # printing all cards and points for dealer
            sleep(2)
            self.print_cards_points(self.dealer)
            print('-' * 90)

            # checking players points
            players_in_game = self.first_round_check(players_in_game)

            print('Players take cards:'.center(90, ' '))

            # adding cards to players
            for player in players_in_game:
                self.add_cards(player)
            print('-' * 90)

            # checking players points
            players_in_game = self.second_round_check(players_in_game)

            if len(players_in_game) != 0:
                print('-' * 90)
                print('Dealer take cards:'.center(90, ' '))

                # adding cards to dealer
                self.add_cards(self.dealer)
                print('-' * 90)

                # printing all cards and points for each player
                print('Second hand:'.center(90, ' '))
                for player in players_in_game:
                    sleep(2)
                    self.print_cards_points(player)
                print('-' * 90)

                # printing all cards and points for dealer
                sleep(2)
                self.print_cards_points(self.dealer)
                print('-' * 90)

                # Getting results of the game
                sleep(2)
                print('Final results:'.center(90, ' '))
                self.get_result(players_in_game)
                print('-' * 90)

            # Rounding and printing players bank
            sleep(2)
            print('Players bank after the game:'.center(90, ' '))
            for player in self.players:
                player.bank = ceil(player.bank)
                print(f'{player} has {player.bank}$')
            print('-' * 90)

            if self.player.bank == 0:
                print('Sorry, but you lost all your money:(')
                exit(0)
            else:
                choice = self._user_choice('Want to play again?(y/n): ')
                print('-' * 90)
                if choice == 'n':
                    print('We hope you liked playing with us:)')
                    break
                else:
                    # Deleting players with empty bank
                    self.players = [i for i in self.players if i.bank != 0]

                    # Clear story of last game
                    for player in self.players:
                        self.restart(player)
                    self.restart(self.dealer)

                    # Create a new deck
                    self.deck = Deck()
