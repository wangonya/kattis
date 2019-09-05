# https://open.kattis.com/problems/abc
import sys


def abc(nums, order):
    max_order_pos = order.index(max(order))
    min_order_pos = order.index(min(order))
    max_nums_pos = nums.index(max(nums))
    min_nums_pos = nums.index(min(nums))
    nums.insert(max_order_pos, nums.pop(max_nums_pos))
    nums.insert(min_order_pos, nums.pop(min_nums_pos))
    print(' '.join(n for n in nums))


if __name__ == '__main__':
    a, b, c, = sys.stdin.readline().split()
    o = sys.stdin.readline().strip()
    abc([a, b, c], o)
