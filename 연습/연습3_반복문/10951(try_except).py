while True:         # input이 몇 개인지 알 수 없으므로 try-except 사용.
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        break