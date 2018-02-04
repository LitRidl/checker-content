#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать количество существительных в тексте на немецком языке(артикль + [прилагательное] + существительное)
In den Zeiten der allgemeinen Globalisierung\nverscharft sich wesentlich die Konkurrenz.
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def check_s(w):
    if (len(w) < 2):
        return 0
    if w[-1] == "," or w[-1] == "." or w[-1] == "!" or w[-1] == "?":
        w = w[:-1]
    if w[0] not in ascii_uppercase:
        return 0
    if len(w) > 1:
        for i in w[1:]:
            if i not in (ascii_lowercase + ascii_uppercase):
                return 0
    else:
        return 0
    return 1

def check_p(w):
    if len(w) > 1:
        for i in w:
            if i not in (ascii_lowercase):
                return 0
    else:
        return 0
    return 1

words = [w for w in stdin.read().split() if len(w.strip()) > 0]

ar = "der des dem den die ein eins einem einen das die einer eine".split()

status = 0

res = 0

for word in words:
    if (word.lower() in ar):
        status = 1
    elif (status == 1):
        if (check_s(word) == 1):
            res += 1
            status = 0
        elif (check_p(word) == 1):
            status = 2
        else:
            status = 0
    elif (status == 2):
        if (check_s(word) == 1):
            res += 1
        status = 0

print(res)