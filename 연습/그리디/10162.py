T = int(input())
A,B,C = 0,0,0
if int(T/300) >= 1:
    A = int(T/300)
    T -= 300*A
if int(T/60) >= 1 :
    B = int(T/60)
    T -= 60*B
if int(T/10) >= 1:
    C = int(T/10)
    T -= 10*C
if T != 0:
    print("-1")
else: print(A,B,C)
