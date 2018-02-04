#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Умножение однозначных чисел в усеченной римской системе счисления.
через пробел записано два беззнаковых одноциферных числа в римской системе счисления (в алфавите {I, V, X, L, C, D, M})
число в римской системе счисления, равное произведение исходных, представимое в исходном алфавите
L V
'''

alphabet = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

a, b = raw_input().split()

pair = dict(zip(alphabet, range(0, 7)))

tens = pair[a] / 2 + pair[b] / 2
fives = pair[a] % 2 + pair[b] % 2

if fives == 0:
	result = 'I'
elif fives == 1:
	result = 'V'
else:
	result = 'XXV'

result = ''.join([alphabet[pair[x] + 2 * tens] for x in result])

print("{0} {1} {2}".format(a, b, result))