n, m = map(int, input().split())
a = list(map(int, input().split()))
q = [-1] * n
head = tail = 0
print(0)
for i in range(n):
    while head < tail and a[q[tail - 1]] > a[i]:
        tail -= 1
    while head < tail and q[head] + m <= i:
        head += 1
    q[tail] = i
    tail += 1
    if i == n - 1:
        break
    print(a[q[head]])