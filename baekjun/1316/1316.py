n = int(input())
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