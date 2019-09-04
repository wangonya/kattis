# https://open.kattis.com/problems/faktor
import sys


def faktor(articles, impact):
    print(int(articles)*(int(impact)-1) + 1)


if __name__ == '__main__':
    a, i = sys.stdin.readline().split()
    faktor(a, i)

# We want to find the minimum number of citations C_min so that our rounded
# value of impact equals to I. We know that I = math.ceil( C / A ),
# therefore, the value of (C / A) must be something between I-1 and I. That
# is, I-1 < (C/A) <= I. From this, we can write, (I-1)*A < C < I*A. Now we
# know that value of C should be strictly higher than (I-1)*A and it should
# be less than or equal to I*A. C is an integer, therefore the minimum
# value of C that satisfies the above condition must be (I-1)*A + 1.
#
# Hence it's proved that, C_min = (I-1)*A + 1.
