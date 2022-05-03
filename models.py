import random
from exceptoins import EnemyDown, GameOver
from score import Score
from settings import valid_choices


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = 1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives < 1:
            Score.add_score(self.name, self.score)
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

    def attack(self, enemy_obj):
        attack = None
        while attack not in valid_choices:
            try:
                attack = int(input('Choose your fighter to attack (Warrior(1), Rogue(2), Wizard(3)): '))
            except ValueError:
                print('You can type only 1, 2 or 3')
        defense = enemy_obj.enemy_choice()
        result_of_fight = self.fight(attack, defense)
        if result_of_fight == 0:
            print("It's a draw!")
        elif result_of_fight == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        elif result_of_fight == -1:
            print("You missed!")

    def defense(self, enemy_obj):
        defense = None
        while defense not in valid_choices:
            try:
                defense = int(input('Choose your fighter to defense (Warrior(1), Rogue(2), Wizard(3)): '))
            except ValueError:
                print('You can type only 1, 2 or 3')
        attack = enemy_obj.enemy_choice()
        result_of_fight = self.fight(attack, defense)
        if result_of_fight == 0:
            print("It's a draw!")
        elif result_of_fight == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        elif result_of_fight == -1:
            print("Enemy missed!")


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def enemy_choice():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives < 1:
            raise EnemyDown()
