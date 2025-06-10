n = int(input())
count = 0

for a in range(1, n):
    for b in range(a, n):
        c = n - a - b
        if c < b or c <= 0:
            break
        if a + b > c:
            count += 1

print(count)
