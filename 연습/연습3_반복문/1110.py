N = int(input())
N1 = N
cycle = 0
while True:
    a = int(N1/10)
    b = N1%10
    N1 = b*10 + (a+b)%10
    cycle += 1
    if N1==N: 
        print(cycle)
        break
