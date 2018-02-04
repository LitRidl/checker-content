#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
отделить пробелом слова, находящиеся вплотную к концу строки и к началу следующей (выводить с теми же разделителями)
chair table sofa\n pillow 
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *



for i in stdin.readlines():
    if (not i[0].isspace()):
        print(" ", end="")
    if ("\r\n" in i):
        try:
            if (not i[-3].isspace()):
                print(i[:-2] +" " + i[-2:], end="")
            else:
                print(i, end="")
        except:
            print(i, end="")
    elif ("\n" in i):
        try:
            if (not i[-2].isspace()):
                print(i[:-1] +" " + i[-1:], end="")
            else:
                print(i, end="")
        except:
            print(i, end="")
    else:
        if (not i[-1].isspace()):
            print(i + " ", end="")
        else:
            print(i, end="")