#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Кодирование числа в римской записи по Цезарю (в алфавите {I, V, X, L, C, D, M}) с фиксированным сдвигом, равным 3
записано число в римской системе счисления, записанное цифрами в рамках алфавита
слово из букв данного алфавита, являющееся кодом по Цезарю исходного числа
MCDXLVII
'''

from __future__ import print_function

alphabet = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

a = raw_input().strip()

pair = dict(zip(alphabet, alphabet[3:] + alphabet[:-3]))
result = ''.join([pair[x] for x in a])

print("{0} {1}".format(a, result))
