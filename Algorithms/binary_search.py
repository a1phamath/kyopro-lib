def isOK(m, arr):
    # 条件判定のコードを書く
    return arr[m] <= 1998


def binary_search(ok, ng, arr=[]):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid, arr):
            ok = mid
        else:
            ng = mid
    return ok


A = [i*2 for i in range(1000)]
ok = 0
ng = 1000
x = binary_search(ok, ng, A)
print(x, A[x])