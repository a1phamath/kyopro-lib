# 1-indexed BIT
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def update(self,k,w):      #update list
        x = k
        while x <= self.n:
            self.data[x] += w
            x += x&(-x)

    def sums(self,k):     #sum of 1~k
        x = k
        s = 0
        while x > 0:
            s += self.data[x]
            x -= x&(-x)
        return s
    
    def search(self,s):     # binary search for min k that sums(k) >= s
        ok = self.n
        ng = 0
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if self.sums(mid) >= s:
                ok = mid
            else:
                ng = mid
        return ok


# TEST PROBLEM
# calculate inversion number
N = int(input())
A = list(map(int, input().split()))
bit = BIT(N)
ans = 0
for j in range(N):
    ans += j - bit.sums(A[j])
    bit.update(A[j],1)
print(ans)