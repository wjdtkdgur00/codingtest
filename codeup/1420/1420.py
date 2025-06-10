n = int(input())
dic = {}
for i in range(n):
    name, score = input().split()
    dic[name] = int(score)


dic = list(dic.items())
dic = sorted(dic, key = lambda x : x[1], reverse=True)
print(dic[2][0])