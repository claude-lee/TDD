import unittest
import Halloween


class TestHalloween(unittest.TestCase):



    halloween = Halloween.Halloween()
    #
    # def test_1(self):
    #     self.assertEqual([4,7,9], self.halloween.readTestNumber())

    # def test_output(self):
    #     self.assertEqual([4, 12 , 20], self.halloween.compute_output())



    def test_prime(self):
        self.assertEqual([2,3], self.halloween.getPrimes(3))

    def test_isPrime(self):
        self.assertEqual(True, self.halloween.isPrime(3))

    def test_isPrime2(self):
        self.assertEqual(False, self.halloween.isPrime(4))

    def test_getMaxNumber4s(self):
        self.assertEqual(1, self.halloween.getMax4s(5))

    def test_getLists(self):
        self.assertEqual([[4,1]], self.halloween.getLists(5))

    def test_getLists2(self):
        self.assertEqual([[4,1,1]], self.halloween.getLists(6))
        self.assertEqual([[4,1,1,1,1,1], [4,4,1]], self.halloween.getLists(9))

    def test_calcPerm(self):
        self.assertEqual(5, self.halloween.getNumPerms(7))

    def test_murder(self):
        self.assertEqual(3, self.halloween.solve_MurderCase(7))


if __name__ == '__main__':
    unittest.main()