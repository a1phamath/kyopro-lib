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
S = []
T = []
for i in range(N):
    s, t = input()[:-1].split()
    S.append(s)
    T.append([int(t), i])

# functions
def main():
    T.sort(reverse=True)
    print(S[T[1][1]])


if __name__ == '__main__':
    main()

