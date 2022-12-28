n, m = map(int, input().split())
T = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - 1, i, -1):
        if T[j] < T[j - 1]:
            T[j], T[j - 1] = T[j - 1], T[j]

def check(t):
    num = 0
    for i in T:
        num += t // i
        if num >= m:
            return True
    return False

L, R = 1, T[-1] * m
ans = R
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = min(ans, mid)
        R = mid - 1
    else:
        L = mid + 1
print(ans)