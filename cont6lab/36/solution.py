#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Натурализация двоичного числа в позиционной записи (перевод в еденичную систему счисления{|}).
записано неотрицательное число в двоичной системе счисление
число, равное исходному, в еденичной системе счисления
1011
'''

from __future__ import print_function


a = raw_input().strip()

inta = long(a, base=2)

result = ""

for i in range(inta):
    result += "|"

print('{0} {1}'.format(a, result))
