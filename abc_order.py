# https://open.kattis.com/problems/abc
import sys


def abc(nums, order):
    for _ in range(3):
        max_order_pos = order.index(max(order))
        max_nums_pos = nums.index(max(nums))
        nums.insert(max_order_pos, nums.pop(max_nums_pos))
        min_order_pos = order.index(min(order))
        min_nums_pos = nums.index(min(nums))
        nums.insert(min_order_pos, nums.pop(min_nums_pos))

    print(' '.join(n for n in nums))


if __name__ == '__main__':
    a, b, c, = sys.stdin.readline().split()
    o = sys.stdin.readline().strip()
    abc([a, b, c], o)
