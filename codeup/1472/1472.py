n, m  = input().split()
n,m = int(n), int(m)
arr = [[0 for i in range(m)] for j in range(n)]
k = 1
for i in range(n -1, -1, -1):
    if (n - i) % 2 == 1:
        for j in range(m - 1, -1, -1):
            arr[i][j] = k
            k += 1
    else:
        for j in range(m):
            arr[i][j] = k
            k += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()