# https://open.kattis.com/problems/faktor
import sys


def faktor(articles, impact):
    print(int(articles)*(int(impact)-1) + 1)


if __name__ == '__main__':
    a, i = sys.stdin.readline().split()
    faktor(a, i)
