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
    if bank < 5:
        print("Sorry but you cant play with less than 5$")
        exit(0)
    while True:
        bots_amount = get_int(f'Players num (max: {MAX_PLAYERS - 1}): ')
        if bots_amount <= MAX_PLAYERS - 1:
            break
        else:
            print('Invalid input')
    print('-' * 60)

    game = Game(user_name, bank)
    game.start_game(bots_amount)
