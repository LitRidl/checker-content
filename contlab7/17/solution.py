#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление поразрядной конъюнкции исходных чисел.
Входное слово представляет собой два беззнаковых двоичных числа (возможно, с ведущими нулями), разделенные знаком "&amp;".
двоичное число, результат поразрядной конъюнкции
11000011&100111111
'''

from __future__ import print_function
from numpy import base_repr


def bit_and(a, b):
    return int(a) & int(b)

b, a = raw_input().split('&')
inta = int(a, base=2)
intb = int(b, base=2)

result = base_repr(bit_and(inta, intb), base=2)

print (result)