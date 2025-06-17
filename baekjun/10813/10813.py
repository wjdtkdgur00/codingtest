n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(i + 1)

for i in range(m):
    j, k = map(int, input().split())

    arr[j - 1], arr[k - 1] = arr[k - 1], arr[j - 1]

for i in arr:
    print(i, end=' ')
