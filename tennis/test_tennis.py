
import tennis
import unittest

class TestTennis(unittest.TestCase):

    game = tennis.Tennis()

    def test_score1(self):   
        self.assertEqual('love', self.game.getScore(0))

    def test_score2(self):   
        self.assertEqual('fifteen', self.game.getScore(1))

    def test_score3(self):   
        self.assertEqual('thirty', self.game.getScore(2))

    def test_score4(self):   
        self.assertEqual("fourty", self.game.getScore(3))





if __name__ == '__main__':
    unittest.main()
