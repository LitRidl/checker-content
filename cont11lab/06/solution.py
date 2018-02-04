#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Подсчитать колическтво слов - правильных идентификаторов языков Си или Паскаль
a h_e_l_l_o 1hj\n World 8628 ab%cd
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


s = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" , "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
words = [w.lower() for w in stdin.read().split() if len(w.strip()) > 0]

res = 0

for i in words:
    can = True
    for j in range(len(i)):
        if (i[j] not in s or (i[j] in s[0:10] and j == 0)):
            can = False
            break
    if can:
        res += 1

print(res)



