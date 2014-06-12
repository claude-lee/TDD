class Tennis:

    scores = {0: "love", 1:"fifteen", 2:"thirty", 3:"fourty"}

    def getScore(self, num):
        return self.scores.get(num)
