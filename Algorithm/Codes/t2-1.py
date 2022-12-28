d, s, t = [0], [0], [0]

n, m = map(int, input().split())
rest = list(map(int, input().split()))
for i in range(m):
    tmp = list(map(int, input().split()))
    d.append(tmp[0]); s.append(tmp[1]); t.append(tmp[2])


def isok(x):
    diff = [0] * (n + 10)
    need = [0] * (n + 10)
    for i in range(1, x + 1):
        diff[s[i]] += d[i]
        diff[t[i] + 1] -= d[i]
    for i in range(1, n + 1):
        need[i] = need[i - 1] + diff[i]
        if need[i] > rest[i - 1]:
            return False
    return True


l, r = 1, m
if isok(m):
    print("0")
else:
    while l < r:
        mid = (l + r) // 2
        if isok(mid):
            l = mid + 1
        else:
            r = mid
    print("-1")
    print(l)
