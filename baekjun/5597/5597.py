arr = []
for i in range(28):
    arr.append(int(input()))
nota = []
for i in range(1, 31):
    if i not in arr and i != 0:
        nota.append(i)

for i  in sorted(nota):
    print(i)