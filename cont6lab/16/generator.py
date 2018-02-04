from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr
import sys

alf = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def test():
    test_idx = 2
    for i in range(111):
        t = ""
        for i in range(randint(0, 100)):
            t += choice(alf)
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(t)
            test_idx += 1

if __name__ == '__main__':
    test()