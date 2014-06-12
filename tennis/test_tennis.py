import tennis
import unittest

class TestTennis(unittest.TestCase):

    def test_basic(self):
        steffi = tennis.Tennis()
        self.assertEqual(42, steffi.calcTennisScore(42))


if __name__ == '__main__':
    unittest.main()
