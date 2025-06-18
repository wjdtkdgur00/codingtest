arr = [list(input().split()) for _ in range(20)]
sum = 0
sum2 = 0
for i in range(20):
    arr[i][1] = float(arr[i][1])
    if arr[i][2] == 'A+':
        arr[i][2] = 4.5
    elif arr[i][2] == 'A0':
        arr[i][2] = 4.0
    elif arr[i][2] == 'B+':
        arr[i][2] = 3.5
    elif arr[i][2] == 'B0':
        arr[i][2] = 3.0
    elif arr[i][2] == 'C+':
        arr[i][2] = 2.5
    elif arr[i][2] == 'C0':
        arr[i][2] = 2.0
    elif arr[i][2] == 'D+':
        arr[i][2] = 1.5
    elif arr[i][2] == 'D0':
        arr[i][2] = 1.0
    elif arr[i][2] == 'F':
        arr[i][2] = 0.0
    
for i in range(20):
    if arr[i][2] != 'P':
        sum += float(arr[i][1]) * float(arr[i][2])
        sum2 += arr[i][1]
print(sum / sum2)

# arr = [list(input().split()) for _ in range(20)]
#sum = 0
#sum2 = 0
#grade = {
#    'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0 , 'F' : 0.0
#}
#for i in range(20):
#    arr[i][1] = float(arr[i][1])
#    
#for i in range(20):
#    if arr[i][2] != 'P':
#        sum += float(arr[i][1]) * float(grade[arr[i][2]])
#        sum2 += arr[i][1]
#print(sum / sum2)

# 위 코드는 if-elif 문으로 비효율적이다. 주석 코드인 grade dictionary 를 활용해서 등급을 key로 점수에 접근하여 빠르게 풀이할 수 있다.