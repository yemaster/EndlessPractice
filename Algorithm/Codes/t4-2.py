n, l, r = map(int, input().split())
w = list(map(int, input().split()))
ans = 0

def dfs(u, s):
    global ans
    if s > r:
        return
    if u >= n:
        if l <= s <= r:
            ans += 1
        return
    dfs(u + 1, s + w[u])
    dfs(u + 1, s)

dfs(0, 0)
print(ans)