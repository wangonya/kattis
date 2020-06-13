#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def a1paper(smallest_size, number_of_sheets):
    print(smallest_size, number_of_sheets)


if __name__ == '__main__':
    smallest_size = int(sys.stdin.readline().strip())
    number_of_sheets = sys.stdin.readline().strip().split()

    a1paper(smallest_size, number_of_sheets)
