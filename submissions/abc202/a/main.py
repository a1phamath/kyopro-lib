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
a, b, c = map(int, input().split())

# functions
def main():
    print(7 * 3 - a - b - c)


if __name__ == '__main__':
    main()

