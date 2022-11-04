A,B,C = map(int,input().split())
K=0
if (B > C) :
    K = -1
elif (C-B) == 0:
    K = -1
else:
    K += int(A / (C-B)) + 1
print(K)