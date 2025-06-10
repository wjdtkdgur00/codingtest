n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
start = 0
end = 0
sum = 0

while True:
    if sum >= k:
        sum -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        sum += arr[end]
        end += 1
    if sum == k:
        cnt += 1

print(cnt)
