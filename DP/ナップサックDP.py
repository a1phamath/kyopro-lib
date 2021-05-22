"""
https://atcoder.jp/contests/dp/tasks/dp_d
"""


import sys
input = sys.stdin.readline


def main():
    N, W = map(int, input().split())
    weight = [0]*N
    value = [0]*N
    for i in range(N):
        weight[i], value[i] = map(int, input().split())
    
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j - weight[i] >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j - weight[i]] + value[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

    # for i in range(N+1):
    #     print(dp[i])
    print(dp[N][W])


if __name__ == '__main__':
    main()