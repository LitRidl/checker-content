#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Проверка арифметической прогрессии трех десятичных чисел
записаны через пробел три десятичных числа
0 или 1 -- результат проверки
2 4 6
'''

from __future__ import print_function

a, b, c = raw_input().strip().split()

inta = long(a)
intb = long(b)
intc = long(c)

result = 0
if (intb - inta == intc - intb):
    result = 1


print('{0} {1} {2} {3}'.format(a, b, c, result))