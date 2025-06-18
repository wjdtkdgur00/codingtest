n = input()

counter = []
max = ''
count = 0
for i in n:
    counter.append(i.upper())
for i in set(counter):
    if counter.count(i) > count:
        count = counter.count(i)
        max = i
    elif counter.count(i) == count:
        max = '?'
    
print(max)