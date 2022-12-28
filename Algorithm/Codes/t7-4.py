def bubbleSort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

def unique(arr):
    new = [arr[0]]
    n = len(arr)
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            new.append(arr[i])
    return new

def countSort(arr):
    count = [0] * 1001
    for i in arr:
        count[i] += 1
    new = []
    for i in range(1001):
        if count[i] > 0:
            new.append(i)
    return new

M = int(input())
arr = list(map(int, input().split()))
print(countSort(arr))