n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(i + 1)

for i in range(m):
    j, k = map(int, input().split())
    arr[j - 1:k] = arr[j - 1:k][::-1]
print(*arr) # print(*arr) 이렇게 하면 배열 요소 띄어쓰기 구분자로 출력됨 3 4 1 2 5 