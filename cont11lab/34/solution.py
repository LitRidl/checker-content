#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделить все дясятичные числа от 17 до 77 по модулю и распечатать их значения в словесной форме по-немецки
hgsdf 324 fgd -35\n3 77 67ad
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def check(w):
    try:
        a = int(w)
        if (17 <= abs(a) <= 77):
            return True
    except:
        pass
    return False

def print_num(w):
    w = int(w)
    wrd = ""
    if (w < 0):
        wrd += "minus  "
        w = abs(w)
    if (w == 17):
        return wrd + "siebzehn"
    elif (w == 18):
        return wrd + "achtzehn"
    elif (w == 19):
        return wrd + "neunzehn"

    a = w % 10

    if (a == 1):
        wrd += "einund"
    if (a == 2):
        wrd += "zweiund"
    elif (a == 3):
        wrd += "dreiund"
    elif (a == 4):
        wrd += "vierund"
    elif (a == 5):
        wrd += "fünfund"
    elif (a == 6):
        wrd += "sechsund"
    elif (a == 7):
        wrd += "siebenund"
    elif (a == 8):
        wrd += "achtund"
    elif (a == 9):
        wrd += "neunund"
    a = w // 10
    if (a == 2):
        wrd += "zwanzig"
    elif (a == 3):
        wrd += "dreißig"
    elif (a == 4):
        wrd += "vierzig"
    elif (a == 5):
        wrd += "fünfzig"
    elif (a == 6):
        wrd += "sechzig"
    elif (a == 7):
        wrd += "siebzig"
    return wrd


for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(print_num(w) for w in words))