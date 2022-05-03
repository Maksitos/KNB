from exceptoins import GameOver, EnemyDown
from models import Player, Enemy
import string

valid_characters = string.ascii_letters + '1234567890'


def get_name() -> str:
    full_name = input('Enter your name: ')
    if all([i in valid_characters for i in full_name]) and 3 <= len(full_name) <= 16:
        return full_name
    else:
        print(f'Wrong name!The name shall be at least 3-16 characters long. \n'
              f'Spaces and special characters are not permitted. Only a-z, A-Z, 0-9.')
        return get_name()


def confrontation_display(enemy_lives, player_name, player_lives, player_score):
    print('Enemy(' + '0' * enemy_lives + ')\n'
          'VS\n'
          f'{player_name}(' + '0' * player_lives + ')\n'
          + f'Your score:{player_score}')


def play():
    user_name = get_name()
    player = Player(user_name)
    enemy_level = 1
    enemy = Enemy(enemy_level)
    while True:
        try:
            confrontation_display(enemy.enemy_lives, player.name, player.lives, player.score)
            player.attack(enemy)
            confrontation_display(enemy.enemy_lives, player.name, player.lives, player.score)
            player.defense(enemy)
        except EnemyDown:
            enemy_level += 1
            enemy = Enemy(enemy_level)
            player.score += 5
            print('This enemy is down. Score +5.')


def show_scores():
    with open('scores.txt', 'r') as scores:
        for line in scores:
            print(line)


menu = {'show scores': show_scores, 'play': play, 'exit': exit}


if __name__ == '__main__':
    while True:
        try:
            user_input = input('Menu(play, show scores, exit): ')
            menu[user_input]()
        except GameOver:
            print('Game Over')
        except KeyError:
            print('You can only choose what is on the menu.')
        except KeyboardInterrupt:
            pass
