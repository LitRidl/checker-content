#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из восьмеричной системы счисления в двоичную.
записано целое беззнаковое число произвольной длины в восьмеричной системе счисления
число в двоичной системе счисления, номинально равное исходному
736101
'''
from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = int(a, base=8)

result = base_repr(inta, base=2)

print("{0} {1}".format(a, result))
