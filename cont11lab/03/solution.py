#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать число слов в многострочных комментариях ({ и } или (* и *)) в программе на Паскале (вложенные комментарии не допускаются)
  Program comments;\n  Var a,b:Integer;\n  Begin\n    (* First *)\n    a:=0;\n    b:=10;\n    for a:=1 to 10 do\n      begin\n        Write (a*b, ' ');\n      end;\n    {  Comment\n    for a:=1 to 10 do\n      begin\n        Write (a*b, ' 'ы);\n      end;\n     a b c d}\n  End.
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
        elif (i[j] == "*" and i[j-1] == "(" and count_quotes % 2 == 0 and count_slash == 0):
            count_slash = 1
        elif (i[j]== "*" and i[j+1] == ")" and count_slash == 1):
            count_slash = 0
        elif (i[j] == "{" and count_quotes % 2 == 0):
            count_slash = 2
        elif (i[j] == "}" and count_slash == 2):
            count_slash = 0

            comment += " "
        elif (count_slash >= 1):
            comment += i[j]
    comment += " "

res = len(comment.split())

print(res)