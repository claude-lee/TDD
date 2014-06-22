
class Tennis:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    scores = {0: "love", 1:"fifteen", 2:"thirty", 3:"forty", 4:"advantage", 5:"deuce"}

    def getScore(self, num):
        return self.scores.get(num)

    def getCurrentGameScore(self):
        return self.scores.get(self.player_1.getscore()) + '-' + self.scores.get(self.player_2.getscore())


class Player:

    def __init__(self, name = "Hanni"):
        self.name = name
        self.score = 0

    def getname(self):
        return self.name

    def getscore(self):
        return self.score

    def scorePoint(self):
        self.score += 1


