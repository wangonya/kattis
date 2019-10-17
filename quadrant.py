#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def quadrant(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)


if __name__ == '__main__':
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())
    quadrant(x, y)
