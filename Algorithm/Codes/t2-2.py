n = int(input())
h = [0] + list(map(int, input().split())) # 读取h[i]
g = [0] + list(map(int, input().split()))  # 读取g[i]
f = int(input())

l, r = 1, n
ans = -222222

def judge(m):
    z = [0] + [h[i] + g[i] * (m - 1) for i in range(1, n + 1)]
    for i in range(1, n):
        for j in range(i, n + 1):
            if z[i] > z[j]:
                z[i], z[j] = z[j], z[i]
    s = sum(z[:m + 1])
    if s <= f:
        return True
    else:
        return False

while l <= r:
    m = (l + r) // 2
    if judge(m):
        l = m + 1
        if m > ans:
            ans = m
    else:
        r = m - 1
print(ans)