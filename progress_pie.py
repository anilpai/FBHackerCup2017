'''

 Facebook Hacker Cup 2017
 (Qualification Round) problem 1 : https://www.facebook.com/hackercup/problem/1254819954559001/
 Progress Pie

'''


import sys
import math

DEBUG = 1
TESTCASE = 'input/progress_pie.txt'


def radiusCheck(c_x, c_y, rad, x, y):
    if ((x - c_x) * (x - c_x) + (y - c_y) * (y - c_y) <= rad * rad):
        return True
    else:
        return False


def arcCheck(p, x, y):
    # a1 is constant.
    a1 = 90
    # a2 is dependent on 'p' as percentage.
    a2 = p * 3.6

    # convert a2 to new quadrant system
    a2 = (450 -a2)%360

    point_ang = round(math.atan2(y,x)/math.pi*180, 6)

    if point_ang < 0:
        point_ang = 360 + point_ang


    if p ==0:
        return False
    if p <=25:
        if point_ang >= a2 and point_ang <= a1:
            return True
        else:
            return False
    else:
        if point_ang >= a2 and point_ang <= 360:
            return True
        else:
            return False


def parse():

    if DEBUG:
        with open(TESTCASE) as f:
            lines = f.readlines()
    else:
            lines = sys.stdin.readlines()

    length = int(lines.pop(0).strip('\n'))
    assert len(lines) == length, 'Input len() != lines[0]'
    return lines


if __name__ == '__main__':

    for case, number in enumerate(parse(), start=1):
        i = number.strip('\n').split()

        # Given
        p = int(i[0])
        x = int(i[1])
        y = int(i[2])

        # Additional parameters
        x -= 50
        y -= 50
        c_x = 0
        c_y = 0
        rad = 50

        result = ''
        if radiusCheck(c_x, c_y, rad, x, y) and arcCheck(p, x, y):
            result = "black"
        else:
            result = "white"

        print "Case #%d: %s" % (case, result)
