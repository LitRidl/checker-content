#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать количество слов, которые являются числами в римской системе сичсления(число, менше 4000)
XVI hjb 46 kjdfg 435 XXXX\nxxx XXX
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def checkio(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result


def rome(rome_str):
    res = 0
    rome_str = rome_str.replace("CM", "DCCCC")
    rome_str = rome_str.replace("CD", "CCCC")
    rome_str = rome_str.replace("XC", "LXXXX")
    rome_str = rome_str.replace("XL", "XXXX")
    rome_str = rome_str.replace("IX", "VIIII")
    rome_str = rome_str.replace("IV", "IIII")
    res += rome_str.count("M") * 1000
    res += rome_str.count("D") * 500
    res += rome_str.count("C") * 100
    res += rome_str.count("L") * 50
    res += rome_str.count("X") * 10
    res += rome_str.count("V") * 5
    res += rome_str.count("I")
    return res

res = 0

words = [w for w in stdin.read().split() if len(w.strip()) > 0]

for i in words:
    if i == checkio(rome(i)):
        res += 1

print(res)
