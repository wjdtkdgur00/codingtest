arr = list(map(int, input().split()))
 
for i in range(len(arr) - 1):
    for j in range(1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in range(len(arr)):
    print(arr[i], end=' ')