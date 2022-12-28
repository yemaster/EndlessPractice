m, n = map(int, input().split())
words = list(map(int, input().split()))
que = [0] * 1002
head = tail = 0
isInQue = [False] * 1002
cnt = 0
for i in words:
    if not isInQue[i]:
        que[tail] = i
        tail += 1
        isInQue[i] = True
        cnt += 1
        if tail - head > m:
            isInQue[que[head]] = False
            head += 1
print(cnt)