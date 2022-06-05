"""
https://tsutaj.hatenablog.com/entry/2017/03/29/204841
"""

INF = float("inf")

class SegmentTree:
    def __init__(self, arr):
        size = len(arr)
        n = 1
        while n < size:
            n *= 2
        self.n = n
        self.node = [INF]*n
        for i in range(size):
            self.node[i+n-1] = arr[i]
        for i in reversed(range(n-2)):
            self.node[i] = min(self.node[2*i+1], self.node[2*i+2])
    
    def update(self, x, val):
        x += (self.n - 1)
        self.node[x] = val
        while x > 0:
            x = (x - 1) // 2
            self.node[x] = min(self.node[2*x+1], self.node[2*x+2])