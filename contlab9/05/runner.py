from __future__ import print_function
from random import shuffle, randint, choice
from subprocess import Popen, PIPE, STDOUT
from collections import defaultdict


def grid(xs, ys, zs):
    yes, no = 0, 0
    noes = []
    vars_ = defaultdict(int)
    for x in range(*xs):
        for y in range(*ys):
            for z in range(*zs):
                p = Popen(['./solution'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
                x, y, z = [randint(*x) for x in [xs[:2], ys[:2], zs[:2]]]
                stdout_data = p.communicate(input='{0} {1} {2}\n'.format(x, y, z))[0]
                dd = stdout_data.split()[1:]
                vars_[tuple(dd)] += 1
                if 'Yes' in stdout_data:
                    yes += 1
                elif 'No' in stdout_data:
                    no += 1
                    noes.append((x, y, z))
                if (yes + no) % 10000 == 0:
                    print(yes, no)
                    # print(vars_)
                if no > 0:
                    print('FOUND!!!')
                    print(noes)
                    return

    print(yes, no)
    print(noes)

if __name__ == '__main__':
    #runner(1, 2, 3)
    grid([-100, 100, 1], [-100, 100, 1], [-100, 100, 1])
