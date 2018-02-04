#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
вычислить дополнительный десятичный код
123456
'''

from __future__ import print_function
from sys import stdin, stdout

def convert(a):
    a = int(a, 10)
    if a > 0:
        return a
    else:
        res = 99999999 + a + 1
        return res

words = stdin.read().strip().split()

for word in words:
    print(convert(word))