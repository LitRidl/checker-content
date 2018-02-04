#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать количество положительных десятичных чисел в строке, допустимых 16-битными процессорами
256423 53247  d gsffg gds fgsd 325453254325452\nfsdf 61253512567 vdg 187 -324 hxvcbh
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

max_v = 2 ** 16
def check(w):
    try:
        a = int(w)
        if (0 <= a <= max_v):
            return True
    except:
        pass
    return False

for line in stdin:
    res = 0
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    for i in words:
        if check(i):
            res += 1
    print(res)