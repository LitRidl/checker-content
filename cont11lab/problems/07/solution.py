#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно закодировать слова по Цезарю с переменным ключом, равным номеру буквы в слове +3
aBcAbC129xyzXYZ 10z\n0000000000000000
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def caesar_char(c, shift):
    alphabet = ascii_lowercase + ascii_uppercase + digits
    a_lower = ascii_lowercase[shift % 26:] + ascii_lowercase[:shift % 26]
    a_upper = ascii_uppercase[shift % 26:] + ascii_uppercase[:shift % 26]
    a_digits = digits[shift % 10:] + digits[:shift % 10]
    table = maketrans(alphabet, a_lower + a_upper + a_digits)
    return c.translate(table)


def caesar(word):
    return ''.join(caesar_char(c, i + 3) for i, c in enumerate(word))

for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    if len(words) > 0:
        print(' '.join(caesar(word) for word in words))
