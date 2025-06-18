paper = [list(0 for _ in range(100)) for i in range(100)]
a = int(input())
count = 0
for i in range(a):
    n, m = map(int, input().split())
    for j in range(m, m + 10):
        for k in range(n, n + 10):
            if paper[j][k] == 0:
                paper[j][k] = 1
            elif paper[j][k] == 1 or paper[j][k] == 2:
                paper[j][k] = 2
                count += 1

print((10 * 10 * a) - count)