#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def carrots(problems):
    print(int(problems))


if __name__ == '__main__':
    contestants, problems = sys.stdin.readline().strip().split()
    for _ in range(0, int(contestants)):
        sys.stdin.readline()
    carrots(problems)
