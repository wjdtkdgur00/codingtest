import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(len(arr)):
    print(arr[i][0] + arr[i][1])

# input() 이 아닌, sys.stdin.readline() 을 이용하여 빠른 속도로 처리할 수 있다.