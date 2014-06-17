
import tennis
import unittest

class TestTennis(unittest.TestCase):

    player_1 = "Steffi"
    player_2 = "Boris"

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
        player_id = 0
        self.assertEqual(self.player_1, self.game.getName(player_id))

    def test_PlayerNames2(self):
        player_id = 1
        self.assertEqual(self.player_2, self.game.getName(player_id))

    def test_getCurrentScore(self):
        self.assertEqual("love-love", self.game.getCurrentResult())




if __name__ == '__main__':
    unittest.main()
