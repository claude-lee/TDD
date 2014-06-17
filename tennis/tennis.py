
class Tennis:

    def __init__(self, player_1 = "Hanni", player_2 = "Nanni"):
        self.name_player_1 = player_1
        self.name_player_2 = player_2
        self.score_player_1 = 0
        self.score_player_2 = 0

    scores = {0: "love", 1:"fifteen", 2:"thirty", 3:"forty", 4:"advantage"}

    def getScore(self, num):
        return self.scores.get(num)

    def getName(self, player_id):
        return self.name_player_2 if player_id else self.name_player_1


    def getCurrentResult(self):
        return self.scores.get(self.score_player_1) + '-' + self.scores.get(self.score_player_2)
