T = int(input())
for i in range(1,T+1):
    a,b = map(int, input().split())
    r = str(a+b)
    str1 = "Case #" + str(i) + ":"
    print(str1,a,"+",b,"=",r)
