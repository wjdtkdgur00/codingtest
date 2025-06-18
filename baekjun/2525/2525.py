h, m = map(int, input().split())
c = int(input())

m += c
while m >= 60:
    if m >= 60:
        m -= 60
        h += 1
        if h > 23:
            h = 0

print(h, m)