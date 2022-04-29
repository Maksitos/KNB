import random
from exceptoins import EnemyDown, GameOver
from settings import Settings
settings = Settings()


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = settings.player_lives

    @staticmethod
    def fight(attack, defense):


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
