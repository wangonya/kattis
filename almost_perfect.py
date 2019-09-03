import math
from sys import stdin


def almost_perfect(p):
    divisor = 1
    _sum = 0
    while divisor <= math.sqrt(p):
        if p % divisor == 0:
            _sum += divisor
        divisor += 1
    if _sum == p:
        return f"{p} perfect"
    elif _sum == ((p+2) or (p-2)):
        return f"{p} almost perfect"
    else:
        return f"{p} not perfect"


if __name__ == '__main__':
    for p in stdin:
        print(
            almost_perfect(int(p))
        )
