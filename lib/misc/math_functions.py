'''
cmb(n, r)
組み合わせ nCr の計算
'''
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r < 0: return 0
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


'''
nCk mod p を求める
'''
MOD = 998244353
class Combination(object):
    def __init__(self, N):
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



'''
gcd(a, b)
整数 a, b の最大公約数を返す.

gcd_list(A)
整数リスト A についての最大公約数を返す。

lcm(a, b)
整数 a, b の最小公倍数を返す。

lcm(A)
整数リスト A についての最小公倍数を返す。
'''
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def gcd_list(A):
    ans = A[0]
    for i in range(1, len(A)):
        ans = gcd(ans, A[i])
    return ans


def lcm(a, b):
    return a*b // gcd(a, b)

def lcm_list(A):
    ans = A[0]
    for i in range(1, len(A)):
        ans = lcm(ans, A[i])
    return ans


#nを素因数分解したリストを返す
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n = n // i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


# エラトステネスの篩(素数判定)
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table


# bit全探索
n = 3     # 桁数
for i in range(2**n):
    for j in range(n):
        if (i>>j) & 1:
            pass
        else:
            pass


"""
extgcd(a,b): 互いに素なa,bについて、a*x+b*y=1の一つの解
mod_inv(a,m): aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
"""
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

