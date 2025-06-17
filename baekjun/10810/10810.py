n, m = map(int, input().split())
arr = [0] * n
for a in range(m):
    i,j,k = map(int, input().split())
    arr[i -1 :j] = [k] * (j - i + 1)

for i in range(n):
    print(arr[i], end=' ')