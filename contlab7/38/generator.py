from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr


HEX_DIGITS = '0123456789ABCDEF'


def rnd(l, r, base=10):
    return base_repr(randint(l, r), base=base)


def rnd_word(length, prefix=' ', alphabet=HEX_DIGITS):
    word = ''.join(choice(alphabet) for _ in range(length))
    return (choice(prefix) + word).lstrip(' ').lstrip('0') or '0'


def generate_test1(params):
    a = rnd_word(randint(*params['word_len'][0]), alphabet='|')
    return '{0} '.format(a)


def generate_test2(params):
    a = rnd_word(randint(*params['word_len'][0]), alphabet='|')
    b = rnd_word(randint(*params['word_len'][1]), alphabet='|')
    return '{0}*{1} '.format(a, b)


def seq_tests1(var1_bounds, var2_bounds):
    test_idx = 2
    for a in range(*var1_bounds):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            ares = '|' * int(a)
            res = '{0}'.format(ares)
            f.write(res)
            test_idx += 1


def seq_tests2(var1_bounds, var2_bounds):
    alphabet = '|'
    test_idx = 2
    for c1 in range(*var1_bounds):
        for c2 in range(*var2_bounds):
            with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
                c1res = '|' * int(c1)
                c2res = '|' * int(c2)
                res = '{0}*{1}'.format(c1res, c2res)
                f.write(res)
                test_idx += 1

def rnd_tests():
    params = {
        'word_len': [(10, 20), (0, 0)],
        'word_radix': [2, 2],
        'word_prefix': [' ', ' '] # can be '     +-', for example
    }

    test_first = 11
    tests = 50

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(generate_test1(params))


if __name__ == '__main__':
    #seq_tests1([1, 10], [0, 0])
    rnd_tests()
