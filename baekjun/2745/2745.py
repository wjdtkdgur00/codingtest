n, b = input().split()
b = int(b)

alpha = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = 0

for i in range(len(n)):
    a = alpha.index(n[i])
    res = res * b + a

print(res)
##### ZZZZZ 36 -> Z = 35 이므로 35 * 36 ^ 0 + 35 * 36 ^ 1.... 이런식이다. 어차피 36이 곱해지고 35가 더해지기 때문에 위 코드처럼 간결하게 표현할 수 있다.