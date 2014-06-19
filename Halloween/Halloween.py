__author__ = 'claude'

import sys
import math
import itertools

from math import factorial

class Halloween(object):


    def __init__(self):
        pass

    def compute_output(self):
        num_list = self.readTestNumber()
        v = [((i / 2) * ((i + 1) / 2)) for i in num_list]
        for i in v:
            print i
        return v


    def getPrimes(self, num):
        nn = 0
        for i in range(2,num+1):
            if self.isPrime(i):
                nn += 1

        return nn


    def isPrime(self, num):
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True

    def getMax4s(self, num):
        return num/4

    def getLists(self, num):
        fours = self.getMax4s(num)
        poss_list = []
        for i in range(1, fours+1):
            poss_list.append([i, (num-(4*i))])
        return poss_list

    def getNumPerms(self, num):
        poss_lists = self.getLists(num)
        perms = [(factorial(x+y)/((factorial(x))*(factorial(y)))) for (x,y) in poss_lists]
        return sum(perms)+1

    def solve_MurderCase(self, num):
        num_perm = self.getNumPerms(num)
        return self.getPrimes(num_perm)

    def run_all(self):
        lines = sys.stdin.readlines()
        for i in lines[1:]:
            print self.solve_MurderCase(int(i))

if __name__ == '__main__':
    Halloween = Halloween()
    Halloween.run_all()

