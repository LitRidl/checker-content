#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Проверить палиндромию двоичного числа.
записано беззнаковое число произвольной длины в двоичной системе счисления
0 -- если не палиндром, 1 -- если палиндром
11011
'''
from __future__ import print_function

num = raw_input().strip()
tmp = num[::-1]
result = 0
if tmp == num:
  result = 1
else:
  result = 0

print("{0} {1}".format(num, result))
