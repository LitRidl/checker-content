#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление наибольшего общего делителя двух чисел в натуральной системе счисления.
через пробел записано два числа произвольной длины в натуральной системе счисления {|}
число в натуральной системе счисления, которое является наибольшим общем делителем исходных чисел
||| ||||||
'''

from __future__ import print_function
from fractions import gcd

a, b = raw_input().split()
aCount = a.count("|")
bCount = b.count("|")

GCD = gcd(aCount, bCount)
result = "|" * GCD

print('{0} {1} {2}'.format(a, b, result))
