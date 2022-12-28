n, d, k = map(int, input().split())
dis, val = [0], [0]
for i in range(n):
    tmp = list(map(int, input().split()))
    dis.append(tmp[0]) # dis存储每个格子到起点的距离
    val.append(tmp[1]) # val存储每个格子的数字

def check(g):
    jumpL = max(1, d - g)
    jumpR = d + g
    dp = [-123412341234] * (n + 1)
    dp[0] = 0
    que = [0] * (n + 1)
    canL = 0 # canL,canR分别表示能跳到当前格子的格子范围
    canR = 0
    head = tail = 0
    for i in range(1, n + 1):
        while dis[i] - dis[canR] >= jumpL:
            while head < tail and dp[que[tail]] < dp[canR]:
                tail -= 1
            tail += 1
            que[tail] = canR
            canR += 1
        while head < tail and dis[i] - dis[que[head + 1]] > jumpR:
            head += 1
        if head >= tail:
            continue
        dp[i] = max(dp[i], dp[que[head + 1]] + val[i])
        if dp[i] >= k:
            return True
    return False

l, r = 0, dis[n]
res = -1
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)