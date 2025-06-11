n,m = input().split()
n,m = int(n), int(m)
arr = [[0 for i in range(m)] for i in range(n)]
a = 1
for k in range(n + m - 1, -1, -1):
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if i + j == k:
                arr[i][j] = a
                a += 1
                break
            
            

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()