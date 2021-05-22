'''
https://atcoder.jp/contests/abc054/tasks/abc054_d
DP法(3次元)
'''

def solve():
    N, Ma, Mb = map(int, input().split())
    a = [0]*N
    b = [0]*N
    c = [0]*N
    for i in range(N):
        a[i], b[i], c[i] = map(int, input().split())

    INF = sum(c)
    dp = [[[INF]*(10*N+1) for _ in range(10*N+1)] for _ in range(N+1)]
    
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(10*N+1-a[i]):
            for k in range(10*N+1-b[i]):
                if dp[i][j][k]==INF:
                    continue
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][j+a[i]][k+b[i]] = min(dp[i+1][j+a[i]][k+b[i]], dp[i][j][k]+c[i])

    ans = INF
    for i in range(1, 10*N+1):
        if i*Ma>10*N or i*Mb>10*N:
            break
        ans = min(ans, dp[N][i*Ma][i*Mb])
    if ans==INF:
        ans = -1

    print(ans)


solve()