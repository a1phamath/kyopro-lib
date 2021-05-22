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
    ans = ''
    for s in reversed(S):
        if s == '6':
            s = '9'
        elif s == '9':
            s = '6'
        ans += s
    
    print(ans)

if __name__ == '__main__':
    main()

