#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать число слов в многострочных комментариях (/* и */) комментариях в программе на Си
#include <stdio.h>\nint main(void)\n{\n    int a = 5, b = 15;\n    /* this\n        is\n        comment\n    */\n    printf("%d\n", a + b); /*\n    comment*/\n    return 0;\n}
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

res = 0
count_slash = 0
comment = ""

for i in stdin.read().replace("\r\n", "\n").split('\n'):
    count_quotes = 0
    i = " " + i + " "
    for j in range(1, len(i) - 1):
        if (i[j] == "\"" and count_slash != 1):
            count_quotes += 1
        elif (i[j] == "*" and i[j-1] == "/" and count_quotes % 2 == 0 and count_slash == 0):
            count_slash = 1
        elif (i[j]== "*" and i[j+1] == "/" and count_slash == 1):
            count_slash = 0
            comment += " "
        elif (count_slash == 1):
            comment += i[j]
    comment += " "

res = len(comment.split())

print(res)