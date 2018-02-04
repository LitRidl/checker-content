#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм перевода числа из девятеричной системы счисления в троичную.
Входное слово представляет собой беззнаковое девятеричное число (возможно, с ведущими нулями).
троичное число, равное исходному девятериному, без ведущих нулей
00183276
'''

from __future__ import print_function
from numpy import base_repr

a = long(raw_input().strip(), base=9)
result = base_repr(a, base=3)

print('{0}'.format(result))
