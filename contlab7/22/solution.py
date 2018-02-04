#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм получения десятичного дополнительного кода для отрицательного числа с тем же абсолютным значением.
Входное слово представляет собой десятичную запись (возможно, с ведущими нулями) целого неотрицательного числа в прямом коде.
десятичное число, дополнительный код отрицательного числа с тем же абсолютным значением
283764
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=10)

result = ''
alen = len(base_repr(inta, base=10))
result = result + base_repr((10**(alen + 1) - inta), base=10)

print("{0}".format(result))
