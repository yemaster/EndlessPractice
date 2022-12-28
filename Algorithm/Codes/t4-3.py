import sys
n = int(input())
a = [0] + list(map(int, input().split()))
s = sum(a)

for i in range(1, n):
    for j in range(i + 1, n + 1):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

nxt = [n] * (n + 1)  # nxt[i]记录每根木棍后面的最后一根与这根木棍长度相等的木棍
for i in range(n - 1, 0, -1):
    if a[i] == a[i + 1]:
        nxt[i] = nxt[i + 1]
    else:
        nxt[i] = i
used = [False] * (n + 1)
m = 0
flag = False

def dfs(k, last, rest):
    global flag, m, origin
    if rest == 0:
        if k == m:
            flag = True
            return
        for i in range(1, n + 1):
            if not used[i]:
                break
        used[i] = True
        dfs(k + 1, i, origin - a[i])
        used[i] = False
        if flag:
            return
    l = last + 1
    r = n
    while l < r:
        mid = (l + r) // 2
        if a[mid] <= rest:
            r = mid
        else:
            l = mid + 1
    i = l
    while i <= n:
        if not used[i]:
            used[i] = 1
            dfs(k, i, rest - a[i])
            used[i] = 0
            if flag:
                return
            if rest == a[i] or rest == origin:
                return
            i = nxt[i]
            if i == n:
                return
        i += 1

for origin in range(a[1], s // 2 + 1):
    if s % origin != 0:
        continue
    m = s // origin
    flag = False
    used[1] = True
    dfs(1, 1, origin - a[1])
    used[1] = False
    if flag:
        print(origin)
        sys.exit(0)
print(s)