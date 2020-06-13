#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://open.kattis.com/problems/bijele
import sys


def bijele(current_pieces):
    correct_pieces = '112228'
    difference = []
    current_piece_index = 0
    for piece in correct_pieces:
        _difference = int(piece) - int(current_pieces[current_piece_index])
        difference.append(_difference)
        current_piece_index += 1
    print(*difference)


if __name__ == '__main__':
    current_pieces = sys.stdin.readline().strip().split()
    bijele(current_pieces)
