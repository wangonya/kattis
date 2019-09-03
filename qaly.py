# https://open.kattis.com/problems/qaly
import sys


def quality_of_life(p):
    _list = []
    for _ in range(p):
        q, l = sys.stdin.readline().split()
        qaly = float(q)*float(l)
        _list.append(qaly)
    print(sum(_list))


if __name__ == '__main__':
    quality_of_life(int(sys.stdin.readline()))
