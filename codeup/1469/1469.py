n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
k = 1
for i in range(n):
    if i % 2 == 1:
        for j in range(n):
            arr[i][j] = k
            k += 1
    else:
        for j in range(n - 1, -1, -1):
            arr[i][j] = k
            k += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()