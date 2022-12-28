n = int(input())
a = list(map(int, input().split()))
l = 0
ans = 0
while l < n:
    if a[l] == l + 1:
        l += 1
    else:
        mx = a[l]
        r = l
        while mx > r + 1:
            r += 1
            mx = max(a[r], mx)
        ans += r - l + 1
    l = r + 1
print(ans)
