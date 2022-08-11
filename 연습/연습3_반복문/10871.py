N, X = map(int, input().split())
A = list(map(int, input().split()))
str1 = ""
for i in range(N):
    if A[i] < X: 
        str1 += str(A[i]) +" "
print(str1)