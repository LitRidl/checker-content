#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
выделить все шестнадцатеричные числа имеющие максимальное число цифр в 32-битной архитектуре
sdfdsg3v hdsfbsd 34 hxhf 324\nAAEC236D
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def check(w):
    try:
        a = long(w, base = 16)
        if (len(w) == 8):
            return True
    except:
        pass
    return False

for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(w for w in words))