import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    print(f"Case #{i + 1}: {arr[i][0]} + {arr[i][1]} = {arr[i][0] + arr[i][1]}")