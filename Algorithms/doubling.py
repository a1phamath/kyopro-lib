import math

N = 5 * 100000
LOG = 30    # 30 > log2(10**9)
nxt = [[-1]*N for _ in range(LOG)]

# 初期化 
for i in range(N):
    nxt[0][i] = None

for k in range(LOG-1):
    for i in range(N):
        if nxt[k][i] == -1:
            nxt[k+1][i] = -1
        else:
            nxt[k+1][i] = nxt[k][nxt[k][i]]

# ----ここまで準備----
# 処理内容は問題によって柔軟に

Q = None
ans = [i for i in range(N)]
for bit in range(LOG):
    if (1 << bit) & Q:
        for n in range(N):
            ans[n] = nxt[bit][ans[n]]

for n in range(N):
    print(ans[n] + 1)