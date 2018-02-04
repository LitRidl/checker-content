#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм перевода четверичного числа в шестнадцатеричную систему счисления.
Входное слово представляет собой беззнаковое четверичное число (возможно, с ведущими нулями).
шестнадцатеричное число, равное исходному четверичному, без ведущих нулей
01231
'''

from __future__ import print_function
from numpy import base_repr

a = long(raw_input().strip(), base=4)
result = base_repr(a, base=16)

print('{0}'.format(result))
