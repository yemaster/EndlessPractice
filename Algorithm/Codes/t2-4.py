a = list(map(int, input().split()))
n = len(a)
l = 2
r = n - 3
while l - r - 1 <= r:
    mid = (l + 2 * r) // 4
    if 2 * a[mid + 1] >= a[mid - 1] + a[mid + 2]:
        l = 2 * mid + 2
    else:
        r = mid - 1
print(a[r] + a[r + 1] - a[r + 2])
