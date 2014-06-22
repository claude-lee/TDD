
import tennis
import unittest

class TestTennis(unittest.TestCase):

    name_1 = "Steffi"
    name_2 = "Boris"
    player_1 = tennis.Player(name_1)
    player_2 = tennis.Player(name_2)
    game = tennis.Tennis(player_1, player_2)

    def test_score1(self):   
        self.assertEqual('love', self.game.getScore(0))

    def test_score2(self):   
        self.assertEqual('fifteen', self.game.getScore(1))

    def test_score3(self):   
        self.assertEqual('thirty', self.game.getScore(2))

    def test_score4(self):   
        self.assertEqual("forty", self.game.getScore(3))

    def test_PlayerNames1(self):
        self.assertEqual(self.name_1, self.game.player_1.getname())

    def test_PlayerNames2(self):
        self.assertEqual(self.name_2, self.game.player_2.getname())

    def test_getCurrentScore(self):
        self.assertEqual("love-love", self.game.getCurrentGameScore())

    def test_increaseScore(self):
        self.player_2.scorePoint()
        self.assertEqual("love-fifteen", self.game.getCurrentGameScore())

    def test_scoreWithAdvantage(self):
        self.player_1.setScore(3)
        self.player_2.setScore(4)
        self.assertEqual("Advantage " + self.name_2, self.game.getCurrentGameScore())




if __name__ == '__main__':
    unittest.main()
