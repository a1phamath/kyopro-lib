MOD = 1000000007
class Combination(object):
    def __init__(self, N, MOD):
        self.fac = [0] * (N + 1)
        self.inv = [0] * (N + 1)
        self.finv = [0] * (N + 1)
        self.fac[0] = 1
        self.finv[0] = 1
        if N > 0:
            self.fac[1] = 1
            self.inv[1] = 1
            self.finv[1] = 1
 
        # 前計算
        for i in range(2, N + 1):
            self.fac[i] = self.fac[i - 1] * i % MOD
            self.inv[i] = self.inv[MOD % i] * (MOD - (MOD // i)) % MOD
            self.finv[i] = self.finv[i - 1] * self.inv[i] % MOD
 
    def com(self, N, k):
        return (self.fac[N] * self.finv[k] * self.finv[N - k]) % MOD
