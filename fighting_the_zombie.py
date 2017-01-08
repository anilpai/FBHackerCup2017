'''

 Facebook Hacker Cup 2017
 (Qualification Round) problem 3 : https://www.facebook.com/hackercup/problem/326053454264498/
 Fighting the Zombie

'''

import sys

DEBUG = 1
TESTCASE = 'input/fighting_the_zombie_example_input.txt'


def castSpell(m, n, x):
    table = [[0 for _ in xrange(x+1)] for _ in xrange(n+1)]
    i = 1
    while i <= m and i <= x:
        table[1][i] = 1
        i += 1
    for i in range(2, n+1):
        for j in range(1, x+1):
            k = 1
            while k <= m and k < j:
                table[i][j] += table[i-1][j-k]
                k += 1
    return table[n]


def parse():

    if DEBUG:
        with open(TESTCASE) as f:
            lines = f.readlines()
    else:
            lines = sys.stdin.readlines()

    length = int(lines.pop(0).strip('\n'))
    result = []

    for i in range(length):
        h, s = map(int, lines.pop(0).strip('\n').split(' '))
        result.append((h, lines.pop(0).strip('\n').strip(' ')))
    return result


if __name__ == '__main__':
    for case, a in enumerate(parse(), start=1):
        h = a[0]
        spell = a[1].split(' ')
        p = [0.000000 for _ in range(len(spell))]
        c = 0
        for s in spell:
            x = h
            n = int(s.split('d')[0])
            m = int(s.split('d')[1].split('+')[0].split('-')[0])
            if '+' in s or '-' in s:
                z = int(s.split('+')[-1].split('-')[-1])
                if '+' in s:
                    x -= z
                if '-' in s:
                    x += z
            x -= 1
            p[c] = 1 - sum(castSpell(m, n, x))/float(m**n)
            c += 1
        print "Case #%d: %f" % (case, round(max(p), 6))
