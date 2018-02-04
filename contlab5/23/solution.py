#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Умножение двух чисел в кардинальной системе счисления {|}.
через пробел записано два беззнаковых числа произвольной длины в кардинальной системе счисления
число в кардинальной системе счисления, которое является произведением исходных чисел
||| ||
'''
from __future__ import print_function

a, b = raw_input().split()
aCount = a.count("|")
bCount = b.count("|")
aCount -= 1
bCount -= 1

tmp = aCount * bCount
result = "|" * tmp + "|" or "|"

print('{0} {1} {2}'.format(a, b, result))
