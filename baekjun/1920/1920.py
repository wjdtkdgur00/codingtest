n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

m = int(input())
b = list(map(int, input().split()))

def search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in range(len(b)):
    print(search(b[i], a))

# n, m 은 딱히 내 코드에서 필요는 없다..