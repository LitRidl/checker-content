#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм инкрементирования целого неотрицательного шестнадцатеричного числа.
Входное слово представляет собой целое неотрицательное шестнадцатеричное число (возможно, с ведущими нулями).
шестнадцатеричное число, результат увеличения на единицу исходного числа
DEADBEEF
'''

from __future__ import print_function
from numpy import base_repr

a = long(raw_input().strip(), base=16)
result = base_repr(a + 1, base=16)

print('{0}'.format(result))
