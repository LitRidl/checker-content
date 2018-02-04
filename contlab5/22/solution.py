#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Закодировать двоичное число азбукой Морзе.
записано беззнаковое число произвольной длины в двоичной системе счисления
последовательность знаков точка и тире, соответствующее заданному числу
0111011
'''

from __future__ import print_function

a = raw_input().strip()

inta = long(a)
newa = str(inta)
result = newa.replace('0', '-----')
result = result.replace('1', '.----')

print("{0} {1}".format(a, result))