#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Натурализация числа в римской записи
записано число в римской записи меньше 4000
число в еденичной системе счисления(натуральной)
XIV
'''

from __future__ import print_function

a = raw_input().strip()

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


result = ""
for i in range(rome(a)):
    result += "|"

print('{0} {1}'.format(a, result))