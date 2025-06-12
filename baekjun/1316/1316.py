n = int(input())

arr = [input() for i in range(n)]
cmp = ''
check = 0
cnt = 0
for i in range(n):
    for j in range(len(arr[i])):
        if cmp == arr[i][j]:
            check = 0
            break
        else:
            cmp = arr[i][j]
            check = 1
    if check == 1:
        cnt += 1
print(cnt)