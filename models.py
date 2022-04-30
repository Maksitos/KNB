import random
from exceptoins import EnemyDown, GameOver
from settings import Settings


settings = Settings()


def choice_validator(func):
    def validator(*args):
        try:
            func(*args)
        except ValueError:
            print('You can type only 1, 2 or 3')
            func(*args)
    return validator


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = settings.player_lives

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    @staticmethod
    def fight(attack: int, defense: int) -> int:
        if attack == defense:
            return 0
        elif attack == 1 and defense == 2:
            return 1
        elif attack == 2 and defense == 3:
            return 1
        elif attack == 3 and defense == 1:
            return 1
        else:
            return -1

    @choice_validator
    def attack(self, enemy_obj):
        attack = int(input('Choose your fighter to attack (Warrior(1), Rogue(2), Wizard(3)): '))
        if attack not in [1, 2, 3]:
            print('You can type only 1, 2 or 3')
            Player.attack(self, enemy_obj)
        defense = enemy_obj.enemy_choice()
        result_of_fight = Player.fight(attack, defense)
        if result_of_fight == 0:
            print("It's a draw!")
        elif result_of_fight == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        elif result_of_fight == -1:
            print("You missed!")

    @choice_validator
    def defense(self, enemy_obj):
        defense = int(input('Choose your fighter to defense (Warrior(1), Rogue(2), Wizard(3)): '))
        if defense not in [1, 2, 3]:
            print('You can type only 1, 2 or 3')
            Player.defense(self, enemy_obj)
        attack = enemy_obj.enemy_choice()
        result_of_fight = Player.fight(attack, defense)
        if result_of_fight == 0:
            print("It's a draw!")
        elif result_of_fight == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        elif result_of_fight == -1:
            print("Enemy missed!")


class Enemy:
    def __init__(self, level):
        self.enemy_lives = level

    @staticmethod
    def enemy_choice():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.enemy_lives -= 1
        if self.enemy_lives == 0:
            raise EnemyDown()
