from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr

def seq_tests2(var1_bounds, var2_bounds, var3_bounds):
    test_idx = 2
    for a in range(*var1_bounds):
        for b in range(*var2_bounds):
            for c in range(*var3_bounds):
                with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
                    res = '{0} {1} {2}'.format(base_repr(a, 2), base_repr(b, 2), base_repr(c, 2))
                    f.write(res)
                    test_idx += 1


if __name__ == '__main__':
    seq_tests2([0, 8], [0, 8], [0, 8])