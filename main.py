from game import Game

MAX_PLAYERS = 7


def get_int(phrase='Input: '):
    while True:
        try:
            num = int(input(f'{phrase}'))
        except ValueError:
            print('Invalid input')
        else:
            return num if num >= 0 else print('Invalid input')


if __name__ == '__main__':
    print('Welcome to cbs blackjack!'.center(60, '_'))
    user_name = input('Your name: ')
    if len(user_name) == 0:
        user_name = 'User'
    bank = get_int('Your bank: ')
    if bank == 0:
        print("Sorry but we dont play in ")
        exit(0)
    while True:
        players_amount = get_int(f'Players num (max: {MAX_PLAYERS - 1}): ')
        if players_amount <= MAX_PLAYERS - 1:
            break
        else:
            print('Invalid input')
    print('-' * 60)

    game = Game(user_name, bank, players_amount)

