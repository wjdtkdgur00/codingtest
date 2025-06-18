n = int(input())

arr = [input() for _ in range(n)]
cnt = 0
check = []
for i in range(n):
    for j in range(len(arr[i])):
        check = []
        if arr[i][j] in check and arr[i][j - 1] != arr[i][j]:
            arr[i] = 'fail'
            break
        elif arr[i][j] not in check and arr[i][j - 1] != arr[i][j]:
            check.append(arr[i][j])
        
    if arr[i] != 'fail':
        cnt += 1

print(cnt)