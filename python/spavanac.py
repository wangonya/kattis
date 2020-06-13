#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def spavanac(hour, minute):
    if minute - 45 > 0:
        print(hour, minute - 45)
    elif hour - 1 > 0:
        print(hour - 1, 60 + (minute - 45))
    else:
        print(24 - 1, 60 + (minute - 45))


if __name__ == '__main__':
    time = sys.stdin.readline().strip().split()
    hour = int(time[0])
    minute = int(time[1])
    spavanac(hour, minute)
