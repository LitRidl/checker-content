from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr
import sys

alf = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def test():
    test_idx = 2
    for i in range(111):
        t1 = ""
        t = ""
        for i in range(randint(1, 100)):
            t += choice(alf)
        if (randint(0, 1) == 1):
            n1 = randint(0, len(t))
            n2 = randint(n1, len(t))
            t1 = t[n1 : n2]
        else:
            for i in range(randint(0, 100)):
                t1 += choice(alf)

        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(t1 + " " + t)
            test_idx += 1

if __name__ == '__main__':
    test()