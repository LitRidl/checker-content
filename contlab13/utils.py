import os
import sys
import shutil
import subprocess


def _read_problem_info(path):
    with open(path, r'r') as f:
        m = [l.rstrip() for l in f.readlines()]

    return {
        'task': m[1],
        'test_yes': m[2],
        'test_no': m[3]
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
        data = _read_problem_info(r'./{0:02d}/solution.c'.format(i))

        with open(r'./{0:02d}/tests/001.dat'.format(i), 'w') as f:
            f.write(data['test_yes'])

        with open(r'./{0:02d}/tests/002.dat'.format(i), 'w') as f:
            f.write(data['test_no'])


def make_answers(problem_names):
    for i in problem_names:
        cmd = 'cd ./{0:02d}/ && make answers'.format(i)
        print(subprocess.check_output(['bash', '-c', cmd]))


def fix_test(problemset, test_idx, test_ok):
    for i in problem_names:
        old = './{0:02d}/tests/{0:03d}.dat'.format(i, test_idx)
        os.remove(old)
        shutil.copyfile('./{0:03d}.dat'.format(test_ok), old)

    make_answers(problemset)

# [problem]
# id = 32
# super = "Generic"
# short_name = "32"
# long_name = "32"
# standard_checker = "cmp_file_nospace"

def problem_description(problemset, checker):
    desc = ''
    for i in problemset:
        desc += '[problem]\n'
        desc += 'id = {0}\n'.format(i)
        desc += 'super = "Generic"\n'
        desc += 'short_name = "{0}"\n'.format(i)
        desc += 'long_name = "{0}"\n'.format(i)
        desc += 'standard_checker = "{0}"\n'.format(checker)
        desc += '\n'
    return desc


if __name__ == '__main__':
    problemset = [23, 24, 25, 26]

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
problems: problem_description (set checker!)
fix TEST_IDX CORRECT_TEST_FILE: fix_test''')
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
        elif sys.argv[1] == 'problems':
            print(problem_description(problemset, 'cmp_yesno'))
        elif sys.argv[1] == 'fix':
            if len(sys.argv) == 4:
                fix_test(sys.argv[2], sys.argv[3], problemset)
            else:
                print('python utils.py fix TEST_IDX CORRECT_TEST_FILE')

