"""
AGC033_A
https://atcoder.jp/contests/agc033/tasks/agc033_a

幅優先探索をnumpyで
"""

import numpy as np
 
H, W = map(int, input().split())
A = tuple(input() for _ in range(H))
 
INF = H * W
 
dp = np.full((H, W), INF, dtype=np.int)
 
for i in range(H):
	for j in range(W):
		dp[i, j] = 0 if A[i][j] == '#' else dp[i, j]
 
for i in range(1, H):
	dp[i, :] = np.minimum(dp[i, :], dp[i-1, :] + 1)
for i in range(0, H-1)[::-1]:
	dp[i, :] = np.minimum(dp[i, :], dp[i+1, :] + 1)
for j in range(1, W):
	dp[:, j] = np.minimum(dp[:, j], dp[:, j-1] + 1)
for j in range(0, W-1)[::-1]:
	dp[:, j] = np.minimum(dp[:, j], dp[:, j+1] + 1)
 
print(np.max(dp))