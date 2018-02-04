#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
удалить десятичные числа, превышающие INT_MAX
24456 35454 2132324454\45nsdgfdg fgfdh 2341
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

INT_MAX = 2 ** 31 - 1

def check(w):
    try:
        a = long(w)
        if (a <= INT_MAX):
            return True
    except:
        pass
    return False

for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(w for w in words))