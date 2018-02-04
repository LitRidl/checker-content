from __future__ import print_function
from random import shuffle, randint, choice, random
from string import *


def test(text, end='\n'):
    with open('tests/{0:03d}.dat'.format(test.idx), 'w') as f:
        f.write(str(text).lstrip().decode('string_escape') + end)
    test.idx += 1


INT_MIN = -2147483648
INT_MAX = +2147483647

randoms = list(set(randint(INT_MIN, INT_MAX) for _ in range(100 * 1000)))
shuffle(randoms)

def number():
    global randoms
    n = str(randoms.pop())
    if n[0] != '-' and random() <= 0.3:
        n = '+' + n
    return n


if __name__ == '__main__':
    test.idx = 2
    test('')

    test('0 0 0 0 0 1\n1 1 1 1 2 2 2 2')

    # One digit w/wo sign
    for x in range(0, 10):
        test(str(x))
        test('-' + str(x))
        test('+' + str(x))

    # One random number
    for _ in range(30):
        test(str(number()))

    # INT_MAX, INT_MIN
    test('+' + str(INT_MAX))
    for i in range(0, 20 + 1):
        test(str(INT_MAX - i))
        test(str(INT_MIN + i))

    # Big digit set in one line
    text = ' '.join(choice('0123456789') for _ in range(3000))
    test(text + '\n' + text)

    text = ' '.join(str(n) for n in range(-100 * 1000, 100 * 1000, 47))
    test(text)

    # Random numeric tests w/o endline and trailing separator
    for _ in range(50):
        test(' '.join(str(number()) for _ in range(randint(1, 5))).strip(), end='')

    # Random numeric tests
    for _ in range(300):
        test(' '.join(str(number()) for _ in range(randint(1, 100))).strip())
