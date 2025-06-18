n = input()
cmp = ''
for i in range(len(n) -1, -1, -1):
    cmp += (n[i])
if n == cmp:
    print(1)
else:
    print(0)