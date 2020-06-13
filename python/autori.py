# https://open.kattis.com/problems/autori
import sys


def autori(name):
    print(
        ''.join(c for c in name if c.isupper())
    )


if __name__ == '__main__':
    n = sys.stdin.readline()
    autori(n)
