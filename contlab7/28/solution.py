#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм, восстанавливающий целое шестнадцатеричное число по его обратному коду.
Входное слово представляет собой обратный код целого шестнадцатеричного числа (возможно, с ведущими нулями).
шестнадцатеричное число, восстановленное из исходного
DEADBEEF
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=16)
alen = len(base_repr(inta, base=16))

if long(a[0], base=16) > 7:
    result = inta - 16 ** alen + 1
else:
    result = inta

result = base_repr(result, base=16)

print("{0}".format(result))
