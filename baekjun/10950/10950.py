n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(arr)):
    print(arr[i][0] + arr[i][1])