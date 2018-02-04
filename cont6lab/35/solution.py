#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Восстановление целого числа в восьмеричной системе счисления по обратному коду.
записано число в восьмеричной системе счисления, являющееся обратным кодом искомого числа
восьмеричное число (возможно отрицательное), восстановленное из данного обратного кода
60342715
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input()
inta = long(a, base=8)
alen = len(base_repr(inta, base=8))

if long(a[0]) > 3:
	result = inta - 8 ** alen + 1
else:
	result = inta


result = base_repr(result, base=8)

print('{0} {1}'.format(a, result))