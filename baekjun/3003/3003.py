arr = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))
res = []

for i in range(len(chess)):
    res.append(arr[i] - chess[i])

for i in res:
    print(i, end=' ')