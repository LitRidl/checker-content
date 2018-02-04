#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление наименьшего общего кратного двух чисел в натуральной системе счисления.
через пробел записано два числа произвольной длины в натуральной системе счисления {|}
число в натуральной системе счисления, которое является наименьшим общим кратным исходных чисел
||| ||||||
'''

from __future__ import print_function
from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

a, b = raw_input().split()
aCount = a.count("|")
bCount = b.count("|")

LCM = lcm(aCount, bCount)
result = "|" * LCM

print('{0} {1} {2}'.format(a, b, result))
