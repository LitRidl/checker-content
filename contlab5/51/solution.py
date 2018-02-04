#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Проверка делимости на 9.
записано целое беззнаковое число произвольной длины в десятичной системе счисления
0 -- если не делится, 1 -- если делится
648
'''

from __future__ import print_function

a = raw_input().strip()
inta = long(a, base=10)

result = int(inta % 9 == 0)

print("{0} {1}".format(a, result))
