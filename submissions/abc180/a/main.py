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
N, A, B = map(int, input().split())

# functions
def main():
    print(N - A + B)


if __name__ == '__main__':
    main()

