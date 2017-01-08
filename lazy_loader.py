'''

 Facebook Hacker Cup 2017
 (Qualification Round) problem 2 : https://www.facebook.com/hackercup/problem/169401886867367/
 Lazy Loader

'''

import sys

DEBUG = 1
TESTCASE = 'input/lazy_loading.txt'


def maxTrips(a):
    a = sorted(a)
    trips = 0
    while len(a) > 0:
        w = a.pop()
        k = w
        while w <= 50 and len(a) > 0:
            a.pop(0)
            w += k
        if w >= 50:
            trips += 1
    return trips


def parse():

    if DEBUG:
        with open(TESTCASE) as f:
            lines = f.readlines()
    else:
            lines = sys.stdin.readlines()

    length = int(lines.pop(0).strip('\n'))
    result = []

    for i in range(length):
        tmp = []
        l = int(lines.pop(0).strip('\n'))
        for _ in range(l):
            tmp.append(lines.pop(0).strip('\n'))
        result.append(tmp)
    return result


if __name__ == '__main__':
    for case, a in enumerate(parse(), start=1):
        res = maxTrips(map(int, a))
        print "Case #%d: %d" % (case, res)
