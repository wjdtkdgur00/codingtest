h, w = input().split()
h, w = int(h), int(w)
arr = [[0 for col in range(w)] for row in range(h)]
n = int(input())
ldxy = [list(map(int, input().split())) for _ in range(n)]

def stick(arr, l, d, x, y):
    if d == 0:
        for j in range(y, y + l):
            arr[x][j] = 1 - arr[x][j]
    else:
        for i in range(x, x + l):
            arr[i][y] = 1 - arr[i][y]

for l, d, x, y in ldxy:
    stick(arr, l, d, x - 1, y - 1)

for row in arr:
    print(' '.join(map(str, row)))