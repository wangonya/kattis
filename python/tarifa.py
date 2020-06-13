#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://open.kattis.com/problems/tarifa
import sys


def tarifa(mbs, usage):
    available_mbs = 0

    for amount in usage:
        available_mbs += mbs - amount

    print(available_mbs + mbs)


if __name__ == '__main__':
    mbs = int(sys.stdin.readline().strip())
    months = int(sys.stdin.readline().strip())

    usage = []

    for _ in range(0, months):
        amount = int(sys.stdin.readline().strip())
        usage.append(amount)

    tarifa(mbs, usage)
