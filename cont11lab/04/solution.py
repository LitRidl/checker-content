#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Подсчитать колическтво полнотетрадных (со всеми необходимыми ведущими нулями) двоичнокодированных десятичных чисел (BCD - Binary Coded Decimal)
hello 01010111\n1011 world 2134
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


words = [w.lower() for w in stdin.read().split() if len(w.strip()) > 0]

words_asc = 0

words = [w for w in words if (len(w) % 4 == 0)]

res = 0

for i in words:
        j = 0
        can = True
        while (j + 4 < len(i) + 1):
            try:
                a = int(i[j: j + 4], base=2)
                if (a > 9):
                    can = False
                    break
            except:
                can = False
                break
            j += 4
        if can:
            res += 1


print(res)
