#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Получение обратной кодировки двоичного отрицательного числа с тем же абсолютным значением
задано неотрицательное двоичное число
отрицательное число, полученное из исходного с помощью обратного кода
101
'''

from __future__ import print_function

a = raw_input().strip()
b = ""

for i in range(len(a)):
    if a[i] == "0":
        b += "1"
    else:
        b += "0"

if b[0] == "0":
    result = "1" + b
else:
    result = b
print('{0} {1}'.format(a, result))