#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import sys
import shutil
import subprocess


area_types = {
    1: u'кольцо, ограниченное двумя окружностями с центрами в точках (10, 10), где радиус внутренней окружности равен 5, а радиус внешней равен 10',
    2: u'квадрат с длиной стороны 10, стороны квадрата параллельны осям координат, центр квадрата в точке (10, −10)',
    3: u'лунка, являющаяся пересечением двух кругов радиуса 10, центр первого круга — в точке (−10, −10), центр второго — в точке (−20, −20)',
    4: u'полоса, ограниченная прямыми i + j + 10 = 0 и i + j + 20 = 0',
    5: u'треугольник с вершинами в точках (−10,0), (0, 10), (−10, 20)',
    6: u'эллипс с центром в точке (20, 0), проходящий через точки (10, 0), (30, 0), (20, 5) и (20, −5)'
}


problem_info = [
    ('mod(i * max(j, l), 30) + mod(j * min(i, l), 20) + k',
        'min(i, max(j, min(l, max(i - l, j - l))))',
     'sign(k - 10) * abs(i - j + l - k)'),
    ('_div(abs(i - j + l), (3 - sign(i - j + k))) + 10',
        '_div(abs(i + j - l), (3 - sign(j - i + k))) + 10',
     'mod(max(i * j, j * l) * (k + 1), 40)'),
    ('max(min(i + j - l - k, i - j + l - k), min(k + i - j - l, k - i - j + l))',
        'j + mod(l * sign(j), 20) + mod(k * sign(i), 10)',
     'abs(i - j + l - k) * sign(i) * sign(j)'),
    ('mod(min(i + j, i + l) * (k + 1), 30)',
        'j + mod(l * sign(j), 20) + mod(k * sign(i), 10)',
     'mod(max(max(i * j, i * l), j * l), 30)'),
    ('mod(max(j - k, l - k), 30) + mod(max(i + l, j + k), 20)',
        'mod(abs(i - l) * sign(j + k) + abs(i - k) * sign(j + k), 20)',
     'mod((i + k) * (j - k) * (l + k), 25)'),

    ('min(mod(l, 5),mod(i * k, 5)) + j + _div(k ,3)',
        '_div(max(-3 * i, 2 * j), 5) - abs(j - l)',
     'j + mod(l, 7) + mod(k * sign(i), 10)'),
    ('abs(k - 15) - min(_div(i, 3), mod(j + l, 10)) - 20',
        '-1 * _div(j + k, 5) + abs(mod(i * l, 8))',
     'max(mod(i + j, 15), mod(l + k, 14))'),
    ('mod((i + j + l) * (k + 1), 25) - mod(i * j * l * (k + 2), 10) + 10',
        'min(mod((i + j + l) * (k + 3), 25), mod(i * j * l * (k + 4), 25)) + 10',
     '2 * sign(l) * abs(mod((i + j + l) * (k + 5), 10) - mod(i * j * l * (k + 6), 25))'),
    ('mod(abs(max(i * (k + 5), j * (k + 6))) - abs(min(j * (k + 7), l * (k + 8))), 20)',
        '(3 - sign(i - j)) * mod(abs(min(min(i * l + 5, j * l - 3), i * j + 6)), 25) - 7',
     'mod(i, 10) + mod(j, 10) + mod(l, 10)'),
    ('mod((i + k) * (j - k) * (l + k), 25)',
        'mod(min(i + k, max(j - k, l - k)), 30)',
     'abs(j - l) * sign(i) - abs(i - l) * sign(j)'),

    ('_div(i, 3) - abs(i - k) * sign(l - j)',
        'mod(j, 10) - mod(max(i, l), k + 1)',
     'i + mod(j * k, 5) + _div(l, 5) + 3'),
    ('sign(min(i, j)) * max(mod(i + k, 20), mod(j + l, 20))',
        'abs(max(i, j)) - k * min(j, l)',
     '_div(k - l, mod((i + j + l) * (i + j + l), 5) + 1)'),
    ('_div(mod(i + j, 30), mod(abs(l), 5) + 1) + _div(mod(i + l, 30), mod(abs(j), 5) + 1)',
        'mod(max(k * i, (k + 1) * j), 25) - _div(abs(j - l), 10)',
        '_div(abs(j - l), 10) + min(mod(i + l, 20), mod(j * k, 20)) - 10'),
    ('mod(i * i * i - j * j * j + l * l * l - k, 20)',
        'mod(min(min(i * j * j - k, i * i * l - k), j * l * l - k), 30)',
     'mod(max(max(i * j * j - k, i * i * l - k), j * l * l - k), 30)'),
    ('max(mod(47 * i, 25), min(mod(47 * j, 30), mod(47 * l, 30))) - mod(k, 15)',
        'min(max(mod(47 * i, 25), mod(47 * j, 25)), mod(47 * l, 30)) + mod(k, 5)',
     'mod(47 * i * j * l, 25) + mod(k, 5)'),

    ('abs(i - l) + min(mod(j, 10), mod(l * k, 10)) - 20',
        'mod(max(k - i, min(j, max(i - l, j - l))), 30)',
     'mod(l * l, 20) - mod(max(i ,j), k + 1)'),
    ('sign(i + 1) * abs(abs(k - j) - abs(i - l))',
        'mod(j, 20) + max(mod(i, 20), min(j - k, l - k)) - 10',
     'mod(k * (i + 1) * (j + 2) * (l + 3), 20)'),
    ('mod(_div(i * j, abs(l) + 1) + _div(j * l, abs(i) + 1) + _div(i * l, abs(j) + 1), 30)',
        'mod(i * max(j, l), 20) + mod(j * min(i, l), 30) - k',
     'mod(max(max(i * j, i * l), j * l), 30) + 20'),
    ('mod(i * min(j, l) + j * min(i, l) + k * k, 20)',
        'mod((mod(i, 10) - k) * (mod(j, 10) + k) * (mod(l, 10) - k), 25)',
     'max(mod(min(i + j, i + l), 25), mod(max(i + l, j + k), 20)) + 10'),
    ('mod(abs(i - j) * l - abs(j - l) * i + abs(i - l) * j, 20) - k',
        'mod(min(i, j) * max(j, l) * min(i, l), 25) + 5 * sign(i) + k',
     'abs(l) * sign(i - j) - abs(i) * sign(j - l) + abs(j) * sign(i - l)'),

    ('max(mod(min(i - j, j - l), 20), mod(min(i - l, j - k), 20)) + 10',
        'sign(i - j) * min(mod(i, 20), mod(j, 20)) - mod(max(abs(i - l), abs(k - 20)), 20) + 20',
     'mod(i, 10) * mod(j, 10) + mod(l, 10)'),
    ('mod(mod(i + j, abs(min(j - l, l - k)) + 1) - k, 20)+ 10',
        'max(_div(i + j, 2 + sign(j * l - i * k)), _div(j + l, 2 + sign(i * j - l * k))) - 10',
     'mod(max(i, j) * min(i, l), 30)'),
    ('mod(min(max(min(i - j, i - l), j - l), i - k), 30)',
        'mod(max(min(max(i - j, i - l), j - l), i - k), 30)',
     'mod(i, 30) - mod(j, 30) + mod(l, 30) - mod(k, 30)'),
    ('mod((i - k) * max(j, l) + (j - k) * min(i, l) + (l - k) * max(i, j), 23)',
        '-1 * mod((i - k) * min(j, l) + (j - k) * max(i, l) + (l - k) * min(i, j), 27)',
     'abs(i + j - l - k) * sign(i - j + l - k)'),
    ('mod(_div(i * i, abs(j - l) + k + 1) - _div(j * j, abs(i - l) + k + 1), 30)',
        'sign(l) * min(i, j) - sign(j) * max(i, l) + k',
     'mod((i - j) * (j - l) * (l - i), 20)'),

    ('abs(max(mod(min(i + j, i + l), 30), mod(max(i + l, j + k), 25)))',
        'mod(abs(i + k), 10) + mod(abs(j + k), 10) + mod(abs(l + k), 10)',
    'mod(((i * i * i) + (j * j * j) + (l * l * l) - k), 35)'),
    ('mod(abs((i + k) * (j + 2 * k) * (l + 3 * k)), 35)',
        'sign(max(i, j)) * min(mod(i + k, 20), mod(j + l, 20))',
    '_div(i, 3) - abs(i - k) * sign(l - j)'),
    ('i * mod(max(j, l), 20) + j * mod(min(i, l), 30) + k',
        '(mod(abs(i - j + l - k) * sign(k - 10), 20))',
    'mod((abs(i - j) * l - abs(j - l) * i + abs(i - l) * j), 20) - k'),
    ('mod(max(max(i * j, i * l), j * l), 30) + k',
        'abs(j - l) * sign(i) - abs(i - l) * sign(j)',
    'min(i, max(j, min(l, max(i - l, j - l))))'),
    ('mod(abs(sign(i - j) * l - sign(j - l) * i + sign(i - l) * j - k), 35)',
        'mod(i * max(j, l), 30) + mod(j * min(i, l), 20) - k',
    'mod((i + k) * (j - k) * (l + k), 25)')
]


def _read_problem_info(i):
    area_idx = (i - 1) / 5 + 1
    data = {
        'formula_i': problem_info[i - 1][0],
        'formula_j': problem_info[i - 1][1],
        'formula_l': problem_info[i - 1][2],
        'in_area': 'in_area_{0}'.format(area_idx),
        'area': area_types[area_idx]
    }
    return data


def initial_solution_files(problem_names, ext='c'):
    with open(r'./solution.{0}'.format(ext), 'r') as f:
        tpl = f.read()
        for i in problem_names:
            with open(r'./{0:02d}/solution.c'.format(i), r'w') as f:
                code = '' + tpl
                data = _read_problem_info(i)
                for k, v in data.items():
                    code = code.replace(r'{{' + '{0}'.format(k) + '}}', v)
                f.write(code)


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
            #data = _read_problem_info(r'./{0:02d}/solution.{1}'.format(i, ext))
            data = _read_problem_info(i)
            with open(r'./{0:02d}/tests/001.ans'.format(i), 'r') as ans_f:
                data['test_out'] = ans_f.read()
            statements = tpl.replace(ur'{{id}}', str(i))
            for k, v in data.items():
                statements = statements.replace(
                    ur'{{' + u'{0}'.format(k) + u'}}', v)
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
    problemset = range(1, 25 + 1)
    if len(sys.argv) > 1:
        if sys.argv[1] in ('-h', '--help'):
            print(r'''solutions: initial_solution_files
mkdirs: create_directories
move: place_solutions
statements: create_statements
makefile: copy_makefile
tests: copy_tests_directory
#test1: create_test_001
answers: make_answers
problems: problems_list''')
        elif 'solution' in sys.argv[1]:
            initial_solution_files(problemset, sys.argv[
                                   2] if len(sys.argv) >= 3 else 'c')
        elif 'mkdir' in sys.argv[1]:
            create_directories(problemset)
        elif sys.argv[1] == 'move' or sys.argv[1] == 'mv':
            place_solutions(problemset, sys.argv[
                            2] if len(sys.argv) >= 3 else 'c')
        elif 'statement' in sys.argv[1]:
            create_statements(problemset, sys.argv[
                              2] if len(sys.argv) >= 3 else 'c')
        elif sys.argv[1] in ('makefile', 'make'):
            copy_makefile(problemset)
        elif sys.argv[1] == 'tests':
            copy_tests_directory(problemset)
        elif sys.argv[1] == 'test1':
            print("Not implemented")
            # create_test_001(problemset, sys.argv[2] if len(sys.argv) >= 3 else 'c')
        elif sys.argv[1] == 'answers':
            make_answers(problemset)
        elif sys.argv[1] == 'problems':
            problems_list(problemset)
