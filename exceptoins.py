class EnemyDown(Exception):
    pass
class GameOver(Exception):
    def __init__(self, score, name):
        with open('score.txt', 'rw') as lead_score:

        leaderboard = {}

class WrongName(Exception):
    pass
