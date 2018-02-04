import os
import shutil
import subprocess


def _read_matrix(path):
    with open(path, r'r') as f:
        m = [problem_names.rstrip() for problem_names in f.readlines()]
    return '\n'.join(m[1:5])


def initial_solution_files(problem_names):
    for i in problem_names:
        shutil.copyfile(r'./solution.c', r'./{0:02d}.c'.format(i))


def create_directories(problem_names):
    for i in problem_names:
        os.mkdirs(r'./{0:02d}', i)


def place_solutions(problem_names):
    for i in problem_names:
        shutil.move(r'./{0:02d}.c'.format(i), r'./{0:02d}/solution.c'.format(i))


def create_statements(problem_names):
    with open(r'statement.xml', r'r') as f:
        tpl = f.read()

    for i in problem_names:
        with open(r'./{0:02d}/statement.xml'.format(i), r'w') as f:
            matrix = _read_matrix(r'./{0:02d}/solution.c'.format(i))
            statements = tpl.replace(r'{{id}}', str(i)).replace(r'{{matrix}}', matrix)
            f.write(statements)


def copy_makefile(problem_names):
    for i in problem_names:
        shutil.copyfile(r'Makefile', r'./{0:02d}/Makefile'.format(i))


def copy_tests_directory(problem_names):
    for i in problem_names:
        shutil.copytree(r'./tests', './{0:02d}/tests'.format(i))


def create_test_001(problem_names):
    for i in problem_names:
        with open(r'./{0:02d}/tests/001.dat'.format(i), 'w') as f:
            f.write('2 4\n4\n')
            matrix = _read_matrix(r'./{0:02d}/solution.c'.format(i))
            f.write(matrix)
            f.write('\n1\n1000')


def make_answers(problem_names):
    for i in problem_names:
        cmd = 'cd ./{0:02d}/ && make answers'
        print(subprocess.check_output(['bash','-c', cmd]))


if __name__ == '__main__':
    problemset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

    # initial_solution_files(problemset)
    # create_directories(problemset)
    # place_solutions(problemset)
     create_statements(problemset)
    # copy_makefile(problemset)
    # copy_tests_directory(problemset)
    # create_test_001(problemset)
    # make_answers(problemset)

