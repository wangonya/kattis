#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://open.kattis.com/problems/timeloop
import sys


def timeloop(n):
    for time in range(1, n + 1):
        print(f'{time} Abracadabra')


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    timeloop(n)
