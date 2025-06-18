n = int(input())
<<<<<<< HEAD

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
=======
cnt = 0
for i in range(n):
    word = input()
    check = []
    for j in range(len(word)):
        if j > 0 and word[j] != word[j - 1] and word[j] in check:
            word = 'NO'
            break
        if word[j] not in check:
            check.append(word[j])
    if word != 'NO':
        cnt += 1

print(cnt)        
>>>>>>> c5ccf60027d2dc74a4f58eb299c640e386ff833d
