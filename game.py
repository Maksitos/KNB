from exceptoins import WrongName, GameOver, EnemyDown
from settings import Settings
from models import Player, Enemy

settings = Settings()


def get_name() -> str:
    try:
        full_name = input('Enter your name: ')
        for i in full_name:
            if i not in settings.valid_characters:
                raise WrongName
        if len(full_name) > 16 or len(full_name) < 3:
            raise WrongName
    except WrongName:
        print(f'Wrong name!The name shall be at least 3-16 characters long. \n'
              f'Spaces and special characters are not permitted. Only a-z, A-Z, 0-9.')
        return get_name()
    return full_name


def play():
    user_name = get_name()
    player = Player(user_name)
    enemy_level = 1
    enemy = Enemy(enemy_level)
    attack_or_defense = 1
    while True:
        try:
            print('Enemy(' + '0' * enemy.enemy_lives + ')\n'
                  'VS\n'
                  f'{player.name}(' + '0' * player.lives + ')\n'
                  + f'Your score:{player.score}')
            if attack_or_defense == 1:
                player.attack(enemy)
                attack_or_defense *= -1
            elif attack_or_defense == -1:
                player.defense(enemy)
                attack_or_defense *= -1
        except EnemyDown:
            enemy_level += 1
            enemy = Enemy(enemy_level)
            player.score += 5
            attack_or_defense *= 1
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
