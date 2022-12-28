cnt = [1] * 100000
n, c = list(map(int, input().split()))
nums = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - 1, i, -1):
        if nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

top = 0
for i in range(1, n):
    if nums[i] == nums[i - 1]:
        cnt[top] += 1
    else:
        top += 1
        nums[top] = nums[i]
j = top
i = top - 1
ans = 0
while j > 0:
    while i >= 0 and nums[j] - nums[i] < c:
        i -= 1
    if nums[j] - nums[i] == c:
        ans += cnt[j] * cnt[i]
    j -= 1
print(ans)