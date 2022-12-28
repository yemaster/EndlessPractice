from queue import PriorityQueue
m, n = map(int, input().split())
Map = [[-1] * 105 for i in range(105)]
vis = [[False] * 105 for i in range(105)]
for i in range(n):
    a, b, c = map(int, input().split())
    Map[a][b] = c

q = PriorityQueue()
q.put([0, 1, 1, Map[1][1]])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = -1
while q.qsize() > 0:
    t = q.get()
    if t[1] == m and t[2] == m:
        res = t[0]
        break
    vis[t[1]][t[2]] = True
    for i in range(4):
        tx = t[1] + dx[i]
        ty = t[2] + dy[i]
        col = Map[tx][ty]
        if tx < 1 or tx > m or ty < 1 or ty > m or vis[tx][ty]:
            continue
        if col == -1 and t[3] == -1:
            continue
        if col == -1:
            q.put([t[0] + 2, tx, ty, t[3]])
        else:
            if col == t[3]:
                q.put([t[0], tx, ty, col])
            else:
                q.put([t[0] + 1, tx, ty, col])
print(res)