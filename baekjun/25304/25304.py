x = int(input())
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
sum = 0

for i in range(len(arr)):
    sum += arr[i][0] * arr[i][1]

if sum == x:
    print("Yes")
else:
    print("No")