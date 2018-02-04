#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм перевода шестнадцатеричного числа в четверичную систему счисления.
Входное слово представляет собой беззнаковое шестнадцатеричное число (возможно, с ведущими нулями).
четверичное число, равное исходному шестнадцатеричному, без ведущих нулей
01231
'''

from __future__ import print_function
from numpy import base_repr

a = long(raw_input().strip(), base=16)
result = base_repr(a, base=4)

print('{0}'.format(result))
