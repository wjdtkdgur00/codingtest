while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break

# 무한이 계속 input() 을 받다가 input 이 없을 때 EOF(End Of File) 에러가 발생하므로
# try-except 문으로 예외 처리를 해준다.