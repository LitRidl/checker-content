#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Копирование троичного числа со знаком.
записано число произвольной длины в троичной системе счисления
копия исходного числа без ведущих нулей и знака +
-0102221
'''

from __future__ import print_function

olda = raw_input().strip()
a = olda
result = ''
if a[0] == '-':
	result = '-'
	a = a[1:]

result = result + a.lstrip('+').lstrip('0') or '0'

print("{0} {1}".format(olda, result))
