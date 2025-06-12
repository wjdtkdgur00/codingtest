cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n = input()
count = 0
for i in cro:
    while i in n:
        count += 1
        n = n.replace(i, '*')

print(len(n))

# cro 알파벳은 하나의 문자열로 보므로 cro가 n에 나오지 않을 때 까지 계속 cro 를 
# * 로 바꾸면 cro 알파벳을 하나의 문자로 보고 구할 수 있음.