n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in range(len(arr)):
    res = n + 1
    if arr[i] >= k:
        res = i + 1
        break

print(res)