from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


# input
N = int(input())

# functions
def main():
    if N % 2 == 0:
        print('White')
    else:
        print('Black')


if __name__ == '__main__':
    main()
