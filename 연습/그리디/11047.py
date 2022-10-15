N, K = map(int, input().split())
A = [0 for n in range(N)]
for i in range(N):
    A[i] = int(input())
A.sort()
A.reverse()
count = 0
for i in range(N):
    if K < A[i]:
        continue
    else :
        count += K // A[i]
        K = K % A[i]
print(count)