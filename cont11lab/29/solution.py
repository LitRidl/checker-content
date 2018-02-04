#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
удалить десятичные числа, не превышающие INT_MAX
2147483647 2147483648 av 21bh\n-2334345455 vvvAQ5\n9999999999
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

INT_MAX = 2 ** 31 - 1

def check(w):
    try:
        a = long(w)
        if (a > INT_MAX):
            return True
    except:
        pass
    return False

for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(w for w in words))