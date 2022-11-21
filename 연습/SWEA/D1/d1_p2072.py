def d1_p2072():
    T = int(input())
    for t in range(T):
        num = "#"
        result = 0
        t_case = list(map(int,input().split()))
        for i in t_case:
            if i % 2 == 1:
                result += i
        num += str(t+1)
        print(num,result)

