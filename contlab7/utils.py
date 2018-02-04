#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import shutil
import subprocess


def _read_problem_info(path):
    with open(path, r'r') as f:
        m = [l.rstrip() for l in f.readlines()]
    return {
        'task': m[4],
        'input_type': m[5],
        'answer_type': m[6],
        'test_in': m[7]
    }


def initial_solution_files(problem_names, ext='c'):
    for i in problem_names:
        shutil.copyfile(r'./solution.{0}'.format(ext), r'./{0:02d}.{1}'.format(i, ext))


def create_directories(problem_names):
    for i in problem_names:
        os.makedirs(r'./{0:02d}'.format(i))


def place_solutions(problem_names, ext='c'):
    for i in problem_names:
        shutil.move(r'./{0:02d}.{1}'.format(i, ext),
                    r'./{0:02d}/solution.{1}'.format(i, ext))


def create_statements(problem_names, ext='c'):
    with open(r'statement.xml', r'r') as f:
        tpl = f.read()
    for i in problem_names:
        with open(r'./{0:02d}/statement.xml'.format(i), r'w') as f:
            data = _read_problem_info(r'./{0:02d}/solution.{1}'.format(i, ext))
            with open(r'./{0:02d}/tests/001.ans'.format(i), 'r') as ans_f:
                data['test_out'] = ans_f.read()
            statements = tpl.replace(r'{{id}}', str(i))
            for k, v in data.items():
                if k == 'answer_type':
                    v = v.decode('utf-8')[0].upper().encode('utf-8') + v.decode('utf-8')[1:].encode('utf-8') + '.'
                statements = statements.replace(r'{{' + '{0}'.format(k) + '}}', v)
            f.write(statements)


def copy_makefile(problem_names):
    for i in problem_names:
        shutil.copyfile(r'Makefile', r'./{0:02d}/Makefile'.format(i))


def copy_tests_directory(problem_names):
    for i in problem_names:
        shutil.copytree(r'./tests', './{0:02d}/tests'.format(i))


def create_test_001(problem_names, ext='c'):
    for i in problem_names:
        with open(r'./{0:02d}/tests/001.dat'.format(i), 'w') as f:
            data = _read_problem_info(r'./{0:02d}/solution.{1}'.format(i, ext))
            f.write(data['test_in'] + '\n')


def make_answers(problem_names):
    for i in problem_names:
        cmd = 'cd ./{0:02d}/ && make answers'.format(i)
        print(subprocess.check_output(['bash', '-c', cmd]))


def problems_list(problemset):
    tpl = '''[problem]
id = {0}
super = "Generic"
short_name = "{1}"
long_name = "{2}"
standard_checker = "cmp_file_nospace"\n'''
    for p_id in problemset:
        print(tpl.format(p_id, str(p_id).ljust(2), str(p_id).ljust(2)))


if __name__ == '__main__':
    problemset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                  21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                  31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
    if len(sys.argv) > 1:
        if sys.argv[1] in ('-h', '--help'):
            print(r'''solutions: initial_solution_files
mkdirs: create_directories
move: place_solutions
statements: create_statements
makefile: copy_makefile
tests: copy_tests_directory
test1: create_test_001
answers: make_answers
problems: problems_list''')
        elif sys.argv[1] == 'solutions':
            initial_solution_files(problemset, sys.argv[2] if len(sys.argv) >= 3 else 'c')
        elif sys.argv[1] == 'mkdirs':
            create_directories(problemset)
        elif sys.argv[1] == 'move':
            place_solutions(problemset, sys.argv[2] if len(sys.argv) >= 3 else 'c')
        elif sys.argv[1] == 'statements':
            create_statements(problemset, sys.argv[2] if len(sys.argv) >= 3 else 'c')
        elif sys.argv[1] == 'makefile':
            copy_makefile(problemset)
        elif sys.argv[1] == 'tests':
            copy_tests_directory(problemset)
        elif sys.argv[1] == 'test1':
            create_test_001(problemset, sys.argv[2] if len(sys.argv) >= 3 else 'c')
        elif sys.argv[1] == 'answers':
            make_answers(problemset)
        elif sys.argv[1] == 'problems':
            problems_list(problemset)
