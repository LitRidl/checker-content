#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Обмен местами двух двоичных чисел.
через пробел записано два числа произвольной длины в двоичной системе счисления
два двоичных исходных числа, поменянные местами
11010 111011
'''

from __future__ import print_function

a, b = raw_input().split()

print("{0} {1} {2} {3}".format(a, b, b, a))
