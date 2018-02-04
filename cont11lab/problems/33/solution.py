#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделить все дясятичные числа от 17 до 77 по модулю и распечатать их значения в словесной форме по-английски
hgsdf 324 fgd -34\n3 77 67ad
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def check(w):
    try:
        a = long(w)
        if (17 <= abs(a) <= 77):
            return True
    except:
        pass
    return False

def print_num(w):
    w = int(w)
    wrd = ""
    if (w < 0):
        wrd += "minus "
        w = abs(w)
    if (w == 17):
        return wrd + "seventeen"
    elif (w == 18):
        return wrd + "eighteen"
    elif (w == 19):
        return wrd + "nineteen"
    a = w // 10
    if (a == 2):
        wrd += "twenty"
    elif (a == 3):
        wrd += "thirty"
    elif (a == 4):
        wrd += "forty"
    elif (a == 5):
        wrd += "fifty"
    elif (a == 6):
        wrd += "sixty"
    elif (a == 7):
        wrd += "seventy"

    a = w % 10

    if (a == 1):
        wrd += " one"
    if (a == 2):
        wrd += " two"
    elif (a == 3):
        wrd += " three"
    elif (a == 4):
        wrd += " four"
    elif (a == 5):
        wrd += " five"
    elif (a == 6):
        wrd += " six"
    elif (a == 7):
        wrd += " seven"
    elif (a == 8):
        wrd += " eight"
    elif (a == 9):
        wrd += " nine"
    return wrd


for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(print_num(w) for w in words))