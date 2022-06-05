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
S = input()[:-1]

# functions
def main():
    if S[-1]=="s":
        print(S + "es")
    else:
        print(S + "s")


if __name__ == '__main__':
    main()

