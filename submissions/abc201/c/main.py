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
    ans = 0
    for i in range(10000):
        flg1 = True
        flg2 = True
        p = str(i).zfill(4)
        for j in range(4):
            if S[int(p[j])] == 'x':
                flg1 = False
        for k in range(10):
            if S[k] == 'o' and str(k) not in p:
                flg2 = False
        if flg1 and flg2:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()

