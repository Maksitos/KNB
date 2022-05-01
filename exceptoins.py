class EnemyDown(Exception):
    pass


class GameOver(Exception):
    @staticmethod
    def add_score(name: str, score: int):
        with open('scores.txt', 'r') as lead_score:
            leaderboard = [line.rstrip('\n') for line in lead_score]
        with open('scores.txt', 'w') as lead_score:
            leaderboard.append(name + ' ' + str(score))
            leaderboard = Score.ten_best(leaderboard)
            for place in leaderboard:
                lead_score.write(place + '\n')


class WrongName(Exception):
    pass


class Score:

    @staticmethod
    def score_definition(place: str) -> int:
        place = place.split()
        return int(place[1])

    @staticmethod
    def ten_best(board: list[str]) -> list[str]:
        return sorted(board, key=Score.score_definition, reverse=True)[:9]
