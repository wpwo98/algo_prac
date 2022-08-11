A,B = map(int, input().split())
a = A%10*100 + int(A/10%10)*10 + int(A/100)
#print(a)
b = B%10*100 + int(B/10%10)*10 + int(B/100)
#print(b)

if a > b : print(a)
else : print(b)