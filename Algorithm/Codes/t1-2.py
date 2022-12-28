n, m = list(map(int, input().split()))
artist = list(map(int, input().split()))
cnt = [0] * 2005
num = 0
l, r = 0, -1
ansa, ansb = -1, 123456789
while r < n - 1:
    r += 1
    if (cnt[artist[r]] == 0):
        num += 1
    cnt[artist[r]] += 1
    while num == m:
        cnt[artist[l]] -= 1
        if (cnt[artist[l]] == 0):
            num -= 1
        l += 1
    if num == m:
        if r - l < ansb - ansa:
            ansa = l
            ansb = r
        cnt[artist[l]] -= 1
        if (cnt[artist[l]] == 0):
            num -= 1
        l += 1
    
print(ansa + 1, ansb + 1)