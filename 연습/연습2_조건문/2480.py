A, B, C = map(int, input().split())

if (A!=B) & (B!=C) & (C!=A):
    temp = A
    if temp<B: temp=B
    if temp<C: temp=C
    print(100*temp)
elif A==B==C:
    print(10000 + 1000*A)
elif A==B & A!=C:
    print(1000+A*100)
elif B==C & C!=A:
    print(1000+B*100)
elif C==A & A!=B:
    print(1000+C*100)