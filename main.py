from game import Game

from const import MAX_PLAYERS, get_int


if __name__ == '__main__':
    print('Welcome to cbs blackjack!'.center(90, '-'))
    '''
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
    '''
    print('-' * 90)

    user_name = 'test'
    bank = 20
    bots_amount = 3

    game = Game(user_name, bank)
    game.start_game(bots_amount)
