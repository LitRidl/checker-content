import os
import sys
import shutil
import subprocess


def _read_problem_info(path):
    with open(path, r'r') as f:
        m = [l.rstrip() for l in f.readlines()]

    return {
        'task': m[1],
        'answer_type': m[2],
        'matrix': '\n'.join(m[3:5 + 1])
    }


def initial_solution_files(problem_names):
    for i in problem_names:
        shutil.copyfile(r'./solution.c', r'./{0:02d}.c'.format(i))


def create_directories(problem_names):
    for i in problem_names:
        os.makedirs(r'./{0:02d}'.format(i))


def place_solutions(problem_names):
    for i in problem_names:
        shutil.move(r'./{0:02d}.c'.format(i),
                    r'./{0:02d}/solution.c'.format(i))


def create_statements(problem_names):
    with open(r'statement.xml', r'r') as f:
        tpl = f.read()

    for i in problem_names:
        with open(r'./{0:02d}/statement.xml'.format(i), r'w') as f:
            data = _read_problem_info(r'./{0:02d}/solution.c'.format(i))
            with open(r'./{0:02d}/tests/001.ans'.format(i), 'r') as ans_f:
                data['test_out'] = ans_f.read()
            statements = tpl.replace(r'{{id}}', str(i))
            for k, v in data.items():
                statements = statements.replace(r'{{' + '{0}'.format(k) + '}}', v)
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
            data = _read_problem_info(r'./{0:02d}/solution.c'.format(i))
            f.write('2 3\n3\n')
            f.write(data['matrix'])
            f.write('\n1\n1000')


def make_answers(problem_names):
    for i in problem_names:
        cmd = 'cd ./{0:02d}/ && make answers'.format(i)
        print(subprocess.check_output(['bash', '-c', cmd]))


if __name__ == '__main__':
    problemset = [6, 9, 10, 11, 12, 15, 19, 20, 22, 24, 27, 29, 30, 33, 35]

    if len(sys.argv) > 1:
        if sys.argv[1] in ('-h', '--help'):
            print(r'''solutions: initial_solution_files
mkdirs: create_directories
move: place_solutions
statements: create_statements
makefile: copy_makefile
tests: copy_tests_directory
test1: create_test_001
answers: make_answers''')
        elif sys.argv[1] == 'solutions':
            initial_solution_files(problemset)
        elif sys.argv[1] == 'mkdirs':
            create_directories(problemset)
        elif sys.argv[1] == 'move':
            place_solutions(problemset)
        elif sys.argv[1] == 'statements':
            create_statements(problemset)
        elif sys.argv[1] == 'makefile':
            copy_makefile(problemset)
        elif sys.argv[1] == 'tests':
            copy_tests_directory(problemset)
        elif sys.argv[1] == 'test1':
            create_test_001(problemset)
        elif sys.argv[1] == 'answers':
            make_answers(problemset)
