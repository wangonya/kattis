# https://open.kattis.com/problems/abc
import sys


def abc(nums):
    order = sys.stdin.readline().strip()
    max_order_pos = order.index(max(order))
    min_order_pos = order.index(min(order))
    max_nums_pos = nums.index(max(nums))
    min_nums_pos = nums.index(min(nums))
    nums[max_nums_pos], nums[min_nums_pos] = nums[max_order_pos], nums[min_order_pos]
    print(f'{nums[max_nums_pos]}, {nums[min_nums_pos]} = '
          f'{nums[max_order_pos]}, {nums[min_order_pos]}')
    print(' '.join(n for n in nums))


if __name__ == '__main__':
    # a, b, c, = sys.stdin.readline().split()
    inp = list(map(str, sys.stdin.readline().split()))
    abc(inp)
