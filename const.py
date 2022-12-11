MAX_PLAYERS = 7

SUITS = ['Heart', 'Diamond', 'Club', 'Spade']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

BOT_NAMES = ['Jon', 'Tom', 'Bob', 'Anna', 'May']


def get_int(phrase='Input: '):
    while True:
        try:
            num = int(input(f'{phrase}'))
        except ValueError:
            print('Invalid input')
        else:
            return num if num >= 0 else print('Invalid input')
