#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм перевода числа из троичной системы счисления в девятеричную.
Входное слово представляет собой беззнаковое троичное число (возможно, с ведущими нулями).
девятеричное число, равное исходному троичному, без ведущих нулей
012212
'''

from __future__ import print_function
from numpy import base_repr

a = long(raw_input().strip(), base=3)
result = base_repr(a, base=9)

print('{0}'.format(result))
