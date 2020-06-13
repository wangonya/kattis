#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math


def siblice(matches, width, height):
    hypotenuse = math.sqrt(width**2 + height**2)
    results = []
    for lenth in matches:
        if lenth > hypotenuse:
            results.append('NE')
        else:
            results.append('DA')

    for result in results:
        print(result)


if __name__ == '__main__':
    number_of_matches, width, height = sys.stdin.readline().strip().split()
    matches = []
    for _ in range(0, int(number_of_matches)):
        length = int(sys.stdin.readline())
        matches.append(length)

    siblice(matches, int(width), int(height))
