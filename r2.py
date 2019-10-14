#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://open.kattis.com/problems/r2
import sys


def r2(R1, S):
    R2 = 2 * S - R1
    print(R2)


if __name__ == '__main__':
    R1, S = sys.stdin.readline().split()
    r2(int(R1), int(S))
