n, a, b = map(int, input().split())
k = [0] + list(map(int, input().split()))
link = []
head = [-1] * 420
def add(x, y):
    link.append([y, head[x]])
    head[x] = len(link) - 1
for i in range(1, n + 1):
    if i + k[i] <= n:
        add(i, i + k[i])
    if i - k[i] >= 1:
        add(i, i - k[i])
dis = [333333] * 420
dis[a] = 0
que = [a] * 420
isInQue = [False] * 420
isInQue[a] = True
h, t = 0, 1
while h < t:
    x = que[h]
    h += 1
    isInQue[x] = False
    i = head[x]
    while i != -1:
        y = link[i][0]
        if dis[x] + 1 < dis[y]:
            dis[y] = dis[x] + 1
            if not isInQue[y]:
                isInQue[y] = True
                que[t] = y
                t += 1
        i = link[i][1]
print(dis[b])