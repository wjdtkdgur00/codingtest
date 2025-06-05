maap = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1
while x < 10 and y < 10:
    if maap[x][y] == 2:
        maap[x][y] = 9
        break
    elif maap[x][y] == 0:
        maap[x][y] = 9

    if maap[x][y + 1] == 0 or maap[x][y + 1] == 2:
        y += 1
    else:
        x += 1

for i in range(len(maap)):
    for j in range(len(maap)):
        print(maap[i][j],end=' ')
    print()